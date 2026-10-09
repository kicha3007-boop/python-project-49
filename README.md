# Игры разума (Python)

[![hexlet-check](https://github.com/kicha3007-boop/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/kicha3007-boop/python-project-49/actions)

«Игры разума» — набор из пяти консольных игр для тренировки мозга. Каждая игра задаёт три вопроса:
три правильных ответа подряд — победа, первый неправильный ответ завершает игру.

| Команда | Игра |
|---|---|
| `brain-even` | Чётное ли число |
| `brain-calc` | Калькулятор: вычислить выражение |
| `brain-gcd` | Наибольший общий делитель двух чисел |
| `brain-progression` | Пропущенное число в арифметической прогрессии |
| `brain-prime` | Простое ли число |

## Требования

- Python 3.10+
- [uv](https://docs.astral.sh/uv/)

## Установка

```bash
git clone https://github.com/kicha3007-boop/python-project-49.git
cd python-project-49
make install          # зависимости для разработки
make build            # сборка пакета в dist/
make package-install  # установка команд brain-* в систему
```

## Использование

После установки игры запускаются по имени:

```bash
brain-progression
Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
What number is missing in the progression?
Question: 5 7 9 11 13 .. 17 19 21 23
Your answer: 15
Correct!
Question: 2 5 8 .. 14 17 20 23 26 29
Your answer: 11
Correct!
Question: 14 19 24 29 34 39 44 49 54 ..
Your answer: 59
Correct!
Congratulations, Sam!
```

Без установки — `make brain-even`, `make brain-calc` и т.д. Проверка стиля — `make lint`.

## Устройство

- `brain_games/engine.py` — общий движок: приветствие, три раунда, проверка ответа.
- `brain_games/games/` — по модулю на игру: описание `DESCRIPTION` и `generate_round()`,
  возвращающая вопрос и правильный ответ.
- `brain_games/scripts/` — точки входа: только импорт игры и запуск движка.

---

<details>
<summary>Автоматические тесты Хекслета</summary>

Тесты запускаются на каждый коммит. За запуск отвечает файл `.github/workflows/hexlet-check.yml` — не удаляйте и не переименовывайте ни его, ни репозиторий.

</details>
