class AppleTree
    attr_accessor :age
    attr_reader :height, :count
    def initialize
        @age = 0
        @height = 10
        @count = 0
    end
    def year_gone_by 
        @age += 1
        @height += (@height * 0.1)
        @count += 2 if (4..10).include?(@age)
    end

    def pick_apples
        apples = @count
        @count = 0
        apples
    end

end