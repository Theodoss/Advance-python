class FacePamphlet:

    def __init__(self,__n):
        self.__username = __n
        self.firend_list = []
        self.__history = {}

    def post(self, message):
        self.__history[len(self.__history)+1] = message
        print(f'{self.__username} posted " {message} "')

    def set_username(self,new_name):
        self.__username = new_name

    def add_friend(self,profile):
        self.firend_list.append(profile)
        print(f'{self.__username} added {profile.getusername()}')

    def get_username(self):
        return self.__username

    def get_post_history(self):
        return self.__history

    def get_friends(self):
        if len(self.firend_list) == 0:
            return '[]'
        s ='['
        for obj in self.firend_list:
            s += obj.get_username()
            s += ','

        return s[:-2]+']'



