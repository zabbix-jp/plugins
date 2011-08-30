#!/usr/bin/php
<?php

/*
** This program is sendmail script with ISO-2022-JP for ZABBIX.
**
** Auther: Takanori Suzuki
** 
** Copyright (C) 2005-2011 ZABBIX-JP 
** This program is licenced under the GPL
**/

mb_language("japanese");
mb_internal_encoding("JIS");
require("phpmailer/class.phpmailer.php");


/* setting */
$MAIL_FROM      = "zabbix@localhost";
$MAIL_FROMNAME  = "Zabbix 障害通知";
// sample: using gmail smtp
// $MAIL_SMTP_HOST = 'ssl://smtp.gmail.com:465';
// sample: using smtp
// $MAIL_SMTP_HOST = 'smtp.example.com:25';
$MAIL_SMTP_HOST = 'smtp.example.com:25';
$MAIL_SMTP_USER = 'XXXXXXXX';
$MAIL_SMTP_PASS = 'XXXXXXXX';
/* setting */


$MAIL_TO      = $argv[1];
$MAIL_SUBJECT = $argv[2];
$MAIL_MESSAGE = $argv[3];

class PHPMailer_JP extends PHPMailer {
	public $CharSet           = "iso-2022-jp";
	public $Encoding          = '7bit';
}

$mailer = new PHPMailer_JP();
$mailer->IsSMTP();

$mailer->Host = $MAIL_SMTP_HOST;
$mailer->SMTPAuth = true;
$mailer->Username = $MAIL_SMTP_USER;
$mailer->Password = $MAIL_SMTP_PASS;

$mailer->From     = $MAIL_FROM;
$mailer->AddAddress($MAIL_TO);

$mailer->FromName = mb_encode_mimeheader(mb_convert_encoding($MAIL_FROMNAME,"JIS","UTF-8"),"JIS");
$mailer->Subject  = mb_encode_mimeheader(mb_convert_encoding($MAIL_SUBJECT,"JIS","UTF-8"),"JIS");
$mailer->Body     = mb_convert_encoding($MAIL_MESSAGE,"JIS","UTF-8");
// $mailer->AddReplyTo($email, $from);
 
if(!$mailer->Send()){
   print "failed: " . $mailer->ErrorInfo . "\n";
}else{
   print "success" . "\n";
}
?>
