<?php

// Init the Custom Configs
require_once 'configs.php';

// Custom Configs Overrides
// Put here some configs to override, this is useful if different configs are needed in a page with multiple different forms
// Example: $configs['recaptcha_enabled'] = false;

// Form fields array
// Here there are all the form fields ordered. One field for each line. You can simply add/edit one or more lines to make this definition equal to the html form code.
$fields = array();
$fields[] = array('name' => 'files',		'display_name' => 'Upload file',    'type' => 'file',        'required' => true);
$fields[] = array('name' => 'email',		'display_name' => 'Email',          'type' => 'email',       'required' => true,			'is_user_email' => true);
$fields[] = array('name' => 'message',		'display_name' => 'Message',        'type' => 'textarea',    'required' => true);

// Init the functions
require_once 'functions.php';

// Custom Overrides before processing request
function beforeProcessing()
{
	global $lang;
	
	// Put here some language messages to override, this is useful if you need different messages only for this form
	// Example: $lang->emails_info->subject = "New subject for this form";
}

// Start processing
require_once 'process-upload.php';

?>
