#include "race_utils.h"
#include "dumpling_handler.h"
#include <fmt/core.h>

int main() {
    fmt::print("Dumpling Squishy Race Utility\n");

    auto positions = get_race_positions();
    fmt::print("Current positions: {}\n", fmt::join(positions, ", "));

    auto dumpling = create_dumpling("StickyRice");
    fmt::print("Created dumpling: {}\n", dumpling->get_name());

    return 0;
}