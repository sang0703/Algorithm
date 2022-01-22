import json
from pprint import pprint


def movie_info(movie, genres):
    pass 
    # 여기에 코드를 작성합니다.
    genres_name = []

    id = movie.get('id')
    title = movie.get('title')
    poster_path = movie.get('poster_path')
    vote_average = movie.get('vote_average')
    overview = movie.get('overview')
    genre_ids = movie.get('genre_ids')

    for genre in genres:                         # 장르 분리
        for id in genre_ids:                     # 분리
            if genre['id'] == id:                # t/f로 확인
                genres_name.append(genre.get('name'))

    result = {
        'genre_name': genres_name, 
        'id': id, 
        'overview': overview,
        'poster_path' : poster_path, 
        'title' : title, 
        'vote_average' : vote_average
        
    }

    return(result)
   
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))