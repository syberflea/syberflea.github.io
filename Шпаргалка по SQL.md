## SQL  
```
SELECT ('столбцы (* - для выбора всех столбцов); обязательно')
(могут применяться агрегатные функции COUNT, MIN, MAX, AVG и SUM; необязательно)
(и ключевое слово DISTINCT; необязательно)
FROM ('таблица; обязательно')
WHERE ('условие/фильтрация; необязательно')
GROUP BY ('столбец, по которому нужно сгруппировать данные; необязательно')
HAVING ('условие/фильтрация на уровне сгруппированных данных; необязательно')
ORDER BY ('столбец, по которому нужно ранжировать вывод; необязательно')
LIMIT ('сколько записей показывать; необязательно')
OFFSET ('сколько записей в выборке пропустить; необязательно')
``` 

Исключим из выборки все группы, в которых сумма кассовых сборов равна NULL: 
```
SELECT type,
       SUM(gross)
FROM movies
GROUP BY type
-- Это условие относится к группам:
HAVING SUM(gross) IS NOT NULL;
-- ('Фильм', 318868922)
```

Посчитаем (COUNT), сколько в таблице фильмов каждого типа:
```
SELECT type,
       COUNT(*)
FROM movies
GROUP BY type;
```

Найдём самый старый фильм (MIN) в каждой группе: 
```
SELECT type,
       MIN(release_year)
FROM movies
GROUP BY type; 
```

Просуммируем кассовые сборы (SUM) для фильмов разного типа: 
```
SELECT type,
       SUM(gross)
FROM movies
GROUP BY type; 

SELECT type,
       SUM(gross)
FROM movies
WHERE release_year > 1990
GROUP BY type; 
```

Сгруппируем записи по одинаковым значениям в поле gross и выведем количество записей в каждой группе:
```
SELECT gross,
       COUNT(*)
FROM movies
GROUP BY gross; 
```

### Отношения между таблицами. Один-к-одному  
```
import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS original_names(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS movies(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    original_name_id INTEGER NOT NULL UNIQUE,
    FOREIGN KEY(original_name_id) REFERENCES original_names(id)
);
''')

con.commit()
con.close()
```  

### Вот как создаётся связь:  
1. В таблице movies создаётся поле original_name_id типа INTEGER (только числа).
2. UNIQUE объявляет это поле уникальным в пределах таблицы: в ячейках этой колонки не может быть двух одинаковых значений — ведь два разных фильма не могут ссылаться на одно и то же оригинальное название.
3. NOT NULL — поле не может быть пустым, при создании каждой записи его обязательно нужно заполнять.
4. FOREIGN KEY(original_name_id) — объявляет поле original_name_id внешним ключом.
5. Ключевое слово  REFERENCES указывает с каким полем связан ключ. В нашем случае это поле  id в таблице original_names.

```
import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

original_names = [
    (1, 'Last Action Hero'),
    (2, 'Murder, She Wrote'),
    (3, 'Looney Tunes'),
    (4, 'Il Buono, il brutto, il cattivo'),
    (5, 'Who Framed Roger Rabbit'),
    (6, 'Merrie Melodies')
]

movies = [
    (1, 'Безумные Мелодии Луни Тюнз', 3),
    (2, 'Весёлые мелодии', 6),
    (3, 'Кто подставил кролика Роджера', 5),
    (4, 'Хороший, плохой, злой', 4),
    (5, 'Последний киногерой', 1),
    (6, 'Она написала убийство', 2)
]

cur.executemany('INSERT INTO original_names VALUES(?, ?);', original_names)
cur.executemany('INSERT INTO movies VALUES(?, ?, ?);', movies)

con.commit()
con.close()
```

Получение информации из связанных таблиц
Выборку из таблиц, связанных 1:1, можно получить, например, таким запросом:
```
cur.execute('''
-- Вернуть поле name из таблицы movies и поле name из original_names
SELECT movies.name,
       original_names.name
-- ...из двух таблиц
FROM movies,
     original_names
-- Выводить только те значения полей, для которых верно условие
WHERE movies.original_name_id = original_names.id
''')

for result in cur:
    print(result)
```

Длинным названиям столбцов лучше давать короткие псевдонимы с помощью оператора AS:
```
SELECT movies.name AS translation,
       original_names.name AS original
FROM movies,
     original_names
WHERE 
    movies.original_name_id = original_names.id
  -- Для интереса добавим условие
  AND
    original LIKE 'M%' 
```    
    
### Спринт 1/11 → Тема 3/4: Базы данных → Урок 13/17  
Отношения между таблицами. Один-ко-многим

  В Python создание связанных таблиц movies и types будет выглядеть так:
```  
import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS types(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS movies(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    type_id INTEGER NOT NULL,
    FOREIGN KEY(type_id) REFERENCES types(id)
);
''')

con.commit()
con.close() 
```

Заполним таблицы данными; следим, чтобы не перепутать значения полей type_id в movies:
```
import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

movies = [
    (1, 'Безумные Мелодии Луни Тюнз', 2),
    (2, 'Весёлые мелодии', 2),
    (3, 'Кто подставил кролика Роджера', 3),
    (4, 'Хороший, плохой, злой', 3),
    (5, 'Последний киногерой', 3),
    (6, 'Она написала убийство', 4),
]
types = [
    (1, 'Мультфильм'),
    (2, 'Мультсериал'),
    (3, 'Фильм'),
    (4, 'Сериал'),
]
cur.executemany('INSERT INTO types VALUES(?, ?);', types)
cur.executemany('INSERT INTO movies VALUES(?, ?, ?);', movies)

con.commit()
con.close()
```

### Спринт 1/11 → Тема 3/4: Базы данных → Урок 15/17
Отношения между таблицами. Многие-ко-многим

```
CREATE TABLE IF NOT EXISTS movies(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
```

```
CREATE TABLE IF NOT EXISTS directors(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
```

```
CREATE TABLE IF NOT EXISTS directors_movies(    
    director_id INTEGER NOT NULL,
    movie_id INTEGER NOT NULL,
    -- Пару полей назначаем композитным первичным ключом:
    PRIMARY KEY (director_id, movie_id),
    FOREIGN KEY(director_id) REFERENCES directors(id),
    FOREIGN KEY(movie_id) REFERENCES movies(id)
);
```

Спринт 1/11 → Тема 3/4: Базы данных → Урок 16/17
Изменение таблиц в БД. Ссылочная целостность