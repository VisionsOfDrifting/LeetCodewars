#include <condition_variable>
#include <mutex>
#include <thread>
#include <iostream>
#include <functional>
void printFirst()
{
  std::cout<<"first";
}
void printSecond()
{
  std::cout<<"second";
}
void printThird()
{
  std::cout<<"third";
}
class Foo {
public:
    unsigned int test = 0;
    std::condition_variable cv;
    std::mutex m;
    Foo() {
        
    }

    void first(std::function<void()> printFirst) {
        std::unique_lock<std::mutex> lock(m);
        cv.wait(lock, [this](){return test == 0;});
        // printFirst() outputs "first". Do not change or remove this line.
        printFirst();
        ++test;
         cv.notify_one();
        // notify first_semaphore has changed
    }

    void second(std::function<void()> printSecond) {
        std::unique_lock<std::mutex> lock(m);
        cv.wait(lock, [this](){return test == 1;});

        // printSecond() outputs "second". Do not change or remove this line.
        printSecond();
  
        ++test;
        cv.notify_one();
        // notify second semaphore has changed
    }

    void third(std::function<void()> printThird) {
        std::unique_lock<std::mutex> lock(m);
        cv.wait(lock, [this](){return test == 2;});
        // printThird() outputs "third". Do not change or remove this line.
        printThird();
        test = 0;
        cv.notify_one();
        // notify third semaphore has changed and reset all values
        
    }
};
int main()
{
  Foo test;
  std::thread first([&test](std::function<void()> f){test.first(f);}, printFirst);
  std::thread third([&test](std::function<void()> f){test.third(f);}, printThird);
  std::thread second([&test](std::function<void()> f){test.second(f);}, printSecond);

  first.join();
  third.join();
  second.join();
}
