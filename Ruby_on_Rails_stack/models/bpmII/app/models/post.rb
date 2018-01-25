class Post < ActiveRecord::Base
  validates :title, :content, presence: true, length: { minimum: 1 }
  has_many :comments, as: :imageable
  has_many :messages
  belongs_to :blog
  belongs_to :user
end
