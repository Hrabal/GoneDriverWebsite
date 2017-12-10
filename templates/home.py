# -*- coding: utf-8 -*-
from flask import url_for
from tempy.tags import *
from tempy.widgets import TempyPage

base_keywords = ['Gone Driver', 'blues', 'band', 'sax', ]
content = 'Gone Driver band website'
title = 'Gone Driver'


class Owl(Div):
    def init(self):
        self.attr(klass='square')
        self(
            owl=Div(klass='owl')(
                lwing=Div(klass='left wing'),
                rwing=Div(klass='right wing'),
                nome=Div(klass='nose'),
                leye=Div(klass='left eyes closed')(
                    Div(klass='retina')
                ),
                reye=Div(klass='right eyes closed')(
                    Div(klass='retina')
                ),
            )
        )

class Home(TempyPage):
    def js(self):
        return [
            Script(src="https://code.jquery.com/jquery-3.2.1.min.js",
                   integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4=",
                   crossorigin="anonymous"),
            Script(src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js",
                   integrity="sha384-vFJXuSJphROIrBnz7yo7oB41mKfc8JzQZiCq4NCceLEaO4IHwicKwpJf9c9IpFgh",
                   crossorigin="anonymous"),
            Script(src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js",
                   integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ",
                   crossorigin="anonymous"),
            Script(defer=True, src="https://use.fontawesome.com/releases/v5.0.0/js/all.js"),
            Script(defer=True, src=url_for('static', filename='js/owls.js')),
        ]

    def css(self):
        return [
            Link(href="https://fonts.googleapis.com/css?family=VT323", rel="stylesheet"),
            Link(rel="stylesheet",
                 href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css",
                 integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb",
                 crossorigin="anonymous"),
            Link(href=url_for('static', filename='css/style.css'), rel="stylesheet", typ="text/css"),
        ]
    def init(self):
        self.head(self.css(), self.js())
        self.head.title(title)
        luca = Owl(id='luca')
        giova = Owl(id='giova')
        fede = Owl(id='fede')
        giova.owl.leye.remove_class('closed')
        giova.owl.reye.remove_class('closed')
        fede.owl.leye.attr(klass='half-closed')
        self.content = Main(role='main', klass='inner cover')(
            Div(klass='container-fluid')(
                Div(klass='row')(
                    Div(klass='col')(
                        H1()('Gone Driver')
                    )
                ),
                Div(klass='row')(
                    Div(klass='col')(
                        luca
                    ),
                    Div(klass='col')(
                        giova
                    ),
                    Div(klass='col')(
                        fede
                    )
                ),
                Div(klass='row')(
                    Div(klass='col')(
                        H2()('Luke Madfields')
                    ),
                    Div(klass='col')(
                        H2()('John Millkers')
                    ),
                    Div(klass='col')(
                        H2()('Fred Whitecandl')
                    )
                ),
                Div(klass='row')(
                    Div(klass='col')(Br(),Br(),Br(),Br(),Br(),Br(),
                        H2()(A(href='https://gonedriver.bandcamp.com')(I(klass='fab fa-bandcamp'), ' gonedriver.bandcamp.com')),
                        H2()(A(href='https://www.facebook.com/GoneDriver/')(I(klass='fab fa-facebook-square'), ' facebook.com/GoneDriver'))
                    ),
                    Div(klass='col')(Br(),Br(),
                        H1()('Space Owls Blues weirdos since \'05'),
                        H2()(
                            Pre()("""Get in touch: // Fede - +39 3200653999 \n Press contact: // Elisa - rockngraph@gmail.com""")
                        ),
                    ),
                    Div(klass='col')(Br(),Br(),
                        H2()(
                            Pre()("""Next Shows:\n2018-01-06\nCarbone Festival @ Manitese\nVia Camposanto, 41034 Finale Emilia, MO, Italy\n\n2018-01-06\nEkdina\nVia Livorno, 41034 Carpi, MO, Italy""")
                        )
                    )
                ),
            )
        )
        self.body(
            Div(klass='site-wrapper')(
                Div(klass='site-wrapper-inner')(
                    Div(klass='cover-container')(
                        Header(klass='masthead clearfix'),
                        self.content,
                        Footer(klass='mastfoot')
                    )
                )
            )
        )