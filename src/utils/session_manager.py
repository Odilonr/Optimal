class SessionManager:
    def __init__(self):
        self.current_user = None

    def login(self, user):
        self.current_user = user

    def logout(self):
        self.current_user = None

    def get_current_user(self):
        return self.current_user
    
    def is_logged_in(self):
        return self.current_user is not None
    
    def update_current_user(self, new_user):
        self.current_user = new_user
    

session_manager = SessionManager()