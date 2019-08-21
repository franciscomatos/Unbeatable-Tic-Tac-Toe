import { Injectable } from "@angular/core";
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Move } from './move.model';
import { Board } from '../board/board.model';
import { API_URL_MOVE, API_URL_OPPONENT } from '../env'
import { HttpHeaders } from '@angular/common/http';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type':  'application/json',
    'Authorization': 'my-auth-token'
  })
};

@Injectable()
export class MoveApiService {

    constructor(private http: HttpClient) {}

    private static handleError(err: HttpErrorResponse | any) {
        return Observable.throw(err.message || 'Error: Unable to complete request.')
    }

    public postMove(move: Move): Observable<Board> {
        return this.http.post<Board>(API_URL_MOVE, move, httpOptions);
    }

    public opponentMove(): Observable<Board> {
        return this.http.get<Board>(`${API_URL_OPPONENT}`);
    }
} 