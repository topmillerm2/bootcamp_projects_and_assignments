Rails.application.routes.draw do
  root "familiarize#index"
  
  get "hello" => "familiarize#hello"
  get "say/hello" => "familiarize#says"
  get "say/hello/joe" => "familiarize#joe"
  get "say/hello/michael" => "familiarize#michael"
  get "times" => "familiarize#times"
  get "reset" => "familiarize#reset"
end
