from neo4j import GraphDatabase
import logging
from neo4j.exceptions import ServiceUnavailable

class App:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        # Don't forget to close the driver connection when you are finished with it
        self.driver.close()

    def run_match(self, match_query):
        with self.driver.session(database="neo4j") as session:
            result = session.execute_read(self._return_results, match_query)
            return result

    @staticmethod
    def _return_results(tx, match_query):
        result = tx.run(match_query)
        return [row for row in result]
    

if __name__ == "__main__":
    # Aura queries use an encrypted connection using the "neo4j+s" URI scheme
    uri = "neo4j+s://ef39c519.databases.neo4j.io"
    user = "<Username for Neo4j Aura instance>"
    password = "<Password for Neo4j Aura instance>"
    app = App(uri, user, password)