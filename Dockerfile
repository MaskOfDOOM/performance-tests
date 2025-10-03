FROM python:3.13
WORKDIR /app
COPY . .
RUN python -m pip install termcolor
CMD ["python", "docker_example.py"]