class StudentController < ApplicationController
    def new
        @dojo = Dojo.find(params[:id])
        @other_dojos = Dojo.all
    end

    def create
        new_student = Student.create(student_params)
        if new_student.save
            redirect_to "/dojos/#{new_student.dojo_id}"
        else
            flash[:messages] = new_student.errors.full_messages
            redirect_to :back
        end
    end

    def show
        @dojo = Dojo.find(params[:dojo_id])
        @student = Student.find(params[:id])
        @cohort = Student.where('dojo_id': params[:dojo_id])
        # @student = Student.where(dojo_id = params[:dojo_id]).where(time_range created_at)
    end

    def edit
        @dojo = Dojo.find(params[:dojo_id])
        @other_dojos = Dojo.all
        @student = Student.find(params[:id])
    end

    def update
        updated_student = Student.find(params[:id])
        if updated_student.update(student_params)
            redirect_to "/dojos/#{updated_student.dojo_id}/student/#{updated_student.id}", notice: "You have successfully updated this student"
        else
            flash[:messages] = updated_student.errors.full_messages
            redirect_to :back
        end
    end

    def destroy
        Student.find(params[:id]).destroy
        destroyed_student_dojo = Dojo.find(params[:dojo_id])
        redirect_to "/dojos/#{destroyed_student_dojo.id}"
    end

    private
    def student_params
        params.require(:student).permit(:first_name, :last_name, :email, :dojo_id)
    end
end
