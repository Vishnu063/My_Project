const express = require('express');
const path = require('path');
const app = express();
const PORT = 3000;

// Serve static files from public directory
app.use(express.static('public'));

// API routes
app.get('/health', (req, res) => {
    res.json({ status: 'healthy', service: 'api-gateway' });
});

app.get('/api/users', async (req, res) => {
    try {
        const response = await fetch('http://user-service:8000/users');
        const users = await response.json();
        res.json(users);
    } catch (error) {
        res.json({ users: [], error: error.message });
    }
});

// Serve the main page
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(PORT, () => console.log(`API Gateway running on port ${PORT}`));
