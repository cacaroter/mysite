import os
from django.core.mail import EmailMultiAlternatives


os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

# if __name__ == '__main__':
#     send_mail(
#         '来自Tim的测试邮件',
#         'Hello world！',
#         'luoting1125@126.com',
#         ['28007255@qq.com'],
#     )

if __name__ == '__main__':

    subject,from_email,to = '来自Tim的测试邮件','luoting1125@126.com','28007255@qq.com'
    text_content = 'hello world! this is a txt version'
    html_content = '<p>欢迎访问<a href="http://http://127.0.0.1:8000/login/" target=blank>http://127.0.0.1:8000/login</a>，' \
                   'this is a html version！</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    print('send done!')
