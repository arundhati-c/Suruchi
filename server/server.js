// load the env variables (PORT)
// if we are in development mode, we will use the .env file
// if we are in production mode, we will use the env variables set on the server
if (process.env.NODE_ENV !== 'production'){
    require('dotenv').config();
}
    
import express from 'express';
import cors from 'cors';
import mongoose from 'mongoose';

const app = express();

app.use(cors());
app.use(express.json());
app.use("/");

mongoose.connect('mongodb://localhost/recipe', {useNewUrlParser: true, useUnifiedTopology: true});

app.listen(process.env.PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});