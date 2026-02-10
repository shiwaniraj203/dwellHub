import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@db:5432/dwellhub')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'dwellhub-secret-key-2024')
    JWT_SECRET = os.getenv('JWT_SECRET', 'jwt-secret-key-2024')