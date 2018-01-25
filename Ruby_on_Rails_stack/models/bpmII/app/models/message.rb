class Message < ActiveRecord::Base
  validates :author, :message, presence: true, length: {  minimum: 1 }
  has_many :comments, as: :imageable
  belongs_to :user
  belongs_to :post
end
