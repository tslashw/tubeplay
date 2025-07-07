# ytplay

**ytplay** is a simple CLI Python tool that lets you instantly open a YouTube playlist from a list of video URLs or launch a random video from the list, right in your default browser.

No API keys, no setup bullshit, just run and watch.

---

## Features

- Open all YouTube links as a playlist (using YouTube’s temporary playlist feature)
- Randomly pick and open one video
- Opens in your system’s default browser
- No YouTube API required
- Works cross-platform (Windows, macOS, Linux)

---

## Usage

### Provide a list of YouTube URLs
Add a list of youtube URLs to the file `videos.txt`

For example:

https://www.youtube.com/watch?v=abc123
https://www.youtube.com/watch?v=def456
https://www.youtube.com/watch?v=ghi789


### Command Line Arguments

```python3 ytplay.py random``` (opens a random video from list)
```python3 ytplay.py queue``` (queues all videos in list)

## Future Additions
- Add a command line option for a custom file path of URLS e.g --path /your/txt/file

