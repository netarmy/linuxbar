#!/usr/bin/env python3


import re


# Whether an email address is valid is finally checked by the activation mail
email_regex = re.compile('[^@]+@[^@]+')
sha256_regex = re.compile('[0123456789abcdef]{64}')


class ValidationError(Exception):
    pass


def _(string):
    return string # reserved for l10n


def validate(field, string, min=0, max=0, not_empty=False, regex=None):
    size = len(string.encode('utf8'))
    if(min and size < min):
        raise ValidationError(_(
            '%s should be at least %d bytes.' % (field, min)
        ))
    if(max and size > max):
        raise ValidationError(_(
            '%s should be at most %d bytes.' % (field, max)
        ))
    if(not_empty and size == 0):
        raise ValidationError(_('%s should not be empty.' % field))
    if(regex and not regex.fullmatch(string)):
        raise ValidationError(_('%s: Wrong format.' % field))


def validate_email(field, string):
    validate(field, string, regex=email_regex)


def validate_sha256(field, string):
    validate(field, string, regex=sha256_regex)
