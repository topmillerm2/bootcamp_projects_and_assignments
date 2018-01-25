require_relative 'human'

class Wizard < Human
    def initialize
        @health = 50
        @intelligence = 25
    end

    def heal
        @health +=10
    end

    def fireball obj
        if obj.class.ancestors.include?(Human)
            obj.health -= 20
            # remember that we don't need to write "return" in ruby
            # stating true below will automatically return the boolean true
            true
        else
            false
        end
    end
end