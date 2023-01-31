#!/usr/bin/env ruby

string = ARGV[0]
regex = /^\d{10}$/

puts string.scan(regex).join
