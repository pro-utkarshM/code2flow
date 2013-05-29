def writeDotFile(dotFile,nodes,edges,groups):
	#write the output dot file
	with open(dotFile,'w') as outfile:
		outfile.write(generateDotFile(nodes,edges,groups))

def generateDotFile(nodes,edges,groups):
	ret = "digraph G {\n"
	ret += """
		subgraph legend{
		rank = min;
		label = "legend";
		Legend [shape=none, margin=0, label = <
			<table cellspacing="0" cellpadding="0" border="1"><tr><td>Code2flow Legend</td></tr><tr><td>
			<table cellspacing="0">
			<tr><td>Regular function</td><td width="50px"></td></tr>
			<tr><td>Trunk function (nothing calls this)</td><td bgcolor='red'></td></tr>
			<tr><td>Leaf function (this calls nothing else)</td><td bgcolor='green'></td></tr>
			<tr><td>Function call which returns no value</td><td>&#8594;</td></tr>
			<tr><td>Function call returns some value</td><td><font color='blue'>&#8594;</font></td></tr>
			</table></td></tr></table>
			>];}"""
	for node in nodes:
		if str(node):
			ret += str(node)+';\n'
	for edge in edges:
		ret += str(edge)+';\n'
	#pdb.set_trace()
	for group in groups:
		ret += str(group)+';\n'

	ret += '}'

	return ret