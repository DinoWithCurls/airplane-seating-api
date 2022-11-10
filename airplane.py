class Airplane:
    def __init__(self, noOfPassengers, seatsGrid) -> None:
        self.noOfPassengers = noOfPassengers
        self.seatsGrid = seatsGrid
        self.groups = len(seatsGrid)
        self.filled = 0
    
    def construct(self):
        # construct the array of seats, as they should be presented
        seats = []
        for i in self.seatsGrid:
            rows = i[1]
            cols = i[0]
            mat = []
            # initialise all seats with -1 for empty
            for i in range(rows):
                mat.append([-1]*cols)
            seats.append(mat)
        return seats
    # function for filling the aisle seats
    def fill_aisle_seats(self, seats):
        # start filling from the first row of seats
        row = 0
        tempFilled = -1
        seatGroups = self.groups
        while(self.filled < self.noOfPassengers and self.filled != tempFilled):
            # get the no of seats already filled
            tempFilled = self.filled
            for i in range(seatGroups):
                if self.seatsGrid[i][1] > row:
                    # check for first block of seats
                    if i == 0 and self.seatsGrid[i][0] > 1:
                        # update the seat with passenger number
                        self.filled += 1
                        # the aisle is the last column of this block
                        aisleCol = self.seatsGrid[i][0] - 1
                        seats[i][row][aisleCol] = self.filled
                        # check if all passengers have been seated
                        if self.filled >= self.noOfPassengers:
                            break
                    # check for last block of seats
                    elif i == seatGroups - 1 and self.seatsGrid[i][0] > 1:
                        self.filled += 1
                        # the aisle is the first column in this block
                        seats[i][row][0] = self.filled
                        # check if all passengers have been seated
                        if self.filled >= self.noOfPassengers:
                            break
                    else:
                        # the blocks in the middle of first and last blocks will each have two columns of aisle seats
                        self.filled += 1
                        # fill the left hand column first
                        seats[i][row][0] = self.filled
                        # check if all passengers have been seated
                        if self.filled >= self.noOfPassengers:
                            break
                        # check for the block where aisle seats have to be filled
                        if self.seatsGrid[i][0] > 1:
                            self.filled += 1
                            aisleCol = self.seatsGrid[i][0] - 1
                            seats[i][row][aisleCol] = self.filled
                            # check if all passengers have been seated
                            if self.filled >= self.noOfPassengers:
                                break
            row += 1
    # function for filling the window seats
    def fill_window_seats(self, seats):
        # start filling from the first row of seats
        row = 0
        tempFilled = -1
        seatGroups = self.groups
        while self.filled < self.noOfPassengers and self.filled != tempFilled:
            # get the no of seats already filled
            tempFilled = self.filled
            # first block
            if self.seatsGrid[0][1] > row:
                self.filled += 1
                # fill the window seats for the first block
                seats[0][row][0] = self.filled
                # check if all passengers have been seated
                if self.filled >= self.noOfPassengers:
                    break
            # last block
            if self.seatsGrid[seatGroups-1][1] > row:
                self.filled += 1
                window = self.seatsGrid[seatGroups-1][0] - 1
                # fill the window seats
                seats[seatGroups-1][row][window] = self.filled
                # check if all passengers have been seated
                if self.filled >= self.noOfPassengers:
                    break
            row += 1
    def fill_middle_seats(self, seats):
        # start filling from the first row of seats
        row = 0
        tempFilled = -1
        seatGroups = self.groups
        while self.filled < self.noOfPassengers and self.filled != tempFilled:
            # get the no of seats already filled
            tempFilled = self.filled
            for i in range(seatGroups):
                if self.seatsGrid[i][1] > row:
                    if self.seatsGrid[i][0] > 2:
                        for col in range(1, self.seatsGrid[i][0] - 1):
                            self.filled += 1
                            seats[i][row][col] = self.filled
                            # check if all passengers have been seated
                            if self.filled >= self.noOfPassengers:
                                break
            row += 1


def airplane_seating(seatGrid, passengers):
    if(len(seatGrid) == 0):
        return 0
    airplane = Airplane(passengers, seatGrid)
    seats = airplane.construct()
    # As per the rule, fill up the aisle seats first
    airplane.fill_aisle_seats(seats)
    # As per the rule, fill up the windows seats next
    if(airplane.filled < passengers):
        airplane.fill_window_seats(seats)
    # As per the rules, fill up the middle seats last
    if airplane.filled < passengers:
        airplane.fill_middle_seats(seats)
    return seats
