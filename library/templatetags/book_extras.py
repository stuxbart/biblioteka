from django import template

register = template.Library()

book_endings = ['ka', 'ki', 'ek']


def word_endings(count):
    if count == 1:
        return book_endings[0]
    num = str(count)

    if num[-1] in ['2', '3', '4']:
        if count in [12, 13, 14]:
            return book_endings[2]
        return book_endings[1]
    return book_endings[2]


register.filter('endings', word_endings)