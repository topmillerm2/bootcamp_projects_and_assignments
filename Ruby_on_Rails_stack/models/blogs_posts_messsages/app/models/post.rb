class Post < ActiveRecord::Base
  has_many :messages, dependent: :destroy 
  belongs_to :blog
  validates :title, presence: true
  validates :content, presence:true, length: { minimum: 7 }
end
