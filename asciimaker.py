def generate_ascii_art(text):
    lines = ['' for _ in range(6)]  # 6 satırlık ASCII sanat için yer aç

    for char in text.upper():
        if char == ' ':
            for i in range(6):
                lines[i] += "     "  # Boşluk karakteri için 5 boşluk ekleyin
        else:
            ascii_chars = ascii_dict.get(char, ascii_dict['?']).splitlines()
            for i in range(6):
                lines[i] += ascii_chars[i] + " "  # ASCII sanatı satırını ekleyin

    return "\n".join(lines)

# ASCII sanat karakterleri
ascii_dict = {
    'A': r'''
       A       
      A A      
     A   A     
    AAAAAAA    
   A       A   
  A         A  ''',
    'B': r'''
   BBBBBB    
   B     B   
   BBBBBB    
   B     B   
   BBBBBB    ''',
    'C': r'''
   CCCCCC    
  C         
  C         
  C         
   CCCCCC    ''',
    'D': r'''
   DDDDDD    
   D     D   
   D     D   
   D     D   
   DDDDDD    ''',
    'E': r'''
   EEEEEEE   
   E        
   EEEEE    
   E        
   EEEEEEE   ''',
    'F': r'''
   FFFFFF    
   F        
   FFFF     
   F        
   F        ''',
    'G': r'''
   GGGGGGG   
  G         
  G    GGG   
  G      G   
   GGGGGG    ''',
    'H': r'''
   H     H   
   H     H   
   HHHHHHH   
   H     H   
   H     H   ''',
    'I': r'''
   IIIIII    
     I      
     I      
     I      
   IIIIII    ''',
    'J': r'''
   JJJJJJJ   
      J      
      J      
  J   J      
   JJJ       ''',
    'K': r'''
   K    K    
   K  K      
   KK        
   K  K      
   K    K    ''',
    'L': r'''
   L        
   L        
   L        
   L        
   LLLLLL   ''',
    'M': r'''
   M     M   
   MM   MM   
   M M M M   
   M  M  M   
   M     M   ''',
    'N': r'''
   N     N   
   NN    N   
   N N   N   
   N  N  N   
   N   NN    ''',
    'O': r'''
   OOOOOO    
  O     O   
  O     O   
  O     O   
   OOOOOO    ''',
    'P': r'''
   PPPPPP    
   P    P   
   PPPPPP    
   P        
   P        ''',
    'Q': r'''
   QQQQQQ    
  Q     Q   
  Q     Q   
  Q   Q Q   
   QQQQQ Q  ''',
    'R': r'''
   RRRRRR    
   R    R   
   RRRRRR    
   R   R     
   R    R    ''',
    'S': r'''
   SSSSSSS   
  S         
   SSSSSS   
        S   
  SSSSSS    ''',
    'T': r'''
   TTTTTTT   
     T      
     T      
     T      
     T       ''',
    'U': r'''
   U     U   
   U     U   
   U     U   
   U     U   
   UUUUUUU   ''',
    'V': r'''
   V     V   
   V     V   
    V   V    
     V V     
      V      ''',
    'W': r'''
   W     W   
   W  W  W   
   W W W W   
   WW   WW   
   W     W   ''',
    'X': r'''
   X     X   
    X   X    
     X X     
    X   X    
   X     X   ''',
    'Y': r'''
   Y     Y   
    Y   Y    
     YYY     
      Y      
      Y       ''',
    'Z': r'''
   ZZZZZZZ   
       Z    
      Z     
     Z      
   ZZZZZZZ   ''',
    ' ': r'''


            ''',
    '?': r'''
   ??????    
  ?     ?   
       ?    
      ?     
      ?      '''
}

# Metin girişi al
text = input("ASCII sanatını oluşturmak için bir metin girin: ")

# ASCII sanatını oluştur ve yazdır
ascii_art = generate_ascii_art(text)
print(ascii_art)
