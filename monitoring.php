<?php

$charge  = shell_exec('cat /proc/loadavg | awk \'{print $1}\'');

$nbproc = shell_exec('cat /proc/cpuinfo | grep processor | wc -l');
$percent = 0;
if((float)$charge != 0.00){
        $percent = $charge / $nbproc * 100;
}

$charge = trim($charge);
$data =array(
         'charge'=> $charge,
         'percent'=>$percent,
        );

$json = json_encode($data);
header('Content-Type: application/json');
echo $json;
