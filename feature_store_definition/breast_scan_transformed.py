from aladdin import FeatureView, FeatureViewMetadata, Entity, Int32, Float, String
from feature_store_definition.source import breast_scan_file

class BreastScanTransformedFeatureView(FeatureView):

    metadata = FeatureViewMetadata(
        name="breast_scans_transformed",
        description="Features defining a scan and diagnose of potential cancer cells",
        tags={},
        batch_source=breast_scan_file
    )

    scan_id = Entity(dtype=Int32())

    diagnosis = String().description("The given diagnose. M for malignant, and B for benigne")
    is_malignant = (diagnosis == "M").description("If the scanned cells was diagnosed as dangerous")

    radius_mean = Float()
    radius_mean_scaled = radius_mean.standard_scaled()

    perimeter_mean = Float()
    perimeter_mean_scaled = perimeter_mean.standard_scaled()

    area_mean = Float()
    area_mean_scaled = area_mean.standard_scaled()

    smoothness_mean = Float()
    smoothness_mean_scaled = smoothness_mean.standard_scaled()
    
    compactness_mean = Float()
    compactness_mean_scaled = compactness_mean.standard_scaled()