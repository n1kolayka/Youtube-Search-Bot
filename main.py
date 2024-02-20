from youtubesearchpython import VideosSearch


def search_videos_by_title(title, max_results=10):
    videos_search = VideosSearch(title, limit=max_results)
    videos = videos_search.result()['result']

    for video in videos:
        print(f"Title: {video['title']}")
        print(f"Link: https://www.youtube.com/watch?v={video['id']}")
        print(f"Views: {video['viewCount']['short']}")
        print("")


search_term = input("Введите название для поиска видео на YouTube: ")
search_videos_by_title(search_term)
