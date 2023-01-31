#!/usr/bin/env ruby

string = ARGV[0]
regex = /[A-Z]/

puts string.scan(regex).join
