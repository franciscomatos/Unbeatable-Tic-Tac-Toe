import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Game } from '../dataTypes/game.model';
import { API_URL_BEGIN} from '../env'
import { HttpHeaders } from '@angular/common/http';


const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type':  'application/json',
    'Authorization': 'my-auth-token'
  })
};

@Injectable({
  providedIn: 'root'
})
export class GameApiService {

  constructor(private http: HttpClient) {}
  
  private static handleError(err: HttpErrorResponse | any) {
    return Observable.throw(err.message || 'Error: Unable to complete request.')
  }

  public beginGame(game: Game): Observable<Game> {
    return this.http.post<Game>(`${API_URL_BEGIN}`, game, httpOptions);
  }
}
