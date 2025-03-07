const express = require('express');
const axios = require('axios');
const cors = require('cors');

const app = express();
const PORT = 4000;

app.use(express.json());
app.use(cors());

// Route to send data to Flask API
app.post('/predict', async (req, res) => {
    try {
        const response = await axios.post('http://127.0.0.1:5000/predict', req.body);
        console.log(response)  // <-- Add this to check what is received
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});


app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
