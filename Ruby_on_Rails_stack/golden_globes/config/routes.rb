Rails.application.routes.draw do
  root 'sessions#new'

  get 'nominations' => "nominations#index"

  resources :sessions, only: [:new, :create, :destroy]
  resources :users, only: [:create, :edit, :update]
end
