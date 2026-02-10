from models import db, User, Apartment
from werkzeug.security import generate_password_hash

def seed_database():
    # Clear existing data
    db.drop_all()
    db.create_all()
    
    # Create admin user
    admin = User(
        name='Admin User',
        email='admin@apartments.com',
        password_hash=generate_password_hash('admin123'),
        role='admin'
    )
    
    # Create regular user
    user = User(
        name='John Doe',
        email='user@example.com',
        password_hash=generate_password_hash('user123'),
        role='user'
    )
    
    db.session.add(admin)
    db.session.add(user)
    
    # Create sample apartments
    apartments = [
        Apartment(
            title='Modern Studio Apartment',
            location='Downtown, New York',
            price=1200.00,
            amenities='WiFi, AC, Kitchen, Parking'
        ),
        Apartment(
            title='Cozy 2BHK Flat',
            location='Brooklyn, New York',
            price=1800.00,
            amenities='WiFi, AC, Gym, Pool'
        ),
        Apartment(
            title='Luxury Penthouse',
            location='Manhattan, New York',
            price=3500.00,
            amenities='WiFi, AC, Gym, Pool, Terrace, Concierge'
        ),
        Apartment(
            title='Budget Friendly Room',
            location='Queens, New York',
            price=800.00,
            amenities='WiFi, Shared Kitchen'
        ),
        Apartment(
            title='Family Villa',
            location='Staten Island, New York',
            price=2500.00,
            amenities='WiFi, AC, Garden, Parking, Garage'
        )
    ]
    
    for apt in apartments:
        db.session.add(apt)
    
    db.session.commit()
    print('Database seeded successfully!')