""" Функции для проведения необходимых вычислений"""
from typing import Dict


def get_metrics(sample: list, population: bool = True) -> Dict[str, float]:
    """Рассчитывает: среднее, дисперсию, стандартное отклонение."""

    avg = lambda x: sum(x) / len(x)

    sample_mean = avg(sample)
    sample_mean_diff = [(i - sample_mean) ** 2 for i in sample]
    sample_var = avg(sample_mean_diff)
    sample_std = sample_var ** 0.5

    if population:
        metrics = {
            "Mu": sample_mean,
            "Sigma^2": sample_var,
            "Sigma": sample_std
        }

    else:
        metrics = {
            "Mean": sample_mean,
            "Variance": sample_var,
            "STD": sample_std
        }

    return metrics
