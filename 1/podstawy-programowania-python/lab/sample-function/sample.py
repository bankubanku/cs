import random


def sample(sampleNums, howMany):
    result = []
    
    while howMany != 0:
        x = random.randint(0,len(sampleNums)-1)
        result.append(sampleNums[x])
        if sampleNums[x] != sampleNums[-1]:
            sampleNums[x] = sampleNums[-1]
        sampleNums.pop(-1)
        howMany-=1

    return result

def main():
    print(sample([3,5,1,7,8],2))

if __name__ == "__main__":
    main()
