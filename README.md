# Engeto Python projekt �. 3
T�et� projekt v r�mci Python Akademie od Engeta.

## Popis projektu
Projekt je v�nov�n n�stroji slou��c�mu k extrahov�n� v�sledk� parlamentn�ch voleb konan�ch v roce 2017. Odkaz k prohl�dnut� najdete [zde](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ).

## Instalace knihoven
Knihovny, kter� byly pou�ity v r�mci projektu, jsou ulo�eny v p�ilo�en�m souboru requirements.txt. Pro instalaci doporu�uji vytvo�it nov� virtu�ln� prost�ed� a s nainstalovan�m mana�erem postupovat v konzoli n�sledovn�:

	Ov��en� verze mana�eru: pip --version
	Instalace knihoven: pip install -r requirements.txt	

## Spu�t�n� projektu
Pro �sp�n� spu�t�n� souboru "election_scraper.py" je pot�eba do p��kazov�ho ��dku konzole zadat dva povinn� argumenty:

	Python election_scraper.py "odkaz_�zemn�ho_celku" "v�sledn�_soubor" 

Po spu�t�n� dojde ke sta�en� a n�sledn�mu z�pisu v�sledk� voleb do souboru s p��ponou .csv.

## Uk�zka projektu
V�sledky hlasov�n� pro okres Fr�dek-M�stek:

	1. argument: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8102
	2. argument: results_fr�dek-m�stek.csv

Spu�t�n� programu:

	Python election_scraper.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8102" "results_fr�dek-m�stek.csv"

Pr�b�h stahov�n�:

	Initiating data scraping from selected URL: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8102
	Saving data into file: results_fr�dek-m�stek.csv
	10% complete
	20% complete
	30% complete
	40% complete
	50% complete
	60% complete
	70% complete
	80% complete
	90% complete
	100% complete. Your file "results_fr�dek-m�stek.csv" is ready for use.

��ste�n� v�stup:

	code;location;registered;envelopes;valid...
	598011;Ba�ka;3 093;2 065;2 053;175;1;1;124;1;49;192;21;12;21;1;0;216;0;0;44;665;2;9;194;1;16;7;3;293;5
	598020;B�l�;285;178;178;19;0;0;14;0;10;21;3;1;0;1;0;12;1;0;3;52;0;0;15;0;3;0;0;23;0
	511633;Bocanovice;358;197;197;20;0;0;32;0;3;13;3;1;0;0;0;18;0;1;1;45;0;0;43;0;0;0;0;17;0...




