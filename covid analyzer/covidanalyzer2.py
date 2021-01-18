# -*- coding: utf-8 -*-

import myMod as m

if __name__ == "__main__":
    print('Pakistan', m.ratio('Pakistan'))
    print(
        '\nDeath Rate from ',
        'Partial lockdown: ',
        m.deathRate(
            m.countriesMeasure('Partial lockdown')),
        '%')
    print('\nMost Frequent ')
    m.pprint(m.frequent())
    print('\n')
    m.printEfficiency()
