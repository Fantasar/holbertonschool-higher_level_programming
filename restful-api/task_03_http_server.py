#!/usr/bin/python3

"""
Module qui permet de simuler un serveur locals sous le ports 8000
"""


from http.server import BaseHTTPRequestHandler
import socketserver
import json


class Simple_Serveur(BaseHTTPRequestHandler):

    """
    Création de la classs Simple_serveur.
    Prends en compte plusieurs sorties en fonction de la
    position de l'utilisateur sur le site.
    """

    def do_GET(self):

        """
        Définition de la méthode Get qui prends en compte un
        appel HTTP de l'utilisateur vers le serveur :
         - En cas de succès code retour 200
         - En cas d'échecs code retour 404
        """

        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode())

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"version": "1.0", "description":
                    "A simple API built with http.server"}
            self.wfile.write(json.dumps(data).encode())

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Endpoint not found".encode())


PORT = 8080
Handler = Simple_Serveur

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
