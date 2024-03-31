from django import template
from django.utils.html import mark_safe
import re
from django.utils.timesince import timesince
from django.utils import timezone

register = template.Library()

@register.filter
def highlight_text(text, query):
    highlighted_text = re.sub(r'(' + re.escape(query) + r')', r'<span class="highlight">\1</span>', text, flags=re.IGNORECASE)
    return mark_safe(highlighted_text)

@register.filter
def get_liked_status(replies_liked_by_user, reply_id):
    return replies_liked_by_user.get(reply_id)

@register.filter
def custom_timesince(value):
    now = timezone.now()
    delta = now - value
    if delta.days > 365:
        return '{} year{} ago'.format(delta.days // 365, 's' if delta.days // 365 > 1 else '')
    elif delta.days > 30:
        return '{} month{} ago'.format(delta.days // 30, 's' if delta.days // 30 > 1 else '')
    elif delta.days > 7:
        return '{} week{} ago'.format(delta.days // 7, 's' if delta.days // 7 > 1 else '')
    elif delta.days > 0:
        return '{} day{} ago'.format(delta.days, 's' if delta.days > 1 else '')
    elif delta.seconds // 3600 > 0:
        return '{} hour{} ago'.format(delta.seconds // 3600, 's' if delta.seconds // 3600 > 1 else '')
    else:
        return 'Just now'
