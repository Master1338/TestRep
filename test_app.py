import os

def test_project():
    # Проверяем, существует ли файл index.html
    assert os.path.exists("index.html"), "Ошибка: файл index.html не найден!"
    
    # Проверяем, что внутри файла есть нужный текст
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()
    assert "Моя лаборатория CI/CD" in content, "Ошибка: неверный заголовок сайта!"
    
    print("Все тесты успешно пройдены!")

if __name__ == "__main__":
    test_project()