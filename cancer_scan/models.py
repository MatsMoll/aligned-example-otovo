from aligned.model import ModelService
from cancer_scan.area import BreastScanAreaFeatureView
from cancer_scan.radius import BreastScanRadius
from cancer_scan.compactness import BreastScanCompactnessFeatureView
from cancer_scan.smoothness import BreastScanSmoothnessFeatureView
from cancer_scan.diagnosis import BreastScanDiagnosisFeatureView

cancer_detection = ModelService(
    features=[
        BreastScanAreaFeatureView.select(lambda view: [
            view.area_mean_scaled,
            view.area_se_scaled,
            view.area_worst_scaled
        ]),
        BreastScanRadius.select(lambda view: [
            view.radius_mean_scaled,
            view.radius_se_scaled,
            view.radius_worst_scaled,

            view.radius_depending_on_multiple
        ]),
        BreastScanCompactnessFeatureView.select(lambda view: [
            view.compactness_mean_scaled,
            view.compactness_se_scaled,
            view.compactness_worst_scaled
        ]),
        BreastScanSmoothnessFeatureView.select(lambda view: [
            view.smoothness_mean_scaled,
            view.smoothness_se_scaled,
            view.smoothness_worst_scaled
        ]),
        BreastScanDiagnosisFeatureView.select(lambda view: [
            view.is_malignant
        ])
    ]
)