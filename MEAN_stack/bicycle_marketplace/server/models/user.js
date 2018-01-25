let mongoose= require('mongoose');
var Schema = mongoose.Schema;


let UserSchema = mongoose.Schema({
    FirstName: {type: String, required:true} ,
    LastName: {type: String, required: true},
    Email: {type: String, required: true},
    Password: {type: String, required: true},
    bicycles: [{ type: Schema.Types.ObjectId, ref: "Bicycle"}]
}, {timestamps: true});


let BicycleSchema = mongoose.Schema({
    Image: {type: String, required:true},
    Title: {type: String, required:true},
    Description: {type: String, required:true},
    Price: {type: Number, required:true},
    Location: {type: String, required:true},
    _user: { type: Schema.Types.ObjectId, ref: "User"}

}, {timestamps: true})

mongoose.model('User', UserSchema);
mongoose.model('Bicycle', BicycleSchema);