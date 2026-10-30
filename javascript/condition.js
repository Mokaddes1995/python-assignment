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

    } else{

        console.log("Odd Number")
    }
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


// Find the Largest Number

function find_large_number(a, b, c){

    if (a >= b && a >= c) {
        console.log(a, "is greater than", b, "and", c)
    }
    else if (b >= a && b >= c) {
        console.log(b, "is greater than", a, "and", c)
    }
    else{
        console.log(c, "is greater than", a, "and", b)
    }
}

find_large_number(20, 30, 50)

find_large_number(40, 30, 20)

find_large_number(10, 30, 20)


// 5. Pass or Fail

function pass_fail(number) {

    if (number >= 33) {
        console.log("Pass")
    }else {
        console.log("Fail")
    }
}


pass_fail(33)

pass_fail(31)

pass_fail(40)


// Next challenge: Level 2

// Leap Year: Check whether a year is a leap year.


function leap_year(year){

    if ( year % 400 == 0) {
        console.log("Leap Year")
    }

    else if (year % 100 == 0) {
        console.log("Not Leap year")
    }

    else if (year % 4 == 0) {
        console.log("Leap Year")
    }

    else{
        console.log("Not Leap Year")
    }
}

leap_year(1900)


// Divisibility: Check whether a number is divisible by both 5 and 3.

function divisibility(n){

    if (n % 5 == 0 && n % 3 == 0 ) {
        console.log( n, "Divisible by 5 and 3")
    }

    else {
        console.log("Not Divisible")
    }
}

divisibility(10)

divisibility(15)


// Grade Calculator: Calculate grades using marks (A+, A, A-, B, C, Fail).

function grade_calculator(num) {

    if (num >= 80) {

        console.log("A+")
    }

    else if (num >= 70) {

        console.log("A")
    }

    else if (num >= 60) {

        console.log("A-")
    }

    else if (num >= 50) {

        console.log("B")
    }

    else if (num >= 33) {

        console.log("C")
    }
    else {
        console.log("Fail")
    }
}

grade_calculator(90)
grade_calculator(70)
grade_calculator(33)
grade_calculator(23)


// Vowel or Consonant: Check whether a character is a vowel or consonant.


function check_alphabet(alpha) {

    const vowel = "aeioAEIOU"

    if (vowel.includes(alpha)) {

        console.log(alpha, "is Vowel")
    }
    else{

        console.log(alpha, "is Consonant")
    }
}

check_alphabet("a")

check_alphabet("B")

check_alphabet("A")


// Challenge 5: Largest of Four Numbers

function find_largest(a, b, c, d) {

    if ((a >= b && a >= c) && a >= d ) {

        console.log(a, "is the largest")
    }

    else if ((b >= a && b >= c) && b >= d ) {

        console.log(b, "is the largest")
    }

    else if ((c >= a && c >= b) && c >= d ) {

        console.log(c, "is the largest")
    }
    else{

        console.log(d, "is the largest")
    }

}

find_largest(10, 50, 30, 20);
// Output: 50 is the largest

find_largest(100, 40, 60, 80);
// Output: 100 is the largest

find_largest(20, 20, 10, 5);
// Output: 20 is the largest