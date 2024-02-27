#!/usr/bin/env ruby

arg = ARGV[0]
output = arg.scan(/hbt{1,}n/)
puts output.join("")
