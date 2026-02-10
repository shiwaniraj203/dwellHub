# DwellHub - Residential Apartment Rental Portal

A full-stack web application for managing apartment rentals with separate portals for residents and administrators. Built with modern technologies and containerized for seamless deployment.

## 🎯 Project Overview

DwellHub is a comprehensive apartment rental management system that enables users to browse available apartments, request bookings, and track their rental status. Administrators can manage property listings, handle booking requests, and oversee the entire rental process through an intuitive dashboard.

## ✨ Features

### User Portal
- **User Registration & Authentication** - Secure account creation with JWT-based authentication
- **Apartment Browsing** - View available apartments with detailed information (location, price, amenities)
- **Booking Management** - Request apartment bookings and track booking status in real-time
- **Personal Dashboard** - View all your bookings and their approval status

### Admin Portal
- **Property Management** - Add, edit, and remove apartment listings
- **Booking Administration** - Review and approve/reject booking requests
- **Comprehensive Dashboard** - Monitor all bookings and property availability
- **User Management** - Oversee registered users and their activities

## 🛠️ Tech Stack

### Frontend
- **Angular 20** - Modern component-based architecture with TypeScript
- **Tailwind CSS** - Responsive, utility-first CSS framework
- **RxJS** - Reactive programming for handling async operations
- **HTML5** - Semantic markup for accessibility

### Backend
- **Python Flask** - Lightweight and flexible REST API framework
- **SQLAlchemy** - ORM for database operations
- **PostgreSQL** - Robust relational database
- **JWT** - Secure token-based authentication
- **Flask-CORS** - Cross-origin resource sharing support

### DevOps
- **Docker** - Containerization for consistent environments
- **Docker Compose** - Multi-container orchestration
- **Nginx** - Production-ready web server for frontend

## 📁 Project Structure

```
dwellhub/
├── backend/
│   ├── app.py              # Main Flask application
│   ├── models.py           # Database models
│   ├── config.py           # Configuration settings
│   ├── seed_data.py        # Demo data seeding
│   ├── requirements.txt    # Python dependencies
│   └── Dockerfile          # Backend container config
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   │   ├── login/      # Login component
│   │   │   ├── register/   # Registration component
│   │   │   ├── apartments/ # Apartment listing
│   │   │   ├── bookings/   # User bookings
│   │   │   └── admin/      # Admin dashboard
│   │   ├── main.ts         # Application entry point
│   │   └── styles.css      # Global styles
│   ├── angular.json        # Angular configuration
│   ├── package.json        # Node dependencies
│   ├── nginx.conf          # Nginx configuration
│   └── Dockerfile          # Frontend container config
└── docker-compose.yml      # Container orchestration
```

## 🗄️ Database Schema

### Users Table
- Stores user credentials and role information
- Fields: `id`, `name`, `email`, `password_hash`, `role`

### Apartments Table
- Contains property listings with complete details
- Fields: `id`, `title`, `location`, `price`, `amenities`

### Bookings Table
- Manages rental requests and their status
- Fields: `id`, `user_id`, `apartment_id`, `status`, `created_at`

## 🚀 Getting Started

### Prerequisites
- Docker Desktop (version 20.10 or higher)
- Git for version control
- 4GB RAM minimum

