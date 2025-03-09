import random

def get_random_word():
    # Daftar kata yang bisa ditebak
    words = ['python', 'programming', 'developer', 'hangman', 'game', 'challenge']
    return random.choice(words)

def display_word(word, guessed_letters):
    # Menampilkan kata dengan huruf yang telah ditebak dan underscore untuk huruf yang belum
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman():
    print("Selamat datang di game Hangman!")
    word = get_random_word()
    guessed_letters = set()
    attempts = 6  # Jumlah kesempatan pemain
    
    while attempts > 0:
        print("\nKata:", display_word(word, guessed_letters))
        print("Sisa kesempatan:", attempts)
        guess = input("Tebak satu huruf: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Masukkan satu huruf yang valid!")
            continue
        
        if guess in guessed_letters:
            print("Anda sudah menebak huruf tersebut. Coba huruf lain!")
            continue
        
        guessed_letters.add(guess)
        
        if guess not in word:
            attempts -= 1
            print("Salah tebak!")
        else:
            print("Benar!")
        
        # Jika semua huruf dalam kata sudah ditebak, pemain menang
        if all(letter in guessed_letters for letter in word):
            print("\nSelamat, Anda menang!")
            print("Kata yang benar:", word)
            break
    else:
        print("\nGame over! Kesempatan Anda habis.")
        print("Kata yang benar adalah:", word)

if __name__ == '__main__':
    hangman()
