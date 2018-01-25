class UsersController < ApplicationController
  skip_before_action :require_login, only: [:new]
  before_action :require_correct_user, only: [:show, :edit, :update, :destroy]

  def new
  end
  def create
    user = User.create(user_params)
    if user.save
      redirect_to "/sessions/new"
    else
      flash[:errors] = user.errors.full_messages
      redirect_to :back
    end
  end
  def show
    @user = User.find(params[:id])
    @secrets = Secret.all
    @likes = Like.all
  end

  def edit
    @user = User.find(params[:id])
  end
  def update
    user = User.find(params[:id])
    if user.update(user_params)
      redirect_to "/users/#{user.id}/edit"
    else
      flash[:errors]= user.errors.full_messages
      redirect_to :back
    end
  end
  def destroy
    User.find(params[:id]).destroy
    reset_session
    redirect_to "/users/new"
  end

  private 
  def user_params
    params.require(:user).permit(:name, :email, :password, :password_confirmation)
  end
end
