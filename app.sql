-- Drop the table if it exists
DROP TABLE IF EXISTS registration;

-- Create the registration table
CREATE TABLE registration (
    id SERIAL,
    full_name TEXT,
    gender TEXT,
    course TEXT,
    email TEXT,
    phone_number TEXT,
    address TEXT,
    registration_date DATE
);

-- Insert sample data into the registration table
INSERT INTO registration (full_name, gender, course, email, phone_number, address, registration_date)
VALUES
    ('Ahmad Maulana', 'male', 'General English', 'ahmad@example.com', '62838', 'address1', '2023-10-01'),
    ('Renata Zahab', 'female', 'Business English', 'renata@example.com', '62838', 'address2', '2022-10-02'),
    ('Nunuk Reni', 'female', 'TOEFL Preparation', 'nunuk@example.com', '62838', 'address3', '2022-10-03'),
    ('Bro Ulil', 'male', 'IELTS Preparation', 'ulil@example.com', '62838', 'address4', '2022-10-04'),
    ('Wah Bowi', 'male', 'General English', 'wah@example.com', '62838', 'address5', '2022-10-05'),
    ('Iis Mika', 'female', 'Business English', 'iis@example.com', '62838', 'address6', '2022-10-06'),
    ('Zizah Lana', 'female', 'TOEFL Preparation', 'zizah@example.com', '62838', 'address7', '2022-10-07'),
    ('Alif Iman', 'male', 'IELTS Preparation', 'alif@example.com', '62838', 'address8', '2022-10-08'),
    ('Zaka Zaki', 'female', 'General English', 'zaka@example.com', '62838', 'address9', '2022-10-09'),
    ('Faus Rahmi', 'male', 'Business English', 'faus@example.com', '62838', 'address10', '2022-10-11');
