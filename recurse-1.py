def taxi_mode(distance):
    end_taxa = 4+(0.25*distance)
    return taxi_mode(distance-end_taxa)



def main():
    print(taxi_mode(200))
