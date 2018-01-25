require_relative 'human'

class Ninja < Human
    def initialize 
        @stealth = 175
    end

    def steal obj
        if obj.class.ancestors.include?(Human)
            obj.health -= 10
        # remember that we don't need to write "return" in ruby
        # stating true below will automatically return the boolean true
            true
        else
            false
        end
    end

    def get_away
        @health -= 15
    end

end

# ninja1 = Ninja.new