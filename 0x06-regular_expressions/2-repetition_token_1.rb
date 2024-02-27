#!/usr/bin/env ruby

arg = ARGV[0]
output = arg.scan(/hb{0,1}tn/)
puts output.join("")
