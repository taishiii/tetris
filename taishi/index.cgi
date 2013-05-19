#!/usr/bin/perl

use strict;
use warnings;

use CGI;
use HTML::Template::Pro;


my $tmpl = HTML::Template::Pro->new(filename => 'index.tmpl');
$tmpl->param("block1", 1);

print "Content-Type: text/html\n\n";
print $tmpl->output();

my $start = time();

while ( time() - $start > 20 ) {
	while ($start % 2) {
		
		my $margin_top = 0;
		$margin_top += 10;
		$tmpl->param("margin-top", $margin_top);

		print "Content-Type: text/html\n\n";
		print $tmpl->output();


	}


}
