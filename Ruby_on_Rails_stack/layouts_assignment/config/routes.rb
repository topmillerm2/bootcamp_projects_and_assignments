Rails.application.routes.draw do
  root "users#index"
  get "posts" => "posts#index"
end
