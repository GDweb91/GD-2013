<?php
   //google reCaptcha API key settings
   $secretKey='6Lc0K4IgAAAAABSzJPRFX4QnJ3SEuu2998rcqe5u';

   //Email settings
   $recipientEmail = 'gddomain.77@gmail.com';

   //Assign default values
   $postData = $valErr = $statusMsg = '';
   $status = 'error';

   //If form is submited
   if(isset($_POST['submit_gd_form'])) {
    //Get submitted form data
    $postData = $_POST;
    $name = trim($_POST['gdname']);
    $email = trim($_POST['gdemail']);
    $url = trim($_POST['gdurl']);
    $subject = trim($_POST['gdsubject']);
    $message = trim($_POST['gdmessage']);


    //Validate input fileds
    if(empty($name)){
        $valErr .= 'Please enter your name.<br/>';

    }
    if(empty($email) || filter_var($email, FILTER_VALIDATE_EMAIL) === false) {
        $valErr .= 'Please enter a valid email address. <br/>';

    }
    if(empty($url)){
        $valErr .= 'Please enter you website address. <br/>';

    }
    if(empty($subject)){
        $valErr .= 'Please enter a subject <br/>';
    }
    if(empty($message)){
        $valErr .= 'Please enter your questions or message <br/>';
    }
    //Check whether submited input  data is valid
    if(empty($valErr)) {
        //Validate reCAPTCHA response
        if(isset($_POST['g-recaptcha-response']) && !empty($_POST['g-recaptcha-response'])){
            //Google reCAPTCHA verification API request
            $api_url = 'https://www.google.com/recaptcha/api/siteverify';
            $reqs_data = array(
                'secret' => $secretKey,
                'reponse' => $_POST['g-recaptcha-response'],
                'remoteip' => $_SERVER['REMOTE_ADDR']
            );
            $curlConfig = array(
                CURLOPT_URL => $api_url,
                CURLOPT_POST => true,
                CURLOPT_RETURNTRANSFER => true,
                CURLOPT_POSTFIELDS => $reqs_data
            );
            $ch = curl_init();
            curl_setopt_array($ch, $curlCongfig);
            $response = curl_exec($ch);
            curl_close($ch);

            //Decode JSON data of API response in array
            $responseData = json_decode($response);

            //If reCAPTCHA API response is valid
            if($responseData->success){
                //Send email notification to the site admin
                $to = $recipientEmail;
                $subject = 'New Contact Request Submitted';
                $htmlContent = "
                <h4>Contact request details</h4>
                <p><b>Name: </b>".$name."</p>
                <p><b>Email: </b> ".$email."</p>
                <p><b>Url: </b>".$url."</p>
                <p><b>Subject: </b>".$subject."</p>
                <p><b>Message: </b>".$message."</p>
                ";
                //Always set content-type when sending HTML email
                $headers = "MIME-Version: 1.0" . "\r\n";
                $headers = "Content-type: text/html;charset=UTF-8" . "\r\n";
                //Sender info header
                $headers .= 'From:' .$name.'<'.$email. '>' . "\r\n";

                //Send email
                mail($to, $subject, $htmlContent, $headers);
                $status = 'Success';
                $statusMsg = 'Thank you! Your request has been submitted succesfully.';
                $postData = '';
            }else{
                $statusMsg = 'The reCAPTCHA verification failed, please try again.';
            }

        }else{
                $statusMsg = 'Something went wront, please try again.';
            }
    }else{
       $valErr = !empty($valErr)? '<br/>'.trim($valErr, '<br/>'): '';
       $statusMsg = 'Please fill all the mandatory fields:'.$valErr;
    }


   }
?>