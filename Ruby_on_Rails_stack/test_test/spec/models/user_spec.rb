require 'rails_helper'

RSpec.describe User, type: :model do
  context "With valid attributes" do 
    it "should save" do 
      user = User.new(
        first_name: 'shane',
        last_name: 'chang',
        email: 'schang@codingdojo.com'
      )
      expect(user).to be_valid
    end
  end
  
  it "should not save if first_name field is blank" do
      user = User.new(
            first_name: '', 
            last_name: 'chang', 
            email: 'schang@codingdojo.com'
        )
      expect(build(:user, first_name: "")).to be_invalid
    end
    it "should not save if last_name field is blank" do
      user = User.new(first_name: 'Michael', last_name: "", email: "michael@chang.com")
      expect(user).to be_invalid
    end
    
    it "should not save if email already exists" do
      user = User.new(first_name: 'Michael', last_name: "Chang", email: "")
      expect(user).to be_invalid
    end
    
    it "should contain a valid email" do
      user = User.new(first_name: "Michael", last_name: "Chang", email: "michaelchang.com")
      expect(user).to be_invalid
    end
    
end
