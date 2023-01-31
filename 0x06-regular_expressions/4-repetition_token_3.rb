#!/usr/bin/env ruby

string = ARGV[0]
regex = /(hbn)|(hbt*n)/

puts string.scan(regex).join
