# SerialDataViewer

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/PyQt5-41CD52?style=for-the-badge&logo=qt&logoColor=white" alt="PyQt5" />
  <img src="https://img.shields.io/badge/pySerial-20232A?style=for-the-badge" alt="pySerial" />
</p>

## 🇬🇧 Overview

A PyQt5 desktop tool that connects to a serial port and shows incoming sensor packets (acceleration, gyro, angle, temperature, pressure, humidity) in a live table.

**Quick start:** `pip install -r requirements.txt && python main.py`

## 🇹🇷 Proje hakkında

Seri porttan gelen sensör paketlerini canlı bir tabloda gösteren PyQt5 masaüstü aracı. İvme, jiroskop, açı, sıcaklık, basınç ve nem değerlerini boşlukla ayrılmış paketlerden ayrıştırır.

## ✨ Özellikler

- Port ve baud hızı seçimi (9600–115200)
- Bağlan / bağlantıyı kes
- 13 kanallı veri tablosu: accel XYZ, gyro XYZ, angle XYZ, iki sıcaklık, basınç, nem
- Arayüz Qt Designer ile tasarlandı (`qtdesigner.py`)

## ⚙️ Kurulum ve çalıştırma

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

```bash
python main.py
```

## 📁 Dosya yapısı

```text
SerialDataViewer/
├── main.py
└── qtdesigner.py
```
