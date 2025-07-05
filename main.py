from datetime import datetime
import json
import re
from collections import Counter, defaultdict

STOP_WORDS = {
    "і", "в", "на", "з", "що", "це", "до", "та", "по", "у", "я", "ти", "ви", "ми", "він", "вона", "вони",
    "не", "так", "але", "як", "же", "чи", "а", "із", "за", "про", "та", "щоб", "то", "для", "тому",
    "еще", "уже", "да", "нет", "же", "ли", "бы", "быть", "этот", "тот", "такой", "её", "его", "них", "она",
    "и", "все", "к", "с", "о", "от", "до", "со", "об", "без", "под", "над", "при", "из"
}

def get_all_msgs(filename="chat_export/result.json"):
    with open(filename, encoding="utf-8") as json_file:
        return json.load(json_file)

def parse_human_date(date_str):
    return datetime.strptime(date_str, "%d.%m.%Y %H:%M")

def get_messages_by_time_range(start_time_str, end_time_str, data):
    try:
        start_time = parse_human_date(start_time_str)
        end_time = parse_human_date(end_time_str)
    except ValueError:
        return

    for msg in data.get("messages", []):
        date_str = msg.get("date")
        if not date_str:
            continue
        try:
            msg_time = datetime.fromisoformat(date_str)
        except Exception:
            continue
        if start_time <= msg_time <= end_time:
            yield msg

def show_message(msg):
    time_str = msg.get("date", "")
    try:
        dt = datetime.fromisoformat(time_str)
        time = dt.strftime("%Y/%m/%d %H:%M:%S")
    except Exception:
        time = time_str

    sender = msg.get("from", "невідомо")
    text = msg.get("text", "")
    print(f"[{time}] {sender}: {text}")

def show_messages_in_range(start_time_str, end_time_str, data):
    print(f"\nПовідомлення з {start_time_str} по {end_time_str}:")
    found = False
    for msg in get_messages_by_time_range(start_time_str, end_time_str, data):
        show_message(msg)
        found = True
    if not found:
        print("Повідомлень у цей період немає.")

def analytics(data):
    messages = data.get("messages", [])
    message_count = {}

    for msg in messages:
        sender = msg.get("from", "невідомо")
        message_count[sender] = message_count.get(sender, 0) + 1

    print("Кількість повідомлень від кожного користувача:")
    for sender, count in message_count.items():
        print(f"{sender}: {count}")

    print("\nПерші 5 повідомлень:")
    for msg in messages[:5]:
        show_message(msg)

def extract_words(text):
    if isinstance(text, list):
        text = ''.join(part["text"] if isinstance(part, dict) else str(part) for part in text)
    if not isinstance(text, str):
        return []
    return re.findall(r'\b\w+\b', text.lower(), flags=re.UNICODE)

def get_top_words_all_users(data, top_n=10, exclude_stopwords=True):
    all_words = Counter()
    user_words = defaultdict(Counter)

    for msg in data.get("messages", []):
        if msg.get("type") != "message":
            continue

        sender = msg.get("from", "невідомо")
        words = extract_words(msg.get("text", ""))

        if exclude_stopwords:
            words = [w for w in words if w not in STOP_WORDS]

        all_words.update(words)
        user_words[sender].update(words)

    result = {"всі": all_words.most_common(top_n)}
    for user, counter in user_words.items():
        result[user] = counter.most_common(top_n)

    return result

def get_top_words_by_user(data, user, top_n=10, exclude_stopwords=True):
    words = extract_words(data.get("messages", []))
    if exclude_stopwords:
        words = [w for w in words if w not in STOP_WORDS]




if __name__ == '__main__':
    data = get_all_msgs("chat_export/result.json")

    print("Аналітика повідомлень:")
    analytics(data)

    exclude = input("\nВиключати стоп-слова? (так/ні): ").strip().lower()
    exclude_stopwords = exclude in {"так", "yes", "y", "true", "т", "1"}

    result = get_top_words_all_users(data, exclude_stopwords=exclude_stopwords)

    print("\nТОП слова серед усіх:")
    for word, count in result["всі"]:
        print(f"{word:<15} ➤ {count}")

    print("\nТОП слова по кожному користувачу:")
    for user, top_words in result.items():
        if user == "всі":
            continue
        print(f"\n{user}:")
        for word, count in top_words:
            print(f"{word:<15} ➤ {count}")

    while True:
        print("\nБажаєте переглянути повідомлення за певний період?")
        use_date_filter = input("Ввести діапазон дат? (так/ні): ").strip().lower()
        if use_date_filter not in {"так", "yes", "y", "т", "1"}:
            print("Вихід із програми. Гарного дня!")
            break

        start_human = input("Початкова дата (дд.мм.рррр гг:хх): ")
        end_human = input("Кінцева дата (дд.мм.рррр гг:хх): ")
        show_messages_in_range(start_human, end_human, data)

        cont = input("\nБажаєте зробити ще один запит? (так/ні): ").strip().lower()
        if cont not in {"так", "yes", "y", "т", "1"}:
            print("Вихід із програми. До зустрічі!")
            break



