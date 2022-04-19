import HW03_Aman_Pawar_wordle


def log_writer(selected_word, user_input, played, won, stats):
    f = open("gameplay.log", "a+")
    f.write(f"Selected word: {selected_word} \n")
    f.write("Words: ")
    for val in user_input:
        f.write(f"{val}\t")
    f.write(f"\nGames played: {played}\n")
    f.write(f"Win percentage: {(won*100/played): .2f} \n")
    for i, game in enumerate(stats):
        f.write(f"Games won in {i+1} attempt: {game} \n")
    f.close()
