#!/usr/bin/env ruby

string = ARGV[0]
regex = /(?<=from:|to:|flags:).+?(?=\])/

puts string.scan(regex).join(',')
