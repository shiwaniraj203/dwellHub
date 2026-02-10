import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-admin',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './admin.component.html'
})
export class AdminComponent implements OnInit {
  apartments: any[] = [];
  bookings: any[] = [];
  showApartmentForm = false;
  editingApartment: any = null;
  
  apartmentForm = {
    title: '',
    location: '',
    price: 0,
    amenities: ''
  };

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.loadApartments();
    this.loadBookings();
  }

  loadApartments(): void {
    this.apiService.getApartments().subscribe({
      next: (res) => {
        this.apartments = res;
      }
    });
  }

  loadBookings(): void {
    this.apiService.getAllBookings().subscribe({
      next: (res) => {
        this.bookings = res;
      }
    });
  }

  openApartmentForm(): void {
    this.showApartmentForm = true;
    this.editingApartment = null;
    this.apartmentForm = { title: '', location: '', price: 0, amenities: '' };
  }

  editApartment(apt: any): void {
    this.showApartmentForm = true;
    this.editingApartment = apt;
    this.apartmentForm = { ...apt };
  }

  saveApartment(): void {
    if (this.editingApartment) {
      this.apiService.updateApartment(this.editingApartment.id, this.apartmentForm).subscribe({
        next: () => {
          this.loadApartments();
          this.showApartmentForm = false;
        }
      });
    } else {
      this.apiService.createApartment(this.apartmentForm).subscribe({
        next: () => {
          this.loadApartments();
          this.showApartmentForm = false;
        }
      });
    }
  }

  deleteApartment(id: number): void {
    if (confirm('Delete this apartment?')) {
      this.apiService.deleteApartment(id).subscribe({
        next: () => {
          this.loadApartments();
        }
      });
    }
  }

  updateBookingStatus(id: number, status: string): void {
    this.apiService.updateBookingStatus(id, status).subscribe({
      next: () => {
        this.loadBookings();
      }
    });
  }
}