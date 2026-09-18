from scipy.stats import median_abs_deviation
import numpy as np


def is_outlier(adata, metric: str, nmads: int):
    M = adata.obs[metric]
    outlier = (M < np.median(M) - nmads * median_abs_deviation(M)) | (
        np.median(M) + nmads * median_abs_deviation(M) < M
    )
    return outlier


def is_outlier_mt(adata, metric: str, nmads: int):
    M = adata.obs[metric]
    outlier = np.median(M) + nmads * median_abs_deviation(M) < M
    return outlier
