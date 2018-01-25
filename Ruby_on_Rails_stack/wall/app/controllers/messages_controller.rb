class MessagesController < ApplicationController
  def index
    @name = User.find(session[:id])
    # puts @name
  end
end
