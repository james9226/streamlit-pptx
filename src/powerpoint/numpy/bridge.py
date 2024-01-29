from typing import Union
import numpy as np
import pandas as pd

from src.powerpoint.constants.data_type_map import NUMPY_TO_PPTX_MAP


def convert_series_to_list(
    array: Union[pd.Series, np.ndarray]
) -> list[Union[str, int, float]]:
    dtype = str(array.dtype)
    mapper = NUMPY_TO_PPTX_MAP.get(dtype)

    if not mapper:
        raise ValueError(
            f"Unable to find dtype {dtype} for array {array} in internal lookup :()"
        )

    return [mapper(x) for x in array]
