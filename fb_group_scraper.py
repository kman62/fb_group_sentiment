import requests
from bs4 import BeautifulSoup
import streamlit as st
import os

# The following function is assumed to be provided
def google_sheets_add_row(sheets_url, sheet_name, data):
    pass

def get_facebook_group_posts(group_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    }

    response = requests.get(group_url, headers=headers)

    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    posts = soup.find_all("div", class_="_5pcr userContentWrapper")

    post_texts = []

    for post in posts:
        post_text = post.find("div", class_="userContent").text.strip()
        post_texts.append(post_text)

    return post_texts

def main():
    st.title("Facebook Group Posts to Google Sheets")

    group_url = st.text_input("Enter the Facebook Group URL:")

    if group_url:
        posts = get_facebook_group_posts(group_url)

        if posts:
            st.write("Posts found:")
            for post in posts:
                st.write(post)

            sheets_url = "https://docs.google.com/spreadsheets/d/1Atszy9fGR6WYxMsTodoWzDLZviQKb54zb0fzfmE773g/edit#gid=1780586757"
            sheet_name = "Sheet1"

            for post in posts:
                google_sheets_add_row(sheets_url, sheet_name, [post])

            st.write("Posts have been added to Google Sheets.")
        else:
            st.write("No posts found.")

if __name__ == "__main__":
    main()

