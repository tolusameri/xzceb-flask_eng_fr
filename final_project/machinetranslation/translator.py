"""import MyMemoryTranslator from deep_translator package"""
from deep_translator import MyMemoryTranslator
#import deep_translator.MyMemoryTranslator as MemTrans

def english_to_french(engtext):
    '''
    function to convert english to french
    '''
    fren_tran = MyMemoryTranslator(source='en', target='fr')
    frentext = fren_tran.translate(model_id='en-fr', text=engtext)
    return frentext

def french_to_english(frentext):
    '''
    function to convert french to english
    '''
    eng_tran = MyMemoryTranslator(source='fr', target='en')
    engtext = eng_tran.translate(model_id='fr-en', text=frentext)
    return engtext
