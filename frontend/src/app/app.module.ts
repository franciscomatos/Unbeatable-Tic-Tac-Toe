import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { BoardApiService } from './board/board-api.service';
import { MoveApiService } from './move/move-api.service';
import { GameComponent } from './game/game.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatToolbarModule, MatIconModule, MatSidenavModule, MatListModule, MatButtonModule, MatMenuModule } from  '@angular/material';


@NgModule({
  declarations: [
    AppComponent,
    GameComponent  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    NgbModule,
    BrowserAnimationsModule,
    MatToolbarModule,
    MatSidenavModule,
    MatListModule,
    MatButtonModule,
    MatIconModule,
    MatMenuModule ],
  providers: [BoardApiService, MoveApiService],
  bootstrap: [AppComponent]
})
export class AppModule { }
