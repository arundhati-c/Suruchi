import mongoose from "mongoose";
import validator from 'validator';
import bcrypt from 'bcrypt';

const userSchema = new mongoose.Schema({
    username: {
        type: String, 
        unique:true, 
        required: [
            true,
            'Please enter a username'
        ],
        maxLength: 30,
        minLength: 3
    },
    email: {
        type: String, 
        unique:true, 
        required: [
            true,
            'Please enter an email'
        ],
        validate: [
            validator.isEmail, 
            'Please enter a valid email'
        ]
    },
    passwordHash: {type: String, required: true},
    preferences: {type: Map, of: String},
}, {timestamps: true});