from django import template
import markdown

register = template.Library()


@register.filter
def markdownify(text):
    # safe_mode governs how the function handles raw HTML
    return markdown.markdown(
        text, extensions=['markdown.extensions.tables'], safe_mode='escape')
