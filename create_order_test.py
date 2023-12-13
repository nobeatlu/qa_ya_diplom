# Страдания Калюжного Николая с 11 когорты
import main
import data


def test_create_and_get_info_order():
    # Создание заказа и получение информации
    response_create = main.post_new_order(data.ORDER_BODY)
    track = response_create.json().get('track')
    response_get_info = main.get_number_order(track)
    assert response_get_info.status_code == data.OK_STATUS
