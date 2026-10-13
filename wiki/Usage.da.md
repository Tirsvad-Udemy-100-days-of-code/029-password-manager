[English](Usage) | **Dansk** | [Bahasa Malaysia](Usage.ms)

# Brug

## Tilføj en post

1. Skriv webstedet i **Website**.
2. Kontroller eller ret e-mailen i **Email/Username**.
3. Klik på **Generate Password**. Adgangskoden vises og kopieres til udklipsholderen.
4. Klik på **Add**. En dialog viser, hvad der bliver gemt.
5. Klik på **OK** for at gemme. Felterne for websted og adgangskode bliver tømt.

![En genereret adgangskode](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/029-password-manager/raw/branch/main/docs/images/mypass-generated.png)

![Bekræftelsesdialogen](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/029-password-manager/raw/branch/main/docs/images/mypass-confirm.png)

## Tomme felter

Hvis webstedet eller adgangskoden er tom, vises en advarsel, og der gemmes intet.

## Hvor data havner

Hver post er én linje i `data.txt` i den mappe, du starter programmet fra, på formen `website | email | password`.

> Advarsel: filen er ren tekst og ikke krypteret. Brug den ikke til rigtige adgangskoder.
