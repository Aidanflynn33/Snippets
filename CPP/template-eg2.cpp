#include <iostream>

template<typename T, typename U>
auto chain (T function1, U function2)
{
    auto fn1 = [=] { function1(); function2(); };
    return fn1;
}

int main() {
    auto fn1_called = false;
    auto fn2_called = false;

    auto fn1 = [&] { fn1_called = true; };
    auto fn2 = [&] { fn2_called = true; };

    std::cout << fn1_called;
    std::cout << fn2_called;

    fn1();

    std::cout << fn1_called;
    std::cout << fn2_called;

    return 0;
}
