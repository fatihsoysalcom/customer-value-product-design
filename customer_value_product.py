import sys

# Core concept: Define customer problems first, reflecting the article's emphasis on customer needs.
CUSTOMER_PROBLEMS = [
    "Yavaş internet bağlantısı", # Slow internet connection
    "Karmaşık yazılım arayüzleri", # Complex software interfaces
    "Yüksek enerji faturaları", # High energy bills
    "Zaman alıcı günlük işler", # Time-consuming daily tasks
    "Güvenlik endişeleri (veri gizliliği)", # Security concerns (data privacy)
]

# Core concept: Solutions (products/features) are designed *after* identifying specific problems.
# This dictionary maps a customer problem (key) to a set of features (value) that directly solve it.
PRODUCT_SOLUTIONS = {
    "Yavaş internet bağlantısı": [
        "Yüksek hızlı fiber optik modem",
        "Akıllı bant genişliği yönetimi yazılımı",
        "Mesh Wi-Fi sistemi"
    ],
    "Karmaşık yazılım arayüzleri": [
        "Sezgisel sürükle-bırak arayüzü",
        "Özelleştirilebilir kontrol paneli",
        "Yapıcı yapay zeka destekli yardım asistanı"
    ],
    "Yüksek enerji faturaları": [
        "Akıllı termostat",
        "Enerji verimli ev aletleri",
        "Güneş paneli entegrasyonu"
    ],
    "Zaman alıcı günlük işler": [
        "Otomatik görev planlayıcı",
        "Sesli komutla kontrol edilen robot süpürge",
        "Tek tıkla alışveriş listesi oluşturucu"
    ],
    "Güvenlik endişeleri (veri gizliliği)": [
        "Uçtan uca şifreleme",
        "İki faktörlü kimlik doğrulama",
        "Anonim veri toplama seçenekleri"
    ]
}

def identify_customer_needs():
    """
    Asks the user to identify the most pressing customer problem.
    This simulates the initial step of a customer-centric business model:
    understanding what value the customer seeks.
    """
    print("\nMüşteri değerine odaklanarak bir ürün geliştirelim.")
    print("Lütfen aşağıdaki müşteri sorunlarından en önemlisini seçin:")

    for i, problem in enumerate(CUSTOMER_PROBLEMS):
        print(f"{i + 1}. {problem}")

    while True:
        try:
            choice = input("Seçiminiz (numara girin): ")
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(CUSTOMER_PROBLEMS):
                selected_problem = CUSTOMER_PROBLEMS[choice_index]
                print(f"\nSeçilen müşteri sorunu: '{selected_problem}'")
                return selected_problem
            else:
                print("Geçersiz seçim. Lütfen listeden bir numara girin.")
        except ValueError:
            print("Geçersiz giriş. Lütfen bir sayı girin.")

def design_product_based_on_needs(problem):
    """
    Designs a product (lists features) based on the identified customer problem.
    This demonstrates building solutions *after* understanding the need,
    ensuring the product delivers direct customer value.
    """
    if problem in PRODUCT_SOLUTIONS:
        solutions = PRODUCT_SOLUTIONS[problem]
        print(f"\n'{problem}' sorununu çözmek için tasarlanan ürün özellikleri:")
        for i, solution in enumerate(solutions):
            print(f"- {solution}")
        print("\nBu ürün, doğrudan müşterinin ihtiyacına odaklanarak değer yaratmayı hedefler.")
    else:
        print(f"Üzgünüz, '{problem}' için henüz bir çözümümüz yok. Müşteri araştırması yapmalıyız!")

if __name__ == "__main__":
    print("--- Müşteri Odaklı Ürün Geliştirme Simülasyonu ---")
    
    # Step 1: Identify the customer's core problem (the "value" to deliver).
    # This is where the business model starts, according to the article.
    selected_problem = identify_customer_needs()
    
    # Step 2: Design the product (features) specifically to address that problem.
    # The product's existence is justified by solving a customer's problem.
    if selected_problem:
        design_product_based_on_needs(selected_problem)
    
    print("\n--- Simülasyon Sonu ---")
