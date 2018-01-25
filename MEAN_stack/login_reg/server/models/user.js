var mongoose = require('mongoose');
var bcryptP = require('bcrypt-as-promised');
var UserSchema = new mongoose.Schema({
    first_name: {type: String},
    last_name: {type: String},
    email: {type: String, unique:true},
    dob: {type: Date},
    password: {type:String}
    
}, {timestamps:true
  });


  UserSchema.pre('save', function(next){
	var user = this;
	console.log("this:", this);
	bcryptP.hash(user.password, 10)
	.then((hashed_password)=>{
		console.log("hashed_password", hashed_password);
		user.password = hashed_password;
		next();
    })
  })
mongoose.model('User', UserSchema)