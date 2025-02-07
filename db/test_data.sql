-- テストデータ
INSERT INTO users (name, email, password) VALUES ('Test User', 'test@example.com', 'password123');
INSERT INTO events (title, date, location, description, created_by) VALUES ('Sample Event', '2025-02-10', 'Tokyo', 'This is a sample event.', 1);
INSERT INTO attendance (user_id, event_id, status) VALUES (1, 1, 'attending');
