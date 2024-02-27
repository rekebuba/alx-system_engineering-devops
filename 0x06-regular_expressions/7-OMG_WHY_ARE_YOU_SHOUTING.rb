#!/usr/bin/env ruby

arg = ARGV[0]
output = arg.scan(/[[:upper:]]/)
puts output.join("")
