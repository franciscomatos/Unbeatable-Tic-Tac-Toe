import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { BoardApiService } from './services/board-api.service';
import { MoveApiService } from './services/move-api.service';
import { GameComponent } from './game/game.component';
import { MainScreenComponent } from './main-screen/main-screen.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatToolbarModule, MatIconModule, MatSidenavModule, MatListModule, MatButtonModule, MatMenuModule } from  '@angular/material';
import { MatFormFieldModule } from '@angular/material/form-field';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {MatNativeDateModule} from '@angular/material/core';
import {MatInputModule} from '@angular/material';
import {MatSelectModule} from '@angular/material/select';
import {MatRadioModule} from '@angular/material'
import {MatCardModule} from '@angular/material/card';
import { GameApiService } from './services/game-api.service';






@NgModule({
  declarations: [
    AppComponent,
    GameComponent,
    MainScreenComponent  ],
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
    MatMenuModule,
    MatFormFieldModule,
    FormsModule,
    ReactiveFormsModule,
    MatNativeDateModule,
    MatInputModule,
    MatSelectModule,
    MatRadioModule,
    MatCardModule
   ],
  providers: [BoardApiService, MoveApiService, GameApiService],
  bootstrap: [AppComponent]
})
export class AppModule { }
