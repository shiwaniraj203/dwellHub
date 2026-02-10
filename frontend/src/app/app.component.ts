import { Component } from '@angular/core';
import { RouterOutlet, Router, RouterLink } from '@angular/router';
import { CommonModule } from '@angular/common';
import { AuthService } from './auth.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, CommonModule, RouterLink],
  template: `
    <div class="min-h-screen bg-gray-50">
      <nav class="bg-blue-600 text-white shadow-lg">
        <div class="container mx-auto px-4 py-4">
          <div class="flex justify-between items-center">
            <h1 class="text-2xl font-bold">DwellHub</h1>
            <div class="flex gap-4" *ngIf="isLoggedIn()">
              <a routerLink="/apartments" class="hover:text-blue-200">Apartments</a>
              <a routerLink="/bookings" class="hover:text-blue-200" *ngIf="!isAdmin()">My Bookings</a>
              <a routerLink="/admin" class="hover:text-blue-200" *ngIf="isAdmin()">Admin</a>
              <button (click)="logout()" class="hover:text-blue-200">Logout</button>
            </div>
          </div>
        </div>
      </nav>
      <router-outlet></router-outlet>
    </div>
  `
})
export class AppComponent {
  constructor(
    private authService: AuthService,
    private router: Router
  ) {}

  isLoggedIn(): boolean {
    return this.authService.isLoggedIn();
  }

  isAdmin(): boolean {
    return this.authService.isAdmin();
  }

  logout(): void {
    this.authService.logout();
    this.router.navigate(['/login']);
  }
}