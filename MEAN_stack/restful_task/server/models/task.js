var mongoose = require('mongoose');
var TaskSchema = new mongoose.Schema({
    title: {String},
    description: {String},
    completed: {Boolean, default:True},
    created_at: {Date, default: Date.now},
    updated_at: {Date, default: Date.now}
})
mongoose.model('Task', TaskSchema);