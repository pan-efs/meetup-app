# `MeetUp-Web-App` :sunglasses:

### Info
- This repo has been created following a `4h` great tutorial on [youtube.](https://www.youtube.com/watch?v=t7DrJqcUviA)
- `Dockerfile`, `docker-compose.yml` and `.github\workflows\build.yml` have been added by me for personal development reasons.

### Download Docker
Get docker from [here.](https://docs.docker.com/get-docker/)
### Build and run docker
Clone the repo using your desired IDE.

Navigate to the root project directory and run:
- Build docker image: `docker compose build`
- Run docker container in background: `docker compose up -d`

Open your desired web browser and search for: `http://localhost:8000/`

- Check existence: `docker ps`, [optional]
- Stop container: `docker stop <container id>`, [optional]