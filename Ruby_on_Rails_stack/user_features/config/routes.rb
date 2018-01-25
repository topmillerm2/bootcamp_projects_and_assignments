Rails.application.routes.draw do
  get 'likes/create'

  get 'likes/destroy'

  get 'users/new' => "users#new"
  get "users/:id" => "users#show"
  get "users/:id/edit" => "users#edit"
  post "users" => "users#create"
  patch "users/:id" => "users#update"
  delete "users/:id" => "users#destroy"

  get "secrets" => "secrets#index"
  post "secrets" => "secrets#create"
  delete "secrets/:id" => "secrets#destroy"

  post "likes/:id" => "likes#create"
  delete "likes/:id" => "likes#destroy"
  

  get "sessions/new" => "sessions#new"
  post "sessions" => "sessions#create"
  delete "sessions/:id" => "sessions#destroy"


  

  # resources :sessions, only: [:new, :create, :destroy]
  # resources :users

  
end
