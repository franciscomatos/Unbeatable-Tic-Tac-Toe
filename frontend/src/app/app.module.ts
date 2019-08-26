import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { BoardApiService } from './board/board-api.service';
import { MoveApiService } from './move/move-api.service';
import { GameComponent } from './game/game.component';
import { MainScreenComponent } from './main-screen/main-screen.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';


@NgModule({
  declarations: [
    AppComponent,
    GameComponent,
    MainScreenComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    NgbModule ],
  providers: [BoardApiService, MoveApiService],
  bootstrap: [AppComponent]
})
export class AppModule { }
