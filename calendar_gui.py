"""
WxPython based GUI for calendar
"""
import wx
import wx.html2

class MyBrowser(wx.Dialog):
    """
    WxPython Browser Class
    """
    def __init__(self, *args, **kwds):
        wx.Dialog.__init__(self, *args, **kwds)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.browser = wx.html2.WebView.New(self)
        sizer.Add(self.browser, 1, wx.EXPAND, 10)
        self.SetSizer(sizer)
        self.SetSize((700, 700))

if __name__ == '__main__':
    APP = wx.App()
    DIALOG = MyBrowser(None, -1)
    # dialog.browser.LoadURL("calendarApp.html")
    DIALOG.browser.SetPage(open("calendarApp.html").read(), "")
    DIALOG.Show()
    APP.MainLoop()
