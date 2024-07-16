print("hello")
def replace_words(input_string, replacements):
    """
    input_string: Değiştirilecek string
    replacements: Bir sözlük, anahtarlar değiştirilecek kelimeleri, değerler ise değişecek yeni kelimeleri içerir.
    """
    for old_word, new_word in replacements.items():
        input_string = input_string.replace(old_word, new_word)
    return input_string

# Değiştirilecek string

input_string = """


void rakamYazdir(int digit) {
  switch(digit) {
    case 0:
      digitalWrite(pinA, HIGH);
      digitalWrite(pinB, HIGH);
      digitalWrite(pinC, HIGH);
      digitalWrite(pinD, HIGH);
      digitalWrite(pinE, HIGH);
      digitalWrite(pinF, HIGH);
      digitalWrite(pinG, LOW);
      break;
    case 1:
      digitalWrite(pinA, LOW);
      digitalWrite(pinB, HIGH);
      digitalWrite(pinC, HIGH);
      digitalWrite(pinD, LOW);
      digitalWrite(pinE, LOW);
      digitalWrite(pinF, LOW);
      digitalWrite(pinG, LOW);
      break;
    case 2:
      digitalWrite(pinA, HIGH);
      digitalWrite(pinB, HIGH);
      digitalWrite(pinC, LOW);
      digitalWrite(pinD, HIGH);
      digitalWrite(pinE, HIGH);
      digitalWrite(pinF, LOW);
      digitalWrite(pinG, HIGH);
      break;
    case 3:
      digitalWrite(pinA, HIGH);
      digitalWrite(pinB, HIGH);
      digitalWrite(pinC, HIGH);
      digitalWrite(pinD, HIGH);
      digitalWrite(pinE, LOW);
      digitalWrite(pinF, LOW);
      digitalWrite(pinG, HIGH);
      break;
    case 4:
      digitalWrite(pinA, LOW);
      digitalWrite(pinB, HIGH);
      digitalWrite(pinC, HIGH);
      digitalWrite(pinD, LOW);
      digitalWrite(pinE, LOW);
      digitalWrite(pinF, HIGH);
      digitalWrite(pinG, HIGH);
      break;
    case 5:
      digitalWrite(pinA, HIGH);
      digitalWrite(pinB, LOW);
      digitalWrite(pinC, HIGH);
      digitalWrite(pinD, HIGH);
      digitalWrite(pinE, LOW);
      digitalWrite(pinF, HIGH);
      digitalWrite(pinG, HIGH);
      break;
    case 6:
      digitalWrite(pinA, HIGH);
      digitalWrite(pinB, LOW);
      digitalWrite(pinC, HIGH);
      digitalWrite(pinD, HIGH);
      digitalWrite(pinE, HIGH);
      digitalWrite(pinF, HIGH);
      digitalWrite(pinG, HIGH);
      break;
    case 7:
      digitalWrite(pinA, HIGH);
      digitalWrite(pinB, HIGH);
      digitalWrite(pinC, HIGH);
      digitalWrite(pinD, LOW);
      digitalWrite(pinE, LOW);
      digitalWrite(pinF, LOW);
      digitalWrite(pinG, LOW);
      break;
    case 8:
      digitalWrite(pinA, HIGH);
      digitalWrite(pinB, HIGH);
      digitalWrite(pinC, HIGH);
      digitalWrite(pinD, HIGH);
      digitalWrite(pinE, HIGH);
      digitalWrite(pinF, HIGH);
      digitalWrite(pinG, HIGH);
      break;
    case 9:
      digitalWrite(pinA, HIGH);
      digitalWrite(pinB, HIGH);
      digitalWrite(pinC, HIGH);
      digitalWrite(pinD, LOW);
      digitalWrite(pinE, LOW);
      digitalWrite(pinF, HIGH);
      digitalWrite(pinG, HIGH);
      break;
    default:
      // Hata durumu
      break;
  }
}




"""

# Değiştirmek istediğiniz kelimeler ve yeni kelimeleri içeren bir sözlük
replacements = {
    "hearts": "canlar",
    "ballx": "topx",
    "bally": "topy",
    "moveBall": "topuHareketEttir",
    "gameOver":"oyunBitti",
    "onKill":"topDuserse",
    "buttonCode":"butonKodu",
    "platformPower":"platformGucu",
    "objects":"nesneler",
    "drawObjects":"nesneleriCizdir",
    "resetGame":"oyunuResetle",
    "drawStartScreen":"baslangicEkraniCiz",
    "drawBlocks":"blocklariCizdir",
    "drawBlock":"blockCizdir",
    "resetBlocks":"blocklariResetle",
    "MAX_LEVELS":"maksLeveller",
    "BLOCKS_PER_ROW":"satirdakiBlockSayisi",
    "MAX_BLOCKS_PER_ROW":"satirdakiMaksBlock",
    "BLOCK_NUM_ROWS":"blockNumarasiSatir",
    "blockImages":"blockResimleri",
    "vSpeed":"dikeyHiz",
    "hSpeed":"yatayHiz",
"PLATFORM_SPEED":"platformHizi",
"PLATFORM_ROW":"platformSatiri",
"platformWidth":"platfromgenislik",
"platformPos":"pppp11",
"LEFT_EDGE":"solEEE",
"RIGHT_EDGE":"sagEEE",
"startLevel":"leveliBaslat",
"SCREEN_HEIGHT":"ekranGenisligi",
"PLATFORM_HEIGHT":"platformBoyu",
"SPEED_SHIFT":"hiz1",
"drawPlatform":"platformuCiz",
"drawBall":"topCiz",
"newx":"yeniX",
"newy":"yeniY",
"MAX_GAME_OBJECTS":"maksOyunObjesi",
"collision":"colDef11",
"party":"pY"
,"partx":"pX",
"INITIAL_H_SPEED":"inYuksekHiz",
"INITIAL_V_SPEED":"inYatayHiz",
"BLOCK_WIDTH":"blockGenislik",
"updateStatusPanel":"bilgiPaneliGuncelle",
"drawFieldEdges":"cizdirme1223",
"nextLevel":"sonrakiLevel"
,"drawStatusPanel":"bilgiPaneliCizdir"

,"pinA":"4",
"pinB":"5",
"pinC":"6",
"pinD":"7",
"pinE":"8",
"pinF":"9",
"pinG":"10"

    
}

# Stringi değiştir ve sonucu yazdır
print(replace_words(input_string, replacements))