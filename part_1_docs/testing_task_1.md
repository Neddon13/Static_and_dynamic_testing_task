### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

  # Missing 'def __init__' which means we cannot initialise our Class Object

  def check_for_ace(self, card):
    if card.value = 1:    
    # Wrong operator used. Should be the 'Equal to' operator ('==') rather than assignment operator ('=').
      return True
    else             # Should have a colon (:) after 'else'
      return False
   

  dif highest_card(self, card1 card2): 
  # Spelling error. Should be 'def' not 'dif'. Also should have a comma (,) between 'card1' and 'card2'.
  if card1.value > card2.value: 
    return card   # Should be the same as the parameter (card1)
  else:
    return card2
  


def cards_total(self, cards):
  total                           # Hasn't been assigned to anything. Should be, for example, 'total = 0'
  for card in cards:
    total += card.value
    return "You have a total of" + total 
    # Should be using string interpolation e.g f"You have a total of + {total}"
  
```
