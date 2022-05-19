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

    func Length, [expr]
        return len(str(expr))