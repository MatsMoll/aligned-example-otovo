from aladdin import FileSource, RedisConfig
from aladdin.repo_definition import RepoReference

breast_scan_file = FileSource(
    path="data.csv", 
    mapping_keys={"id" : "scan_id"}
)

online_source = RedisConfig.localhost().online_source()

repo_files = RepoReference(
    env_var_name="ENVIRONMENT",
    repo_paths={
        "local": FileSource(path="./feature-store.json", mapping_keys={})
    }
)