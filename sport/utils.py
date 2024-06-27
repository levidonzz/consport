import hashlib
from django.template.loader import render_to_string


def generate_avatar(user):
    letter = user.username[0].upper() if user.username else '?'
    color_ix = int(hashlib.md5(str(user.id).encode()).hexdigest(), 16) % 10
    context = {'color_ix': color_ix, 'letter': letter}
    return render_to_string('accounts/avatar.svg', context)