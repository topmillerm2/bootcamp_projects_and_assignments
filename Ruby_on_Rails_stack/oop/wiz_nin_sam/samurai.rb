require_relative 'human'

class Samurai < Human
    @@number_of_sam = 0
    def initialize
        @health = 200
        @@number_of_sam += 1
    end

    def death_blow obj
        if obj.class.ancestors.include?(Human)
            obj.health = 0
            # remember that we don't need to write "return" in ruby
            # stating true below will automatically return the boolean true
            true
        else
            false
        end
    end

    def meditate
        @health = 200
    end

end