# Reflexion – Persistenzmodul (JSON)

## Nutzen eines Persistenzmoduls
Ein Persistenzmodul ermöglicht es, Daten über die Laufzeit eines Programms hinaus zu speichern.

## Eignung von JSON
JSON ist leichtgewichtig, gut lesbar und ohne zusätzliche Infrastruktur nutzbar.

## Kritische Randfälle
Fehlende, leere oder fehlerhafte Dateien müssen robust behandelt werden.

## Weiterentwicklung
In größeren Systemen würde eine Datenbank verwendet werden.

## Abwärtskompatibilität
Durch Versionierung und Migrationen.


Im Rahmen dieser Prüfungsleistung wurde deutlich, wie wichtig eine systematische Qualitätssicherung auch bei vergleichsweise kleinen Softwareprojekten ist. Durch den Einsatz von Unit-Tests konnten zentrale fachliche Anforderungen des Bürgerregisters überprüft und abgesichert werden, insbesondere in Bezug auf Validierung, Duplikaterkennung und Persistenz. Die Tests haben dabei nicht nur zur Fehlererkennung beigetragen, sondern auch das Vertrauen in die Korrektheit von Änderungen erhöht.

Die Analyse der Testabdeckung zeigte, dass ein großer Teil der fachlich relevanten Logik durch Tests abgedeckt ist. Gleichzeitig wurde deutlich, dass hohe Coverage-Werte allein keine Garantie für gute Softwarequalität darstellen. Entscheidend ist vielmehr, ob die richtigen Szenarien getestet werden und ob Rand- und Fehlerfälle sinnvoll berücksichtigt sind. Diese Erkenntnis führte zu einer bewussteren Bewertung der Testergebnisse.

Ergänzend verdeutlichte die Betrachtung einfacher Code-Metriken, dass insbesondere Validierungs- und Persistenzlogik eine erhöhte Komplexität aufweisen. Diese Komplexität ist fachlich nachvollziehbar, da hier viele Fehlerfälle abgefangen werden müssen, stellt jedoch langfristig einen Ansatzpunkt für strukturelle Verbesserungen dar. Insgesamt hat die Prüfungsleistung gezeigt, dass Qualitätssicherung nicht als nachgelagerter Schritt, sondern als integraler Bestandteil des Softwareentwicklungsprozesses zu verstehen ist.
