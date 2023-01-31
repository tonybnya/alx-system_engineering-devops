#!/usr/bin/env ruby

string = ARGV[0]
regex = /(htn|hbtn)/

puts string.scan(regex).join
