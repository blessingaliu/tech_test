# Tech Test 

### Description of how I approached this test
<br/>

1. Set up repo in local filesystem and another in Github and connected them
```
echo "# tech_test" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/blessingaliu/tech_test.git
git push -u origin main
```
<br/>


2. Set up folders 
Create a subfolder called Exercises 
```
mkdir Exercises
cd Exercises
```
Within Exercises folder, create a subfolder called FizzBuzz

```
mkdir FizzBuzz
cd FizzBuzz
touch step_one.py
```
<br/>


## Step 1 

Write a Python program that prints the numbers from 1 to 100. 
- If a number is a multiple of three, print "Fizz" instead of the number. 
- If the number is a multiple of five, print "Buzz" instead of the number.
- For numbers which are multiples of both three and five, print "FizzBuzz" instead of the number. 

<br/>


## Step 2

FizzBuzz is pretty simple as programs go. But it's interesting to see what happens if you try adding new rules. 

Work through these in order, adding one at a time. How easy is it? How neat and tidy is the resulting code? Can you make changes to your program to make these sorts of enhancements easier, or cleaner? 
- If a number is a multiple of 7, print "Bang" instead of the number. For numbers which are multiples of seven and three / five, append Bang to what you'd have printed anyway. (E.g. 3 * 7 = 21: "FizzBang").
- If a number is a multiple of 11, print "Bong" instead of the number. Do not print anything else in these cases. (E.g. 3 * 11 = 33: “Bong").
- If a number is a multiple of 13, print "Fezz" instead of the number. For multiples of most other numbers, the Fezz goes immediately in front of the first thing beginning with B, or at the end if there are none. (E.g. 5 * 13 = 65: "FezzBuzz", 3 * 5 * 13 = 195: "FizzFezzBuzz"). Note that Fezz should be printed even if Bong is also present (E.g. 11 * 13 = 143: “FezzBong").
- If a number is a multiple of 17, reverse the order in which any fizzes, buzzes, bangs etc. are printed. (E.g. 3 * 5 * 17 = 255: “BuzzFizz") 
