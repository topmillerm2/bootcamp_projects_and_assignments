require_relative 'apple'
RSpec.describe AppleTree do
    before(:each) do
        @tree = AppleTree.new
    end
    it 'has a getter and setter method for age attribute' do
        expect(@tree.age = 5).to eq(5)
    end
    it 'has a getter method for height attribute' do
        expect(@tree.height).to eq(10)
    end
    it 'has a getter method for apple count attribute' do
        expect(@tree.count).to eq(0)
    end
    it 'raises an error when setting height attribute' do
        expect{@tree.height=6}.to raise_error(NoMethodError)
    end
    it 'raises an error when setting count attribute' do
        expect{@tree.count=6}.to raise_error(NoMethodError)
    end

    context "should have a method year_gone_by" do
        before(:each) do
        @tree.year_gone_by
        end

        it "adds one year to the age attribute" do
        expect(@tree.age).to eq(1)
        end

        it "increases the height by 10% of it's current height" do
        expect(@tree.height).to eq(11)
        end

        context "increases the apple count by 2 within a range" do
            it "should not increase if the age is less than or equal to 3" do
                # current age is 3 since the before(:each) in the parent context
                2.times { @tree.year_gone_by }
                expect(@tree.count).to eq(0)
            end

            it "should increase if the age is between 4 and 10" do
                # current age is 5 since the before(:each) in the parent context
                4.times { @tree.year_gone_by }
                expect(@tree.count).to eq(4)
            end

            it "should not increase if the age is greater than 10" do
                # current age is 11 since the before(:each) in the parent context
                10.times { @tree.year_gone_by }
                expect(@tree.count).to eq(14)
            end
        end
    end

    it 'has a method that resets the count' do
        expect(@tree.pick_apples).to eq(0)
    end
end