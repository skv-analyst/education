import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from deap import base
from deap import creator
from deap import tools
from deap import algorithms

sns.set_style("whitegrid")

toolbox = base.Toolbox()


class GeneticAlgorithm:
    def __init__(self, seed, one_max_length, population_size, p_crossover, p_mutation, max_generation,
                 selection_operator, selection_params=None, verbose=False):
        self.seed = seed
        self.one_max_length = one_max_length
        self.population_size = population_size
        self.p_crossover = p_crossover
        self.p_mutation = p_mutation
        self.max_generation = max_generation
        self.selection_operator = selection_operator
        self.selection_params = selection_params or {}
        self.toolbox = base.Toolbox()
        self.generation_with_max_fitness = None
        self.verbose = verbose

    def register_operators(self):
        """Регистрирует необходимые операторы для эволюции."""
        random.seed(self.seed)

        # Создаем классы только один раз
        if "FitnessMax" not in creator.__dict__:
            creator.create("FitnessMax", base.Fitness, weights=(1.0,))
        if "Individual" not in creator.__dict__:
            creator.create("Individual", list, fitness=creator.FitnessMax)

        # Регистрируем функции
        self.toolbox.register("zeroOrOne", random.randint, 0, 1)
        self.toolbox.register("individualCreator", tools.initRepeat, creator.Individual, self.toolbox.zeroOrOne,
                              self.one_max_length)
        self.toolbox.register("populationCreator", tools.initRepeat, list, self.toolbox.individualCreator)

        # Регистрируем целевую функцию
        self.toolbox.register("evaluate", lambda ind: (sum(ind),))

        # Регистрируем оператор отбора, переданный в класс
        self.toolbox.register("select", self.selection_operator, **self.selection_params)

        # Регистрируем операторы скрещивания и мутации
        self.toolbox.register("mate", tools.cxTwoPoint)
        self.toolbox.register("mutate", tools.mutFlipBit, indpb=0.1)

    def create_population(self):
        """Создает начальную популяцию."""
        self.population = self.toolbox.populationCreator(n=self.population_size)

    def gather_statistics(self):
        """Собирает статистику."""
        stats = tools.Statistics(lambda ind: ind.fitness.values)
        stats.register("max", np.max)
        stats.register("avg", np.mean)
        return stats

    def find_first_max_generation(self, logbook, max_fitness=100):
        """Находит первое поколение, в котором достигнут максимальный фитнес."""
        max_fitness_values = logbook.select("max")
        for gen, fitness in enumerate(max_fitness_values):
            if fitness >= max_fitness:
                self.generation_with_max_fitness = gen + 1  # Поколения начинаются с 1
                break

    def visualize(self, logbook):
        """Визуализация."""
        maxFitnessValues, meanFitnessValues = logbook.select("max", "avg")
        generations = range(1, len(maxFitnessValues) + 1)

        plt.figure(figsize=(15, 5))
        sns.lineplot(x=generations, y=maxFitnessValues, color='red', label='Максимальное')
        sns.lineplot(x=generations, y=meanFitnessValues, color='green', label='Среднее')

        # Если найдено поколение с максимальным фитнесом, отмечаем его
        if self.generation_with_max_fitness is not None:
            plt.axvline(
                x=self.generation_with_max_fitness,
                color='red',
                linestyle='--',
                label=f"Цель достигнута на поколении {self.generation_with_max_fitness}"
            )

        plt.xlabel("Поколения")
        plt.ylabel("Фитнес")
        plt.legend()
        plt.show()

    def run(self):
        """Запуск алгоритма."""
        self.register_operators()
        self.create_population()
        stats = self.gather_statistics()
        hof = tools.HallOfFame(10)

        # Запуск алгоритма
        population, logbook = algorithms.eaSimple(
            population=self.population,
            toolbox=self.toolbox,
            cxpb=self.p_crossover,
            mutpb=self.p_mutation,
            ngen=self.max_generation,
            stats=stats,
            halloffame=hof,
            verbose=self.verbose
        )

        # Найти первое поколение с максимальным фитнесом
        self.find_first_max_generation(logbook)

        # Визуализация
        self.visualize(logbook)


if __name__ == "__main__":
    pass
