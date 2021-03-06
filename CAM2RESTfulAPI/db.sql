CREATE TABLE Users
(
    username VARCHAR(30) PRIMARY KEY,
    password_hash VARCHAR(100) NOT NULL
);

CREATE TABLE Submissions
(
    username VARCHAR(30),
    submission_id CHAR(23),
    status CHAR(11) NOT NULL,
    stdout TEXT,
    stderr TEXT,
    PRIMARY KEY(username, submission_id),
    FOREIGN KEY(username) REFERENCES Users(username) ON DELETE CASCADE
);
