from youtubesearchpython import VideosSearch


def search_videos_by_title(title, max_results=15):
    videos_list = []
    videos_search = VideosSearch(title, limit=max_results)
    videos = videos_search.result()['result']
    for video in videos:
        videos_list.append([video['title'], video['id'], video['thumbnails'][0]['url'], video['duration']])
    return videos_list


