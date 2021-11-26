FROM python:3.10-alpine

# Create a user
RUN adduser -S -h /calcapp -s /bin/ash calcapp
USER calcapp

# Change working directory
WORKDIR /calcapp

# Copy install the requirements
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Copy the source
COPY calc calc

# Define environment variables
ENV HOST=0.0.0.0
ENV PORT=8080
ENV DEBUG=False

# Run the app
ENTRYPOINT [ "python", "calc/app.py" ]
