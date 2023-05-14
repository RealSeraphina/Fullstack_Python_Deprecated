# The Bs and the Ps are two warring ASCII Character Clans and they cannot decide who is the better ASCII Character Clan. 
# The B's think they are better because they have an even number of humps, while the Ps think their odd number of humps are more artistically pleasing.

# Write a function Bs_or_Ps that takes a string battle as an argument, that only contains the characters 
# "B" and "P" (capitalization counts) in varying amounts.

#     If there are more Bs than Ps, return "The B Character Clan is victorious!"
#     If there are more Ps than Bs, return "The P Character Clan is victorious!"
#     In the event of a tie:
#         If there are an even amount or Bs and Ps, then the Bs ultimately win and return "The B Character Clan is victorious!"
#         If there are an odd amount of Bs and Ps, then the Ps ultimately win and return "The P Character Clan is victorious!"
#     BONUS: Only write the victorious return statements one time for the B Clan and the P Clan

# # Examples:

# Bs_or_Ps("BBBBBPPP") ==> "The B Character Clan is victorious!"`

# Bs_or_Ps("BBBBPPPPPPPPP") ==> "The P Character Clan is victorious!"

# Bs_or_Ps("BBPP") ==> "The B Character Clan is victorious!"`

# Hint: Pseudocode breakdown

#     Define the function Bs_or_Ps with the argument battle
def Bs_or_Ps(battle):
#   Define a boolean Bs_win and set it equal to False   
    Bs_win = False
#   Define 2 counters, Bs_counter and Ps_counter and set them both equal to 0
    Bs_counter = 0
    Ps_counter = 0
#   Loop through battle
    for char in battle:
        char = str(char)
        #print(char)
#       If the current character is a B, increment Bs_counter
        if char == "B":
            Bs_counter = Bs_counter + 1
            #print("B Found")
#       If the current character is a P, increment Ps_counter
        if char == "P":
            Ps_counter = Ps_counter  + 1
            #print("P Found")
    #print("BS: " + str(Bs_counter))
    #print("PS: " + str(Ps_counter))
#   If there are equal amounts of Bs and Ps:
    if Bs_counter == Ps_counter:
#       If there are an even amount of Bs and Ps, set Bs_win to True
        if (Bs_counter + Ps_counter) % 2 == 0:
            Bs_win = True
#       If there are an odd amount of Bs and Ps, set Bs_win to False
        if (Bs_counter + Ps_counter) % 2 != 0:
            Bs_win = False
#   If there are more Bs than Ps, set Bs_win to True
    if Bs_counter > Ps_counter:
        Bs_win = True
#   If there are more Ps than Bs, set Bs_win to False
    if Bs_counter < Ps_counter:
        Bs_win = False
#   If Bs_win is True:
    if Bs_win == True:
        #print(str(Bs_counter))
        #print(str(Ps_counter))
#       return "The B Character Clan is victorious!"
        return "The B Character Clan is victorious!"
#   If Bs_win is False:
    if Bs_win == False:
#       return "The P Character Clan is victorious!"
        return "The P Character Clan is victorious!"

def main():
    print(Bs_or_Ps("BBBBBPPP")) # B
    print(Bs_or_Ps("BBBBPPPPPPPPP"))# P
    print(Bs_or_Ps("BBPP")) # B
    print(Bs_or_Ps("P"))
    
if __name__ == "__main__":
    main()

