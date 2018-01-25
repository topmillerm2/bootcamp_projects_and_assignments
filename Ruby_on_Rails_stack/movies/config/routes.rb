Rails.application.routes.draw do
  get "movies" => "movies#index"
  get "movies/new" => "movies#new"
  post "movies" => "movies#create"
end
