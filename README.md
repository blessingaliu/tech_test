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
