class Member < ActiveRecord::Base
  EMAIL_REGEX = /\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]+)\z/i
  has_secure_password
  validates :name, presence: true
  validates :email, presence: true, uniqueness: { case_sensitive: false}, format: { with: EMAIL_REGEX }
  before_save { |member| member.email = email.downcase }

  # before_save :email_lowercase

  # def email_lowercase
  #   email.downcase!
  # end
end
