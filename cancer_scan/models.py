from aligned.model import Model
from aligned.feature_view.combined_view import CombinedFeatureView, CombinedFeatureViewMetadata
from cancer_scan.area import BreastScanAreaFeatureView
from cancer_scan.radius import BreastScanRadius
from cancer_scan.compactness import BreastScanCompactnessFeatureView
from cancer_scan.smoothness import BreastScanSmoothnessFeatureView
from cancer_scan.diagnosis import BreastScanDiagnosisFeatureView

cancer_detection = Model(
    features=[
        BreastScanDiagnosisFeatureView.select(lambda view: [
            view.is_malignant
        ])
    ]
)