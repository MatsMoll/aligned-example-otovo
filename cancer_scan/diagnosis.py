from aligned import FeatureView, FeatureViewMetadata, Entity, Int32, Float, String
from cancer_scan.source import breast_scan_file, breast_scan_topic

class BreastScanDiagnosisFeatureView(FeatureView):

    metadata = FeatureViewMetadata(
        name="breast_scans_diagnosis",
        description="Features defining a scan and diagnose of potential cancer cells",
        batch_source=breast_scan_file,
        stream_source=breast_scan_topic
    )

    scan_id = Entity(dtype=Int32())

    diagnosis = String().description("The given diagnose. M for malignant, and B for benigne")
    is_malignant = (diagnosis == "M").description("If the scanned cells was diagnosed as dangerous")