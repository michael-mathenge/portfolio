from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()

@register.filter
def bulletize(value):
    """
    Convert text with paragraph breaks into HTML bullet points.
    Each paragraph (separated by blank lines) becomes a bullet point.
    """
    if not value:
        return ""
    
    # Normalize line endings and split by double line breaks (paragraphs)
    normalized_text = value.replace('\r\n', '\n').replace('\r', '\n')
    paragraphs = [para.strip().replace('\n', ' ') for para in normalized_text.split('\n\n') if para.strip()]
    
    # Remove existing bullet points (• character) from the beginning of paragraphs
    clean_paragraphs = []
    for para in paragraphs:
        # Remove bullet points and extra spaces from the beginning
        cleaned = re.sub(r'^[•\-\*]\s*', '', para.strip())
        if cleaned:
            clean_paragraphs.append(cleaned)
    
    if len(clean_paragraphs) <= 1:
        # If only one paragraph or no paragraphs, return as paragraph
        return mark_safe(f'<p>{value}</p>')
    
    # Create bullet list
    bullet_items = ''.join([f'<li>{para}</li>' for para in clean_paragraphs])
    return mark_safe(f'<ul>{bullet_items}</ul>')

@register.filter
def bulletize_custom(value, separator='\n'):
    """
    Convert text with custom separator into HTML bullet points.
    Usage: {{ description|bulletize_custom:";" }}
    """
    if not value:
        return ""
    
    # Split by custom separator and filter out empty items
    items = [item.strip() for item in value.split(separator) if item.strip()]
    
    if len(items) <= 1:
        # If only one item or no items, return as paragraph
        return mark_safe(f'<p>{value}</p>')
    
    # Create bullet list
    bullet_items = ''.join([f'<li>{item}</li>' for item in items])
    return mark_safe(f'<ul>{bullet_items}</ul>')