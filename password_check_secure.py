import bcrypt
import os

# Hash a password (do this ONCE during setup/registration)
def hash_password(password):
    """
    Hash a password using bcrypt.
    This should be done during user registration/setup.
    """
    # Generate a salt and hash the password
    salt = bcrypt.gensalt(rounds=12)  # rounds=12 provides good security-performance balance
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


# Verify a password against its hash
def verify_password(guess, hashed_password):
    """
    Verify that a guessed password matches the stored hash.
    Returns True if the password is correct, False otherwise.
    """
    return bcrypt.checkpw(guess.encode('utf-8'), hashed_password)


# Main authentication function
def authenticate_user(stored_hash, max_attempts=3):
    """
    Authenticate user with password attempt limiting.
    
    Args:
        stored_hash: The bcrypt hashed password
        max_attempts: Maximum number of login attempts allowed
    """
    attempts = 0
    
    while attempts < max_attempts:
        guess = input("Enter password: ")
        
        if verify_password(guess, stored_hash):
            print("✓ Correct! Access granted.")
            return True
        else:
            attempts += 1
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"✗ Wrong password. Attempts remaining: {remaining}")
            else:
                print("✗ Wrong password.")
    
    print("⚠️  Account locked out - Too many failed attempts!")
    return False


# Example setup (run this once to create/store the hash)
def setup_example():
    """
    Example: This demonstrates how to set up the system.
    In production, this would be part of user registration.
    """
    print("=== Password Setup (Registration) ===")
    new_password = "sarthak"  # In real app, get from user input
    
    # Hash the password
    hashed = hash_password(new_password)
    print(f"Original Password: {new_password}")
    print(f"Hashed Password: {hashed.decode('utf-8')}")
    print("\n(In production, store this hash in a database)\n")
    
    return hashed


# Main program
if __name__ == "__main__":
    # Step 1: Setup (Registration) - do this once
    stored_password_hash = setup_example()
    
    # Step 2: Authentication - this happens on login attempts
    print("=== Password Authentication (Login) ===")
    success = authenticate_user(stored_password_hash, max_attempts=3)
    
    if success:
        print("\nUser authenticated successfully!")
    else:
        print("\nAuthentication failed. Account locked.")
