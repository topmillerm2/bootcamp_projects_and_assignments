let mongoose= require('mongoose');
let PlayerSchema = mongoose.Schema({
    name: String,
    position: String,
    status: String
}, {timestamps: true})

mongoose.model('Player', PlayerSchema);