// 1. Positive, Negative or Zero


function check_number(n) {

    if (n > 0) {
        console.log("Positive Number")
    }

    else if (n < 0) {

        console.log("Negative Number")
    }

    else if (n == 0) {

        console.log("Zero")
    }
}


check_number(10)

check_number(0)

check_number(-1)


// 2. Even or Odd


function even_odd (n) {

    if (n % 2 == 0) {

        console.log("Even Number")

    } else(

        console.log("Odd Number")
    )
}


even_odd (0)

even_odd (2)

even_odd (1)


// 3. Age Checker


function age_checker (age) {

    if (age >= 18) {

        console.log("You can vote")

    } else {

        console.log("You cannot vote")
    }
}

age_checker (18)

age_checker (15)