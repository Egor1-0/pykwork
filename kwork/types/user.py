from typing import List, Optional

from pydantic import BaseModel

from kwork.types.achievement import Achievement
from kwork.types.kwork_object import KworkObject
from kwork.types.portfolio import PortfolioItem
from kwork.types.review import Review


class User(BaseModel):
    id: str = None
    username: str = None
    status: str = None
    fullname: str = None
    profilepicture: str = None
    description: str = None
    slogan: str = None
    location: str = None
    rating: float = None
    rating_count: int = None
    level_description: str = None
    good_reviews: int = None
    bad_reviews: int = None
    online: bool = None
    live_date: int = None
    cover: str = None
    custom_request_min_budget: int = None
    is_allow_custom_request: int = None
    order_done_persent: int = None
    order_done_intime_persent: int = None
    order_done_repeat_persent: int = None
    timezoneId: int = None
    blocked_by_user: bool = None
    allowedDialog: bool = None
    addtime: int = None
    achievments_list: List[Achievement] = None
    completed_orders_count: int
    specialization: Optional[str] = None
    profession: Optional[str] = None
    kworks_count: int
    kworks: List[KworkObject]
    portfolio_list: Optional[List[PortfolioItem]] = None
    reviews: Optional[List[Review]] = None


# data = {'id': 15580936, 'username': 'BB_Merodzh', 'status': 'active', 'fullname': 'Бабаджанов Меродж',
#         'profilepicture': 'https://cdn-edge.kwork.ru/files/avatar/big/41/15580936-5.jpg',
#         'description': 'Привет! Я веб-разработчик с опытом работы на React Native, HTML, CSS и JavaScript, а также в технологиях ReactJS, TypeScript, и Git. Я имею опыт в создании качественных веб-страниц, пользовательских интерфейсов.\nЯ использую React Native и ReactJS для создания интерактивных пользовательских интерфейсов и мобильных приложений, а TypeScript помогает мне писать более надежный и понятный код. Я также владею Git, что позволяет мне эффективно управлять кодом и контролировать версии.\nЯ готов взяться за ваш проект, чтобы создать высококачественные и профессиональные веб-страницы. Свяжитесь со мной, если у вас есть вопросы или вы хотите обсудить свой проект с надежным веб-разработчиком! Надеюсь на ваш отклик.',
#         'slogan': '', 'location': 'Санкт-Петербург', 'rating': '0.0', 'rating_count': 0, 'level_description': '',
#         'good_reviews': 0, 'bad_reviews': 0, 'reviews_count': 0, 'online': False, 'live_date': 1741533005,
#         'cover': 'https://cdn-edge.kwork.ru/files/cover/41/15580936-1726164675_x1.jpg',
#         'custom_request_min_budget': 500, 'is_allow_custom_request': False, 'order_done_persent': 0,
#         'order_done_intime_persent': 0, 'order_done_repeat_persent': 0, 'timezoneId': 1, 'blocked_by_user': False,
#         'allowedDialog': True, 'addtime': 1690881101, 'achievments_list': [], 'completed_orders_count': 0,
#         'specialization': 'Фронтэнд и Бэкенд-разработчик', 'profession': 'Фронтэнд и Бэкенд-разработчик',
#         'kworks_count': 0, 'kworks': [], 'portfolio_list': [
#         {'id': 14148380, 'title': 'Работа №13', 'order_id': None, 'category_id': 37, 'category_name': 'Создание сайта',
#          'type': 'photo', 'photo': 'https://cdn-edge.kwork.ru/files/portfolio/t3/73/cover-14148380-1726406745.jpg',
#          'video': None, 'views': 1, 'views_dirty': 3, 'comments_count': 0, 'images': [{
#             'original': 'https://cdn-edge.kwork.ru/files/portfolio/t0/63/010e06c3ed97eae9ed36287d1b466a952e0ae526-1726406898.jpg',
#             'link': 'https://cdn-edge.kwork.ru/files/portfolio/t3/63/010e06c3ed97eae9ed36287d1b466a952e0ae526-1726406898.jpg',
#             'thumbnail': 'https://cdn-edge.kwork.ru/files/portfolio/t4/63/010e06c3ed97eae9ed36287d1b466a952e0ae526-1726406898.jpg',
#             'position': 0}], 'videos': [],
#          'audios': [], 'pdf': [], 'duplicate_from': None, 'pined_at_timestamp': 0},
#         {'id': 14148375, 'title': 'Работа №11', 'order_id': None, 'category_id': 37, 'category_name': 'Создание сайта',
#          'type': 'photo', 'photo': 'https://cdn-edge.kwork.ru/files/portfolio/t3/35/cover-14148375-1726406723.jpg',
#          'video': None, 'views': 1, 'views_dirty': 3, 'comments_count': 0, 'images': [{
#             'original': 'https://cdn-edge.kwork.ru/files/portfolio/t0/73/e7fbce00a3283c20143a4f47f29e2215f5567bbd-1726406898.jpg',
#             'link': 'https://cdn-edge.kwork.ru/files/portfolio/t3/73/e7fbce00a3283c20143a4f47f29e2215f5567bbd-1726406898.jpg',
#             'thumbnail': 'https://cdn-edge.kwork.ru/files/portfolio/t4/73/e7fbce00a3283c20143a4f47f29e2215f5567bbd-1726406898.jpg',
#             'position': 0}], 'videos': [],
#          'audios': [], 'pdf': [], 'duplicate_from': None, 'pined_at_timestamp': 0},
#         {'id': 14148344, 'title': 'Работа №10', 'order_id': None, 'category_id': 37, 'category_name': 'Создание сайта',
#          'type': 'photo', 'photo': 'https://cdn-edge.kwork.ru/files/portfolio/t3/48/cover-14148344-1726406506.jpg',
#          'video': None, 'views': 1, 'views_dirty': 4, 'comments_count': 0, 'images': [{
#             'original': 'https://cdn-edge.kwork.ru/files/portfolio/t0/34/ecfd8fb803fe48aeab5892e5050ab865bd80c20e-1727015478.jpg',
#             'link': 'https://cdn-edge.kwork.ru/files/portfolio/t3/34/ecfd8fb803fe48aeab5892e5050ab865bd80c20e-1727015478.jpg',
#             'thumbnail': 'https://cdn-edge.kwork.ru/files/portfolio/t4/34/ecfd8fb803fe48aeab5892e5050ab865bd80c20e-1727015478.jpg',
#             'position': 0}, {
#             'original': 'https://cdn-edge.kwork.ru/files/portfolio/t0/11/14e6a778012baaf6f5d7f90cc021e2d6d3e65d5f-1726406577.jpg',
#             'link': 'https://cdn-edge.kwork.ru/files/portfolio/t3/11/14e6a778012baaf6f5d7f90cc021e2d6d3e65d5f-1726406577.jpg',
#             'thumbnail': 'https://cdn-edge.kwork.ru/files/portfolio/t4/11/14e6a778012baaf6f5d7f90cc021e2d6d3e65d5f-1726406577.jpg',
#             'position': 1}, {
#             'original': 'https://cdn-edge.kwork.ru/files/portfolio/t0/13/721c19dea7416adc56e289574ca998227482221c-1726406632.jpg',
#             'link': 'https://cdn-edge.kwork.ru/files/portfolio/t3/13/721c19dea7416adc56e289574ca998227482221c-1726406632.jpg',
#             'thumbnail': 'https://cdn-edge.kwork.ru/files/portfolio/t4/13/721c19dea7416adc56e289574ca998227482221c-1726406632.jpg',
#             'position': 2}, {
#             'original': 'https://cdn-edge.kwork.ru/files/portfolio/t0/65/cec00c533cb8b848c20487ae7b87fc23b05c0059-1726406633.jpg',
#             'link': 'https://cdn-edge.kwork.ru/files/portfolio/t3/65/cec00c533cb8b848c20487ae7b87fc23b05c0059-1726406633.jpg',
#             'thumbnail': 'https://cdn-edge.kwork.ru/files/portfolio/t4/65/cec00c533cb8b848c20487ae7b87fc23b05c0059-1726406633.jpg',
#             'position': 3}], 'videos': [],
#          'audios': [], 'pdf': [], 'duplicate_from': None, 'pined_at_timestamp': 0},
#         {'id': 14148296, 'title': 'Работа №9', 'order_id': None, 'category_id': 37, 'category_name': 'Создание сайта',
#          'type': 'photo', 'photo': 'https://cdn-edge.kwork.ru/files/portfolio/t3/52/cover-14148296-1726406259.jpg',
#          'video': None, 'views': 1, 'views_dirty': 4, 'comments_count': 0, 'images': [{
#             'original': 'https://cdn-edge.kwork.ru/files/portfolio/t0/97/cc9a8b560ec84f92d15d184f163c5f46ab1f3920-1726406896.jpg',
#             'link': 'https://cdn-edge.kwork.ru/files/portfolio/t3/97/cc9a8b560ec84f92d15d184f163c5f46ab1f3920-1726406896.jpg',
#             'thumbnail': 'https://cdn-edge.kwork.ru/files/portfolio/t4/97/cc9a8b560ec84f92d15d184f163c5f46ab1f3920-1726406896.jpg',
#             'position': 0}, {
#             'original': 'https://cdn-edge.kwork.ru/files/portfolio/t0/29/f50fd11ab7bad4fa65be491f8ce0c4f0256d0f2e-1726406246.jpg',
#             'link': 'https://cdn-edge.kwork.ru/files/portfolio/t3/29/f50fd11ab7bad4fa65be491f8ce0c4f0256d0f2e-1726406246.jpg',
#             'thumbnail': 'https://cdn-edge.kwork.ru/files/portfolio/t4/29/f50fd11ab7bad4fa65be491f8ce0c4f0256d0f2e-1726406246.jpg',
#             'position': 1}], 'videos': [],
#          'audios': [], 'pdf': [], 'duplicate_from': None, 'pined_at_timestamp': 0},
#         {'id': 14148281, 'title': 'Работа №7', 'order_id': None, 'category_id': 37, 'category_name': 'Создание сайта',
#          'type': 'photo', 'photo': 'https://cdn-edge.kwork.ru/files/portfolio/t3/58/cover-14148281-1726406153.jpg',
#          'video': None, 'views': 1, 'views_dirty': 3, 'comments_count': 0, 'images': [{
#             'original': 'https://cdn-edge.kwork.ru/files/portfolio/t0/84/f2e9f3b75270288e77c48c69637ac3f17b505aea-1726406896.jpg',
#             'link': 'https://cdn-edge.kwork.ru/files/portfolio/t3/84/f2e9f3b75270288e77c48c69637ac3f17b505aea-1726406896.jpg',
#             'thumbnail': 'https://cdn-edge.kwork.ru/files/portfolio/t4/84/f2e9f3b75270288e77c48c69637ac3f17b505aea-1726406896.jpg',
#             'position': 0}, {
#             'original': 'https://cdn-edge.kwork.ru/files/portfolio/t0/80/752e8c0de2fc6bba69a83ce289717af3f25a8afa-1726406155.jpg',
#             'link': 'https://cdn-edge.kwork.ru/files/portfolio/t3/80/752e8c0de2fc6bba69a83ce289717af3f25a8afa-1726406155.jpg',
#             'thumbnail': 'https://cdn-edge.kwork.ru/files/portfolio/t4/80/752e8c0de2fc6bba69a83ce289717af3f25a8afa-1726406155.jpg',
#             'position': 1}, {
#             'original': 'https://cdn-edge.kwork.ru/files/portfolio/t0/18/4b7fdafb8c3a0b3e9e34c5dc1533b742657a1c1d-1726406156.jpg',
#             'link': 'https://cdn-edge.kwork.ru/files/portfolio/t3/18/4b7fdafb8c3a0b3e9e34c5dc1533b742657a1c1d-1726406156.jpg',
#             'thumbnail': 'https://cdn-edge.kwork.ru/files/portfolio/t4/18/4b7fdafb8c3a0b3e9e34c5dc1533b742657a1c1d-1726406156.jpg',
#             'position': 2}], 'videos': [],
#          'audios': [], 'pdf': [], 'duplicate_from': None, 'pined_at_timestamp': 0}], 'reviews': None,
#         'skills': [{'id': 2970250, 'name': 'SCSS/SASS'}, {'id': 2970290, 'name': 'Python'},
#                    {'id': 2970247, 'name': 'Figma'}, {'id': 4739791, 'name': 'Node.js'},
#                    {'id': 4739793, 'name': 'Redux'}, {'id': 4739795, 'name': 'React Native'},
#                    {'id': 4739823, 'name': 'React'}, {'id': 4739820, 'name': 'Git/Github'},
#                    {'id': 2970237, 'name': 'CSS'}, {'id': 2970234, 'name': 'HTML'},
#                    {'id': 2970244, 'name': 'Java Script'}], 'is_verified_worker': False, 'note': []}
#
# # Преобразование JSON в объект Pydantic
# user_profile = User.parse_obj(data)
#
# # Вывод данных
# print(user_profile)
