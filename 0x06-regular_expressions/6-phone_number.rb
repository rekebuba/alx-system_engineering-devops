#!/usr/bin/env ruby

arg = ARGV[0]
output = arg.scan(/\A\d{10}\z/)
puts output.join("")
