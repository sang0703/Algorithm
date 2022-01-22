import json


def max_revenue(movies):
    pass 
    # 여기에 코드를 작성합니다.
    max_title = ''
    max = 0
    for movie in movies:
        id = movie.get('id')
        id_json ='data/movies/' + str(id) + '.json'
        budget_json = open(id_json, encoding='UTF8')
        budget_list = json.load(budget_json)
        budget_val = budget_list.get('revenue')
    
        if budget_val > max:
            max_title = budget_list.get('title')
            max = budget_val
            
    return max_title     
        
 
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))