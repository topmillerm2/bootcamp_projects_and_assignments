class UsersController < ApplicationController
  def new
  end
  def create
  @user = User.new(params.require(:user).permit(:first_name, :last_name, :email))
  if @user.save
    # session[:id] = @user.id
    # session[:name] = @user.first_name
    # flash[:notice] = ['Welcome #{session[:name]}']
    redirect_to user_path(@user.id)
  else
    flash[:notice] = @user.errors.full_messages
    redirect_to new_user_path
  end
  def show
    @user = User.find(params[:id])
  end
end
end
