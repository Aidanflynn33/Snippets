#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>


struct Converted {
	Converted(): conv{"["} {}

	template <typename T>
	void operator()(T n) {
		std::ostringstream strs;
		strs << n;
		conv += strs.str();
		conv += ", ";
	}

	std::string converted()  {
		if (conv.length() > 1)
			conv.erase(conv.length()-2,2);
		conv += "]";
		return conv;
	}

private:
	std::string conv;
};

template <typename T>
std::string dump_list (const T container)
{
	Converted conv = std::for_each(container.begin(), container.end(), Converted());
	return conv.converted();
}

template <typename T>
std::string dump_list2 (const T container)
{
    std::string conv="[";
    for (const auto i: container)
    {
        std::ostringstream strs;
		strs << i;
		conv += strs.str();
        conv += ", ";
    }
	if (container.size() > 0)
		conv.erase(conv.length()-2,2);
    conv+="]";
    return conv;
}


int main() {
	std::vector<int>  vec1;
	std::cout << dump_list(vec1) << std::endl;
	std::cout << dump_list2(vec1) << std::endl;

	std::vector<int>  vec2 = {1, 2, 3, 4};
	std::cout << dump_list(vec2) << std::endl;
	std::cout << dump_list2(vec2) << std::endl;

	std::vector<std::string>  vec3 = {"a", "b", "c", "d"};
	std::cout << dump_list(vec3) << std::endl;
	std::cout << dump_list2(vec3) << std::endl;

	std::vector<double>  vec4 = {1.1, 2.2, 3.3, 4.4};
	std::cout << dump_list(vec4) << std::endl;
	std::cout << dump_list2(vec4) << std::endl;

	return 0;
}
