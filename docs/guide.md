---
source-sentry:
  reviewed:
    at: 2026-11-14T20:15:48Z
    by: 'Claude'
  sources:
    - path: '../src/settings.py'
      oid: 'sha1:34255e989acc1ee70727abbaf58ab24152eeb81e'
      reviewed:
        at: 2026-11-14T20:15:48Z
        by: 'Claude'
---
# Running the service

The service listens on port 8080. Each client may make up to 60 requests
per minute; further requests are refused until the minute has passed.
