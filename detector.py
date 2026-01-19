from config import MY_NAME, MY_ROLL

def normalize(text: str) -> str:
    return text.upper().replace(" ", "")

def is_me_present(text: str) -> bool:
    text = normalize(text)
    return (
        normalize(MY_NAME) in text
        or normalize(MY_ROLL) in text
    )
