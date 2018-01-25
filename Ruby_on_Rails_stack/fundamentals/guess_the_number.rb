def guess_number guess
    number = 25
    if guess > number
        return "Guess was too high!"
    end
    if guess < number
        return "Guess was too low!"
    end
    if guess == number
        return "You got it!"
    end
end 

puts guess_number 25
puts guess_number 0