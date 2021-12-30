"""
My real site below this line

<!doctype html>
<html class="no-js" lang="">

<head>
  <meta charset="utf-8">
  <title>Bit Quoin</title>
  <meta name="description" content="">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  {% load static %}
  <link rel="stylesheet" href="{% static 'styles.css'%}">
</head>

<body>



  <!-- Background image will occupy full screen -->
  <div class="background_image">
    <!--img class="main_image_background" src="images/background.jpg"-->
  </div>

  <!-- Header menu will sit on top, and hide all of background image -->
  <div class="nav">
    <a class="nav_link topnav_menu" href="#home">Home</a>
    <a class="nav_link topnav_menu" href="#news">News</a>
    <a class="nav_link topnav_menu" href="#contact">Contact</a>
    <a class="nav_link topnav_menu" href="#about">About</a>
  </div>

  <!-- Page welcome will occupy 2/3rds of left side of screen, and test will be centered -->
  <div class="page_welcome">
    <h1 class="page_welcome__title">Consolidated Service Facility</h1>
    <h3 class="page_welcome__message">Running and knocking on all of your neighbors doors</h3>
  </div>

  <!-- Login forms will sit on top of background image, and occupy 1/3rd on the right side of the screen -->
  <div class="login_forms silver-background">

    <div class="login_forms__header">
        <h1 class="login-foms__header__title">Create an Account</h1>
        <h3 class="login-foms__header__signIn">Already have an account? <a class="text_link textLinks" href="a link to signIn page">Sign In</a></h3>

        <button class="login-foms__header__google" type="button" id="google">Google</button>
        <button class="login-foms__header__linkedIn" type="button" id="linkedIn">LinkedIn</button>

        <h3 class="login-foms__header__alternative_signIn">or create with</h3>
      </div>

    <div class="login__forms__section">
      <div class="login_forms__section__unit">
        <h3 class="login-foms__section__unit__title">Email</h3>
        <input class="login_forms__section__unit__text" type="text=" placeholder="Enter Email" required>
      </div>

    <div class="login_forms__section__unit">
      <h3 class="login-foms__section__unit__title">Username</h3>
      <input class="login_forms__section__unit__text" type="text=" placeholder="Enter Username" required>
    </div>

    <div class="login_forms__section__unit">
      <h3 class="login-foms__section__unit__title">Password</h3>
      <input class="login_forms__section__unit__text" type="text=" placeholder="Enter Password" required>
    </div>

    <div class="login_forms__section__unit">
      <h3 class="login-foms__section__unit__title">Repeat Password</h3>
      <input class="login_forms__section__unit__text" type="text=" placeholder="Repeat Password" required>
      </div>
    </div>

    <div class="login_forms__security_check">
      <h3 class="login-foms__security_check__header">Security Challenge</h3>
      <button class="login-foms__security_check__m_captionia" type="button" id="mcaptionia">mCAPTIONIA</button>
    </div></br>

    <button class="login-foms__createAccount" type="button" id="createAccount">Create Account</button>

    <footer class="login_forms__footer">
    <h6 class="login-forms__footer__waiver">By creating an account you agree to BitQuoion's
      <a class="text_link textLinks" href="http://www.bitquoin.net" target="_blank" title="terms">Terms & Conditions</a> and
      <a class="text_link textLinks" href="http://www.bitquoin.net" target="_blank" title="terms">Privacy Policy</a>
    </h6>
  </footer>

  </div>

  <!-- Footer menu will sit on bottom, and hide all of background image -->
  <div class="footer">
    <footer class="footer__menu">
      <div class="footer_menu__navigation" style="width: 1200px; text-align: right">
        <a class="text_link footer__menu__bna_link" href="www.bitquoin.net" target="_blank" title="fly_nashville">Fly Nashville</a>
        <h6 class="footer__menu__copyright">Bit Quoin 2021 &copy; Copyright</h6>
      </div>
    </footer>
  </div>
</body>

</html>

"""