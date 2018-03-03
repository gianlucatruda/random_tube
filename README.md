# random_tube
A pair of scripts for extracting YouTube links from your watch history, and randomly opening one in your browser.

# Instructions
Head to [Google Takeout](https://takeout.google.com/) and download only your YouTube watch history in JSON format. For some reason it instead comes in HTML format, so running

```
python3 parse.py
```

in the same directory as the watch-history.html file will create a history.txt file with a list of plaintext URLs, one per line.

If you're feeling nostalgic, run

```
python3 random_hist.py
```

and it will read in from history.txt and open a new web browser tab from a randomly selected link.


I spent like 15 minutes on this, so please don't expect it to work without some fiddling. It's dank and lazy. Seriously, you have been warned!
