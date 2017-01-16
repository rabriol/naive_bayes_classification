# coding=utf-8
__author__ = 'brito'

from pymongo import MongoClient

from src import MongoConnect
from src.classification import PreProcess

unnecessary_words = [
'plenário',
'turma',
'ministro',
'ministra',
'ministros',
'ministro-relator',
'senhor',
'tribunal',
'relator',
'votação',
'unânime',
'turma,',
'presidência',
'senhora',
'senhor',
'relator',
'neste',
'voto',
'votos',
'2a',
'1a',
'1ª',
'2ª',
'1ª.',
'2ª.',
'unanimidade',
'ausente justificadamente',
':',
'termos']

minister_names = [
'adalício nogueira',
'adaucto cardoso',
'alberto torres',
'aldir passarinho',
'alencar araripe',
'alfredo buzaid',
'alfredo pinto',
'aliomar baleeiro',
'amaral santos',
'amaro cavalcanti',
'americo braziliense',
'americo lobo',
'amphilophio',
'andrade pinto',
'andré cavalcanti',
'annibal freire',
'antonio neder',
'aquino e castro',
'armando de alencar',
'arthur ribeiro',
'ary franco',
'ataulpho de paiva',
'augusto olyntho',
'ayres britto',
'barão de pereira franco',
'barão de lucena',
'barão de sobral',
'barata ribeiro',
'barros barreto',
'barros monteiro',
'barros pimentel',
'bento de faria',
'bento lisboa',
'bernardino ferreira',
'bilac pinto',
'candido motta',
'canuto saraiva',
'cardoso de castro',
'cardoso ribeiro',
'carlos madeira',
'carlos maximiliano',
'carlos medeiros',
'carlos velloso',
'cármen lúcia',
'carvalho mourão',
'castro nunes',
'célio borja',
'celso de mello',
'cezar peluso',
'clóvis ramalhete',
'coelho e campos',
'cordeiro guerra',
'costa barradas',
'costa manso',
'cunha mello',
'cunha peixoto',
'décio miranda',
'dias toffoli',
'djaci falcão',
'edgard costa',
'edmundo lins',
'edson fachin',
'eduardo espinola',
'ellen gracie',
'eloy da rocha',
'enéas galvão',
'epitacio pessôa',
'eros grau',
'evandro lins',
'faria',
'faria lemos',
'ferreira de resende',
'figueiredo junior',
'firmino paz',
'firmino whitaker',
'francisco rezek',
'freitas henriques',
'geminiano da franca',
'gilmar mendes',
'godofredo cunha',
'gonçalves de carvalho',
'gonçalves de oliveira',
'goulart de oliveira',
'guimarães natal',
'hahnemann guimarães',
'heitor de sousa',
'herculano de freitas',
'hermenegildo de barros',
'hermes lima',
'herminio do espirito santo',
'ilmar galvão',
'joão barbalho',
'joão luiz alves',
'joão mendes',
'joão pedro',
'joaquim barbosa',
'josé hygino',
'josé linhares',
'lafayette de andrada',
'laudo de camargo',
'leitão de abreu',
'leoni ramos',
'lucio de mendonça',
'luiz fux',
'luiz gallotti',
'luiz osorio',
'macedo soares',
'manoel espinola',
'manoel murtinho',
'marco aurélio',
'mário guimarães',
'maurício corrêa',
'mendonça uchôa',
'menezes direito',
'moreira alves',
'muniz barreto',
'nelson hungria',
'nelson jobim',
'néri da silveira',
'octavio gallotti',
'octavio kelly',
'oliveira figueiredo',
'oliveira ribeiro',
'orozimbo nonato',
'oscar corrêa',
'oswaldo trigueiro',
'paulo brossard',
'pedro chaves',
'pedro dos santos',
'pedro lessa',
'pedro mibieli',
'philadelpho e azevedo',
'pindahiba de mattos',
'pires e albuquerque',
'piza e almeida',
'plínio casado',
'prado kelly',
'queiroz barros',
'rafael mayer',
'ribeiro da costa',
'ribeiro de almeida',
'ricardo lewandowski',
'roberto barroso',
'rocha lagôa',
'rodrigo octavio',
'rodrigues alckmin',
'rosa weber',
'sebastião lacerda',
'sepúlveda pertence',
'soares muñoz',
'soriano de souza',
'souza martins',
'souza mendes',
'sydney sanches',
'teori zavascki',
'themístocles cavalcanti',
'thompson flores',
'trigo de loureiro',
'ubaldino do amaral',
'victor nunes',
'vilas boas',
'visconde de sabará',
'viveiros de castro',
'waldemar falcão',
'washington oliveira',
'xavier de albuquerque'
]

if __name__ == '__main__':
    records = MongoConnect.MongoConnect().find({'decisao':{'$ne':""}},{'decisao':1, 'acordaoId':1, '_id':0})

    print 'Total de registros encontrados: ' + str(records.count())

    for record in records:
        lower_decision = PreProcess.PreProcess().lower(record['decisao'])
        no_stop_words_decision = PreProcess.PreProcess().remove_stop_words(lower_decision.split(' '))

        phrase = ''
        for word in no_stop_words_decision:
            phrase += word + ' '

        no_date = PreProcess.PreProcess().remove_date(phrase)
        no_punctuation = PreProcess.PreProcess().remove_punctuation(no_date)

        result = no_punctuation
        for minister in minister_names:
            result = result.replace(minister.decode('utf-8'), '')

        for word in unnecessary_words:
            result = result.replace(word.decode('utf-8'), '')

        final_result = ''

        for word in result.split(' '):
            if word != '':
                final_result += word + ' '

        words = PreProcess.PreProcess().remove_given_stop_words(final_result.split(' '), ['a'])

        phrase = ''

        for word in words:
            phrase += word + ' '

        connection = MongoClient('localhost', 27017)
        db = connection['DJs']
        db.preprocessed.insert({'acordaoId': record['acordaoId'], 'decisao': phrase.strip()})