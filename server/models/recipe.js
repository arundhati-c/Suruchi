import mongoose from "mongoose";

const recipeSchema = new mongoose.Schema ({
    name : {type: String, required: true},
    description : {type: String},
    ingredients : {type: Array, required: true},
})