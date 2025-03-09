from kwork import Kwork
from kwork.types import Actor, User, Connects
import logging
import asyncio

logging.basicConfig(level=logging.INFO)


async def main():
    api = Kwork(login="login", password="password")

    # Если "Необходимо ввести последние 4 цифры номера телефона."
    # api = Kwork(login="login", password="password", phone_last="0102")

    # Можно использовать socks5 прокси
    # api = Kwork(login="login", password="password", proxy="socks5://208.113.220.250:3420")

    # Получение своего профиля
    me: Actor = await api.get_me()
    print(me)

    # Получения профиля юзера
    user: User = await api.get_user(user_id=1456898)
    print(user)

    # Получение ваших коннектов
    connects: Connects = await api.get_connects()
    print(connects)

    # Получения всех диалогов на аккаунте
    all_dialogs = await api.get_all_dialogs()
    print(all_dialogs)

    # Получение всего диалога с указанным юзером
    dialog_with_user = await api.get_dialog_with_user(user_name="avkvl")
    print(dialog_with_user)

    # Получение категорий заказов на бирже, для дальнейшего поиска проектов по их id
    categories = await api.get_categories()
    print(categories)

    # получение категорий, добавленных в избранное
    favorite_categories = await api.get_favorite_categories()
    print(favorite_categories)

    # Получение проектов с биржи по id категорий, которые можно получить из api.get_categories()
    projects = await api.get_projects(categories_ids=[41, 15])
    print(projects)

    # Получение ваших выполненных и отменённых заказов, где вы - работник
    worker_orders = await api.get_worker_orders()
    print(worker_orders)
    # Получение ваших выполненных и отменённых заказов, где вы - заказчик
    # payer_order = await api.get_payer_orders()
    # print(payer_order)
    #
    # # Отправляет сообщение
    # await api.send_message(user_id=123, text="привет!")
    #
    # # Удаляет сообщение
    # await api.delete_message(message_id=123)
    #
    # # У указанного recipient_id будет показываться что вы печатаете
    # await api.set_typing(recipient_id=123)
    #
    # # Делает вас оффлайн
    # await api.set_offline()
    #
    # # Получает уведомления
    # notifications = await api.get_notifications()
    # print(notifications)

    await api.logout()


asyncio.run(main())
