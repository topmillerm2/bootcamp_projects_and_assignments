class FamiliarizeController < ApplicationController

    def index
    end

    def hello
        render text: "Hello World"
    end
    def says 
    end

    def joe
    end

    def michael
        redirect_to "/say/hello/joe"
    end
    
    def times
       session[:count] ||= 0
       session[:count] += 1
       render text: "You have visited this url #{session[:count]} times"
    end

    def reset
        reset_session
        render text: "Destroyed Session"
    end

end
