Sayi tahmin oyunu

Bu Python oyunu, kullanıcının 1 ile 100 arasındaki bir sayıyı tahmin etmesini sağlayan bir oyun sunar. Oyuncunun yalnızca 5 tahmin hakkı vardır. Her yanlış tahminden sonra, oyuncuya daha küçük veya daha büyük sayılar denemesi gerektiği bilgisi verilir. Oyuncu doğru tahmin ettiğinde oyun sonlanır.

Özellikler:
1 ile 100 arasında rastgele bir sayı tutulur.
Kullanıcı, 5 tahmin hakkına sahiptir.
Yanlış tahminler sonrasında kullanıcıya doğru yöne (daha küçük veya daha büyük) yönlendirme yapılır.
Hakkı biten kullanıcıya doğru sayı gösterilir.
Oyunun sonunda kullanıcıya "Tekrar oynamak ister misin?" mesajı gösterilir.

------------------------------------------------------------------------------------------------------------------------------------------

Kullanım Talimatları:
Python'un yüklü olduğundan emin olun.
Aşağıdaki komutla oyunu çalıştırabilirsiniz:
bash
Kodu kopyala
python sayi_tahmin_oyunu.py

------------------------------------------------------------------------------------------------------------------------------------------

Kod Açıklamaları:
random.randint(1, 101): 1 ile 100 arasında rastgele bir sayı üretir.
hak = 5: Başlangıçta oyuncuya 5 tahmin hakkı verilir.
while hak > 0: Oyuncunun hakları bitene kadar oyun devam eder.
input("Tahminin nedir? "): Kullanıcıdan tahmin alınır.
Her yanlış tahminden sonra kalan hak kullanıcıya bildirilir.
Doğru tahmin yapıldığında kullanıcıya "Tebrikler!" mesajı gösterilir ve oyun sona erer.
