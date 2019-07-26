#!/bin/sh
exec gunicorn -b :8000 --access-logfile - --error-logfile - ArtSite.wsgi