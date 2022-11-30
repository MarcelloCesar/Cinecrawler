import psycopg2 as pg

class Migration:

    def __init__(self):
        self.db = pg.connect(
            host="ec2-18-209-187-54.compute-1.amazonaws.com",
            user="oerdlziwkipzzf",
            password="65490a8d2b37124d7ca79b0c3bef8809dccc8f5cd7bd9895302fe20a7a1584a0",
            database="d9mq0hiu9k2pvn"
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