# Taekwondobot

Very simple image scraper to download all the images on the deprecated ICUTKD website.

Built with Scrapy (and in a rush).

## Usage

Set `IMAGES_STORE` in `settings.py`.

```
pipenv install
pipenv run scrapy crawl taekwondobot
```

This will save images into `IMAGES_STORE/ALBUM_NAME/FILENAME`.

## How it works

1. Go to the page that lists all the albums.
2. Get the links to all the albums
3. Visit each album and download the photos

Pretty simple.
