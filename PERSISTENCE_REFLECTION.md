# Reflexion – Persistenzmodul (JSON)

Nutzen eines Persistenzmoduls

Ein Persistenzmodul sorgt dafür, dass Daten nicht nur während der Programmlaufzeit existieren, sondern dauerhaft gespeichert werden. Im Bürgerregister bedeutet das, dass einmal erfasste Personendaten auch nach einem Neustart der Anwendung wieder verfügbar sind. Gleichzeitig trennt ein eigenes Persistenzmodul fachliche Logik von technischer Speicherung, was den Code übersichtlicher und wartbarer macht.

Eignung von JSON

JSON ist für kleine Projekte gut geeignet, da es leichtgewichtig, gut lesbar und ohne zusätzliche Infrastruktur nutzbar ist. Die Struktur passt gut zu einfachen Datenmodellen wie Personenobjekten, und die Verarbeitung ist in Python ohne großen Aufwand möglich. Für Lernzwecke ist JSON daher eine praktische und verständliche Lösung.

Kritische Randfälle

Wichtige Randfälle sind fehlende, leere oder fehlerhafte Dateien sowie fehlende Zugriffsrechte. Das Persistenzmodul muss solche Situationen erkennen und so behandeln, dass das Programm nicht abstürzt, sondern zum Beispiel mit einer leeren Datenbasis weiterarbeitet oder verständliche Fehlermeldungen ausgibt.

Weiterentwicklung

Für größere Systeme wäre JSON nur begrenzt geeignet. Mit wachsender Datenmenge steigen Ladezeiten und Fehleranfälligkeit. In solchen Fällen würde man auf eine Datenbanklösung umsteigen, die besser mit großen Datenmengen und parallelen Zugriffen umgehen kann.

Abwärtskompatibilität

Damit alte Daten auch nach Änderungen am Datenmodell noch nutzbar bleiben, sollten gespeicherte Daten versioniert werden. Beim Laden kann dann geprüft werden, ob eine Migration nötig ist, um alte Formate in das neue Datenmodell zu überführen.


In dieser Prüfungsleistung habe ich ein bestehendes Projekt schrittweise weiterentwickelt und dabei besonderen Wert auf Codequalität, Nachvollziehbarkeit und professionelle Arbeitsweise gelegt. Ausgangspunkt war ein funktionierendes Bürgerregister-Projekt, das bereits grundlegende Funktionen wie Anlegen, Suchen und Validieren von Personen enthielt. Mein Ziel war es nicht, neue Features zu bauen, sondern den vorhandenen Code systematisch zu verbessern und ihn näher an gängige Standards aus dem Software Engineering heranzuführen.

Zunächst habe ich den Code inhaltlich überprüft und auf Lesbarkeit, Struktur und Verständlichkeit geachtet. Dabei habe ich unter anderem Funktions- und Variablennamen vereinheitlicht und aussagekräftiger gestaltet, unnötige oder doppelte Logik reduziert und die Struktur einzelner Dateien übersichtlicher gemacht. Besonders wichtig war mir, dass man auch ohne tiefes Vorwissen schnell erkennt, welche Aufgabe eine Funktion erfüllt und wie der Datenfluss im Programm abläuft.

Parallel dazu habe ich die vorhandenen Tests genutzt, um jede Änderung abzusichern. Nach jedem größeren Schritt habe ich die Tests lokal mit pytest ausgeführt, um sicherzustellen, dass mein Refactoring keine fachlichen Fehler verursacht. Dadurch konnte ich sicher arbeiten, ohne Angst zu haben, unbemerkt Funktionalität zu zerstören. Diese testgetriebene Kontrolle hat mir gezeigt, wie wichtig automatisierte Tests für sauberes Refactoring sind.

Im nächsten Schritt habe ich Werkzeuge zur automatischen Codeprüfung eingeführt. Dazu habe ich das Tool ruff eingebunden, das Stilregeln, typische Fehlerquellen und Import-Strukturen überprüft. Anfangs gab es viele Hinweise, vor allem zu unsauberen Imports und zur Reihenfolge von Anweisungen. Diese Meldungen habe ich systematisch abgearbeitet, indem ich die betroffenen Dateien angepasst, alte Pfad-Tricks entfernt und die Tests so umgebaut habe, dass sie sauber über das installierte Paket importieren. Dadurch ist der Code nicht nur regelkonform, sondern auch deutlich verständlicher und professioneller geworden.

Ein weiterer wichtiger Teil war die Einführung von Continuous Integration über GitHub Actions. Ich habe einen Workflow erstellt, der bei jedem Push und bei Pull Requests automatisch ausgeführt wird. Dieser Workflow installiert das Projekt, führt ruff zur Stil- und Qualitätsprüfung aus und startet anschließend alle Tests mit pytest. So wird jede Änderung automatisch überprüft, ohne dass man manuell daran denken muss. Fehler werden sofort sichtbar, was die Qualität langfristig absichert.

Um strukturiert zu arbeiten, habe ich meine Änderungen in einem eigenen Branch durchgeführt und über einen Pull Request in den Hauptbranch integriert. Dabei habe ich darauf geachtet, dass alle Checks grün sind, bevor gemerged wurde. Dieser Ablauf entspricht dem Vorgehen in professionellen Softwareprojekten und hat mir gezeigt, wie wichtig klare Arbeitsabläufe, Reviews und automatisierte Prüfungen sind.

Zusammenfassend habe ich gelernt, dass „Clean Code“ nicht nur aus schöner Formatierung besteht, sondern aus klaren Namen, einfacher Struktur, nachvollziehbarer Logik und guter Absicherung durch Tests. Durch den Einsatz von Linting-Tools, automatisierten Tests und Continuous Integration habe ich erlebt, wie technische Qualität systematisch unterstützt werden kann. Die Arbeit an diesem Projekt hat mir gezeigt, wie aus einem funktionierenden, aber eher einfachen Code schrittweise ein gut strukturierter, geprüfter und professionell verwalteter Softwarestand entstehen kann.


Bild von allen Workflows (Alle sind Grün)

<img width="1838" height="763" alt="image" src="https://github.com/user-attachments/assets/611bbd50-f165-4789-a5df-8baf950c03fb" />








Bild vom Workflow (Alles Grün)

<img width="1863" height="762" alt="image" src=  "https://github.com/user-attachments/assets/47dfe0e9-9620-48ba-bbe1-cb510505e13a" />





