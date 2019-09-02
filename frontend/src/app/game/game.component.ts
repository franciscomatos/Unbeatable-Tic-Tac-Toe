import { Component, OnInit } from '@angular/core';
import { Board } from '../dataTypes/board.model';
import { Subscription } from 'rxjs';
import { BoardApiService } from '../services/board-api.service';
import { MoveApiService } from '../services/move-api.service';
import { Move } from '../dataTypes/move.model';
import {ActivatedRoute} from "@angular/router";

@Component({
  selector: 'app-game',
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.css']
})
export class GameComponent implements OnInit {

  playerName: string;
  playerToken: string;
  difficulty: string;

  turn: boolean;
  counter: number;

  winSubs: Subscription;
  win: number;
  winStatus: string;

  boardSubs: Subscription;
  board: Board;

  winner: string = 'not yet';

  images: { [id: string] : string; } = { ['X'] : '../../assets/cross.png', ['O'] : '../../assets/circle.png', [''] : ''};
  winLabel: { [id: number] : string } = { [0] : "It's a Tie!", [1] : 'You Won!', [2] : 'Nothing', [3] : 'You Lost!'};

  constructor(private route: ActivatedRoute, private boardService: BoardApiService, private moveService: MoveApiService) { 
    this.turn = true;
    this.win = 2;
    this.winStatus = this.winLabel[this.win];
    this.counter = 0;

    this.playerName = this.route.snapshot.paramMap.get('name');
    this.playerToken = this.route.snapshot.paramMap.get('token');
    this.difficulty = this.route.snapshot.paramMap.get('difficulty');
  }

  ngOnInit() {
    this.getBoard();
  }

  ngOnDestroy() {
    this.boardSubs.unsubscribe();
  }

  newGame() {
    console.log('entrou na função');
    this.boardSubs = this.boardService.resetGame().subscribe(res => {
      this.board = res
      this.turn = true
      this.win = 2
      this.winStatus = this.winLabel[this.win]
      this.counter = 0;}, console.error);
  }

  getBoard() {
    this.boardSubs = this.boardService.getBoard().subscribe(res => {this.board = res;}, console.error);
  }

  changeBoard(position: any) {
    var i: number;
    var j: number;
    for(i = 0; i < 3; i++)
      for(j = 0; j < 3; j++)
        if(this.board.board[i][j] == position) this.board.board[i][j] = this.playerToken; 
  }

  selectPosition(position: any) {
    if (this.turn && this.win == 2) {
      this.changeBoard(position); // to avoid delay in the first play
      this.turn = false // player cannot play 2 times in a row
      var new_move = new Move(position, 0);
      this.boardSubs = this.moveService.postMove(new_move).subscribe(res => {
        this.board = this.board
        this.counter++
        this.checkWin()
        this.opponentMove()
        ;}, console.error);
    }
  }

  opponentMove() {
    console.log(this.counter);
    if (!this.turn && this.counter != 9) {
      this.boardSubs = this.moveService.opponentMove().subscribe(res => {
        this.board = res
        this.turn = true
        this.counter++
        this.checkWin();}, console.error);
    }
  }

  checkWin() {
    this.winSubs = this.boardService.checkWin().subscribe(res => {
      this.win = res
      if(this.win == 1 && this.turn) this.win = 3
      this.winStatus = this.winLabel[this.win]
      ;}, console.error);
    }
}
