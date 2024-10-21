# Engeto Python projekt è. 3
Tøetí projekt v rámci Python Akademie od Engeta.

## Popis projektu
Projekt je vìnován nástroji sloužícímu k extrahování výsledkù parlamentních voleb konaných v roce 2017. Odkaz k prohlédnutí najdete [zde](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ).

## Instalace knihoven
Knihovny, které byly použity v rámci projektu, jsou uloženy v pøiloženém souboru requirements.txt. Pro instalaci doporuèuji vytvoøit nové virtuální prostøedí a s nainstalovaným manažerem postupovat v konzoli následovnì:

	Ovìøení verze manažeru: pip --version
	Instalace knihoven: pip install -r requirements.txt	

## Spuštìní projektu
Pro úspìšné spuštìní souboru "election_scraper.py" je potøeba do pøíkazového øádku konzole zadat dva povinné argumenty:

	Python election_scraper.py "odkaz_územního_celku" "výsledný_soubor" 

Po spuštìní dojde ke stažení a následnému zápisu výsledkù voleb do souboru s pøíponou .csv.

## Ukázka projektu
Výsledky hlasování pro okres Frýdek-Místek:

	1. argument: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8102
	2. argument: results_frýdek-místek.csv

Spuštìní programu:

	Python election_scraper.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8102" "results_frýdek-místek.csv"

Prùbìh stahování:

	Initiating data scraping from selected URL: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8102
	Saving data into file: results_frýdek-místek.csv
	10% complete
	20% complete
	30% complete
	40% complete
	50% complete
	60% complete
	70% complete
	80% complete
	90% complete
	100% complete. Your file "results_frýdek-místek.csv" is ready for use.

Èásteèný výstup:

	code;location;registered;envelopes;valid...
	598011;Baška;3 093;2 065;2 053;175;1;1;124;1;49;192;21;12;21;1;0;216;0;0;44;665;2;9;194;1;16;7;3;293;5
	598020;Bílá;285;178;178;19;0;0;14;0;10;21;3;1;0;1;0;12;1;0;3;52;0;0;15;0;3;0;0;23;0
	511633;Bocanovice;358;197;197;20;0;0;32;0;3;13;3;1;0;0;0;18;0;1;1;45;0;0;43;0;0;0;0;17;0...




