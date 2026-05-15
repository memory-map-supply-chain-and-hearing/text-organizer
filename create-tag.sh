#!/bin/bash

# Calculate minor: days since last tag
# Last tag: most recently created tag in the repo (e.g. v1.0.0). Empty if no tags exist.
# Example: latest tag was 5 days ago -> MINOR=5 -> v1.5.x
LATEST_TAG=$(git tag --sort=-creatordate | head -n 1)
CURRENT_DATE=$(date +'%Y-%m-%d')
if [ -z "$LATEST_TAG" ]; then
  MINOR=0
  PREVIOUS_DATE=""
else
  # Extract commit date from tag
  # ad format is required to tell git to output date instead of commit log
  PREVIOUS_DATE=$(git log -1 --format=%ad --date=format:%Y-%m-%d "$LATEST_TAG")
  PREVIOUS_UNIX_DATE=$(date -d "$PREVIOUS_DATE" +%s)
  CURRENT_UNIX_DATE=$(date -d "$CURRENT_DATE" +%s)
  TOTAL_SECONDS_PER_DAY=86400
  MINOR=$(((CURRENT_UNIX_DATE - PREVIOUS_UNIX_DATE) / TOTAL_SECONDS_PER_DAY))
fi

# Calculate patch: number of tags created on the same day (today)
# Example: 2nd push today -> PATCH=1 -> v1.5.1
if [ "$PREVIOUS_DATE" = "$CURRENT_DATE" ]; then
  PREVIOUS_PATCH=$(echo "$LATEST_TAG" | grep -oP '\d+$')
  PATCH=$((PREVIOUS_PATCH + 1))
else
  PATCH=0
fi

# Major is hardcoded. Increment manually for major changes.
TAG="v1.$MINOR.$PATCH"

git tag "$TAG"
git push origin "$TAG"
