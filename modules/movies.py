#!/usr/bin/env python
# coding=utf-8
"""
Get imdb data
"""


def question(phenny, input):
    """Search movies in imdb.com"""
    if not input.group(2):
        return phenny.reply("No search term")

    import imdb
    ia = imdb.IMDb()

    i = 0
    for movie in ia.search_movie(input.group(2).encode('utf-8')):
        phenny.say(u'%s http://www.imdb.com/title/tt%s/' % \
                       (movie['long imdb title'], movie.movieID))
        i += 1
        if i > 3:
            break

question.commands = ["movie", ]


if __name__ == '__main__':
    print __doc__.strip()
