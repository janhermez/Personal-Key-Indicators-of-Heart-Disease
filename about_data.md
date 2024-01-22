Liczba obserwacji wynosi 319795 
Baza zawiera 18 zmiennych, z czego 4 są ilościowe, a pozostałe 14 to kategoryczne.

Dane były zapisane w ramach jednego pliku w formacie csv. Dane zaimportowane przy pomocy funkcji read_csv z zestawu pakietów tidyverse. Wykorzystany tylko podstawowy argument funkcji, gdyż standard zapisu csv nie wymagał dalszych poleceń.

Modelowaną przez dane zmienną (kolumną) jest wystąpienie choroby serca (HeartDisease). Wszystkie pozostałe kolumny dostarczają dodatkowych atrybutów danych i mogą posłużyć jako predyktory wyjaśniające, co wiąże się z zachorowaniem na chorobę serca. ?

Dane z corocznego badania CDC przeprowadzonego w 2022 r. wśród ponad 400 tys. dorosłych dotyczące ich stanu zdrowia.

Według CDC - Centers for Disease Control and Prevention (agencja rządu federalnego Stanów Zjednoczonych wchodząca w skład Departamentu Zdrowia i Opieki Społecznej) choroby serca są główną przyczyną śmierci ludzi w USA (Afroamerykanów, Indian amerykańskich i rdzennych mieszkańców Alaski oraz "rasy białej"). Około połowa Amerykanów (47%) ma co najmniej 1 z 3 głównych czynników ryzyka chorób serca: wysokie ciśnienie krwi, wysoki poziom cholesterolu i palenie. Inne kluczowe wskaźniki obejmują stan cukrzycy, otyłość (wysokie BMI), brak wystarczającej aktywności fizycznej lub picie zbyt dużej ilości alkoholu. Identyfikacja i zapobieganie czynnikom, które mają największy wpływ na choroby serca, jest bardzo ważne w opiece zdrowotnej. 

Z kolei rozwój informatyki umożliwia zastosowanie metod uczenia maszynowego do wykrywania „wzorców” w danych, które mogą przewidzieć stan pacjenta. 

Skąd pochodzi zbiór danych i jakiemu procesowi został poddany? 

Zbiór danych pochodzi pierwotnie z CDC i stanowi główną część systemu nadzoru nad czynnikami ryzyka behawioralnego (BRFSS), który przeprowadza coroczne ankiety telefoniczne w celu gromadzenia danych na temat stanu zdrowia mieszkańców USA. 

Jakie kroki zastosował do konwersji zbioru danych? Kamil Pytlak

https://github.com/kamilpytlak/data-science-projects/blob/main/heart-disease-prediction/2022/notebooks/data_processing.ipynb

## Wnioski z danych:

Baza nie zawiera żadnych braków danych.  

Dane odstające: BMI, mental health i physical health.

Zdecydowana większość badanych, bo aż prawie 80%, zadeklarowała uprawianie aktywności fizycznej. Jednocześnie, spora grupa osób, prawie połowa, paliła regularnie papierosy.

