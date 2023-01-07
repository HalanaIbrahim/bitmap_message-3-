import sys
bitmap = """
....................................................................
      ************** * *** ** *        ******************************
    ********************* ** ** * *     ****************************** *
   **     *****************         ******************************
          ************* ** *    **** ** ************** *
            *********         ******* **************** * *
            ********           *************************** *
            * * **** ***        ***************                ****** ** *
             **** *               ***************        *** *** *
              ******                *************           ** ** *
                ********              *************          * ** ***
                ********            ******** *              *** ****
               *********             ****** *            **** ** * **
                *********           ****** *             * *** * *
                 ******         ***** ** *          **** *
                *****           **** *              ********
                *****           ****                  *********
               **** **          ******* *
                ***                  *                       *
                **                  *                       *
...................................................................."""

message = input('>')
if message == ' ':
    sys.exit()

#Loop through each line 
for line in bitmap.splitlines():
    for i, bit in enumerate(line):
        if bit == ' ':
            print(' ', end= ' ')
        else:
            print(message[i % len(message)], end= ' ')
    print()