import re

def assess_password_strength(password):
    
    min_length = 8
    max_length = 20
    
    
    length_score = 0
    if len(password) >= min_length:
        length_score = 1
    if len(password) >= max_length:
        length_score = 2
    
    
    has_uppercase = bool(re.search(r'[A-Z]', password))
    
    
    has_lowercase = bool(re.search(r'[a-z]', password))
    
    
    has_number = bool(re.search(r'\d', password))
    
    
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    
    strength_score = length_score
    if has_uppercase:
        strength_score += 1
    if has_lowercase:
        strength_score += 1
    if has_number:
        strength_score += 1
    if has_special:
        strength_score += 1
    
    
    if strength_score <= 2:
        strength = "Weak"
    elif strength_score == 3:
        strength = "Moderate"
    elif strength_score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return {
        "password": password,
        "length": len(password),
        "has_uppercase": has_uppercase,
        "has_lowercase": has_lowercase,
        "has_number": has_number,
        "has_special": has_special,
        "strength_score": strength_score,
        "strength": strength
    }

def print_password_assessment(assessment):
    print(f"Password: {assessment['password']}")
    print(f"Length: {assessment['length']} characters")
    print(f"Contains uppercase letters: {'Yes' if assessment['has_uppercase'] else 'No'}")
    print(f"Contains lowercase letters: {'Yes' if assessment['has_lowercase'] else 'No'}")
    print(f"Contains numbers: {'Yes' if assessment['has_number'] else 'No'}")
    print(f"Contains special characters: {'Yes' if assessment['has_special'] else 'No'}")
    print(f"Strength score: {assessment['strength_score']}")
    print(f"Overall strength: {assessment['strength']}")


if __name__ == "__main__":
    password = input("Enter a password to assess its strength: ")
    assessment = assess_password_strength(password)
    print_password_assessment(assessment)
