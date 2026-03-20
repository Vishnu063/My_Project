from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import boto3
import os
import uuid
from datetime import datetime

app = FastAPI()

# DynamoDB setup
dynamodb = boto3.resource('dynamodb')
table_name = os.getenv('DYNAMODB_TABLE', 'users')
table = dynamodb.Table(table_name)

class User(BaseModel):
    id: str = None
    name: str
    email: str
    created_at: str = None

@app.on_event("startup")
async def create_table():
    # Check if table exists, create if not (for development)
    try:
        dynamodb.meta.client.describe_table(TableName=table_name)
    except dynamodb.meta.client.exceptions.ResourceNotFoundException:
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
            BillingMode='PAY_PER_REQUEST'
        )
        table.wait_until_exists()

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "user-service"}

@app.get("/users", response_model=List[User])
async def get_users():
    try:
        response = table.scan()
        return response.get('Items', [])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/users", response_model=User)
async def create_user(user: User):
    try:
        user_id = str(uuid.uuid4())
        now = datetime.utcnow().isoformat()
        
        item = {
            'id': user_id,
            'name': user.name,
            'email': user.email,
            'created_at': now
        }
        
        table.put_item(Item=item)
        return item
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
