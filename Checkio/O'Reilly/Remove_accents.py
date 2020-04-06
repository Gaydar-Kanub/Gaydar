def checkio(text):
    import unicodedata
    text = unicodedata.normalize('NFKD', text)
    text = ''.join([sym for sym in text if not unicodedata.combining(sym)])
    return text


# print(checkio(u"préfèrent"))


if __name__ == '__main__':
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print('Done')
