class UsersController < ApplicationController
    def index
        render json: User.all
    end
    
    def new
    end
    def create
        @user = User.new(user_params)
        if @user.save
            redirect_to :root
        else
            flash[:errors] = @user.errors.full_messages
            redirect_to :back
        end
    end

    def show 
        puts params[:id]
        render json: User.find(params[:id])
    end

    def edit
        @user = User.find(params[:id])
    end

    def update
        user = User.find(params[:id])

        if user.update(user_params)
            redirect_to :root
        else
            flash[:errors] = user.errors.full_messages
            redirect_to :back
        end
    end

    def destroy
        @user = User.destroy(params[:id])
    end

    def total
        render json: { total: User.count }
    end


    private
    def user_params
        params.require(:user).permit(:name, :power)
    end
end
