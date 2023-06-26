
class festa:
    def __init__(self, database):
        self.db = database

    def create_penguin(self, nome:str, idade:int, cor:str, faixa:str):
        query = "CREATE(:Pinguin{nome:"+"'"+f"{nome}"+"'"+", idade:" + f"{idade}, cor:" +"'"f"{cor}"+"'" + ", faixa:" +"'" + f"{faixa}" +"'" +  ", quantidade_de_puffle: 0})"
        print(query)
        self.db.execute_query(query)

    def create_puffle(self, nome:str, cor:str):
        query = "CREATE(:Puffle{nome:" +"'"f"{nome}"+"'" + ", cor: " + "'" + f"{cor}" + "'" + "})"
        print(query)
        self.db.execute_query(query)


    def create_relation_with_penguin(self, nome1:str, nome2:str):
        query = "MATCH(n:Pinguin{nome:" +"'"+  f"{nome1}"+"'" + "}), (m:Pinguin" + "{nome:" +"'" + f"{nome2}" +"'" + "}) CREATE (n) -[:AMIGO_DE]-> (m) CREATE (m) -[:AMIGO_DE]-> (n)"
        print(query)
        self.db.execute_query(query)

    def create_relation_with_puffle(self, nome1:str, idade:int, cor:str, faixa:str, nome2:str, cor2:str, tempo:int):
        query = "MATCH(n:Pinguin{nome:" +"'" + f"{nome1}" +"'" + ", idade:" + f"{idade}" + ", cor:" +"'" + f"{cor}" +"'" + ", faixa:" +"'" + f"{faixa}" +"'" + "}), (p:Puffle" + "{nome:" +"'"+ f"{nome2}" +"'" + ", cor:" +"'"+ f"{cor2}" +"'" +"}) CREATE (n) -[:DONO_DE{desde:" + f"{tempo}"+"}]->(p) CREATE (p) -[:DONO_DE" + "{desde:" + f"{tempo}" + "}]->(n)"
        print(query)
        self.db.execute_query(query)

    def update_number_puffle(self, nome):
        query = "MATCH(n:Pinguin{nome:" +"'"+f"{nome}" + "'" + "}) SET n.quantidade_de_puffle = n.quantidade_de_puffle + 1"
        print(query)
        self.db.execute_query(query)

    def delete_convidado(self, nome):
        query = "MATCH(n:Pinguin{nome:" +"'"+f"{nome}" + "'" + "}),(m:Puffle) WHERE (n)-[:DONO_DE]->(m) DETACH DELETE m DETACH DELETE n"
        print(query)
        self.db.execute_query(query)
    def show_convidado(self, nome:str):
        query = "MATCH(n:Pinguin{nome:" +"'"+ f"{nome}" +"'"+"}) RETURN n.nome AS Nome, n.idade AS Idade, n.cor AS Cor, n.faixa AS Faixa, n.quantidade_de_puffle AS Numero_de_puffles"
        print(query)
        results = self.db.execute_query(query)
        return [(result["Nome"], result["Idade"], result["Cor"], result["Faixa"], result["Numero_de_puffles"]) for result in results]

    def show_puffle(self, tipo:str, parametro: str):
        query = "MATCH(n:Puffle{" + f"{tipo}:" +"'"+ f"{parametro}" +"'" + "}) RETURN n.nome AS Nome, n.cor AS Cor"
        print(query)
        results = self.db.execute_query(query)
        return [(result["Nome"], result["Cor"]) for result in results]

    def show_relation(self, tipo:str, parametro:str, relacionamento:str,  escolha:int):
        if escolha == 5:
            query = f"MATCH(n:Pinguin) -[r:{relacionamento}] -> (m:Puffle) WHERE COUNT(r) > {parametro} RETRUN n.nome AS nome"
            results = self.db.execute_query(query)
            return [([result["nome"]]) for result in results]
        elif escolha == 6:
            query = f"MATCH(n:Pinguin), (m:Pinguin), (n) - [:{relacionamento}] -> (m) RETURN n.nome AS nome, m.nome AS nome2"
            results = self.db.execute_query(query, parametro)
            return [([result["nome"], result["nome2"]]) for result in results]
        else:
            query = "MATCH (n:Pinguin {" + f"{tipo}:" +"'" + f"{parametro}"+"'"+"}), (m:Pinguin) WHERE (n) - " + f"[:{relacionamento}] -> (m) RETURN n.nome AS Nome1, m.nome AS Nome2"
            print(query)
            results = self.db.execute_query(query)
            return [([result["Nome1"], result["Nome2"]]) for result in results]



    def show_puffles_relations(self, tipo:str, parametro:str, escolha:int):
        if escolha == 3:
            query = "MATCH(n:Pinguin{nome:"+"'"+f"{parametro}"+"'"+"}) -[r:DONO_DE] -> (m:Puffle) RETURN n.nome AS nome_do_dono, m.nome AS nome_do_puffle"
            print(query)
            results = self.db.execute_query(query)
            return [([result["nome_do_dono"], result["nome_do_puffle"]]) for result in results]
        elif escolha == 4:
            query = "MATCH(n:Pinguin) -[:DONO_DE] -> (m:Puffle) RETURN n.nome AS Dono, m.nome AS Puffle"
            print(query)
            results = self.db.execute_query(query)
            return [([result["Dono"], result["Puffle"]]) for result in results]
        else:
            query = "MATCH(p:Puffle{"+f"{tipo}:" +"'" + f"{parametro}"+"'"+"}) <-[:DONO_DE] -(m:Pinguin) RETURN m.nome AS Dono, p.nome AS Nome_do_Puffle "
            print(query)
            results = self.db.execute_query(query)
            return [([result["Dono"], result["Nome_do_Puffle"]]) for result in results]


