# Informacje o danych (BRFSS 2020)

Projekt wykorzystuje plik `heart_2020_cleaned.csv` udostępniony w zbiorze [Personal Key Indicators of Heart Disease](https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease) przez Kamila Pytlaka. Zbiór powstał na podstawie amerykańskiego badania **Behavioral Risk Factor Surveillance System (BRFSS) 2020**. Data utworzenia/udostępnienia materiałów projektu może być późniejsza; nie oznacza to, że dane ankietowe pochodzą z 2022 roku.

- 319 795 rekordów; 18 kolumn, w tym `HeartDisease`.
- Cztery kolumny numeryczne: `BMI`, `PhysicalHealth`, `MentalHealth`, `SleepTime`.
- 0 pustych wartości w udostępnionym CSV.
- `HeartDisease = Yes`: 27 373 (8,56%); `No`: 292 422 (91,44%).
- 18 078 rekordów ma identyczne wartości wszystkich pól jak inny wiersz. Bez identyfikatorów respondentów nie oznacza to potwierdzonych duplikatów osób.

**Ważne:** są to odpowiedzi ankietowe, a nie kliniczne diagnozy. Zależności statystyczne nie dowodzą związków przyczynowych. Nierównowaga klas sprawia, że sama accuracy nie jest wystarczającą metryką modelu.

Dodatkowe materiały o pochodzeniu/przetwarzaniu danych: [oryginalny notebook przetwarzania danych](https://github.com/kamilpytlak/data-science-projects/blob/main/heart-disease-prediction/2022/notebooks/data_processing.ipynb).

Korzystanie i dalsze rozpowszechnianie zbioru należy oceniać na podstawie warunków źródła danych, odrębnie od licencji kodu repozytorium.
