from player import Player
import pandas as pd

anyevent_df = pd.read_csv('any_whatever.csv')
class RandomEvent:
    def __init__(self, Player):
        # random event generation will occur

        # pick a random event from the list
        rand_event = anyevent_df.sample()
        self.prompt = rand_event['prompt'].iloc[0]
        self.mod_foc = rand_event['focus'].iloc[0]
        self.mod_fun = rand_event['fun'].iloc[0]
        self.mod_know = rand_event['knowledge'].iloc[0]


        # modify the player states
        Player.mod_fun(self.mod_fun)
        Player.mod_focus(self.mod_foc)
        Player.mod_knowledge(self.mod_know)

        # print to user
        print(self)

    def __repr__(self):
        return "{} You get {} Fun, {} Focus, {} Knowledge".format(self.prompt, self.mod_fun, self.mod_foc, self.mod_know)

