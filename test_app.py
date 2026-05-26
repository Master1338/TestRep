import os

def test_project():
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()
    # Скрипт ТРЕБУЕТ наличия этой фразы
    assert "Моя лаборатория CI/CD" in content, "ОШИБКА: Заголовок не найден!"
    print("Все тесты успешно пройдены!")

if __name__ == "__main__":
    test_project()