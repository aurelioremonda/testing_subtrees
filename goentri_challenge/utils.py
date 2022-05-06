
def login(page, user, password):
    print(f"Login in...")

    # Click input[name="usernameOrEmail"]
    page.locator("input[name=\"usernameOrEmail\"]").click()

    # Fill input[name="usernameOrEmail"]
    page.locator("input[name=\"usernameOrEmail\"]").fill(user)

    # Click text=Email Address or UsernamePasswordBy continuing, you agree to our Terms of Servic >> button
    page.locator("text=Email Address or UsernamePasswordBy continuing, you agree to our Terms of Servic >> button").click()

    # Click input[name="password"]
    page.locator("input[name=\"password\"]").click()

    # Fill input[name="password"]
    page.locator("input[name=\"password\"]").fill(password)

    # Click button:has-text("Log In")
    page.locator("button:has-text(\"Log In\")").click()

    page.wait_for_url("https://wordpress.com/home/*")

def settings(page):
    print(f"Switching to settings...")

    # Click span:has-text("Settings")
    page.locator("span:has-text(\"Settings\") >> nth=1").click()

    page.wait_for_load_state("networkidle")


def getSiteInfo(page):
    print(f"Getting site's info...")
    blogname = page.input_value("input[name=\"blogname\"]")
    print(f"Blogname: {blogname}")

    blogdescription = page.input_value("input[name=\"blogdescription\"]")
    print(f"Tagline: {blogdescription}")

    blogaddress = page.input_value("input[name=\"blogaddress\"]")
    print(f"Domain: {blogaddress}")