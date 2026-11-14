"""What the example web service stores about each visit, and for how long."""

# The fields kept for each request.
RETAINED_FIELDS = ["timestamp", "path", "status"]

# How long request records are kept, in days.
RETENTION_DAYS = 90
