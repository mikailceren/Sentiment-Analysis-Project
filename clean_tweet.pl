#!/usr/bin/perl



$infile = "tweet1.txt";
open INFILE, $infile;
$outfile = "tweet_output.txt";            
open OUTFILE, ">$outfile" or die "Cannot open $outfile: $!";


 $n = -1;			    
while ($line = <INFILE>) {
    chomp $line;		 
	next if $line =~ /^\s*$/; 

	$line =~ tr/#/ /;
	$line =~ s/RT\s@.*?:/ /i;
	
	while($line =~ /http.*?\s|http.*?$/g){
	$line =~ s/http.*?\s|http.*?$/ /i; 
	next if $line =~ /^\s*$/; 

}
	
	

	@array = split (/\d+/, $line);



#print OUTFILE "@array\n";
    print OUTFILE "@array\n";
}


