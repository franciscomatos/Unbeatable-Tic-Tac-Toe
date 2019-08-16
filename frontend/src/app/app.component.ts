import { Component, OnInit, OnDestroy } from '@angular/core';
import { Player } from './player/player.model';
import { Subscription } from 'rxjs';
import { PlayerApiService } from './player/player-api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'app';
  playerSubs: Subscription;
  player: Player;

  constructor(private playerApi: PlayerApiService) {}

  ngOnInit() {
    this.playerSubs = this.playerApi.getPlayers().subscribe(res => {this.player = res;}, console.error);
  }

  ngOnDestroy() {
    this.playerSubs.unsubscribe();
  }
}
