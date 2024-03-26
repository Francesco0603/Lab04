import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self,e):
        txtIn = self._view.txt_input.value
        self._view.txt_out.controls.append(ft.Text(f"FRASE INSERITA: {txtIn}"))
        self._view.txt_input.value = ""
        self._view.txt_message2.value = ""
        self._view.txt_message.value = ""
        modality = self._view.type_dropdown.value
        language = self._view.language_dropdown.value
        words = txtIn.split()
        paroleErrate = ""

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + ", "
                t2 = time.time()
                self._view.txt_out.controls.append(ft.Text(f"PAROLE ERRATE: {paroleErrate}"))
                self._view.txt_out.controls.append(ft.Text(f"TEMPO DI RICERCA: {t2 - t1}"))
                self._view.update()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + ", "
                t2 = time.time()
                self._view.txt_out.controls.append(ft.Text(f"PAROLE ERRATE: {paroleErrate}"))
                self._view.txt_out.controls.append(ft.Text(f"TEMPO DI RICERCA: {t2 - t1}"))
                self._view.update()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + ", "
                t2 = time.time()
                self._view.txt_out.controls.append(ft.Text(f"PAROLE ERRATE: {paroleErrate}"))
                self._view.txt_out.controls.append(ft.Text(f"TEMPO DI RICERCA: {t2 - t1}"))
                self._view.update()
                return paroleErrate, t2 - t1
            case _:
                return None

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text


