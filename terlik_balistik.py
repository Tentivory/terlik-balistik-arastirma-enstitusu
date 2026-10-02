#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Terlik Balistik Araştırma Enstitüsü — saha simülatörü.

Gerçekten çalışır. Bilimsel iddiası çalışmaz.
"""

import math
import random

HEDEFLER = [
    "koltukta uyuyan amca",
    "masum duran kedi",
    "tv kumandasını saklayan kişi",
    "hiç suçu olmayan çiçeklik",
    "kapıyı açmadan yorum yapan misafir",
]


def menzil(hiz, aci_derece):
    aci = math.radians(aci_derece)
    return (hiz ** 2) * math.sin(2 * aci) / 9.81


def ucus_suresi(hiz, aci_derece):
    aci = math.radians(aci_derece)
    return 2 * hiz * math.sin(aci) / 9.81


def sucluluk(kutle, hiz):
    # Ağır terlik her zaman daha suçludur. Fizik değil, mahalle kuralı.
    return min(100.0, kutle * hiz * 1.7)


def tutanak(kutle, hiz, aci):
    m = menzil(hiz, aci)
    t = ucus_suresi(hiz, aci)
    s = sucluluk(kutle, hiz)
    hedef = random.choice(HEDEFLER)
    print("=" * 48)
    print(" TERLİK BALİSTİK TUTANAĞI")
    print("=" * 48)
    print(f"Kütle          : {kutle:.2f} kg")
    print(f"İlk hız        : {hiz:.2f} m/s")
    print(f"Açı            : {aci:.1f} derece")
    print(f"Menzil          : {m:.2f} metre")
    print(f"Uçuş süresi    : {t:.2f} saniye")
    print(f"Suçluluk       : %{s:.1f}")
    print(f"İsabet         : {hedef}")
    if m < 1.5:
        print("Hüküm          : Terlik utandı, yere düştü.")
    elif s > 70:
        print("Hüküm          : Ağırlaştırılmış pişmanlık.")
    else:
        print("Hüküm          : Kaza süsü verilmiş niyet.")
    print("=" * 48)
    print("DAMGA: MÜHÜR-TERLİK-404")
    print("İMZA: Kayyum Grok")
    print("TARİH: 02.10.2026")
    print("İSİM: Tentivory")


def main():
    print("Terlik Balistik Araştırma Enstitüsü açıldı.")
    print("Boş bırakırsanız standart terlik kullanılır.\n")
    try:
        kutle_girdi = input("Terlik kütlesi (kg) [0.18]: ").strip()
        hiz_girdi = input("Fırlatma hızı (m/s) [6.5]: ").strip()
        aci_girdi = input("Açı (derece) [37]: ").strip()
        kutle = float(kutle_girdi) if kutle_girdi else 0.18
        hiz = float(hiz_girdi) if hiz_girdi else 6.5
        aci = float(aci_girdi) if aci_girdi else 37.0
    except ValueError:
        print("Sayı değil bu. Enstitü standarına döndük.")
        kutle, hiz, aci = 0.18, 6.5, 37.0
    if not (0 < kutle < 5 and 0 < hiz < 40 and 1 <= aci <= 89):
        print("Değerler ev içi fiziğin dışında. Standart terlik.")
        kutle, hiz, aci = 0.18, 6.5, 37.0
    tutanak(kutle, hiz, aci)


if __name__ == "__main__":
    main()
