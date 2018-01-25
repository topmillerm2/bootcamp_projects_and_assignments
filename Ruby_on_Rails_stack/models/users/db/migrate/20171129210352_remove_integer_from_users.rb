class RemoveIntegerFromUsers < ActiveRecord::Migration
  def change
    remove_column :users, :integer, :string
  end
end
