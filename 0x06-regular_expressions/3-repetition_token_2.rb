#!/usr/bin/env ruby

string = ARGV[0]
regex = /hbt{1,}n/

puts string.scan(regex).join
