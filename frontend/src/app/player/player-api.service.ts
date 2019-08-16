import { Injectable } from "@angular/core";
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Player } from './player.model';
import { API_URL } from '../env'


@Injectable()
export class PlayerApiService {

    constructor(private http: HttpClient) {}

    private static handleError(err: HttpErrorResponse | any) {
        return Observable.throw(err.message || 'Error: Unable to complete request.')
    }

    public getPlayers(): Observable<Player> {
        return this.http.get<Player>(`${API_URL}/test`);
    }
}