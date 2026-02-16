import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ApiService } from '../api.service';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-apartments',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './apartments.component.html'
})
export class ApartmentsComponent implements OnInit {
  apartments: any[] = [];
  filteredApartments: any[] = [];
  message = '';
  
  searchLocation = '';
  maxPrice = 70000;

  constructor(
    private apiService: ApiService,
    private authService: AuthService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.loadApartments();
  }

  loadApartments(): void {
    this.apiService.getApartments().subscribe({
      next: (res) => {
        this.apartments = res;
        this.filteredApartments = res;
      },
      error: (err) => {
        console.error('Error loading apartments', err);
      }
    });
  }

  applyFilters(): void {
    this.filteredApartments = this.apartments.filter(apt => {
      if (!this.searchLocation || this.searchLocation.trim() === '') {
        return apt.price <= this.maxPrice;
      }
      
      const locationMatch = apt.location.toLowerCase().includes(this.searchLocation.toLowerCase());
      const priceMatch = apt.price <= this.maxPrice;
      
      return locationMatch && priceMatch;
    });
  }

  clearFilters(): void {
    this.searchLocation = '';
    this.maxPrice = 70000;
    this.filteredApartments = this.apartments;
  }

  bookApartment(apartmentId: number): void {
    // CHECK IF USER IS LOGGED IN
    if (!this.authService.isLoggedIn()) {
      this.message = 'Please login to book apartment';
      setTimeout(() => {
        this.router.navigate(['/login']);
      }, 1500);
      return;
    }

    // USER IS LOGGED IN - CREATE BOOKING
    this.apiService.createBooking(apartmentId).subscribe({
      next: (res) => {
        this.message = 'Booking created successfully!';
        setTimeout(() => this.message = '', 3000);
      },
      error: (err) => {
        this.message = 'Error creating booking';
        setTimeout(() => this.message = '', 3000);
      }
    });
  }
}