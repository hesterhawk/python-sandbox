def two_fer(name="you"):
    return "One for {}, one for me.".format("you" if "" == name else name)