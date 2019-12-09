import pandas
from konlpy.tag import Okt

okt = Okt()

filename = 'semi_politic_test.csv'

name = ['date', 'category', 'press', 'title', 'content', 'url']
df = pandas.read_csv(filename, sep=',', names = name)
print(df[0:3]['content'])

# morphs_not_josa는 커스텀 메소드입니다. commit 메세지를 참고하세요.
df['Token_content'] = df['content'].apply(okt.morphs_not_josa)
print(df[0:3]['Token_content'])

'''
    def morphs_not_josa(self, phrase, norm=False, stem=False):
        """Parse phrase to morphemes."""

        return [s for s, t in self.pos(phrase, norm=norm, stem=stem) if t != 'Josa']
'''

