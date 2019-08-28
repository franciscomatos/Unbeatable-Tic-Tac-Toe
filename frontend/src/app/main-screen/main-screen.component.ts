import { Component, OnInit, Inject } from '@angular/core';
import { Game } from '../dataTypes/game.model';
import { GameApiService } from '../services/game-api.service';
import { Router, ActivatedRoute } from '@angular/router';
import { BoardApiService } from '../services/board-api.service';

@Component({
  selector: 'app-main-screen',
  templateUrl: './main-screen.component.html',
  styleUrls: ['./main-screen.component.css']
})
export class MainScreenComponent implements OnInit {

  selectedName: string;
  selectedSymbol: string;
  selectedDifficulty: string;

  symbols: string[] = ['X', 'O'];
  images: { [id: string] : string; } = {};

  difficulties: string[] = ['Easy', 'Normal', 'Unbeatable'];

  game: Game;

  gameService: GameApiService;

  constructor(@Inject(GameApiService) gameService: GameApiService, private router: Router, private actRouter: ActivatedRoute) { 
    this.images["X"] = "../../assets/cross.png";
    this.images["O"] = "../../assets/circle.png";
    this.gameService = gameService;
  }

  ngOnInit() {
  }

  begin() {
    var newGame = new Game(this.selectedName, this.selectedSymbol);
    this.gameService.beginGame(newGame).subscribe( res => {
      this.game = res
      this.router.navigateByUrl('/game')
      ;}, console.error);
  }

}
