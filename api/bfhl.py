from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class InputData(BaseModel):
    data: List[str]

@app.post("/")
async def process_data(input_data: InputData):
    data = input_data.data
    full_name = "amithav_mrithyunjay_r"  
    dob = "21052004"                    
    email = "amithavmrithyunjay7@gmail.com"       
    roll_number = "22BCE5143"            

    even_numbers, odd_numbers, alphabets, special_characters = [], [], [], []
    total_sum = 0

    for item in data:
        if item.isdigit():
            num = int(item)
            total_sum += num
            (even_numbers if num % 2 == 0 else odd_numbers).append(item)
        elif item.isalpha():
            alphabets.append(item.upper())
        else:
            special_characters.append(item)

    concat_string = "".join(alphabets)[::-1]
    concat_string = "".join(
        ch.upper() if i % 2 == 0 else ch.lower()
        for i, ch in enumerate(concat_string)
    )

    return {
        "is_success": True,
        "user_id": f"{full_name}_{dob}",
        "email": email,
        "roll_number": roll_number,
        "odd_numbers": odd_numbers,
        "even_numbers": even_numbers,
        "alphabets": alphabets,
        "special_characters": special_characters,
        "sum": str(total_sum),
        "concat_string": concat_string
    }
