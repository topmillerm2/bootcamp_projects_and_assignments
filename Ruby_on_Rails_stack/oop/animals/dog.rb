require_relative 'mammal'

class Dog < Mammal
    def pet
        @health += 5
        self
    end

    def walk
        @health -= 1
        self
    end
    
    def run
        @health -=10
        self
    end
        
end

new_dog = Dog.new 
new_dog.walk.walk.walk.run.run.pet.display_health