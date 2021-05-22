import cherrypy

dummy="""{"type": "mc5", "instruction": "Waehlen sie die zutreffende Aussage aus.", "optionset": {"1": "Im tiefen dichten Fichtendickicht dichten Dicke n\u00fcchten t\u00fcchtig.", "2": "Wer andern eine Bratwurst br\u00e4t der hat ein Bratwurstbratger\u00e4t", "3": "Informatik ist toll. Nur das mit den Computern nervt.", "4": "Wer niemals Keks im Bette a\u00df weiss nicht wie Kr\u00fcmel pieken", "5": "In der Ruhe liegt die Kraft. Und in der Truhe liegt der Schnaps"}}"""

songs = {
    '1': {
        'title': 'Lumberjack Song',
        'artist': 'Canadian Guard Choir'
    },

    '2': {
        'title': 'Always Look On the Bright Side of Life',
        'artist': 'Eric Idle'
    },

    '3': {
        'title': 'Spam Spam Spam',
        'artist': 'Monty Python'
    }
}


class Songs:

    exposed = True

    def GET(self, id=None):

#        if id is None:
#            return('Here are all the songs we have: %s' % songs)
#        elif id in songs:
#            song = songs[id]

#            return(
#                'Song with the ID %s is called %s, and the artist is %s' % (
#                    id, song['title'], song['artist']))
#        else:
#            return('No song with the ID %s :-(' % id)
        return(dummy)

#def POST(self, title, artist):

#       id = str(max([int(_) for _ in songs.keys()]) + 1)

#       songs[id] = {
#            'title': title,
#            'artist': artist
#        }

#return ('Create a new song with the ID: %s' % id)

#def PUT(self, id, title=None, artist=None):
#       if id in songs:
#            song = songs[id]

#            song['title'] = title or song['title']
#            song['artist'] = artist or song['artist']

#            return(
#                'Song with the ID %s is now called %s, '
#                'and the artist is now %s' % (
#                    id, song['title'], song['artist'])
#            )
#        else:
#            return('No song with the ID %s :-(' % id)

#    def DELETE(self, id):
#        if id in songs:
#            songs.pop(id)

#            return('Song with the ID %s has been deleted.' % id)
#        else:
#            return('No song with the ID %s :-(' % id)

if __name__ == '__main__':

    cherrypy.tree.mount(
        Songs(), '/dummy',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
         }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()