#!/usr/bin/perl

use LWP::UserAgent;
use HTTP::Request;
use Data::Dumper;

print "Начали тест авторизации \n";


my $crURL="http://192.168.206.3:7547/fgfdg";
my	$crUser='rtk';
my	$crPass='rtk';



printf("making Connection Request to %s, please wait...\n", $crURL||'');
#todo
my $ua  = LWP::UserAgent->new(keep_alive => 1, timeout => 1);
my $req = HTTP::Request->new(GET => $crURL);
my $response;

eval {
    local $SIG{ALRM} = sub { die "alarm\n" };
    alarm $timeout;
    print "Wait...... \n";
    $response = $ua->request($req);
    print "Wait complited \n";
    alarm 0;
};
if ($@)
{
    if ($@ eq "alarm\n")
    {
        print "WARNING: Connection Request failed\n";
    }
    else
    {
        print "WARNING: Connection Request error\n";
    }
    exit;
}


print "Завершил узнавание realm.... \n";


if ($response->is_error() && $response->code() eq '401')
{
    my $realm='';
    my $a = $response->header('Client-Peer');
    my $b = $response->header('www-authenticate');
    if ($b =~ /realm=\"([^\"]+)\"/)
    {
        $realm = $1;
    }

    $ua  = LWP::UserAgent->new(keep_alive => 1, timeout => $timeout);
    $req = HTTP::Request->new(GET => $crURL);
    $ua->credentials($a,$realm, $crUser, $crPass);

    eval {
        local $SIG{ALRM} = sub { die "alarm\n" };
        alarm $timeout;
        $response = $ua->request($req);
        alarm 0;
    };
    if ($@)
    {
        if ($@ eq "alarm\n")
        {
            print "WARNING: Connection Request failed\n";
        }
        else
        {
            print "WARNING: Connection Request error\n";
        }
        return undef;
    }

}
if ($response->is_success)
{
    print "INFO: Connection Request executed\n";
}
else
{
    print "WARNING: Connection Request failed\n";
}

