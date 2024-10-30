import asyncio
import aiohttp
from bs4 import BeautifulSoup

url = 'https://www.coindesk.com/price/bitcoin'

async def fetch():
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False) as response:  # ssl=False для отладки
            return await response.text()

async def get_bitcoin_course():
    page_content = await fetch()
    soup = BeautifulSoup(page_content, 'html.parser')

    # Пытаемся найти элемент, а затем получаем его текст
    element = soup.find(class_='Noto_Sans_2xl_Sans-700-2xl')
    if element:
        return element.text
    else:
        return "Курс биткоина не найден"

# Для тестирования асинхронного вызова
if __name__ == "__main__":
    result = asyncio.run(get_bitcoin_course())
    print(result)
