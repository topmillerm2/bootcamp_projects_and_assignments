class BankAccount
    @@count = 0
    def initialize
        @checking_number = generate
        @savings_number = generate
        @savings_balance = 0
        @checking_balance = 0
        @@count += 1
    end
    
    def display_savings
        puts @savings_balance
        self
    end
    
    def display_checking
        puts @checking_balance
        self
        @checking_balance
    end
    def checking_balance num
        @checking_balance = num
    end

    def savings_deposit(val)
        puts "depositing #{val}"
        @savings_balance += val
        self
    end

    def checking_deposit(val)
        puts "depositing #{val}"
        @checking_balance += val
        self
    end

    def savings_withdrawal(val)
        puts "withdrawing #{val}"
        if @savings_balance - val < 0 
            raise "Insufficient Funds"
        else
            @savings_balance -= val
        end
        val
    end

    def checking_withdrawal(val)
        puts "withdrawing #{val}"
        @checking_balance -= val
        if @checking_balance < 0 
            puts "Insufficient Funds"
            @checking_balance += val
        end
        @checking_balance
    end

    def total
        @savings_balance + @checking_balance
    end

    def self.number_of_accounts
        @@count
    end

    def account_information
        puts "Checking Acct: #{@checking_number}, Savings Account: #{@savings_number}, Total Balance: #{total}, Checking Balance: #{@checking_balance}, Savings Balance: #{@savings_balance}, Interest Rate: #{interest}"
        self
    end

    private
        def interest
            0.01
        end
    
        def generate
            Random.new.rand(0..100000000)
        end
end

# new_acct1 = BankAccount.new
# new_acct2 = BankAccount.new
# new_acct3 = BankAccount.new
# new_acct4 = BankAccount.new
# new_acct5 = BankAccount.new
# new_acct6 = BankAccount.new
# new_acct7 = BankAccount.new
# # BankAccount.number_of_accounts
# new_acct1.checking_deposit(20).savings_deposit(1000)
# new_acct1.display_checking.account_information

# new_acct2.account_information
# new_acct3.account_information
# new_acct4.account_information
# new_acct5.account_information
# new_acct6.account_information
# new_acct7.account_information

# puts BankAccount.number_of_accounts

