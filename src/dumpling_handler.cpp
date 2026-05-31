#include "dumpling_handler.h"

std::unique_ptr<Dumpling> create_dumpling(const std::string& name) {
    return std::make_unique<Dumpling>(name);
}