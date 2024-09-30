def response(hey_bob):
    # Remove leading and trailin
  if '?' in hey_bob:
    return "Sure."
  elif hey_bob.isUpper(): 
    return "Whoa, chill out!"
  elif '?'in hey_bob  and hey_bob.isUpper():
    return "Calm down, I know what I'm doing!"
  elif len(hey_bob.strip()) == 0:
    return "Fine. Be that way!"
  else: 
    return "Whatever."