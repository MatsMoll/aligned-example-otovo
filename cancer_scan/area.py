from aligned import FeatureView, FeatureViewMetadata, Entity, Int32, Float, String
from cancer_scan.source import breast_scan_file, breast_scan_topic

class BreastScanAreaFeatureView(FeatureView):

    metadata = FeatureViewMetadata(
        name="breast_scans_area",
        description="Features defining a scan and diagnose of potential cancer cells",
        batch_source=breast_scan_file,
        stream_source=breast_scan_topic
    )

    scan_id = Entity(dtype=Int32())

    area_mean = Float()
    area_se = Float()
    area_worst = Float()

    area_mean_scaled = area_mean.standard_scaled()
    area_se_scaled = area_se.standard_scaled()
    area_worst_scaled = area_worst.standard_scaled()