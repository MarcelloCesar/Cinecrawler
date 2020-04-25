import psycopg2 as pg

class Migration:

    def __init__(self):
        self.db = pg.connect(
            host="192.168.99.101",
            user="user",
            password="senha",
            database="cinecrawler"
        )

        self.cursor = self.db.cursor()


    def create_table_links(self):
        self.cursor.execute(
        '''
            CREATE TABLE "links" (
                "url" character varying(250) NOT NULL,
                "site" character varying(35) NOT NULL,
                "titulo" character varying(300)
            );
        ''')

        self.cursor.execute(
        '''
            ALTER TABLE "links"
            ADD CONSTRAINT "pk_links" PRIMARY KEY ("url");
        ''')

        self.db.commit()


if __name__ == '__main__':
    migration = Migration()
    migration.create_table_links()