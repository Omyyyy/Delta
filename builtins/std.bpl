class std
    func Lower, [string]
        return string.lower()

    func Upper, [string]
        return string.upper()

    func toString, [expr]
        return str(expr)

    func toInt, [expr]
        return int(expr)

    func toFloat, [expr]
        return float(expr)

    func toList, [expr]
        return list(expr)

    fastfunc Length, [expr]
        var total = 0
        loop foreach, character, str(expr)
            var total += 1

        return total

    func randomInt, [start end]
        return rnd.randint(start, end)

    func randomChar, []
        return rnd.choice(list(pystr.printable))