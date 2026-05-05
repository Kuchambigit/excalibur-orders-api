# use official Python image
FROM python:3.11-slim

# set working directory
WORKDIR /app

# copy project files
COPY . .

# install dependencies
RUN pip install fastapi uvicorn

# expose port
EXPOSE 8000

# run the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
