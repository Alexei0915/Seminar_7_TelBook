import view as v
import controller as contrl

pl_one = v.hi_one()
pl_two = v.hi_two()
gst = contrl.game_start(pl_one_name=pl_one, name_two_player=pl_two, matrix_game=v.playing_table())
v.winner(count=gst[0], random_move=gst[1], pl_one_name=pl_one, name_two_player=pl_two)