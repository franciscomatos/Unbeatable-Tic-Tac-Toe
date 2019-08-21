import { Component, OnInit } from '@angular/core';
import { Board } from '../board/board.model';
import { Subscription } from 'rxjs';
import { BoardApiService } from '../board/board-api.service';
import { MoveApiService } from '../move/move-api.service';
import { Move } from '../move/move.model';
import { Win } from '../board/win.model';

@Component({
  selector: 'app-game',
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.css']
})
export class GameComponent implements OnInit {

  turn: boolean;
  
  winSubs: Subscription;
  win: Boolean = false;

  boardSubs: Subscription;
  board: Board;

  winner: string = 'not yet';

  constructor(private boardService: BoardApiService, private moveService: MoveApiService) { 
    this.turn = true;
  }

  ngOnInit() {
    this.getBoard();
  }

  ngOnDestroy() {
    this.boardSubs.unsubscribe();
  }


  getBoard() {
    this.boardSubs = this.boardService.getBoard().subscribe(res => {this.board = res;}, console.error);
  }

  selectPosition(position: any) {
    console.log(this.win)
    if (this.turn && !this.win) {
      this.turn = false // player cannot play 2 times in a row
      var new_move = new Move(position, 0);
      this.boardSubs = this.moveService.postMove(new_move).subscribe(res => {
        this.board = this.board
        this.opponentMove()
        this.checkWin();}, console.error);
    }
  }

  opponentMove() {
    if (!this.turn) {
      this.boardSubs = this.moveService.opponentMove().subscribe(res => {
        this.board = res
        this.turn = true
        this.checkWin();}, console.error);
    }
  }

  checkWin() {
    this.winSubs = this.boardService.checkWin().subscribe(res => {this.win = res;}, console.error);
    console.log(this.win);
    if(this.win) this.winner = 'Victory!'
  }
}
