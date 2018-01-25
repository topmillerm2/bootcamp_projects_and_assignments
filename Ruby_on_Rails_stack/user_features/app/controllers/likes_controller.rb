class LikesController < ApplicationController
  def create
    secret = Secret.find(params[:id])
    like = Like.create(user: current_user, secret: secret)
    redirect_to "/secrets"
  end

  def destroy
    like = Like.find_by(user_id: current_user.id, secret_id: params[:id])
    like.destroy if current_user === like.user
    redirect_to "/secrets"
  end
end
