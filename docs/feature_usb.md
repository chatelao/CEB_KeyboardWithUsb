# Roadmap: USB-Integration

Dieses Dokument beschreibt die Schritte zur Integration der USB-Funktionalität in das Projekt.

## Hardware

- [ ] **Komponentenauswahl:**
    - [ ] USB-Hub-Controller: CoreChips SL2.1A (bereits ausgewählt).
    - [ ] USB-Anschlüsse:
        - [ ] 2x USB Typ-A Buchsen (für den Anschluss von Peripheriegeräten).
        - [ ] 1x USB Typ-B Buchse (für den Anschluss an einen Host-Computer, ausgewählt für hohe mechanische Stabilität und Langlebigkeit).
    - [ ] Passive Bauteile (Widerstände, Kondensatoren) gemäß Datenblatt des SL2.1A.
    - [ ] ESD-Schutzdioden für alle USB-Datenleitungen.
    - [ ] Spannungsregler für die 5V-Versorgung des USB-Hubs.

- [ ] **Schaltplan-Design:**
    - [ ] SL2.1A-Hub-Controller in den Schaltplan integrieren.
    - [ ] Upstream-Port (USB-B) mit dem Hub verbinden.
    - [ ] Downstream-Ports (2x USB-A) mit dem Hub verbinden.
    - [ ] Beschaltung des Hubs gemäß den Empfehlungen im Datenblatt (inkl. Quarz, Pull-up/Pull-down-Widerstände, Entkopplungskondensatoren).
    - [ ] Stromversorgung für die Downstream-Ports entwerfen (inkl. Überstromschutz, z.B. mit Polyswitches).
    - [ ] ESD-Schutz an allen externen USB-Ports implementieren.

- [ ] **PCB-Layout:**
    - [ ] USB-B-Anschluss für eine stabile und langlebige Verbindung positionieren.
    - [ ] USB-A-Anschlüsse ergonomisch für den einfachen Zugang platzieren.
    - [ ] Differentielle USB-Datenleitungen (D+/D-) als impedanzkontrollierte Paare (90 Ohm) routen.
    - [ ] Länge der differentiellen Paare anpassen (Length Matching).
    - [ ] Kurze Leiterbahnen für die Verbindungen zum Hub-Controller anstreben.
    - [ ] Saubere Stromversorgung für den Hub und die Ports sicherstellen (eigene Power-Plane oder breite Leiterbahnen).
    - [ ] ESD-Schutzbauteile so nah wie möglich an den USB-Anschlüssen platzieren.

- [ ] **Prototyping & Test:**
    - [ ] Prototypen-Platine fertigen lassen.
    - [ ] Bestückung und Inbetriebnahme des USB-Hubs.
    - [ ] Elektrische Überprüfung der Stromversorgung und Signalintegrität.
    - [ ] Funktionstest mit einem Host-Computer und verschiedenen USB-Peripheriegeräten.

## Software/Firmware

Da der SL2.1A ein reiner Hardware-Hub-Controller ist, sind keine spezifischen Treiber oder Firmware-Anpassungen auf dem Gerät selbst erforderlich. Die Funktionalität wird vom Betriebssystem des Host-Computers gehandhabt.

- [ ] **Validierung:**
    - [ ] Sicherstellen, dass der Hub von gängigen Betriebssystemen (Windows, macOS, Linux) ohne zusätzliche Treiberinstallation erkannt wird.
    - [ ] Testen der Datenübertragungsraten (USB 2.0 High Speed).
    - [ ] Überprüfen der Funktionalität aller Downstream-Ports.
