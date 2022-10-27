from aligned import FileSource
from aligned.schemas.repo_definition import RepoReference
from source import redis_cluster

repo_files = RepoReference(
    env_var_name="ENVIRONMENT",
    repo_paths={
        "local": FileSource.from_path(path="./feature-store.json")
    }
)

# location = FileSource.from_path("feature-store.json").repo_reference()

feature_server = repo_files.feature_server(
    online_source=redis_cluster.online_source()
)