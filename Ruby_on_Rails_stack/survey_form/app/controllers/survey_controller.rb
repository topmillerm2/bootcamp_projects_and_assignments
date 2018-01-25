class SurveyController < ApplicationController

    def index
        session[:views] ||= 0
    end

    def create
        session[:views] = session[:views] + 1
        session[:result] = params[:user]
   
        flash[:success] = "Thanks for submitting this form! You have submitted this form #{session[:views]} times(s) now"
        redirect_to "/survey/success"
    end

    def success
        @result = session[:result]
    end

    # private
    # def user_params
    #     params.require(:user).permit(:name, :location, :language, :comment)
    # end
end
