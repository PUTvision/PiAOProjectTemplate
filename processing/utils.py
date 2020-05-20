from typing import Tuple

import numpy as np


def perform_processing(image: np.ndarray) -> Tuple[int, int, int, int]:
    green_roulette = 4
    orange_roulette = 2
    green_bears = 0
    orange_bears = 0

    return green_roulette, orange_roulette, green_bears, orange_bears
