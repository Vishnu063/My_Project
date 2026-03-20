package main

import (
    "fmt"
    "log"
    "net/http"
    "os"
    "time"

    "github.com/aws/aws-sdk-go/aws"
    "github.com/aws/aws-sdk-go/aws/session"
    "github.com/aws/aws-sdk-go/service/dynamodb"
    "github.com/aws/aws-sdk-go/service/dynamodb/dynamodbattribute"
    "github.com/gin-gonic/gin"
)

type Product struct {
    ID          string    `json:"id" dynamodbav:"id"`
    Name        string    `json:"name" dynamodbav:"name"`
    Price       float64   `json:"price" dynamodbav:"price"`
    Description string    `json:"description" dynamodbav:"description"`
    CreatedAt   time.Time `json:"created_at" dynamodbav:"created_at"`
}

var db *dynamodb.DynamoDB
var tableName string

func main() {
    // Initialize AWS session
    sess, err := session.NewSession(&aws.Config{
        Region: aws.String(os.Getenv("AWS_REGION")),
    })
    if err != nil {
        log.Fatal("Failed to create session:", err)
    }

    db = dynamodb.New(sess)
    tableName = os.Getenv("DYNAMODB_TABLE")
    if tableName == "" {
        tableName = "products"
    }

    router := gin.Default()

    router.GET("/health", healthCheck)
    router.GET("/products", getProducts)
    router.POST("/products", createProduct)

    port := os.Getenv("PORT")
    if port == "" {
        port = "8080"
    }

    router.Run(":" + port)
}

func healthCheck(c *gin.Context) {
    c.JSON(http.StatusOK, gin.H{
        "status":  "healthy",
        "service": "product-service",
        "time":    time.Now().Unix(),
    })
}

func getProducts(c *gin.Context) {
    input := &dynamodb.ScanInput{
        TableName: aws.String(tableName),
    }

    result, err := db.Scan(input)
    if err != nil {
        c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
        return
    }

    var products []Product
    err = dynamodbattribute.UnmarshalListOfMaps(result.Items, &products)
    if err != nil {
        c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
        return
    }

    c.JSON(http.StatusOK, products)
}

func createProduct(c *gin.Context) {
    var product Product
    if err := c.ShouldBindJSON(&product); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }

    product.CreatedAt = time.Now()
    product.ID = fmt.Sprintf("%d", time.Now().UnixNano())

    av, err := dynamodbattribute.MarshalMap(product)
    if err != nil {
        c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
        return
    }

    input := &dynamodb.PutItemInput{
        Item:      av,
        TableName: aws.String(tableName),
    }

    _, err = db.PutItem(input)
    if err != nil {
        c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
        return
    }

    c.JSON(http.StatusCreated, product)
}
