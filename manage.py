#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    project_env = os.environ.get('SHZ_BLOG_ENV')
    if project_env == "Test":
        DJANGO_SETTINGS_MODULE = 'shez_blog.settings_test'
    elif project_env == "Product":
        DJANGO_SETTINGS_MODULE = 'shez_blog.settings_product'
    else:
        DJANGO_SETTINGS_MODULE = 'shez_blog.settings'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', DJANGO_SETTINGS_MODULE)
    print('[Manage.py] Use %s as prject settings.' % DJANGO_SETTINGS_MODULE)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
