# Страдания Калюжного Николая с 11 когорты
import requests
import data
import config


def post_new_order(body):
    # POST Запрос на создание заказа
    return requests.post(config.URL_SERV + config.CREATE_ORD,
                         json=body,
                         headers=data.HEADERS)


def get_number_order(track):
    # GET Получение информации о заказе
    params = {'t': track}
    return requests.get(config.URL_SERV + config.GET_ORDER,
                        params=params,
                        headers=data.HEADERS)
