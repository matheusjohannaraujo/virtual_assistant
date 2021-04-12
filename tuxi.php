<?php

$command = "wsl tuxi -r -q " . base64_decode($argv[1]);
die(base64_encode(trim(shell_exec($command))));

?>
