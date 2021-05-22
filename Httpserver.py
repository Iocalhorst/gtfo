import cherrypy

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

if __name__ == '__main__':

    cherrypy.tree.mount(
        Songs(), '/api/songs',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()


def GET(self, id=None):

    if id == None:
        return('Here are all the songs we have: %s' % songs)
    elif id in songs:
        song = songs[id]
        return('Song with the ID %s is called %s, and the artist is %s' % (id, song['title'], song['artist']))
    else:
        return('No song with the ID %s :-(' % id)