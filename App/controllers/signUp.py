from App.database import db

def signupAction():
  form = SignUp() 
  if form.validate_on_submit():
    data = request.form 
    newuser = User(username=data['username'], email=data['email']) 
    newuser.set_password(data['password']) 
    db.session.add(newuser) 
    db.session.commit()
    flash('Account Created!')
    return redirect(url_for('index'))
  flash('Error invalid input!')
  return redirect(url_for('signup')) 
  