def main():
    from selenium import webdriver
    import argparse
    import time
    import os

    # Setup argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("tex_name", type=str, help="The name of your tex file - e.g. `science.tex` or just `science` - it should be located in the same folder as the compiled PDF and should have the same name as this PDF")
    parser.add_argument("--PATH", type=str, default="C:/Program Files (x86)/chromedriver.exe", help="The path to your selenium webdriver")
    parser.add_argument("--TBR", type=float, default=2, help="VSTAR detects changes to the `.tex` file and then subsequently refreshes the pdf after a given amount of time (it takes a little time to compile) - note: TBF = Time Before Refresh")
    args = parser.parse_args()

    pdf_name = tex_name = args.tex_name
    PATH = args.PATH

    # Making it a little more user friendly
    if ".tex" == tex_name[-4:]:
        pdf_name = tex_name = tex_name[:-4]
    pdf_name = f"{pdf_name}.pdf"
    tex_name = f"./{tex_name}.tex"

    # The absolute path
    pdf_path = os.path.abspath(pdf_name)

    # Disable selenium logging (to ignore annoying bluetooth error message)
    options = webdriver.ChromeOptions() 
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    # Initialize driver
    driver = webdriver.Chrome(options=options, executable_path=PATH)

    # Go to PDF path
    driver.get(pdf_path)
    print(f"--- Driver initialized at {pdf_path} ---")
    time.sleep(0.5)

    with open(tex_name, "r") as f:
        data = former_data = f.read()
    f.close()

    # The refresher
    while True:
        with open(tex_name, "r") as f:
            data = f.read()
        f.close()

        while not pdf_name in driver.current_url and len(driver.window_handles) >= 2:
            driver.switch_to.window(driver.window_handles[1])

        if data != former_data and pdf_name in driver.current_url:
            time.sleep(args.TBR)
            driver.refresh()

        former_data = data

if __name__ == "__main__":
    main()




