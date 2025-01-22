FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install 
CMD ["python", "-m", "unittest", "discover"]




