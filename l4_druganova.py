if __name__ == "__main__":
    # Write your solution here
    class BuildingMaterial:
        """ Базовый класс строительные материалы. """

        def __init__(self, name: str, density: float):
            if not isinstance(density, float):
                raise TypeError("Плотность должна быть числом с плавающей запятой")

            if not density > 0:
                raise ValueError("Плотность должна быть положительной")

            self._name = name  # Непубличный атрибут, что бы избежать прямого доступа
            self._density = density  # Непубличный атрибут, что бы избежать прямого доступа

        def __str__(self) -> str:
            return f"{self._name}, плотность: {self._density} кг/м³"

        def __repr__(self) -> str:
            return f"BuildingMaterial(name='{self._name}', density={self._density})"


    class Concrete(BuildingMaterial):
        """ Дочерний класс бетон. """

        def __init__(self, name: str, density: float, strength: float):
            if not isinstance(strength, float):
                raise TypeError("Прочность должна быть числом с плавающей запятой")

            if not strength > 0:
                raise ValueError("Прочность должна быть положительной")

            super().__init__(name, density)
            self._strength = strength  # Непубличный атрибут, что бы избежать прямого доступа

        def __str__(self) -> str:
            return f"{super().__str__()} | Прочность: {self._strength} МПа"

        def __repr__(self) -> str:
            return (f"{self.__class__.__name__}(name={self._name!r}, "
                    f"density={self._density!r}, strength={self._strength!r})")

    class Wood(BuildingMaterial):
        """ Дочерний класс дерево. """

        def __init__(self, name: str, density: float, wood_type: str):

            super().__init__(name, density)
            self.wood_type = wood_type  # Публичный атрибут

        def __str__(self) -> str:
            return f"{super().__str__()} | Тип: {self.wood_type} МПа"

        def __repr__(self) -> str:
            return (f"{self.__class__.__name__}(name={self._name!r}, "
                    f"density={self._density!r}, wood_type={self.wood_type!r})")


    class Steel(BuildingMaterial):
        """ Дочерний класс сталь. """

        def __init__(self, name: str, density: float, tensile_strength: float):
            if not isinstance(tensile_strength, float):
                raise TypeError("Прочность на растяжение должна быть числом с плавающей запятой")

            if not tensile_strength > 0:
                raise ValueError("Прочность на растяжение должна быть положительной")

            super().__init__(name, density)
            self._tensile_strength = tensile_strength  # Непубличный атрибут, что бы избежать прямого доступа

        def __str__(self) -> str:
            return (f"{super().__str__()} | Прочность на растяжение: "
                    f"{self._tensile_strength} МПа")

        def __repr__(self) -> str:
            return (f"{self.__class__.__name__}(name={self._name!r}, "
                    f"density={self._density!r}, tensile_strength={self._tensile_strength!r})")


    pass

