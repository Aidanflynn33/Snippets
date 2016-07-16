#include <iostream>

template<typename T>
class Memoizer
{
    private:
        bool _hasbeencalled;
        T _calculatedvalue;
        std::function<T()> _callee;
    public:
        Memoizer(std::function<T()> callee): _hasbeencalled(false), _callee(callee){}
        T get_value()
        {
            if(!_hasbeencalled){
                _calculatedvalue = _callee();
                _hasbeencalled = true;
            }
            return _calculatedvalue;
        }

};

int main() {
    size_t amount_of_calls = 0;

    auto expensive_calculation = [&] {
        ++amount_of_calls; //track amount of expensive calculations
        return 5; //expensive calculation
    };

    // create memoizer
    auto memoizer = Memoizer<int>{expensive_calculation};

    std::cout << amount_of_calls;

    auto result1 = memoizer.get_value();
    auto result2 = memoizer.get_value();

    std::cout << amount_of_calls;

	return 0;
}
