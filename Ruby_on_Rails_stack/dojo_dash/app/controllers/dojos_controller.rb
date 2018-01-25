class DojosController < ApplicationController
    def index
        @dojos = Dojo.all
    end
    def new
    end
    def create
        new_dojo = Dojo.new(dojo_params)
        if new_dojo.save
            redirect_to root_url, notice: "You have successfully created a Dojo"
        else
            flash[:messages] = new_dojo.errors.full_messages
            redirect_to :back
        end
    end

    def show
        @dojo = Dojo.find(params[:id])
        @students = Student.where(dojo_id: params[:id]).all
    end

    def edit
        @dojo = Dojo.find(params[:id])
    end

    def update
        # fail
        updated_dojo = Dojo.find(params[:id])
        if updated_dojo.update(dojo_params)
            redirect_to "/dojos/#{updated_dojo.id}", notice: "You have successfully updated this Dojo"
        else
            flash[:messages] = updated_dojo.errors.full_messages
            redirect_to :back
        end
    end
    
    def destroy
        Dojo.find(params[:id]).destroy
        redirect_to :root, notice: "You have successfully deleted a Dojo"
    end

    private
    def dojo_params
        params.require(:dojo).permit(:branch, :street, :city, :state)        
    end
end
