require 'rails_helper'
feature "guest user creates an account" do
    before(:each) do 
    visit new_user_path
  end
  scenario "successfully creates a new username and logs in" do
    fill_in "user_username", with: "shane"
    click_button "Sign In"
    expect(page).to have_current_path(messages_path)
    expect(page).to have_content "Welcome, shane"
  end
  # scenario "successfully finds username and logs in" do
  # end
  scenario "unsuccessfully creates a new user account" do 
    click_button "Sign In"
    expect(current_path).to eq(new_user_path)
  end
end
