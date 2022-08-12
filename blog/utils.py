from django.utils import timezone
import math

def time_since(time):
    now = timezone.now()
    diff = now - time
    if diff.days == 0 and 0 <= diff.seconds < 60:
        seconds = diff.seconds

        if seconds == 1:
            return str(seconds) + "second ago"

        else:
            return str(seconds) + " seconds ago"

    if diff.days == 0 and 60 <= diff.seconds < 3600:
        minutes = math.floor(diff.seconds / 60)

        if minutes == 1:
            return str(minutes) + " minute ago"

        else:
            return str(minutes) + " minutes ago"

    if diff.days == 0 and 3600 <= diff.seconds < 86400:
        hours = math.floor(diff.seconds / 3600)

        if hours == 1:
            return str(hours) + " hour ago"

        else:
            return str(hours) + " hours ago"

    # 1 day to 30 days
    if 1 <= diff.days < 30:
        days = diff.days

        if days == 1:
            return str(days) + " day ago"

        else:
            return str(days) + " days ago"

    if 30 <= diff.days < 365:
        months = math.floor(diff.days / 30)

        if months == 1:
            return str(months) + " month ago"

        else:
            return str(months) + " months ago"

    if diff.days >= 365:
        years = math.floor(diff.days / 365)

        if years == 1:
            return str(years) + " year ago"

        else:
            return str(years) + " years ago"

def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '%.12f' % f
    i, p, d = s.partition('.')
    return eval('.'.join([i, (d+'0'*n)[:n]]))

def views_counter(val):
    if val < 1000:
        return val
    elif val >= 1000 and val < 999999:
        views = math.floor(truncate((val/1000), 0))
        return '{}k'.format(views)
    elif val >= 1000000 and val < 999999999:
        views = math.floor(truncate((val/1000000), 0))
        return '{}m'.format(views)
    elif val >= 1000000000 and val < 999999999999:
        views = math.floor(truncate((val/1000000000), 0))
        return '{}bn'.format(views)

def likes_counter(val):
    if val < 1000:
        return val
    elif val >= 1000 and val < 999999:
        likes = math.floor(truncate((val/1000), 0))
        return '{}k'.format(likes)
    elif val >= 1000000 and val < 999999999:
        likes = math.floor(truncate((val/1000000), 0))
        return '{}m'.format(likes)
    elif val >= 1000000000 and val < 999999999999:
        likes = math.floor(truncate((val/1000000000), 0))
        return '{}bn'.format(likes)

def comments_counter(val):
    if val < 1000:
        return val
    elif val >= 1000 and val < 999999:
        comments = math.floor(truncate((val/1000), 0))
        return '{}k'.format(comments)
    elif val >= 1000000 and val < 999999999:
        comments = math.floor(truncate((val/1000000), 0))
        return '{}m'.format(comments)
    elif val >= 1000000000 and val < 999999999999:
        comments = math.floor(truncate((val/1000000000), 0))
        return '{}bn'.format(comments)
