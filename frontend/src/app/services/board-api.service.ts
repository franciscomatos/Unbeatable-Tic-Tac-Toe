import { Injectable } from "@angular/core";
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Board } from '../dataTypes/board.model';
import { API_URL_BOARD, API_URL_WIN, API_URL_NEW_GAME} from '../env'

@Injectable()
export class BoardApiService {

    constructor(private http: HttpClient) {}

    private static handleError(err: HttpErrorResponse | any) {
        return Observable.throw(err.message || 'Error: Unable to complete request.')
    }

    public resetGame(): Observable<Board> {
        return this.http.get<Board>(`${API_URL_NEW_GAME}`);
    }

    public getBoard(): Observable<Board> {
        return this.http.get<Board>(`${API_URL_BOARD}`);
    }

    public checkWin(): Observable<Boolean> {
        return this.http.get<Boolean>(`${API_URL_WIN}`);
    }
} 