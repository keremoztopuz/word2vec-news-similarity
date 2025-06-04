# Word2Vec ile Haber Verisi Üzerinde Kelime Benzerliği

Bu proje, BBC haber verisinden elde edilen metinler üzerinde Word2Vec modeli eğiterek kelime gömme (word embedding) oluşturmayı ve kullanıcıdan alınan bir kelime için en benzer kelimeleri bulmayı amaçlamaktadır.

## Proje Yapısı

- `data/` : BBC haber verisinin bulunduğu dizin (`bbc_news.csv`).
- `models/` : Eğitilen Word2Vec model dosyaları (`wordvectors.kv`).
- `src/` : Kaynak kod dosyaları.
  - `utils.py` : Temizleme, tokenizasyon ve veri yükleme fonksiyonları.
  - `train_model.py` : Word2Vec modeli eğitimi.
  - `query_model.py` : Eğitilmiş model üzerinde kelime benzerliği sorgulama.
- `main.py` : Kullanıcıdan kelime alarak benzer kelimeleri bulan ana çalıştırılabilir dosya.
- `README.md` : Proje açıklaması ve kullanım talimatları.
- `requirements.txt` : Gerekli Python paketleri.

## Kurulum

Gerekli Python kütüphanelerini yüklemek için:

```bash
pip install -r requirements.txt


### 5. **Kullanım Talimatları**

```markdown
## Kullanım

1. Veriyi yükleyip temizlemek ve Word2Vec modelini eğitmek için:

```bash
python src/train_model.py

python main.py


### 6. **Örnek Kullanım**

```markdown
## Örnek

```bash
Bir kelime girin: economy
en benzer 5 kelime:
growth: 89%
market: 85%
finance: 83%
investment: 80%
trade: 78%


### 7. **Veri Hakkında**

```markdown
## Veri Seti

Kullanılan veri seti: **BBC News Articles Dataset**

Her satırda bir haber açıklaması (`description`) bulunmaktadır.

## Lisans

Bu proje kişisel kullanım ve eğitim amaçlıdır.
