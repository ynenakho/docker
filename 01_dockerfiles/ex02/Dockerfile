FROM ruby
RUN apt-get update && apt-get install nodejs -y && gem install rails
ONBUILD COPY app /opt/
ONBUILD WORKDIR /opt/app
ONBUILD RUN bundle install
ONBUILD RUN rails db:migrate
ONBUILD RUN rails db:seed

#docker build -t ft-rails .
#docker build -t rails-server -f Dockerfile_test .
#docker run -it --rm -p 3000:3000 rails-server
