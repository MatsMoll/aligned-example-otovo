from aladdin.model import ModelService
from feature_store_definition.breast_scan_transformed import BreastScanTransformedFeatureView

breast_cancer_model_v1 = ModelService(
    features=[
        BreastScanTransformedFeatureView.select(lambda view: [
            view.area_mean_scaled,
            view.radius_mean_scaled,
            view.perimeter_mean_scaled,
            view.compactness_mean_scaled,
            view.smoothness_mean_scaled
        ])
    ]
)