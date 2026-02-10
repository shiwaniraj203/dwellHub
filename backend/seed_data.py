from models import db, User, Apartment
from werkzeug.security import generate_password_hash


def seed_database():
    # Clear existing data
    db.drop_all()
    db.create_all()

    # Admin user
    admin = User(
        name='Admin User',
        email='admin@apartments.com',
        password_hash=generate_password_hash('admin123'),
        role='admin'
    )

    # Normal user
    user = User(
        name='Test User',
        email='user@example.com',
        password_hash=generate_password_hash('user123'),
        role='user'
    )

    db.session.add(admin)
    db.session.add(user)

    # Bangalore apartments
    apartments = [
        Apartment(
            title='Whitefield Tech Park Flat',
            location='Whitefield, Bangalore',
            price=25000.00,
            amenities='WiFi, Parking, Lift, Security'
        ),
        Apartment(
            title='Koramangala Studio',
            location='Koramangala 5th Block, Bangalore',
            price=18000.00,
            amenities='WiFi, AC, Furnished'
        ),
        Apartment(
            title='HSR Layout Family 2BHK',
            location='HSR Layout Sector 2, Bangalore',
            price=30000.00,
            amenities='Parking, Balcony, Garden, Power Backup'
        ),
        Apartment(
            title='Electronic City Budget Room',
            location='Electronic City Phase 1, Bangalore',
            price=10000.00,
            amenities='Shared Kitchen, WiFi'
        ),
        Apartment(
            title='Indiranagar Premium Apartment',
            location='Indiranagar 100ft Road, Bangalore',
            price=40000.00,
            amenities='Gym, Pool, Lift, Security, Covered Parking'
        )
    ]

    for apt in apartments:
        db.session.add(apt)

    db.session.commit()

    print("Database seeded successfully!")
