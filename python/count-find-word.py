text = input("متن خودتون رو وارد کنید: ")

if text.strip() == "":
    print("خطا: متن نمی‌تونه خالی باشه!")
else:
    words = text.split()
    word_count = len(words)
    
    char_count = len(text.replace(" ", ""))
    
    search_word = input("کلمه برای جستجو: ")
    
    if search_word.strip() == "":
        print("خطا: کلمه نمی‌تونه خالی باشه!")
    else:
        if text.lower().find(search_word.lower()) != -1:
            search_result = f"کلمه '{search_word}' تو متن پیدا شد!"
        else:
            search_result = f"کلمه '{search_word}' تو متن پیدا نشد!"
        
        print(f"تعداد کلمات: {word_count}")
        print(f"تعداد حروف (بدون فاصله): {char_count}")
        print(search_result)