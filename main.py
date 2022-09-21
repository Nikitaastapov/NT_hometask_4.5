import datetime
import requests
import os

path = '' #прописать путь для файла
path_2 = os.getcwd()


def logs_path(path):
    def logger (old_function):
        
        
        
        def new_function (param):
            func_name = f'{old_function.__name__}'
            args = f'{param}'
            date_time = str(datetime.datetime.now())
            result = f'{old_function(param)}'
            logs = f'date_time:{date_time}, func_name:{func_name}, args:{args}, result:{result}'
            
            file_path = f'{path}/logs.txt'
            with open (file_path, 'a') as logs_file:
                logs_file.write(logs+'\n')
            
            return  logs
        
        return new_function
    return logger


@logs_path(path_2) #изменить на path, для определния места расположения файла

def get_swapi_people(people_id):
    
    
    return requests.get(f'https://swapi.dev/api/people/{people_id}').json()['name']


for i in range(1,10):
    print(get_swapi_people(i))
