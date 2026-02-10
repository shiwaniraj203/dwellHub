import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-bookings',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './bookings.component.html'
})
export class BookingsComponent implements OnInit {
  bookings: any[] = [];

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.loadBookings();
  }

  loadBookings(): void {
    this.apiService.getMyBookings().subscribe({
      next: (res) => {
        this.bookings = res;
      },
      error: (err) => {
        console.error('Error loading bookings', err);
      }
    });
  }
}