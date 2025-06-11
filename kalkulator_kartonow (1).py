
import streamlit as st
from math import ceil

st.set_page_config(page_title="Kalkulator kartonów", layout="centered")
st.image("https://i.imgur.com/yourlogo.png", width=200)
st.title("📦 Kalkulator wymiarów kartonu")

# Pobieranie danych od użytkownika
length_mm = st.number_input("Podaj długość (mm):", min_value=0)
width_mm = st.number_input("Podaj szerokość (mm):", min_value=0)
height_mm = st.number_input("Podaj wysokość (mm):", min_value=0)

if st.button("Oblicz"):
    try:
        # Przeliczenia na cm z zaokrągleniem w górę
        length_cm = ceil(length_mm / 10)
        width_cm = ceil(width_mm / 10)
        height_cm = ceil(height_mm / 10)

        height_fill = height_cm + 6

        dimension_A = (length_cm + 14) + 2 * height_fill
        dimension_B = (width_cm + 14) + 2 * height_fill
        czepek_A = dimension_A + 4
        czepek_B = dimension_B + 4

        st.subheader("Po konwersji:")
        st.write(f"Długość: {length_cm} cm")
        st.write(f"Szerokość: {width_cm} cm")
        st.write(f"Wysokość: {height_cm} cm")

        st.subheader("Wymiary kartonu na chłodnicę:")
        st.write(f"{dimension_A} cm x {dimension_B} cm")

        st.subheader("Wymiary kartonu na czepek:")
        st.write(f"{czepek_A} cm x {czepek_B} cm")

    except Exception as e:
        st.error("Wystąpił błąd podczas obliczeń. Upewnij się, że dane są poprawne.")

st.markdown("---")
st.caption("Autor: Kuba1999 ")
