import hdlparse.vhdl_parser as vhdl
import hdlparse.verilog_parser as vlog

vlog_ex = vlog.VerilogExtractor()
vlog_mods = vlog_ex.extract_objects_from_source('abc.')

for m in vlog_mods:
  print('Module "{}":'.format(m.name))
#vlog_mods = vlog_ex.parse_verilog_file('a.v')