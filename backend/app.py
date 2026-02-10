from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, User, Apartment, Booking
from config import Config
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta
from functools import wraps
import os

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

db.init_app(app)

# JWT decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token missing'}), 401
        try:
            token = token.split(' ')[1]
            data = jwt.decode(token, app.config['JWT_SECRET'], algorithms=['HS256'])
            current_user = User.query.get(data['user_id'])
        except:
            return jsonify({'message': 'Invalid token'}), 401
        return f(current_user, *args, **kwargs)
    return decorated

# Admin only decorator
def admin_required(f):
    @wraps(f)
    def decorated(current_user, *args, **kwargs):
        if current_user.role != 'admin':
            return jsonify({'message': 'Admin access required'}), 403
        return f(current_user, *args, **kwargs)
    return decorated

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'service': 'dwellhub-api'}), 200

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email already exists'}), 400
    
    user = User(
        name=data['name'],
        email=data['email'],
        password_hash=generate_password_hash(data['password']),
        role='user'
    )
    
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    
    if not user or not check_password_hash(user.password_hash, data['password']):
        return jsonify({'message': 'Invalid credentials'}), 401
    
    token = jwt.encode({
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(hours=24)
    }, app.config['JWT_SECRET'], algorithm='HS256')
    
    return jsonify({
        'token': token,
        'user': {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'role': user.role
        }
    }), 200

@app.route('/api/apartments', methods=['GET'])
def get_apartments():
    apartments = Apartment.query.all()
    return jsonify([{
        'id': apt.id,
        'title': apt.title,
        'location': apt.location,
        'price': apt.price,
        'amenities': apt.amenities
    } for apt in apartments]), 200

@app.route('/api/apartments', methods=['POST'])
@token_required
@admin_required
def create_apartment(current_user):
    data = request.json
    apartment = Apartment(
        title=data['title'],
        location=data['location'],
        price=data['price'],
        amenities=data['amenities']
    )
    db.session.add(apartment)
    db.session.commit()
    return jsonify({'message': 'Apartment created'}), 201

@app.route('/api/apartments/<int:id>', methods=['PUT'])
@token_required
@admin_required
def update_apartment(current_user, id):
    data = request.json
    apartment = Apartment.query.get(id)
    if not apartment:
        return jsonify({'message': 'Apartment not found'}), 404
    
    apartment.title = data.get('title', apartment.title)
    apartment.location = data.get('location', apartment.location)
    apartment.price = data.get('price', apartment.price)
    apartment.amenities = data.get('amenities', apartment.amenities)
    
    db.session.commit()
    return jsonify({'message': 'Apartment updated'}), 200

@app.route('/api/apartments/<int:id>', methods=['DELETE'])
@token_required
@admin_required
def delete_apartment(current_user, id):
    apartment = Apartment.query.get(id)
    if not apartment:
        return jsonify({'message': 'Apartment not found'}), 404
    
    db.session.delete(apartment)
    db.session.commit()
    return jsonify({'message': 'Apartment deleted'}), 200

@app.route('/api/bookings', methods=['POST'])
@token_required
def create_booking(current_user):
    data = request.json
    booking = Booking(
        user_id=current_user.id,
        apartment_id=data['apartment_id'],
        status='pending'
    )
    db.session.add(booking)
    db.session.commit()
    return jsonify({'message': 'Booking created'}), 201

@app.route('/api/bookings/my', methods=['GET'])
@token_required
def my_bookings(current_user):
    bookings = Booking.query.filter_by(user_id=current_user.id).all()
    return jsonify([{
        'id': b.id,
        'apartment': {
            'title': b.apartment.title,
            'location': b.apartment.location,
            'price': b.apartment.price
        },
        'status': b.status,
        'created_at': b.created_at.isoformat()
    } for b in bookings]), 200

@app.route('/api/bookings/all', methods=['GET'])
@token_required
@admin_required
def all_bookings(current_user):
    bookings = Booking.query.all()
    return jsonify([{
        'id': b.id,
        'user': {
            'name': b.user.name,
            'email': b.user.email
        },
        'apartment': {
            'title': b.apartment.title,
            'location': b.apartment.location,
            'price': b.apartment.price
        },
        'status': b.status,
        'created_at': b.created_at.isoformat()
    } for b in bookings]), 200

@app.route('/api/bookings/<int:id>/status', methods=['PUT'])
@token_required
@admin_required
def update_booking_status(current_user, id):
    data = request.json
    booking = Booking.query.get(id)
    if not booking:
        return jsonify({'message': 'Booking not found'}), 404
    
    booking.status = data['status']
    db.session.commit()
    return jsonify({'message': 'Booking status updated'}), 200

if __name__ == '__main__':
    with app.app_context():
        from seed_data import seed_database
        seed_database()
    app.run(host='0.0.0.0', port=5000, debug=True)