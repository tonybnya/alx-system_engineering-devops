#!/usr/bin/env ruby

string = ARGV[0]
regex = /School/

puts string.scan(regex).join
