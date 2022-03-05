DELETE FROM `books`;
INSERT INTO `books` 
 VALUES (1, "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", "Charles Scribner's Sons", "1925", 500.00 , 10, 2),
        (2, "Nineteen Eighty-Four", "George Orwell", "Science Fiction", "Secker & Warburg", "1949", 400.00 , 5, 3),
        (3, "Pride and Prejudice", "Jane Austen", "Romance", "R. W. Chapman", "1923", 300.00 , 7, 4),
		(4, "Anna Karenina", "Leo Tolstoy", "Fiction", "Modern Library", "2000", 400.00 , 1, 0),
        (5, "Lord of the Flies", "William Golding", "Fiction", "Faber and Faber", "1954", 500.00 , 6, 2);
        
DELETE FROM `customers`;
INSERT INTO `customers` 
 VALUES (1, "Jane Doe", "1234567890", "y"),
        (2, "John Doe", "0987654321", "n"),
        (3, "Kriya Mahesh", "1234509876", "n"),
        (4, "Ayesha Khan", "0987612345", "y"),
        (5, "James Smith", "5647382910", "n");

DELETE FROM `vendors`;
INSERT INTO `vendors` 
 VALUES (1, "Kohinoor Distributors", "1234567890"),
		(2, "Subha Bookstore", "0987654321"),
        (3, "Vishala Publications", "1234509876"),
        (4, "Apollo Distributors", "0987612345"),
        (5, "SPS Publications", "5647382910");
        
DELETE FROM `fromven`;
INSERT INTO `fromven` 
 VALUES (1, 2, 3, 10, 4000.00),
        (2, 1, 4, 5, 2000.00),
        (3, 3, 5, 7, 3500.00),
        (4, 5, 2, 15, 6000.00),
        (5, 4, 1, 6, 3000.00);
        
DELETE FROM `checkout`;
INSERT INTO `checkout` 
 VALUES (1, 2, 3, 1, 300.00, 300.00),
        (2, 1, 4, 1, 400.00, 360.00),
        (3, 3, 5, 1, 500.00, 300.00),
        (4, 5, 2, 2, 800.00, 300.00),
        (5, 4, 1, 1, 500.00, 450.00);
        
DELETE FROM `reserved`;
INSERT INTO `reserved` 
 VALUES (1, 2, 3, 1, "2022-01-02", 'y'),
        (2, 1, 4, 1, "2022-01-12", 'y'),
        (3, 3, 5, 1, "2022-02-02", 'n'),
        (4, 5, 2, 2, "2022-02-12", 'n'),
        (5, 4, 1, 1, "2022-02-22", 'n');