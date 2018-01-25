require 'rails_helper'
feature "User features" do
  before do
       @user = create(:user)
       log_in
    end
  feature "User Settings Dashboard" do
    before(:each) do
      visit "/users/#{@user.id}/edit"
    end
    scenario "visits users edit page" do
      expect(page).to have_field("Name")
      expect(page).to have_field("Email")
    end
    scenario "visit users edit page" do
      expect(find_field("Name").value).to eq(@user.name)
      expect(find_field("Email").value).to eq(@user.email)
    end
    scenario "incorrectly updates information" do
      fill_in "Name", with: "Another name"
      fill_in "Email", with: "incorrect email format"
      click_button "Update"
      expect(current_path).to eq("/users/#{@user.id}/edit")
      expect(page).to have_text("Email is invalid")
    end
    scenario "correctly updates information" do
      fill_in "Name", with: "Michael"
      fill_in 'Email', with: "correct@email.com"
      click_button "Update"
      expect(find_field('Name').value).to eq("Michael")
    end
    scenario "destroys user and redirects to registration page" do
      click_button "Delete Account"
      expect(current_path).to eq("/users/new")
    end
  end


end
