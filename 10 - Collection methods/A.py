text = "un día que el viento soplaba con fuerza#" \
        "mira como se mueve aquella banderola -dijo un monje#" \
        "lo que se mueve es el viento -respondió otro monje#" \
        "ni las banderolas ni el viento, " \
        "lo que se mueve son vuestras mentes -dijo el maestro"

text = text.split("#")
def format_text():
    new_text = []
    for index, line in enumerate(text):
        line = line.capitalize()
        if index > 0:
            line = " - " + line + "."
        else:
            line = line + "..."
        new_text.append(line)

    return "\n".join(new_text)
        
print(format_text())