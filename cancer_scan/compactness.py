from aligned import FeatureView, FeatureViewMetadata, Entity, Int32, Float
from cancer_scan.source import breast_scan_file, breast_scan_topic

class BreastScanCompactnessFeatureView(FeatureView):

    metadata = FeatureViewMetadata(
        name="breast_scans_compactness",
        description="Features defining a scan and diagnose of potential cancer cells",
        batch_source=breast_scan_file,
        stream_source=breast_scan_topic
    )

    scan_id = Entity(dtype=Int32())

    compactness_mean = Float()
    compactness_se = Float()
    compactness_worst = Float()
