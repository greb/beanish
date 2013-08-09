import corpus

example_trans_map = { 'ᔪ': '_', 'ᔭ': '_', 'ᖚ': '_', 'ᖗ': '_',
                      'ᑲ': '_', 'ᑫ': '_', 'ᖆ': '_', 'ᖉ': '_',   
                      'ᘈ': '_', 'ᘊ': '_', 'ᘛ': '_', 'ᘖ': '_', 
                      'ᕋ': '_', 'ᓭ': '_', 'ᒣ': '_', 'ᑕ': '_',
                      'ᖊ': '_', 'ᖽ': '_', 'ᔕ': '_', 'ᕬ': '_',
                      'ᕒ': '_', 'ᓄ': '_',
                      'ᐧ': '_', 'ᐣ': '_', 'ᑦ': '_', ',': '_',
                      'ᐨ': '.', 'ᐤ': '?', 'ᐦ': '!'}


def transliterate(s, trans_map):
    '''Substitute glyphs in a string according to a translation map'''
    trans_table = str.maketrans(trans_map)
    return s.translate(trans_table)

if __name__ == '__main__':
    lines = corpus.read_sentences()
    for line in lines:
        print(transliterate(line, example_trans_map))
