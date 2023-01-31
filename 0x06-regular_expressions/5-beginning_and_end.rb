#!/usr/bin/env ruby

string = ARGV[0]
regex = /^h.n$/

puts string.scan(regex).join
