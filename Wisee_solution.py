"""
This file contains the solution of a code interview.
"""
import pandas as pd
from typing import List


def _order_list(item_list: List[List[str, int]]) -> List[str]:
    return [
        item
        for item, num in sorted(item_list, key=lambda x: x[1])
        for _ in range(num)
    ]


def _get_models_colors_class_list(
        cars: List[str], colors: List[str], classes: List[str]
) -> List[List[str, str]]:
    return [
        [f"{car}{color}", exposition_class]
        for car, color, exposition_class in zip(cars, colors, classes)
    ]


def _count_models(series: pd.Series) -> List[str]:
    return [
        f"{index}: {num}"
        for index, num in series.value_counts().iteritems()
    ]


def model_disposition(
        models_exp: List[List[str, int]],
        colors_exp: List[List[str, int]],
        rows: List[List[str, int]]
) -> pd.DataFrame:
    car_colors_classes = _get_models_colors_class_list(
        _order_list(models_exp),
        _order_list(colors_exp),
        _order_list(rows),
    )
    return (
        pd.DataFrame(car_colors_classes, columns=["mod_col", "class"])
        .groupby("class")
        .agg(_count_models)
        .reset_index()
    )


if __name__ == '__main__':
    modelli_auto = [
        ["A", 29],
        ["B", 23],
        ["C", 11],
    ]

    colori = [
        ["r", 25],
        ["g", 23],
        ["b", 15],
    ]

    posti_per_classe = [
        ["I", 15],
        ["II", 15],
        ["III", 15],
        ["IV", 15],
        ["V", 3],
    ]
    print(model_disposition(modelli_auto, colori, posti_per_classe))
