for time import sleep

print('1')
sleep(3)
print('2')

# Blocking 한 함수들로 구성
def sleep_3s():
    sleep(3)
    print('Wake up!')
print('Start Sleeping')
sleep_3s()
print('End of Sleeping')

if __name__ == '__main__':
    main()