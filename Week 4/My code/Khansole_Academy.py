import random

# correct_count = 0

def main():
    print("Khansole Academy")
    
    # first_number = random.randint(10,99)
    # second_number = random.randint(10,99)
    
    # print(first_number)
    # print(second_number)
    
    # print(f'What is {first_number} + {second_number}?')
    
    # user_answer = int(input("Your answer: "))
    
    # actual_answer = first_number + second_number
    correct_count = 0
    while correct_count != 3:
        
            
        first_number = random.randint(10,99)
        second_number = random.randint(10,99)
        
        print(f'What is {first_number} + {second_number}?')
        user_answer = int(input("Your answer: "))
        actual_answer = first_number + second_number
        
        if user_answer == actual_answer:
            correct_count += 1 
            print(f'Correct! You gotten {correct_count} correct in a row')
            
            
            
        else:
            print(f'The expected answer is {actual_answer}')
            
    print("Congratualtions! You mastered addition")
    
if __name__ == '__main__':
    main()