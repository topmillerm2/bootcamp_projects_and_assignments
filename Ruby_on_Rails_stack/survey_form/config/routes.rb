Rails.application.routes.draw do
  root "survey#index"
  get "survey/success" => "survey#success"
  post "survey" => "survey#create"
 
end
