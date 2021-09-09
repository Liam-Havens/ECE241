class Hw1Q1:
    def timeConvert(self,inputSecond):
        timeString = ""
        countUnit = inputSecond // 86400
        if countUnit == 1:
            timeString += "1 day"
        elif countUnit > 1:
            timeString += "{} days".format(countUnit)
        inputSecond = inputSecond % 86400

        countUnit = inputSecond // 3600
        if timeString != "":
            timeString += ", "
        if countUnit == 1:
            timeString += "1 hour"
        elif countUnit > 1:
            timeString += "{} hours".format(countUnit)
        inputSecond = inputSecond % 3600

        countUnit = inputSecond // 60
        if timeString != "":
            timeString += ", "
        if countUnit == 1:
            timeString += "1 minute"
        elif countUnit > 1:
            timeString += "{} minutes".format(countUnit)
        inputSecond = inputSecond % 60

        if timeString != "":
            timeString += ", "
        if inputSecond == 1:
            timeString += "1 second"
        elif inputSecond > 1:
            timeString += "{} seconds".format(inputSecond)

        return timeString


if __name__ == '__main__':
    test = Hw1Q1()
    print(test.timeConvert(2021))
