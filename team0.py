import random

team_name = 'The Only Boy and Girl Combo'     # Only 10 chars displayed.
strategy_name = 'Collude most of the time unless betrayed'
strategy_description = 'In order to gather data on the opponents playing strategy, we will assign our first 8 plays to a different strategy. For our first 8 plays, we will put forth a 50/50 chance of betrayal and collusion. After that: if there is a betrayal within our opponents past 10 moves, we will put forth a 75% of betrayal. In addition to that, if in their most recent move, if we collided and they betrayed, we will automatically betray as to lessen our point loss.'

 

def move(my_history, their_history, my_score, their_score):
    list1 = ['c', 'b']
    if len(my_history)<=8: #for the first 8 moves
       return random.choice(list1) #returns either collude or betray from a list
    else:
        if my_history[-1]=='c' and their_history[-1]=='b': #if our last move was collude and their last move was betray
            return 'b' #Betray
        elif 'b' in their_history[-10:]:  #if the opponent betrayed in the last 10 moves
            if random.random()<0.75: #have a 75% chance of betraying
                return 'b'         
            else:
                return 'c'  #otherwise collude 25% of the time
        else:
            return 'c'   #if the opponent did not betray in the last ten moves, or we did not collude when they betrayed, then collude.
            
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='ccccccccc',
              their_history='bbbbbbbbb', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
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
              result='b') 
      

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.          