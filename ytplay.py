import webbrowser
import random
import sys

def read_file(path):
    out = []
    try:
        with open(path) as stream:
            for line in stream:
                out.append(line.strip())
    except IOError as e:
        print(f"Error opening file: {e}")
        return None
    
    return out

def shuffle_list(data):
    for i in range(len(data) - 1, 0, -1):
        j = random.randint(0, i)
        data[i], data[j] = data[j], data[i]

    return data

def random_video(data):
    webbrowser.open(shuffle_list(data)[0])

def create_queue(data):
    data = shuffle_list(data)

    # https://www.youtube.com/watch_videos?video_ids=abc123,def456,ghi789
    
    base_url = "https://www.youtube.com/watch_videos?video_ids="
    queue_urls = []
    for i in data:
        video_id = i.split("v=")[1]
        queue_urls.append(video_id)
    
    output = base_url + " " + ", ".join(queue_urls)
    output = output.replace(" ", "")

    webbrowser.open(output)


def main():
    videos = shuffle_list(read_file("videos.txt"))

    kwargs = sys.argv

    if len(kwargs) < 2:
        print("USAGE:\npython3 ytplay.py random (opens a random video from list)\npython3 ytplay.py queue (queues all videos in list)")
        exit()
    
    if kwargs[1] == "random":
        random_video(videos)
    elif kwargs[1] == "queue":
        create_queue(videos)


if __name__ == "__main__":
    main()
