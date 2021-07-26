#!/bin/bash
# Generate a random number between 1 and 10 of random events and random hosts

options=( buy_sword/dagger buy_sword/longsword join_guild/Sea_of_Sorrows join_guild/Henge_of_Denravi join_guild/Gates_of_Madness)
hosts=(user1.comcast.com user2.comcast.com user1.att.com)

rand=$RANDOM
let "num = $rand%10 + 1"
echo $num

cmd='docker-compose exec mids ab -n $num -H '"Host:' ${hosts[$rand%3]}'"' http://localhost:5000/${options[$rand%5]}'
eval $cmd