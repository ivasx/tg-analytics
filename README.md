# 📊 Telegram Chat Analyzer

A tool for analyzing exported Telegram chats. Allows you to get message statistics, most popular words, and view messages for a specific time period.

## 🎯 What is this project for?

This script helps you:
- 📈 Analyze chat participant activity
- 🔤 Find the most frequently used words (overall and per user)
- 🕐 View messages for a specific time range
- 📊 Get general conversation statistics

## 📋 Requirements

- Python 3.6 or newer
- Exported JSON file from Telegram

## 🚀 How to use

### 1. Export chat from Telegram

1. Open Telegram Desktop
2. Select the desired chat
3. Click on three dots (⋮) → **Export chat history**
4. In export settings:
   - Format: **JSON**
   - Media size: you can select "Don't export"
   - Other options as desired
5. Save the export

### 2. Project setup

```bash
# Project structure should be:
# your_project/
# ├── main.py
# └── chat_export/
#     └── result.json

# Copy the result.json file from export to chat_export folder
# The chat_export folder already exists, just place the JSON file there
```

### 3. Run the program

```bash
python main.py
```

## 💡 Features

### Automatic analysis on startup

At startup, the program will show:
- Number of messages from each user
- First 5 messages in the chat

### Popular words analysis

After startup, the program will ask:
```
Exclude stop words? (yes/no):
```

- **yes** — will exclude service words (and, in, on, that, etc.)
- **no** — will show all words

Then you'll see TOP-10 most popular words:
- Overall ranking for the entire chat
- Separate ranking for each participant

### Search messages by date

The program will offer to view messages for a specific period:

```
Enter date range? (yes/no): yes
Start date (dd.mm.yyyy hh:mm): 01.01.2024 10:00
End date (dd.mm.yyyy hh:mm): 31.01.2024 23:59
```

Date format: **DD.MM.YYYY HH:MM** (example: `15.03.2024 14:30`)

## 📝 Usage example

```
Message analytics:
Number of messages from each user:
Ivan Petrenko: 1523
Maria Koval: 2341

First 5 messages:
[2024/01/15 10:23:45] Ivan Petrenko: Hello!
...

Exclude stop words? (yes/no): yes

TOP words among all:
meeting        ➤ 45
project        ➤ 38
tomorrow       ➤ 32
...

TOP words per user:

Ivan Petrenko:
work           ➤ 67
task           ➤ 54
...
```

## ⚙️ Technical details

### Stop words

The program uses a list of stop words in Ukrainian. These are service words that usually don't carry semantic meaning (pronouns, prepositions, conjunctions).

### Date formats

- **Input format** (for search): `DD.MM.YYYY HH:MM`
- **Display format**: `YYYY/MM/DD HH:MM:SS`

## 🐛 Possible issues

**"FileNotFoundError" error**
- Make sure the `result.json` file is located in the `chat_export` folder

**Empty statistics**
- Check if the JSON file format is correct
- Make sure the export contains messages

**Incorrect date**
- Use the format `DD.MM.YYYY HH:MM` with dots and colon
- Example: `25.12.2024 18:30`

## 📄 License

Free to use for personal and educational purposes.

---

**Note**: The program works locally and doesn't transmit your data anywhere. All data remains on your computer.

# 📊 Telegram Chat Analyzer

Інструмент для аналізу експортованих чатів Telegram. Дозволяє отримати статистику повідомлень, найпопулярніші слова та переглядати повідомлення за певний період часу.

## 🎯 Для чого цей проект?

Цей скрипт допомагає:
- 📈 Проаналізувати активність учасників чату
- 🔤 Знайти найчастіше використовувані слова (загалом та по кожному користувачу)
- 🕐 Переглянути повідомлення за конкретний проміжок часу
- 📊 Отримати загальну статистику переписки

## 📋 Вимоги

- Python 3.6 або новіше
- Експортований JSON файл з Telegram

## 🚀 Як користуватись

### 1. Експорт чату з Telegram

1. Відкрийте Telegram Desktop
2. Оберіть потрібний чат
3. Клікніть на три крапки (⋮) → **Експортувати історію чату**
4. У налаштуваннях експорту:
   - Формат: **JSON**
   - Розмір медіа: можете обрати "Не експортувати"
   - Інші опції за бажанням
5. Збережіть експорт

### 2. Підготовка проекту

```bash
# Структура проекту має бути:
# ваш_проект/
# ├── main.py
# └── chat_export/
#     └── result.json

# Скопіюйте файл result.json з експорту в папку chat_export
# Папка chat_export вже існує, просто помістіть туди JSON файл
```

### 3. Запуск програми

```bash
python main.py
```

## 💡 Функціонал

### Автоматичний аналіз при запуску

При старті програма покаже:
- Кількість повідомлень від кожного користувача
- Перші 5 повідомлень у чаті

### Аналіз популярних слів

Після запуску програма запитає:
```
Виключати стоп-слова? (так/ні):
```

- **так** — виключить службові слова (і, в, на, що, та ін.)
- **ні** — покаже всі слова

Потім ви побачите ТОП-10 найпопулярніших слів:
- Загальний рейтинг по всьому чату
- Окремий рейтинг для кожного учасника

### Пошук повідомлень за датою

Програма запропонує переглянути повідомлення за певний період:

```
Ввести діапазон дат? (так/ні): так
Початкова дата (дд.мм.рррр гг:хх): 01.01.2024 10:00
Кінцева дата (дд.мм.рррр гг:хх): 31.01.2024 23:59
```

Формат дати: **ДД.ММ.РРРР ГГ:ХХ** (наприклад: `15.03.2024 14:30`)

## 📝 Приклад використання

```
Аналітика повідомлень:
Кількість повідомлень від кожного користувача:
Іван Петренко: 1523
Марія Коваль: 2341

Перші 5 повідомлень:
[2024/01/15 10:23:45] Іван Петренко: Привіт!
...

Виключати стоп-слова? (так/ні): так

ТОП слова серед усіх:
зустріч        ➤ 45
проект         ➤ 38
завтра         ➤ 32
...

ТОП слова по кожному користувачу:

Іван Петренко:
робота         ➤ 67
задача         ➤ 54
...
```

## ⚙️ Технічні деталі

### Стоп-слова

Програма використовує список стоп-слів українською мовою. Це службові слова, які зазвичай не несуть змістового навантаження (займенники, прийменники, сполучники).

### Формати дат

- **Вхідний формат** (для пошуку): `ДД.ММ.РРРР ГГ:ХХ`
- **Формат відображення**: `РРРР/ММ/ДД ГГ:ХХ:СС`

## 🐛 Можливі проблеми

**Помилка "FileNotFoundError"**
- Переконайтесь, що файл `result.json` знаходиться в папці `chat_export`

**Порожня статистика**
- Перевірте, чи правильний формат JSON файлу
- Переконайтесь, що експорт містить повідомлення

**Неправильна дата**
- Використовуйте формат `ДД.ММ.РРРР ГГ:ХХ` з крапками та двокрапкою
- Приклад: `25.12.2024 18:30`

## 📄 Ліцензія

Вільне використання для особистих та навчальних цілей.

---

**Примітка**: Програма працює локально і не передає ваші дані нікуди. Всі дані залишаються на вашому комп'ютері.

---
---

