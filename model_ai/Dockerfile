FROM python:3.9
WORKDIR /app
COPY package_requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 2137
CMD ["python", "main.py"]