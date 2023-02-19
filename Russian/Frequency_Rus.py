# Copyright © 2023 Erow. All rights reserved.
import collections
import pathlib

alphabet = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")


def write_statistic():
    file_data = pathlib.Path("in_Rus.txt").read_text(encoding="utf-8").casefold()
    letters_statistic = {}

    for letter in alphabet:
        letters_statistic[letter] = 0

    count = 0

    for text_letter in file_data:
        if text_letter not in letters_statistic:
            continue
        count += 1
        letters_statistic[text_letter] += 1

    count_data = ""
    percent_data = ""
    percent_csv_data = ""

    counter = collections.Counter(letters_statistic)

    last = 100
    for stat_letter, letter_count in counter.most_common():
        count_data += f"{stat_letter}\t|\t{letter_count}\n"
        new = round(100 / count * letter_count, 2)
        if (
            new < 6 <= last
            or new < 3 <= last
            or new < 2 <= last
            or new < 1 <= last
            or new < 0.5 <= last
        ):
            percent_data += "\n"
        percent_data += f"{stat_letter}\t|\t{round(100 / count * letter_count, 2)}\n"

        percent_csv_data += (
            f"{stat_letter}\t{str(round(round(100 / count * letter_count, 2) / 100, 4)).replace('.', ',')}\n"
        )

        last = round(100 / count * letter_count, 2)

    pathlib.Path("counts_Rus.txt").write_text(count_data, encoding="utf-8")
    pathlib.Path("procent_Rus.txt").write_text(percent_data, encoding="utf-8")
    pathlib.Path("procentForExcel_Rus.txt").write_text(percent_csv_data, encoding="utf-8")


if __name__ == "__main__":
    write_statistic()
