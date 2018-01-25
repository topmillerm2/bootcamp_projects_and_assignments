require 'rails_helper'

RSpec.describe Member, type: :model do
  context "with valid attributes" do 
    it "should save" do 
      expect(build(:member)).to be_valid
    end
    it 'automatically encrypts the password into the password_digest attribute' do
      expect(build(:member).password_digest.present?).to eq(true)
    end 
    it 'email as lowercase' do 
      expect(create(:member, email: 'EMAIL@GMAIL.COM').email).to eq('email@gmail.com')
    end
  end
  context "with invalid attributes should not save if" do 
    it 'name is blank' do
      expect(build(:member, name: '')).to be_invalid
    end
    it 'email is blank' do
      expect(build(:member, email: '')).to be_invalid
    end
    it 'email format is wrong' do
      emails = %w[@ member@ @example.com]
      emails.each do |email|
        expect(build(:member, email: email)).to be_invalid
      end
    end
    it 'email is not unique' do
      create(:member)
      expect(build(:member)).to be_invalid
    end
    it 'password is blank' do
      expect(build(:member, password: '')).to be_invalid
    end
    it "password doesn't match password_confirmation" do
      expect(build(:member, password_confirmation: 'npassword')).to be_invalid
    end
  end
end
