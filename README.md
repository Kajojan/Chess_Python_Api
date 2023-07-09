# Chess_Python_Api

Aplikacja działa na docker, aby odpalić:

będą w folderze /Chess_Python_Api

docker-compose up 

na początku odpali się aplikacja po stwierdzeniu healtcheck odpalą się testy 

Algorytmy ruszania są oparte na pustej tablicy , można to zmienić odkomentowując 7 linijke w app.py ( "# chessboard.create()" ) funkcja ta nakłada na szachownice 16 figór ( 8 czarna i 8 biała ) w początkowym ustawieniu. Wtedy wyniki zapytań będą skorygowane z innymi figurami na planszy, gdyż nie można stanąć na tym samym polu co inna figura lub nie można jej "przeskoczyć" .

