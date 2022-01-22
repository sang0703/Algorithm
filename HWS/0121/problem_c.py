import json
from pprint import pprint


def movie_info(movies, genres):
    pass 
    # 여기에 코드를 작성합니다.  
    results = []

    for movie in movies:

        genres_name = []

        id = movie.get('id')
        title = movie.get('title')
        poster_path = movie.get('poster_path')
        vote_average = movie.get('vote_average')
        overview = movie.get('overview')
        genre_ids = movie.get('genre_ids')

        for genre in genres:
            for id in genre_ids:
                if genre['id'] == id:
                    genres_name.append(genre.get('name'))

        result = {
            'genre_name': genres_name, 
            'id': id, 
            'overview': overview,
            'poster_path' : poster_path, 
            'title' : title, 
            'vote_average' : vote_average
        
        }

        results.append(result)
    
    return result   
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))