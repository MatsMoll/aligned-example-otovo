from aligned import FeatureView, FeatureViewMetadata, Entity, Int32, Float, String
from cancer_scan.source import breast_scan_file, breast_scan_topic

class BreastScanSmoothnessFeatureView(FeatureView):

    metadata = FeatureViewMetadata(
        name="breast_scans_smoothness",
        description="Features defining a scan and diagnose of potential cancer cells",
        batch_source=breast_scan_file,
        stream_source=breast_scan_topic
    )

    scan_id = Entity(dtype=Int32())

    smoothness_mean = Float()
    smoothness_se = Float()
    smoothness_worst = Float()
