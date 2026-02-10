import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ApiService } from '../api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-apartments',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './apartments.component.html'
})
export class ApartmentsComponent implements OnInit {
  apartments: any[] = [];
  message = '';

  constructor(
    private apiService: ApiService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.loadApartments();
  }

  loadApartments(): void {
    this.apiService.getApartments().subscribe({
      next: (res) => {
        this.apartments = res;
      },
      error: (err) => {
        console.error('Error loading apartments', err);
      }
    });
  }

  bookApartment(apartmentId: number): void {
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