class Item:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

    def get_info(self):
        return f"The item {self.name} is {self.genre}."

class Film(Item):
    def __init__(self, name, genre, length):
        super().__init__(name, genre)
        self.length = length

    def total_length(self):
        return self.length
 

    def get_info(self):
        return f"The movie {self.name} is {self.genre} and is {self.length} long."

  
class Serial(Item):
    def __init__(self, name, genre,n_episodes,len_episodes):
        super().__init__(name, genre)
        self.n_episodes = n_episodes
        self.len_episodes = len_episodes

    def total_length(self):
        sum=0
        for part in self.len_episodes:
            sum += part
        return sum

      

    def get_info(self, episode):
        print (f"The serial {self.name} is {self.genre}, it has {self.n_episodes} episodes and episode {episode} is {self.len_episodes[episode-1]} min long.")




movie = Film ("Dirty Dancing", "romantic", "90 min")
series = Serial ("Velvet", "historic","3", [35, 36, 37])
print(movie.get_info())
series.get_info(2)
