class Movie < ActiveRecord::Base
    validates :title, :director, presence: true
end
