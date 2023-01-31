#!/usr/bin/env ruby

string = ARGV[0]
regex = /^h[a-z|A-Z|0-9]$n/

puts string.scan(regex).join
