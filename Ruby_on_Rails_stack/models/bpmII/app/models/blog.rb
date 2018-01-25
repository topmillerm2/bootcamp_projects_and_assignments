class Blog < ActiveRecord::Base
    validates :name, :description, presence: true, length: { minimum: 1}

    has_many :comments, as: :imageable
    has_many :owners
    has_many :users, through: :owners
    has_many :posts
end



