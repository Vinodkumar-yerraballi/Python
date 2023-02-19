def reverse_words_order_and_swap_cases(sentence):
    Words=sentence.split()
    reverse_swap=Words[::-1]
    reversed_sentence=" ".join(reverse_swap)
    return reversed_sentence.swapcase()
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()
###Second hackerran question
    def avergae(*num):
        return sum(num)/len(num)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = list(map(int, input().split()))
    res = avg(*nums)
    
    fptr.write('%.2f' % res + '\n')

    fptr.close()