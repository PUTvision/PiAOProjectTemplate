from typing import Dict

import numpy as np


def perform_processing(image: np.ndarray) -> Dict[str, int]:
    bananas = 4
    apples = 2
    oranges = 0

    return {
        'bananas': bananas,
        'apples': apples,
        'oranges': oranges
    }
