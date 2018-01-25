class RpgController < ApplicationController
    def index
        session[:score] ||= 0
        session[:messages] ||= []
    end

    def farm
        random_num = rand(10..20)
        session[:score] += random_num
        message = "Earned #{random_num} golds from the farm! (#{(Time.now).strftime("%b %d, %Y, %r")})"
        session[:messages].push(message)
        # flash[:messages] = "Earned #{random_num} golds from the farm! (#{(Time.now).strftime("%b %d, %Y, %r")})"
        # flash[:messages] = "Earned #{random_num} golds from the farm! (#{Time.now.utc + Time.zone_offset('PDT')})"
        redirect_to :back
    end
    def cave
        random_num = rand(5..10)
        session[:score] += random_num
        message = "Earned #{random_num} golds from the cave! (#{(Time.now).strftime("%b %d, %Y, %r")})"
        session[:messages].push(message)
        # flash[:messages] = "Earned #{random_num} golds from the cave! (#{Time.now}}"
        # flash[:messages] = "Earned #{random_num} golds from the cave! (#{Time.now.utc + Time.zone_offset('PDT')})"
        redirect_to :back
    end
    def house
        random_num = rand(2..5)
        session[:score] += random_num
        message = "Earned #{random_num} golds from the house! (#{(Time.now).strftime("%b %d, %Y, %r")})"
        session[:messages].push(message)
        # flash[:messages] = "Earned #{random_num} golds from the house! (#{Time.now}}"
        # flash[:messages] = "Earned #{random_num} golds from the house! (#{Time.now.utc + Time.zone_offset('PDT')})"
        redirect_to :back
    end
    def casino
        random_num  = rand(-20..20)
        session[:score] += random_num
        if random_num > 0
            # flash[:messages] = "Earned #{random_num} golds from the casino! (#{Time.now}}"
            message = "Earned #{random_num} golds from the casino! (#{(Time.now).strftime("%b %d, %Y, %r")})"
            session[:messages].push(message)
            redirect_to :back
        else
            random_num = random_num.abs
            message = "Entered a casino and lost #{random_num} golds...Ouch. (#{Time.now.utc + Time.zone_offset('PDT')})"
            session[:messages].push(message)
            redirect_to :back
        end
    end
    def restart
        reset_session
        redirect_to :root
    end
end
