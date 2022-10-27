from aligned import FileSource
from aligned.data_source.stream_data_source import HttpStreamSource

breast_scan_file = FileSource.csv_at(
    path="data/cancer_scans.csv", 
    mapping_keys={"id" : "scan_id"}
)

# Will setup a REST HTTP call on the server
breast_scan_topic = HttpStreamSource(topic_name="breast_scan")