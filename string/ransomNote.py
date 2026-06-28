def canConstruct(ransomNote: str, magazine: str) -> bool:
    frequency_magazine = {}
    for i in magazine:
        if i in frequency_magazine:
            frequency_magazine[i] +=1
        else:
            frequency_magazine[i]=1
    for i in ransomNote:
        if i not in frequency_magazine:
            return False
        frequency_magazine[i] -=1
        if frequency_magazine[i] <0:
            return False
    return True