### Installation & Running

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/dwellhub.git
cd dwellhub
```

2. **Start the application**
```bash
docker-compose up --build
```

3. **Access the application**
- **Frontend**: http://localhost
- **Backend API**: http://localhost:5000

The application will automatically:
- Set up PostgreSQL database
- Create necessary tables
- Seed demo data
- Start all services

### Demo Credentials

**Admin Account**
```
Email: admin@apartments.com
Password: admin123
```

**User Account**
```
Email: user@example.com
Password: user123
```

## 🔌 API Endpoints

### Authentication
- `POST /api/register` - Create new user account
- `POST /api/login` - Authenticate user and return JWT token

### Apartments (Public)
- `GET /api/apartments` - Retrieve all available apartments

### Apartments (Admin Only)
- `POST /api/apartments` - Create new apartment listing
- `PUT /api/apartments/:id` - Update existing apartment
- `DELETE /api/apartments/:id` - Remove apartment listing

### Bookings (User)
- `POST /api/bookings` - Create new booking request
- `GET /api/bookings/my` - Get current user's bookings

### Bookings (Admin)
- `GET /api/bookings/all` - Retrieve all bookings
- `PUT /api/bookings/:id/status` - Approve or reject booking

### Health Check
- `GET /api/health` - Verify API status

## 🎨 Key Implementation Details

### Authentication Flow
- JWT tokens issued upon successful login
- Tokens stored in localStorage for session persistence
- Role-based access control (Admin vs User)
- Protected routes with authentication checks

### State Management
- Angular services for centralized state
- RxJS observables for reactive data flow
- HTTP interceptors for consistent API calls

### Database Design
- Normalized relational schema
- Foreign key constraints for data integrity
- Indexed columns for query optimization
- Automated seeding for development environment

### Containerization
- Multi-stage Docker builds for optimized images
- Service dependencies managed via Docker Compose
- Health checks for database readiness
- Volume persistence for database data

## 🔒 Security Features

- Password hashing using Werkzeug security
- JWT token-based authentication
- Role-based authorization
- CORS configuration for API security
- Input validation on both frontend and backend

## 📊 Application Architecture

```
┌─────────────┐         ┌─────────────┐         ┌─────────────┐
│   Angular   │         │    Flask    │         │ PostgreSQL  │
│  (Frontend) │ ──HTTP─→│  (Backend)  │ ──SQL─→ │  (Database) │
│   Port 80   │ ←─JSON──│  Port 5000  │ ←─Data──│  Port 5432  │
└─────────────┘         └─────────────┘         └─────────────┘
```

## 🧪 Testing the Application

### Manual Testing Steps

1. **User Registration**
   - Navigate to http://localhost/register
   - Create a new account
   - Verify successful registration

2. **User Login & Booking**
   - Login with user credentials
   - Browse available apartments
   - Create a booking request
   - View booking status

3. **Admin Operations**
   - Login with admin credentials
   - Add a new apartment listing
   - Approve/reject user bookings
   - Edit or delete apartments

### API Testing with cURL

**Health Check**
```bash
curl http://localhost:5000/api/health
```

**User Login**
```bash
curl -X POST http://localhost:5000/api/login \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"user123"}'
```

**Get Apartments**
```bash
curl http://localhost:5000/api/apartments
```

## 🚢 Deployment

### Local Development
```bash
docker-compose up --build
```

### Production Deployment
```bash
docker-compose up -d
```

### Stop Services
```bash
docker-compose down
```

### Clean Reset (Remove volumes)
```bash
docker-compose down -v
```

## 📈 Future Enhancements

- [ ] Advanced search and filtering
- [ ] Payment gateway integration
- [ ] Email notifications for booking status
- [ ] Lease management system
- [ ] Chat support between users and admin
- [ ] Mobile app development
- [ ] Unit testing and CI/CD pipeline
- [ ] Multi-tower/building support
- [ ] Occupancy analytics dashboard
- [ ] Document upload for KYC

## 👥 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is created for educational and portfolio purposes.

## 📧 Contact

Your Name - shiwaniraj203@gmail.com

Project Link: [https://github.com/yourusername/dwellhub](https://github.com/yourusername/dwellhub)

---

## 🎓 Skills Demonstrated

This project showcases proficiency in:
- Full-stack web development
- Modern JavaScript frameworks (Angular)
- Backend API development (Python/Flask)
- Database design and management (PostgreSQL)
- Authentication and authorization (JWT)
- Containerization and deployment (Docker)
- RESTful API design
- Responsive UI design (Tailwind CSS)
- Git version control
- Software architecture and design patterns

**Built with ❤️ for learning and portfolio development**