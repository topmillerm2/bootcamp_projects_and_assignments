class SessionsController < ApplicationController
  def new
  end

  def create 
    user = User.find_by(email: params[:email])
    if user && user.authenticate(params[:password])
      session[:user_id] = user.id
      redirect_to "/nominations"
    else
      flash[:errors] = ["Invalid Email/Password Combination"]
      redirect_to :back
    end
  end

  def destroy
    reset_session
    redirect_to "/"
  end
end
