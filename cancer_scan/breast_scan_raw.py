from aligned import FeatureView, FeatureViewMetadata, Entity, Int32, Float, String
from cancer_scan.source import breast_scan_file, breast_scan_topic

class BreastScanRawFeatureView(FeatureView):

    metadata = FeatureViewMetadata(
        name="breast_scans_raw",
        description="Features defining a scan and diagnose of potential cancer cells",
        batch_source=breast_scan_file,
        stream_source=breast_scan_topic
    )

    scan_id = Entity(dtype=Int32())

    diagnosis = String().description("The given diagnose. M for malignant, and B for benigne")

    radius_mean = Float()
    radius_se = Float()
    radius_worst = Float()

    texture_mean = Float()
    texture_se = Float()
    texture_worst = Float()

    perimeter_mean = Float()
    perimeter_se = Float()
    perimeter_worst = Float()

    area_mean = Float()
    area_se = Float()
    area_worst = Float()

    smoothness_mean = Float()
    smoothness_se = Float()
    smoothness_worst = Float()
    
    compactness_mean = Float()
    compactness_se = Float()
    compactness_worst = Float()
    
    concavity_mean = Float()
    concavity_se = Float()
    concavity_worst = Float()
    
    concave_points_mean = Float()
    concave_points_se = Float()
    concave_points_worst = Float()
    
    symmetry_mean = Float()
    symmetry_se = Float()
    symmetry_worst = Float()

    fractal_dimension_mean = Float()
    fractal_dimension_se = Float()
    fractal_dimension_worst = Float()