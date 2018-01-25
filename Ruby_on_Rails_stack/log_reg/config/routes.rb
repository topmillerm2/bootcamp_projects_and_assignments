Rails.application.routes.draw do
  root "sessions#new"  
  post "sessions" => "sessions#create"

  resources :users, only: [:show]

end
