class Locators:

    #Home page objects
    log_reg_button = "//div[@class='top-links']//a[contains(text(),'|')]"
    log_reg_field_username = "//input[@id='username']"
    log_reg_field_password = "//input[@id='password']"
    log_reg_login_button = "//input[@name='login']"

    #MyAccountPage objects
    log_field_username = "//p[@class='woocommerce-form-row woocommerce-form-row--wide form-row form-row-wide']//input[@id='username']"
    log_field_password = "//p[@class='woocommerce-form-row woocommerce-form-row--wide form-row form-row-wide']//input[@id='password']"
    reg_field_email = "//input[@id='reg_email']"
    reg_field_password = "//input[@id='reg_password']"
    login_button = "//button[@name='login']"
    register_button = "//button[@name='register']"
    logout_from_profile = "//div[@class='top-links']//li[@class='logout-link lastItem']//a"
    logout_link = "//p[1]//a[1]"
    back_previous_page = "//a[@class='back-history']"
    begin_link = "//div[@id='breadcrumb']//a"