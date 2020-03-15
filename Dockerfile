# Define environemnt specs
FROM python:3

# Install requirements in environment
COPY requirements.txt /
RUN pip install --requirement ./requirements.txt

# Copy necessary files

ADD . /

# Launch the app
ENTRYPOINT ["python"]
CMD ["app.py"]