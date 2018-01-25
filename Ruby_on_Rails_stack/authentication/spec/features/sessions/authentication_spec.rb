require 'rails_helper'
feature 'authentication feature' do
    before do
        @user = create(:user)
    end
  feature "user attempts to sign-in" do
    scenario 'visits sign-in page, prompted with email and password fields' do
        visit "/sessions/new"
        expect(page).to have_field("email")
        expect(page).to have_field("password")
    end
    scenario 'logs in user if email/password combination is valid' do
        visit "/sessions/new"
        fill_in "email", with: "michael@topmiller.com"
        fill_in "password", with: "password"
        click_button "Log In"
        expect(current_path).to eq("/users/#{@user.id}")
        expect(page).to have_text(@user.email)
    end
    scenario 'does not sign in user if email is not found' do
        visit "/sessions/new"
        fill_in "email", with: "john@doe.com"
        fill_in "password", with: "password"
        click_button "Log In"
        expect(current_path).to eq("/sessions/new")
        expect(page).to have_text("Invalid Email/Password Combination")
    end
    scenario 'does not sign in user if email/password combination is invalid' do
        visit "/sessions/new"
        fill_in "email", with: "michael@topmiller.com"
        fill_in "password", with: "npassword"
        click_button "Log In"
        expect(current_path).to eq("/sessions/new")
        expect(page).to have_text("Invalid Email/Password Combination")
    end
  end
  feature "user attempts to log out" do
    before do
    visit "/sessions/new"
        fill_in "email", with: "michael@topmiller.com"
        fill_in "password", with: "password"
        click_button "Log In"
    end
    scenario 'displays "Log Out" button when user is logged on' do 
        expect(current_path).to eq("/users/#{@user.id}")
        expect(page).to have_button("Log Out")
    end
    scenario 'logs out user and redirects to login page' do
        click_button "Log Out"
        expect(current_path).to eq("/sessions/new")
        end
   end
end