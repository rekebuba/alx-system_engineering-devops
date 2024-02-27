#!/usr/bin/env ruby

arg = ARGV[0]
output = arg.scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)
puts output.join(",")
