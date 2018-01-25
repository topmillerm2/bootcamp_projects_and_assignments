class UsersController < ApplicationController
  def new
  end
  def create
    username = User.new(user_params)
    if username.save
      session[:id]= username.id
      puts session[:id]
      redirect_to messages_path
    elsif user_params[username] == User.where(username: "username")
      session[:id]= username.id
      # puts username.id
      redirect_to messages_path
    else
      flash[:notice] = username.errors.full_messages
      redirect_to new_user_path
    end
  end

  private
  def user_params
    params.require(:user).permit(:username)
  end
end
