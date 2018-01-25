class User < ActiveRecord::Base
    EMAIL_REGEX = /\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]+)\z/i
    validates :first_name, :last_name, presence: true, length: { minimum: 1}
    validates :email_address, presence: true, uniqueness: { case_sensitive: false }, format: { with: EMAIL_REGEX }
    has_many :owners
    has_many :blogs, through: :owners
    has_many :posts
    has_many :messages
    has_many :comments, as: :imageable
end
