class Game:
    def __init__(self, title):
        self._title = title
        self._results = []
        self._players = []
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if isinstance(value, str) and value:
            self._title = value
        else:
            raise Exception
            
    def results(self, new_result=None):
        from classes.result import Result
        if new_result and isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results
    
    def players(self, new_player=None):
        from classes.player import Player
        if new_player and isinstance(new_player, Player):
            self._players.append(new_player)
        return self._players
    
    def average_score(self, player): 
        player_scores = []
        for each_result in self._results:
            if each_result.player == player:
                player_scores.append(each_result.score)
        total_scores = sum(player_scores)
        average_score = total_scores / len(player_scores)
        return average_score

    # def average_score(self, player):
        # player_scores = [r.score for r in self._results if r.player == player]
        # if player_scores:
        # return sum(player_scores) / len(player_scores)
        # return 0