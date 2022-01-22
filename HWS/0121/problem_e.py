import json


def dec_movies(movies):
    pass 
    # 여기에 코드를 작성합니다.  
    dec_titles = []
    for movie in movies:
        id = movie.get('id')
        id_json = 'data/movies/' + str(id) + '.json'
        budget_json = open(id_json, encoding='UTF8')
        budget_list = json.load(budget_json)
        release_date = budget_list.get('release_date')

        year, month, day = map(int, release_date.split('-'))
        if month == 12:
            dec_titles.append(budget_list.get('title'))

    return dec_titles


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))