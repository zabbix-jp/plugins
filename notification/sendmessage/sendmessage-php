#!/usr/bin/php

<?php

/*
** This program is sendmail script with ISO-2022-JP for ZABBIX.
**
** Auther: Kodai Terashima
** 
** Copyright (C) 2005-2009 ZABBIX-JP 
** This program is licenced under the GPL
**/

$MAIL_FROM   = "zabbix@localhost";

mb_language('Japanese');
mb_internal_encoding('UTF-8');

$MAIL_TO      = $argv[1];
$MAIL_SUBJECT = $argv[2];
$MAIL_MESSAGE = $argv[3];

$MAIL_HEADER  = 'MIME-Version: 1.0' . "\r\n";
$MAIL_HEADER .= 'Content-Type: text/plain; charset="iso-2022-jp"' . "\r\n";
$MAIL_HEADER .= 'Content-Transfer-Encoding: 7bit' . "\r\n";
$MAIL_HEADER .= 'Date: ' . date('r') . "\r\n";
$MAIL_HEADER .= 'X-Mailer: PHP/' . phpversion() . "\r\n";
$MAIL_HEADER .= 'From: ' . $MAIL_FROM . "\r\n";

$MAIL_SUBJECT = mb_convert_encoding($MAIL_SUBJECT,"ISO-2022-JP","UTF-8");
$MAIL_MESSAGE = mb_convert_encoding($MAIL_MESSAGE,"ISO-2022-JP","UTF-8");

$MAIL_SUBJECT = '=?ISO-2022-JP?B?' . base64_encode($MAIL_SUBJECT) . '?=';

mail($MAIL_TO, $MAIL_SUBJECT, $MAIL_MESSAGE, $MAIL_HEADER);

?>
