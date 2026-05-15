#!/bin/bash
# In local environment, load env variables. In GitHub Actions, env variables are already loaded in workflow and .env doesn't exist because of .gitignore.
# In short, if .env exists, source it, otherwise, assume remote and variables already loaded so no need to source remotely.
[ -f .env ] && source .env

# Check if current commit has a tag. If so, local changes can be pushed to docker repo, otherwise changes are still in development and are not to be pushed to docker repo.
if [ -f .env ]; then
  export COMMIT_TAG=$(git tag --points-at HEAD)
  if [ -z "$COMMIT_TAG" ]; then
    export COMMIT_TAG=DEV
  fi
fi

# docker compose up switches image to the latest one and replace previous image with <none> tag
docker compose up --watch --remove-orphans
# Then finds images with <none> tag, known as dangling images. Does not work before docker compose up.
docker image prune -f

if [ -f .env ] && [ "$COMMIT_TAG" != "DEV" ]; then
  # Push local changes to docker repo
  docker compose push
fi

# Note '-' prefixing creatordate to show sort in descending order, finding the latest tag.
[ -f .env ] && LATEST_TAG=$(git tag --sort=-creatordate | head -n 1)
