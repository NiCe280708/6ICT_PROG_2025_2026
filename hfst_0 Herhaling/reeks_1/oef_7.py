def seconden_per_dag(aantal):
    secondes = aantal * 86400
    return secondes
    
    """ return het aantal seconden in aantal dagen 
            Tip! een dag is 24u, een uur 60min, een minuut 60s
    """

print( seconden_per_dag(1) )    # 86400
print( seconden_per_dag(3) )    # 259200
print( seconden_per_dag(7) )    # 604800
