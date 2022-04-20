
@app.route('/signup', methods=['GET'])
def signup():
  form = SignUp() # create form object
  return render_template('signup.html', form=form) # pass form object to template


@app.route('/signup', methods=['POST'])
def singUp():
    return signupAction()