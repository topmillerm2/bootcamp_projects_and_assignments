class Project 
    attr_reader :name, :description

    def initialize n, desc
        @name = n
        @description = desc
    end

    def elevator_pitch
        puts "#{@name}, #{@description}"
    end
    # def name 
    #     puts @name
    # end
    # def name=(val)
    #     @name = val
    # end

  end
  project1 = Project.new("Great Idea", "This is such a good project!")
  puts project1.name # => "Project 1"
  project1.elevator_pitch  # => "Project 1, Description 1"
  