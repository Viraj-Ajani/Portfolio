function sendMail(params){
    var tempParams ={
        from_name: document.getElementById("from_name").value,
        your_email: document.getElementById("your_email").value,
        subject: document.getElementById("subject").value,
        message:document.getElementById("message").value
    };

    emailjs.send('service_rr2doak','template_lu9fem1',tempParams)
    .then(function(res){
        console.log("success",res.status)
    })
}