class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        
        attuale = self.root
        
        while True:
            if key < attuale.key:
                if attuale.left is None:
                    attuale.left = Node(key)
                    return
                else:
                    attuale = attuale.left
            else:
                if attuale.right is None:
                    attuale.right = Node(key)
                    return
                else:
                    attuale = attuale.right
    
    def search(self, key):
        attuale = self.root
        
        while attuale is not None:
            if attuale.key == key:
                return True
            
            if key < attuale.key:
                attuale = attuale.left
            else:
                attuale = attuale.right
                
        return False
    
    def print_in_order(self):
        """Metodo pubblico per avviare la stampa"""
        self._stampa_ricorsiva(self.root)
        print()

    def _stampa_ricorsiva(self, nodo_corrente):
        """Metodo di supporto che fa il lavoro sporco"""
        if nodo_corrente is not None:
            self._stampa_ricorsiva(nodo_corrente.left)
        
            print(nodo_corrente.key, end=" ")
        
            self._stampa_ricorsiva(nodo_corrente.right)

    def visualizza(self):
        """Metodo pubblico per vedere la struttura"""
        print("\n--- Struttura dell'Albero (ruotato) ---")
        self._stampa_gerarchica(self.root, 0)
        print("---------------------------------------\n")

    def _stampa_gerarchica(self, nodo_corrente, livello):
        if nodo_corrente is not None:
            self._stampa_gerarchica(nodo_corrente.right, livello + 1)
            
            indentazione = "    " * livello
            print(f"{indentazione}{nodo_corrente.key}")
            
            self._stampa_gerarchica(nodo_corrente.left, livello + 1)

albero = BST()
albero.insert(5)
albero.insert(10)
albero.insert(2)
albero.insert(3)
albero.insert(98)
albero.insert(1)
albero.insert(7)
albero.insert(12)
albero.insert(21)
ris = albero.search(8)
if ris is True:
    print("Trovato")
else:
    print("Non trovato")
albero.print_in_order()
albero.visualizza()