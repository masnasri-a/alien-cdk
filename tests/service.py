from alien_dev_cdk.service import Service

app = Service()

app.set_method('GET')
app.set_path('/hello')
app.set_handler_file('handler.py')
app.cors_allow_origins(['*'])
