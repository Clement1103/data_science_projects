import re

def check_if_presentation_product(intent: str):
    if re.match(r'^presentation\.\S* - context: ongoing-presentation$', intent):
        return True
    else:
        return False

def get_product_name(intent: str):
    match = re.findall(r'presentation\.(\S*) - context: ongoing-presentation', intent)
    return match[0] if match else None



if __name__ == '__main__':
    intent = 'presentation.SyntheMedix - context: ongoing-presentation'
    intent_bis = 'coordinates.incorrect'
    product_name = get_product_name(intent)
    print(product_name)
    print('================')
    print(check_if_presentation_product(intent_bis))