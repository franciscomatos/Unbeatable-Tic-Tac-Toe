import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { MainScreenComponent } from './main-screen/main-screen.component';
import { GameComponent } from './game/game.component';

const routes: Routes = [
  {path: 'game', component: GameComponent}, 
  {path: 'mainScreen', component: MainScreenComponent}, 
  {path: '', redirectTo: '/mainScreen', pathMatch:'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
