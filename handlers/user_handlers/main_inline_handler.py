from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
from aiogram import Router
from aiogram.types import InlineQuery
from utils.youtube_utils.search_util import *

router = Router()


@router.inline_query()
async def show_user_links(inline_query: InlineQuery):
    results = []
    if len(inline_query.query) > 3:
        videos = search_videos_by_title(inline_query.query)
        for i in videos:
            results.append(InlineQueryResultArticle(
            id=f'{i[1]}',
            title=f'{i[0]}',
            description=f'{i[3]}',
            thumbnail_url=f'{i[2]}',
            input_message_content=InputTextMessageContent(
                message_text=f'<b><a href="https://www.youtube.com/watch?v={i[1]}">С вами поделились видео с YouTube</a></b>',
                parse_mode="HTML",
            )
        ))
        await inline_query.answer(results, is_personal=True)
