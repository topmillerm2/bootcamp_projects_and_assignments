class SessionsController < ApplicationController
  skip_before_action :require_login, only: [:new, :create]
  def new
  end
  def create 
    user = User.find_by(email: params[:email])
    if user && user.authenticate(params[:password])
      session[:user_id] = user.id
      redirect_to "/users/#{user.id}"
    else
      flash[:errors] = ["Invalid Email/Password Combination"]
      redirect_to :back
    end
  end
  def destroy
    reset_session
    redirect_to "/sessions/new"
  end
end
