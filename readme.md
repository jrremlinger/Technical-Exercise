# Instructions

1. After pulling the project, run the command `docker image build -t technical-excercise .` in the root folder.
2. Use `docker run -p 5000:5000 -d technical-excercise` to then start the application at localhost:5000.
3. User `docker stop {ID}` to stop the application and `docker rm {ID}` to purge the container. The ID can be found under `docker container ls`.