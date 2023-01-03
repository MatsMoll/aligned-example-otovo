# Aligned Example

This is an example repo, showing how `aligned` can be used.

The repo contains a directory describing some feature views, model services, has a feature store file, a data source, and a notebook that shows a use-case.

## Server
Running `aligned serve` will spin up a server with a HTTP streaming soruce. From there will opening up the 127.0.0.1:8000/docs present a Swagger API to play with.

## Generate file
If you make any changes to the views or models. Run `aligned apply` to update the `feature-store.json` file, and all your changes will be updated.

[Notebook presenting a common use-case](example.ipynb)
