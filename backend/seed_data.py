from models import db, User, Apartment
from werkzeug.security import generate_password_hash


def seed_database():
    db.drop_all()
    db.create_all()

    admin = User(
        name='Admin User',
        email='admin@apartments.com',
        password_hash=generate_password_hash('admin123'),
        role='admin'
    )

    user = User(
        name='Priya Sharma',
        email='user@example.com',
        password_hash=generate_password_hash('user123'),
        role='user'
    )

    db.session.add(admin)
    db.session.add(user)

    apartments = [
        Apartment(
            title='Premium 2BHK in Whitefield',
            location='Whitefield, Bangalore',
            price=28000,
            amenities='WiFi, Parking, Gym, Power Backup',
            image_url='https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=400'
        ),
        Apartment(
            title='Cozy Studio Near Marathahalli',
            location='Marathahalli, Bangalore',
            price=15000,
            amenities='WiFi, Furnished, Security',
            image_url='https://images.unsplash.com/photo-1536376072261-38c75010e6c9?w=400'
        ),
        Apartment(
            title='Spacious 3BHK in Koramangala',
            location='Koramangala 5th Block, Bangalore',
            price=45000,
            amenities='Gym, Pool, Parking, Balcony',
            image_url='https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=400'
        ),
        Apartment(
            title='Budget 1BHK in Electronic City',
            location='Electronic City Phase 1, Bangalore',
            price=12000,
            amenities='WiFi, Security, Water Supply',
            image_url='https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=400'
        ),
        Apartment(
            title='Luxury Villa in Indiranagar',
            location='Indiranagar 100ft Road, Bangalore',
            price=60000,
            amenities='Garden, Gym, Pool, Parking, Security',
            image_url='https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=400'
        ),
        Apartment(
            title='Modern 2BHK in HSR Layout',
            location='HSR Layout Sector 1, Bangalore',
            price=32000,
            amenities='WiFi, AC, Modular Kitchen, Parking',
            image_url='https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=400'
        )
    ]

    for apt in apartments:
        db.session.add(apt)

    db.session.commit()
    print("Database seeded successfully!")