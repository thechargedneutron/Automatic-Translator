from translate import Translator

def Translate(data, _to_lang, _from_lang):
	"""Translates a word or a sentence into the desired language.

	The translate package is based on the API provided by MyMemory API.
	Details and documentation available at http://mymemory.translated.net/doc/spec.php
	Thanks to https://github.com/terryyin/google-translate-python.

	Parameters
	----------
	data: A word or a string.
	    Also accepts a raw utf-8 string.

	_to_lang: The language of the desired output.
	    Use ISO standard names or RFC3066 code for language code.
	    Codes available at http://www.i18nguy.com/unicode/language-identifiers.html

	_from_lang: The language of the input.
	    Use ISO standard names or RFC3066 code for language code.
	    Codes available at http://www.i18nguy.com/unicode/language-identifiers.html

	Returns
	-------
	translation: The translated word or string.
	    Can also be used as a raw utf-8 string.
	"""
	translator = Translator(to_lang=_to_lang, from_lang=_from_lang)
	translation = translator.translate(data)
	return translation