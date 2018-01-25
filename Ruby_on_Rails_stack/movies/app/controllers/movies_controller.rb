class MoviesController < ApplicationController
    def index
        @movies = Movie.all
    end

    def new
    end

    def create
        fail
        puts movie_params
        movie = Movie.new(movie_params)
        if movie.save
            # redirect to home
            redirect_to "/movies"
        else
            # redirect to new page
            flash[messages] = movie.errors.full_messages
            redirect_to :back    
        end    
    end

    private
    def movie_params
        params.require(:movie).permit(:title, :director)
    end

end
