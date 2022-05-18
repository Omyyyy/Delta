class std
    func lower, [string]
        return string.lower()

    func upper, [string]
        return string.upper()
    
    func toInt, [expr]
        return int(expr)
    
    func toString, [expr]
        return str(expr)

    func toFloat, [expr]
        return float(expr)
    
    func toArray, [expr]
        return list(expr)