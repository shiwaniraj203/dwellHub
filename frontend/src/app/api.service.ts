import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { AuthService } from './auth.service';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private baseUrl = 'http://localhost:5000/api';

  constructor(
    private http: HttpClient,
    private authService: AuthService
  ) {}

  private getHeaders(): HttpHeaders {
    const token = this.authService.getToken();
    return new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': token ? `Bearer ${token}` : ''
    });
  }

  register(data: any): Observable<any> {
    return this.http.post(`${this.baseUrl}/register`, data);
  }

  login(data: any): Observable<any> {
    return this.http.post(`${this.baseUrl}/login`, data);
  }

  // PUBLIC - NO AUTH NEEDED
  getApartments(): Observable<any> {
    return this.http.get(`${this.baseUrl}/apartments`);
  }

  createApartment(data: any): Observable<any> {
    return this.http.post(`${this.baseUrl}/apartments`, data, { headers: this.getHeaders() });
  }

  updateApartment(id: number, data: any): Observable<any> {
    return this.http.put(`${this.baseUrl}/apartments/${id}`, data, { headers: this.getHeaders() });
  }

  deleteApartment(id: number): Observable<any> {
    return this.http.delete(`${this.baseUrl}/apartments/${id}`, { headers: this.getHeaders() });
  }

  createBooking(apartmentId: number): Observable<any> {
    return this.http.post(`${this.baseUrl}/bookings`, { apartment_id: apartmentId }, { headers: this.getHeaders() });
  }

  getMyBookings(): Observable<any> {
    return this.http.get(`${this.baseUrl}/bookings/my`, { headers: this.getHeaders() });
  }

  getAllBookings(): Observable<any> {
    return this.http.get(`${this.baseUrl}/bookings/all`, { headers: this.getHeaders() });
  }

  updateBookingStatus(id: number, status: string): Observable<any> {
    return this.http.put(`${this.baseUrl}/bookings/${id}/status`, { status }, { headers: this.getHeaders() });
  }
}