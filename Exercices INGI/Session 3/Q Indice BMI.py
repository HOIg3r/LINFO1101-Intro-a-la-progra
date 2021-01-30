def quetelet(height, weight):
    IMC = weight/height**2
    
    if IMC < 20:
        return "thin"
    if IMC >= 20 and IMC <= 25:
        return "normal"
    if IMC > 25 and IMC <= 30:
        return "overweight"
    if IMC > 30:
        return "obese"