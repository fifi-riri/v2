CREATE TABLE autor(
    id INTEGER NOT NULL PRIMARY KEY,
    FIO VARCHAR(100)  NOT NULL
);

CREATE TABLE book(
    id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    autor_id INTEGER NOT NULL,
    year_of_publication DATE,
    count_book INTEGER NOT NULL,
    FOREIGN KEY (autor) REFERENCES autor(autor(id))
);

CREATE TABLE readers(
    id INTEGER NOT NULL PRIMARY KEY,
    FIO VARCHAR(100) NOT NULL,
    Address VARCHAR(100) NOT NULL,
    phone VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE staff(
    id INTEGER NOT NULL PRIMARY KEY,
    FIO_S VARCHAR(100) NOT NULL,
    phone_S VARCHAR(100) NOT NULL UNIQUE
);
CREATE TABLE issuance(
    id INTEGER NOT NULL PRIMARY KEY,
    book_id INTEGER NOT NULL,
    staff_id INTEGER NOT NULL,
    date_issuance DATE,
    date_delivery DATE,
    FOREIGN KEY(book_id) REFERENCES book(id)
                  ON DELETE CASCADE ON UPDATE NO ACTION,
    FOREIGN KEY(staff_id) REFERENCES staff(id)
                  ON DELETE CASCADE ON UPDATE NO ACTION,
);
