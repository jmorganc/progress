<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
    <meta content="text/html; charset=utf-8" http-equiv="content-type"/>
    <title>Progress</title>
    <link href="/static/style.css" rel="stylesheet" />
    <script src="/static/jquery-1.11.1.min.js"></script>
</head>
<body>
    <h1>0.00000%</h1>
    <div id="progress_bar_bg">
        <div id="progress_bar"></div>
    </div>

    <script>
        var pct_cur = $('h1').text();
        console.log(pct_cur);

        get_percent();
        setInterval(function() {
            get_percent();
        }, 1000);

        function get_percent() {
            $.ajax({
                url: '/get/percent',
                cache: false
            })
            .done(function(pct) {
                $('h1').text(pct + '%');
                $('#progress_bar').css('width', pct + '%');
                console.log(pct);
            });
        }
    </script>
</body>
</html>