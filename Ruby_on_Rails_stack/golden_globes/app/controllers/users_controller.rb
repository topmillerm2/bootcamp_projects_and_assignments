class UsersController < ApplicationController
  def create
    user = User.create(user_params)
      if user.save
        session[:user_id] = user.id
        redirect_to "/nominations"
      else
        flash[:errors] = user.errors.full_messages
        redirect_to :back
      end
  end

  def edit
  end

  def update
  end
  private 
  def user_params
    params.require(:user).permit(:first_name, :last_name, :email, :location, :state, :password, :password_confirmation)
  end
end
