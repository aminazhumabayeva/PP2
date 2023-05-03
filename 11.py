import psycopg2
config = psycopg2.connect(host = "localhost", database="postgres", user="postgres", password="13579")
current = config.cursor()


pagination = """ 
SELECT * FROM contacts LIMIT %s OFFSET %s; 
""" 


search = """ 
CREATE OR REPLACE FUNCTION search(name VARCHAR) 
    RETURNS TABLE ( 
        last_name VARCHAR, 
        first_name VARCHAR, 
        phone_number VARCHAR 
) 

AS $$ 
BEGIN 
    RETURN QUERY SELECT * FROM contacts WHERE contacts.last_name ILIKE name OR contacts.first_name ILIKE name OR contacts.phone_number ILIKE name; 
END; $$ 

LANGUAGE PLPGSQL; 
SELECT * FROM search (%s); 
""" 


update = '''
    create or replace procedure update(name varchar,surname varchar,number varchar)
        as
        $$
            begin
                if exists(select * from contacts where last_name = name) then
                    update contacts set phone_number = number where last_name = name;
                else
                    insert into contacts values(name,surname,number);
                end if;
            end;

        $$ language plpgsql;
        call update(%s, %s, %s);
'''

insert = ''' 
    create or replace procedure insert(name varchar, surname varchar, number varchar)
    as $$
    begin
        insert into contacts values(name,surname,number);
    end; $$ 

    language plpgsql; 
    CALL insert(%s,%s,%s);  
'''

delete = """ 
CREATE OR REPLACE PROCEDURE deleteT(name VARCHAR) 
AS $$ 
BEGIN 
    DELETE FROM contacts WHERE last_name = name OR first_name = name OR phone_number = name; 
END; $$ 

LANGUAGE PLPGSQL; 
CALL deleteT(%s); 
""" 


while True: 
    command = input("search, insert, pagination, delete, exit\n") 
    if command == 'search':
        n = input("Введите часть: ")
        word = '%' + n + '%'
        current.execute(search, [word])
        print(*current.fetchall(), sep="\n")


    if command == 'insert':
        n = int(input("How many users do you want to add?\n"))
        for i in range(n):
            name = str(input("Name of the contact:\n"))
            surname = str(input("Surname of the contact:\n"))
            number = str(input("Phone number of the contact:\n"))
            current.execute(update,(name,surname,number))
        config.commit()


    if command == 'pagination': 
        a, b = map(int, input("LIMIT, OFFSET: ").split()) 
        current.execute(pagination, (a, b)) 
        print(*current.fetchall(), sep = '\n') 


    if command == 'delete':
        n = input("Введите имя или фамилию или номер чтобы удалить: ")
        current.execute(delete,[n])
        config.commit()


    if command == 'exit':
        break



current.close()
config.commit()
config.close()