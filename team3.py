# -*- coding: utf-8 -*-
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'vlogChamp™' # Only 10 chars displayed.
strategy_name = 'How to get free 100 points(No Survey!)'
strategy_description = 'We’ll always collude and if they betray we betray.'
import random
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. '''
    
    if their_score == 100: # If we've been bamboozeled then betray them.
        print("Like yo mama? Make sure to like the video!")
        return 'b'
    else:
        return 'c'
    
    if 'b' in their_history[0:]: # If the other player has betrayed within last round, 
        return 'b'               # Betray them like the frickin' fracks they are.
    else:
        return 'c'         # but 100% of the time collude
    
    if 'c' in my_history[0:]: # If we have not betrayed within the last round.
        return 'b'            # Betray because we take those.
    else:
        return 'c'
    
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.


    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" + ", ".join(["'"+my_history+"'", "'"+their_history+"'", str(my_score), str(their_score)])+") returned " + "'" + real_result + "'" + " and should have returned '" + result + "'")
        return False


if __name__ == '__main__':
    
    # Test 1: Betray on first move.
    if test_move(my_history='ccc',
              their_history='bbb', 
              my_score=0,
              their_score=100,
              result='b'):
         print 'Test passed'
    else:
         print 'Test Failed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='c')             
