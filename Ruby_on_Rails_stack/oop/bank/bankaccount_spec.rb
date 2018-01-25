require_relative 'bank_account'
RSpec.describe BankAccount do
    before(:each) do
        @account1 = BankAccount.new
        @account2 = BankAccount.new
    end
    it 'has a getter method for retrieving the checking acct balance' do
        @account1.checking_balance 5
        expect(@account1.display_checking).to eq(5)
    end
    it 'has a function that allows the user to withdraw cash' do
        @account1.checking_balance 5
        expect(@account1.checking_withdrawal 5).to eq(0)
    end
    it 'raises an error if savings is overdrawn' do
        expect{@account1.savings_withdrawal 5 }.to raise_error("Insufficient Funds")
    end
    it 'has a getter method for retrieving the total(sum) balance' do
        expect(@account1.total).to eq(0)
    end
    it 'raises an error when attempted retrievement of total number of accts' do
        expect{@account1.self.number_of_accounts}.to raise_error(NoMethodError)
    end
    it 'raises an error when attempted adjustment of interest rate' do
        expect{@account1.interest = 0.5}.to raise_error(NoMethodError)
    end
end