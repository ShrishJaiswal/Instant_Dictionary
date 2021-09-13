import justpy as jp
from justpy import tailwind
from pandas.core.dtypes.common import classes
from webapp import layout
from webapp import page

class Home(page.Page):
    path="/"
    @classmethod

    def serve(cls, req):
        wp=jp.QuasarPage(tailwind=True)

        lay=layout.DefaultLayout(a=wp,view="hHh lpR fFf")
        container=jp.QPageContainer(a=lay)

        div=jp.Div(a=container, classes="bg-gray-200 h-screen p-2")
        jp.Div(a=div, text="This is the Home page", classes="text-4xl m-2")
        jp.Div(a=div, text="""
        njdncsdncwnvwndvwnjvnwdkjvnwnvwkjnvkjnkjvnwkjnvwkjdn
        dvjdnvjkwdnvjwnvjnwjkvnwsdjkvnwjkdnvwkjnvjwnvjnwnv
        dvbwbvdwbvjwdnvweuwvnwjdbvuwenjwnvjknwdjkvnwdvn""", classes="text-lg")
        return wp