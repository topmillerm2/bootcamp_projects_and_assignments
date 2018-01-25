class MathDojo
    attr_reader :sum

    def initialize
        @sum = 0
    end

    def add *params
        @sum += params.flatten.reduce(:+)
        self
    end

    def subtract *params
        @sum -= params.flatten.reduce(:+)
        self
    end

  end

test1 = MathDojo.new
# test1.add(2).subtract(7).result
challenge1 = MathDojo.new.add(2).add(2, 5).subtract(3, 2).sum # => 4
puts challenge1
challenge2 = MathDojo.new.add(1).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract([2,3], [1.1, 2.3]).sum # => 23.15
puts challenge2