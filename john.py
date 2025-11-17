import time

def login(username, password, login_time):
    # Simulated user database
    user_db = {
        "alice": {"password": "password123", "locked": False},
        "bob": {"password": "securepass", "locked": False},
        "charlie": {"password": "charlie123", "locked": False}
    }

    SESSION_TIMEOUT = 300  # 5 minutes
    current_time = time.time()

    if current_time - login_time > SESSION_TIMEOUT:
        return "Error: Session expired. Please refresh and try again."
    if username not in user_db:
        return "Error: User ID not found."
    if user_db[username]["locked"]:
        return "Error: Account is locked due to multiple failed attempts."
    if password != user_db[username]["password"]:
        return "Error: Incorrect password."

    return "Login successful!"

# Example usage
if __name__ == "__main__":
    login_time = time.time()
    print(login("john", "password123",time.time()))
