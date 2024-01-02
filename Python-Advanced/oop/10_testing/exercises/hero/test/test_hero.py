from unittest import TestCase, main
from project.hero import Hero


class HeroTests(TestCase):
    def setUp(self) -> None:
        self.hero = Hero('Hero', 1, 100, 100)
        self.enemy_hero = Hero('Enemy Hero', 1, 100, 100)

    def test_hero_is_correctly_initialized(self):
        hero = Hero('Hero', 1, 100, 10)
        self.assertEqual('Hero', hero.username)
        self.assertEqual(1, hero.level)
        self.assertEqual(100, hero.health)
        self.assertEqual(10, hero.damage)

    def test_hero_string_returns_correct_result(self):
        expected_result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"
        actual_result = str(self.hero)
        self.assertEqual(expected_result, actual_result)

    def test_battle_hero_is_same_as_enemy_hero(self):
        self.enemy_hero.username = 'Hero'
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)
        expected_result = "You cannot fight yourself"
        actual_result = str(ex.exception)
        self.assertEqual(expected_result, actual_result)

    def test_battle_hero_has_zero_health(self):
        self.hero.health = 0
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)
        expected_result = "Your health is lower than or equal to 0. You need to rest"
        actual_result = str(ex.exception)
        self.assertEqual(expected_result, actual_result)

    def test_battle_hero_has_negative_health(self):
        self.hero.health = -1
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)
        expected_result = "Your health is lower than or equal to 0. You need to rest"
        actual_result = str(ex.exception)
        self.assertEqual(expected_result, actual_result)

    def test_battle_when_enemy_has_zero_health(self):
        self.enemy_hero.health = 0
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)
        expected_result = f"You cannot fight {self.enemy_hero.username}. He needs to rest"
        actual_result = str(ex.exception)
        self.assertEqual(expected_result, actual_result)

    def test_battle_when_enemy_has_negative_health(self):
        self.enemy_hero.health = -1
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)
        expected_result = f"You cannot fight {self.enemy_hero.username}. He needs to rest"
        actual_result = str(ex.exception)
        self.assertEqual(expected_result, actual_result)

    def test_battle_when_hero_and_enemy_have_zero_health(self):
        expected_result = 'Draw'
        actual_result = str(self.hero.battle(self.enemy_hero))
        self.assertEqual(expected_result, actual_result)

    def test_battle_when_hero_and_enemy_have_negative_health(self):
        self.enemy_hero.damage = 102
        self.hero.damage = 105
        expected_result = 'Draw'
        actual_result = str(self.hero.battle(self.enemy_hero))
        self.assertEqual(expected_result, actual_result)

    def test_battle_when_hero_has_zero_health_and_enemy_has_negative_health(self):
        self.enemy_hero.damage = 100
        self.hero.damage = 105
        expected_result = 'Draw'
        actual_result = str(self.hero.battle(self.enemy_hero))
        self.assertEqual(expected_result, actual_result)

    def test_battle_when_hero_has_negative_health_and_enemy_has_zero_health(self):
        self.enemy_hero.damage = 105
        self.hero.damage = 100
        expected_result = 'Draw'
        actual_result = str(self.hero.battle(self.enemy_hero))
        self.assertEqual(expected_result, actual_result)

    def test_battle_when_hero_has_more_than_zero_health_and_enemy_has_zero_health(self):
        self.enemy_hero.damage = 90
        expected_result = "You win"
        actual_result = str(self.hero.battle(self.enemy_hero))
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(15, self.hero.health)
        self.assertEqual(105, self.hero.damage)

    def test_battle_when_hero_has_more_than_zero_health_and_enemy_has_negative_health(self):
        self.enemy_hero.damage = 90
        self.hero.damage = 105
        expected_result = "You win"
        actual_result = str(self.hero.battle(self.enemy_hero))
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(15, self.hero.health)
        self.assertEqual(110, self.hero.damage)

    def test_battle_when_hero_has_zero_health_and_enemy_has_more_than_zero_health(self):
        self.hero.damage = 90
        expected_result = "You lose"
        actual_result = str(self.hero.battle(self.enemy_hero))
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(2, self.enemy_hero.level)
        self.assertEqual(15, self.enemy_hero.health)
        self.assertEqual(105, self.enemy_hero.damage)

    def test_battle_when_hero_has_negative_health_and_enemy_has_more_than_zero_health(self):
        self.enemy_hero.damage = 105
        self.hero.damage = 90
        expected_result = "You lose"
        actual_result = str(self.hero.battle(self.enemy_hero))
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(2, self.enemy_hero.level)
        self.assertEqual(15, self.enemy_hero.health)
        self.assertEqual(110, self.enemy_hero.damage)


if __name__ == '__main__':
    main()
