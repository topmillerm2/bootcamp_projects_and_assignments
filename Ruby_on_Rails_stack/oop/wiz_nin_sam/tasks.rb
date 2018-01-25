require_relative 'samurai'
require_relative 'wizard'

sam1 = Samurai.new
sam2 = Samurai.new
wiz1 = Wizard.new
puts sam1.death_blow(wiz1)
puts wiz1.health



