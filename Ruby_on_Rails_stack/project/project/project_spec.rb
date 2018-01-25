require_relative 'project'
RSpec.describe Project do
    before(:each) do
        @project1 = Project.new('Project 1', 'description 1', 'owner 1')
        @project2 = Project.new('Project 2', 'description 2', 'owner 2')
    end
    it 'has a getter and setter for name attribute' do
        @project1.name = "Changed Name"
        expect(@project1.name).to eq("Changed Name")
    end
    it 'has a getter and setter for owner attribute' do
        @project1.owner = "Changed Owner"
        expect(@project1.owner).to eq("Changed Owner")
    end
    it 'has a method tasks to return the tasks for each project' do
        expect(@project1.tasks).to eq([])
    end
    it 'has a method to add tasks to tasks array' do
        @project1.add_tasks 'Do the dishes'
        expect(@project1.tasks).to eq(['Do the dishes'])
    end
    it 'has a method elevator_pitch to explain name and description' do
        expect(@project1.elevator_pitch).to eq("Project 1, description 1")
        expect(@project2.elevator_pitch).to eq("Project 2, description 2")
    end
    it 'has a method print_tasks to print each task in project' do
        @project1.add_tasks 'Do the dishes'
        expect(@project1.print_tasks).to eq('Do the dishes')
    end
end