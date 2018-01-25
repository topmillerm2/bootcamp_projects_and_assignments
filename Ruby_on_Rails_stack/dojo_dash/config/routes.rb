Rails.application.routes.draw do
  root "dojos#index"
  # resources :dojos do
  #   resources :students
  # end
  get "dojos/new" => "dojos#new"
  post "dojos" => "dojos#create"
  get "dojos/:id" => "dojos#show"
  get "dojos/:id/edit"=> "dojos#edit"
  patch "dojos/:id" => "dojos#update"
  delete "dojos/:id" => "dojos#destroy"

  get "dojos/:id/student/new" => "student#new"
  post "dojos/:id/student" => "student#create"
  get "dojos/:dojo_id/student/:id" => "student#show"
  get "/dojos/:dojo_id/student/:id/edit" => "student#edit"
  patch "/dojos/:dojo_id/student/:id" => "student#update"
  delete "dojos/:dojo_id/student/:id" => "student#destroy"
end
