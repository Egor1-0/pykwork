import logging
import urllib.parse

import aiohttp

from .types import Actor, User, Connects, Category, Dialog, InboxMessage, Order
from kwork.exceptions import KworkException

logger = logging.getLogger(__name__)


class KworkClient:
    def __init__(
            self,
            login: str,
            password: str,
            proxy: str | None = None,
            phone_last: str | None = None,
    ):
        connector: aiohttp.BaseConnector | None = None

        if proxy is not None:
            try:
                from aiohttp_socks import ProxyConnector
            except ImportError:
                raise ImportError(
                    "You have to install aiohttp_socks for using"
                    " proxy, make it by pip install aiohttp_socks"
                )
            connector = ProxyConnector.from_url(proxy)

        self.session = aiohttp.ClientSession(connector=connector)
        self.host = "https://api.kwork.ru/{}"
        self.login = login
        self.password = password
        self._token: str | None = None
        self.phone_last = phone_last

    @property
    async def token(self) -> str:
        if self._token is None:
            self._token = await self.get_token()
        return self._token

    async def api_request(
        self, method: str, api_method: str, **params
    ) -> dict:
        params = {k: v for k, v in params.items() if v is not None}
        logging.debug(
            f"making {method} request on /{api_method} with params - {params}"
        )
        async with self.session.request(
            method=method,
            url=self.host.format(api_method),
            headers={"Authorization": "Basic bW9iaWxlX2FwaTpxRnZmUmw3dw=="},
            params=params,
        ) as resp:
            if resp.content_type != "application/json":
                error_text: str = await resp.text()
                raise KworkException(error_text)
            json_response: dict = await resp.json()
            if not json_response["success"]:
                raise KworkException(json_response["error"])
            logging.debug(f"result of request on /{api_method} - {json_response}")
            return json_response

    async def close(self) -> None:
        await self.session.close()

    async def get_token(self) -> str:
        resp: dict = await self.api_request(
            method="post",
            api_method="signIn",
            login=self.login,
            password=self.password,
            phone_last=self.phone_last,
        )
        return resp["response"]["token"]

    async def logout(self) -> None:
        await self.api_request(
            method="post",
            api_method="logout",
            token=await self.token
        )
        await self.close()

    async def get_favorite_categories(self) -> list[Category]:
        categories = await self.api_request(
            method="post",
            api_method="favoriteCategories",
            token=await self.token
        )
        return [Category(**category) for category in categories["response"]]

    async def get_me(self) -> Actor:
        actor = await self.api_request(
            method="post", api_method="actor", token=await self.token
        )
        return Actor(**actor["response"])

    async def get_user(self, user_id: int) -> User:
        """
        :param user_id: you can find it in dialogs
        :return:
        """
        user = await self.api_request(
            method="post", api_method="user", id=user_id, token=await self.token
        )
        return User(**user["response"])

    async def set_typing(self, recipient_id: int) -> dict:
        resp = await self.api_request(
            method="post",
            api_method="typing",
            recipientId=recipient_id,
            token=await self.token,
        )
        return resp

    async def get_all_dialogs(self) -> list[Dialog]:
        page = 1
        dialogs: list[Dialog] = []

        while True:
            dialogs_page = await self.api_request(
                method="post",
                api_method="dialogs",
                filter="all",
                page=page,
                token=await self.token,
            )
            if not dialogs_page["response"]:
                break
            for dialog in dialogs_page["response"]:
                dialogs.append(Dialog(**dialog))
            page += 1

        return dialogs

    async def set_offline(self) -> dict:
        return await self.api_request(
            method="post", api_method="offline", token=await self.token
        )

    async def get_dialog_with_user(self, user_name: str) -> list[InboxMessage]:
        page = 1
        dialog: list[InboxMessage] = []

        while True:
            messages_dict: dict = await self.api_request(
                method="post",
                api_method="inboxes",
                username=user_name,
                page=page,
                token=await self.token,
            )
            if not messages_dict.get("response"):
                break
            for message in messages_dict["response"]:
                dialog.append(InboxMessage(**message))

            if page == messages_dict["paging"]["pages"]:
                break
            page += 1

        return dialog

    async def get_worker_orders(self) -> dict:
        return await self.api_request(
            method="post",
            api_method="workerOrders",
            filter="all",
            token=await self.token,
        )

    async def get_payer_orders(self) -> dict:
        return await self.api_request(
            method="post",
            api_method="payerOrders",
            filter="all",
            token=await self.token,
        )

    async def get_notifications(self) -> dict:
        return await self.api_request(
            method="post",
            api_method="notifications",
            token=await self.token,
        )

    async def get_categories(self) -> list[Category]:
        raw_categories = await self.api_request(
            method="post",
            api_method="categories",
            type="1",
            token=await self.token,
        )
        categories = []
        for dict_category in raw_categories["response"]:
            category = Category(**dict_category)
            categories.append(category)
        return categories

    async def get_connects(self) -> Connects:
        connects = await self.api_request(
            method="post",
            api_method="projects",
            categories="",
            token=await self.token,
        )
        return Connects(**connects["connects"])

    async def get_projects(
            self,
            categories_ids: list[int] | str | None = None,
            price_from: int | None = None,
            price_to: int | None = None,
            hiring_from: int | None = None,
            kworks_filter_from: int | None = None,
            kworks_filter_to: int | None = None,
            page: int | None = None,
            query: str | None = None,
    ) -> list[Order]:
        """
        categories_ids - Список ID рубрик через запятую, либо 'all' - для выборки по всем рубрикам.
         С пустым значением делает выборку по любимым рубрикам.
        price_from - Бюджет от (включительно)
        price_to - Бюджет до (включительно)
        hiring_from - Процент найма от
        kworks_filter_from - Количество предложений от (не включительно)
        kworks_filter_to - Количество предложений до (включительно)
        page - Страница выдачи
        query - Поисковая строка
        """
        if isinstance(categories_ids, list):
            categories_ids = ",".join(str(category) for category in categories_ids)

        raw_projects = await self.api_request(
            method="post",
            api_method="projects",
            categories=categories_ids,
            price_from=price_from,
            price_to=price_to,
            hiring_from=hiring_from,
            kworks_filter_from=kworks_filter_from,
            kworks_filter_to=kworks_filter_to,
            page=page,
            query=query,
            token=await self.token,
        )
        projects = []
        for dict_project in raw_projects["response"]:
            project = Order(**dict_project)
            projects.append(project)
        return projects

    async def get_channel(self) -> str:
        channel = await self.api_request(
            method="post", api_method="getChannel", token=await self.token
        )
        return channel["response"]["channel"]

    async def send_message(self, user_id: int, text: str) -> "json":
        logging.debug(f"Sending message for {user_id} with text - {text}")
        resp = await self.api_request(
            method='post',
            api_method='inboxCreate',
            user_id=user_id,
            text=urllib.parse.quote(text),
            token=await self.token,
        )
        json_resp = await resp.json()
        logging.debug(f"result of sending - {json_resp}")
        return json_resp

    async def delete_message(self, message_id) -> dict:
        return await self.api_request(
            method="post",
            api_method="inboxDelete",
            id=message_id,
            token=await self.token,
        )