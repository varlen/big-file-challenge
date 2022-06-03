FROM python:3

WORKDIR /app
COPY create_file.py .
COPY parse_file.py .
RUN python create_file.py
CMD [ "python", "./parse_file.py"]