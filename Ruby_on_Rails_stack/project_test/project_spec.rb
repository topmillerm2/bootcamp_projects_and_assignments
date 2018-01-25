require_relative 'project'
RSpec.describe Project do
    before(:each) do
        @project = Project.new("Project Name", "Description")
    end
    it "has a getter and setter for name attribute" do
        expect(@project.name).to eq("Project Name")
    end
    it "has a getter and setter for the description attribute" do
        expect(@project.description).to eq("Description")
    end
    it 'has a method elevator_pitch to explain name and description' do
        expect(@project.elevator_pitch).to eq("Project Name, Description")
    end
end