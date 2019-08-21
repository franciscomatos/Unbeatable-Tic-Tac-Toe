import { Injectable } from "@angular/core";
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Board } from './board.model';
import { API_URL_BOARD, API_URL_WIN } from '../env'
import { Win } from './win.model';

@Injectable()
export class BoardApiService {

    constructor(private http: HttpClient) {}

    private static handleError(err: HttpErrorResponse | any) {
        return Observable.throw(err.message || 'Error: Unable to complete request.')
    }

    public getBoard(): Observable<Board> {
        return this.http.get<Board>(`${API_URL_BOARD}`);
    }

    public checkWin(): Observable<Boolean> {
        return this.http.get<Boolean>(`${API_URL_WIN}`);
    }
} 