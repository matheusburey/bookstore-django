def make_call(user):
    timezone = pytz.timezone("America/Sao_Paulo")
    now = datetime.datetime.now(tz=timezone)
    weekday = now.today().weekday()
    # rd titular cpf
    titular = Usuario.objects.get(cpf="87094551088")

    if (user.titular and titular == user.titular) and (
        weekday >= 5 or (now.hour >= 20 or now.hour <= 7)
    ):
        # bruno phone
        make_twilio_call("+5511942472373", "https://app.kompa.com.br/adm/call-twilio")


def make_twilio_call(phone, url):
    twilio.client.calls.create(url=url, to=phone, from_=twilio.TWILIO_PHONE)
