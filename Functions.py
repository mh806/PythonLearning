from List import people


def great(name="User", /, *, be_nice=True):
    if not be_nice:
        return "Who do you think you are"
    print("Hey, William")
    print("Welcome " + name)


great("William")
great()
great("Nice", be_nice=True)


# benefit -> save lines of codes, dont repeat codes, update one spot

# arguments and parameters
# arguments -> what you passed to functions
# parameters -> saved in functions

