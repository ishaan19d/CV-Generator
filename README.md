You will need to install <strong>wkhtmltopdf</strong> and then and then add its path in environment variable.
<br>
Also in 'pdf/views.py' in this line
<br>
->config=pdfkit.configuration(wkhtmltopdf=r'<i>path</i>')
<br>
Add the path of wkhtmltopdf
