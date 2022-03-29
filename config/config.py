from dataclasses import dataclass


class Config:
    BASE_URL = 'https://yandex.ru/'
    TIME_WAIT = 10  # Time to wait for the visibility of the element
    HOME_PAGE_TITLE = "Яндекс"
    SEARCH_TEXT = "qsqs"
    TENSOR_LINK = "tensor.ru"
