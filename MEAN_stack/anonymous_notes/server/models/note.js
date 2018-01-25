let mongoose= require('mongoose');
let NoteSchema = mongoose.Schema({
    note: String
}, {timestamps: true})

mongoose.model('Note', NoteSchema);