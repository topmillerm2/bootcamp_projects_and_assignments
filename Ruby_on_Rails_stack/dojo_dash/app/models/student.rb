class Student < ActiveRecord::Base
  validates :first_name, :last_name, :email, presence:true
  belongs_to :dojo
end
