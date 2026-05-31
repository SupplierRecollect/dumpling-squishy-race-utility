#pragma once
#include <string>
#include <memory>

class Dumpling {
public:
    explicit Dumpling(const std::string& name) : name_(name) {}
    std::string get_name() const { return name_; }
private:
    std::string name_;
};

std::unique_ptr<Dumpling> create_dumpling(const std::string& name);