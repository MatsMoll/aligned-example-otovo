from aligned import FeatureView, FeatureViewMetadata, Entity, Int32, Float, Bool
from cancer_scan.source import breast_scan_file, breast_scan_topic

class BreastScanRadius(FeatureView):

    metadata = FeatureViewMetadata(
        name="breast_scans_radius",
        description="Radius features in a cancer scan",
        batch_source=breast_scan_file,
        stream_source=breast_scan_topic
    )

    scan_id = Entity(dtype=Int32())

    radius_se = Float()
    radius_mean = Float()
    radius_worst = Float()

    # Can automatically set validation constraints mean ≈ 0 and most values should be within ±5 or what the 99 percentile is again
    radius_se_scaled = radius_se.standard_scaled()
    radius_mean_scaled = radius_mean.standard_scaled()
    radius_worst_scaled = radius_worst.standard_scaled()

    radius_se_mean_ratio = radius_se / radius_mean

    radius_is_between = radius_se_scaled.transformed(lambda df: df["radius_se_scaled"].between(left=10, right=20), as_dtype=Bool())
    radius_depending_on_multiple = Float().transformed(
        lambda df: df["radius_worst_scaled"] + df["radius_mean_scaled"] + df["radius_se_scaled"], 
        using_features=[radius_worst_scaled, radius_mean_scaled, radius_se_scaled]
    )