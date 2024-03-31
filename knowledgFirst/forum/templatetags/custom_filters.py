from django import template
from django.utils.html import mark_safe
import re

register = template.Library()

@register.filter
def highlight_text(text, query):
    highlighted_text = re.sub(r'(' + re.escape(query) + r')', r'<span class="highlight">\1</span>', text, flags=re.IGNORECASE)
    return mark_safe(highlighted_text)

@register.filter
def get_liked_status(replies_liked_by_user, reply_id):
    return replies_liked_by_user.get(reply_id)
