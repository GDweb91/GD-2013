<?php

if($_POST) {
    $your_name = "";
    $email = "";
    $email_title = "";
    $url = "";  //$concerned_department = "";
    $message = "";
    $email_body = "<div>";
      
    if(isset($_POST['your_name'])) {
        $your_name = filter_var($_POST['your_name'], FILTER_SANITIZE_STRING);
        $email_body .= "<div>
                           <label><b>Visitor Name:</b></label>&nbsp;<span>".$your_name."</span>
                        </div>";
    }
 
    if(isset($_POST['email'])) {
        $email = str_replace(array("\r", "\n", "%0a", "%0d"), '', $_POST['email']);
        $email = filter_var($email, FILTER_VALIDATE_EMAIL);
        $email_body .= "<div>
                           <label><b>Visitor Email:</b></label>&nbsp;<span>".$email."</span>
                        </div>";
    }
      
    if(isset($_POST['email_title'])) {
        $email_title = filter_var($_POST['email_title'], FILTER_SANITIZE_STRING);
        $email_body .= "<div>
                           <label><b>Reason For Contacting Us:</b></label>&nbsp;<span>".$email_title."</span>
                        </div>";
    }
      
    if(isset($_POST['url'])) {
        $url = filter_var($_POST['url'], FILTER_SANITIZE_URL);
        $email_body .= "<div>
                           <label><b>Your Site Url:</b></label>&nbsp;<span>".$url."</span>
                        </div>";
    }
      
    if(isset($_POST['message'])) {
        $message = htmlspecialchars($_POST['message']);
        $email_body .= "<div>
                           <label><b>Visitor Message:</b></label>
                           <div>".$message."</div>
                        </div>";
    }
      
    // if($concerned_department == "billing") {
    //     $recipient = "billing@domain.com";
    // }
    // else if($concerned_department == "marketing") {
    //     $recipient = "marketing@domain.com";
    // }
    // else if($concerned_department == "technical support") {
    //     $recipient = "tech.support@domain.com";
    // }
    // else {
    //     $recipient = "contact@domain.com";
    // }
      
    $email_body .= "</div>";
 
    $headers  = 'MIME-Version: 1.0' . "\r\n"
    .'Content-type: text/html; charset=utf-8' . "\r\n"
    .'From: ' . $email . "\r\n";
      
    if(mail($recipient, $email_title, $email_body, $headers)) {
        echo "<p>Thank you for contacting us, $your_name. You will get a reply within 24 hours.</p>";
    } else {
        echo '<p>We are sorry but the email did not go through.</p>';
    }
      
} else {
    echo '<p>Something went wrong</p>';
}