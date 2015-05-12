#!/usr/bin/perl
#I used this code to clean tweets
$infile = "akp.txt";
open INFILE, $infile;
$outfile = "akp_output.txt";            
open OUTFILE, ">$outfile" or die "Cannot open $outfile: $!";


 $n = -1;			    
while ($line = <INFILE>) {
    chomp $line;		 
	next if $line =~ /^\s*$/; 

	$line =~ s/#//i;
	$line =~ s/RT\s@.*?://i;
	while($line =~ /@.*?:|@.*?:/g){
	$line =~ s/@.*?:|@.*?://i;
	next if $line =~ /^\s*$/;
}
	while($line =~ /@.*?\s|@.*?\s/g){
	$line =~ s/@.*?\s|@.*?\s//i;
	next if $line =~ /^\s*$/;
}
	while($line =~ /http.*?\s|http.*?$/g){
	$line =~ s/http.*?\s|http.*?$//i; 
	next if $line =~ /^\s*$/; 

}
	$line =~ s/^\s.*?//i;
	$line =~ s/^Akp\s%$//i;
	

	@array = split (/\d+/, $line);



#print OUTFILE "@array\n";
    print OUTFILE "@array\n";
}


