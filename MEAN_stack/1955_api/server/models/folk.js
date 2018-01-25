var mongoose = require('mongoose');
var FolkSchema = new mongoose.Schema({
    name: String,
})
mongoose.model('Folk', FolkSchema);