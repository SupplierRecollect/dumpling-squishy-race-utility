#include "../src/race_utils.h"
#include "../src/dumpling_handler.h"
#include <cassert>

void test_race_positions() {
    auto positions = get_race_positions();
    assert(positions.size() == 4);
}

void test_dumpling_creation() {
    auto dumpling = create_dumpling("TestDumpling");
    assert(dumpling->get_name() == "TestDumpling");
}

int main() {
    test_race_positions();
    test_dumpling_creation();
    return 0;
}