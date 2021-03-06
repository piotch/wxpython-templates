import wx

class Config(wx.Config):

    def __init__(self, app = None):
        app = app or 'BoardTrain2'
        wx.Config.__init__(self, app)

        self.db_path = self.Read('db_path', 'test/data/UTL5_data.mdb')
        self.bt_path = self.Read('bt_path', 'test/data/BoardTrain')
        self.list_shops = self.Read('list_shops', 'Bricklane,Battersea').split(',')
        self.default_shop = self.Read('default_shop', 'Bricklane')
        self.show_rollovers = self.ReadBool('show_rollovers', False)
        self.previewer_path = self.Read('previewer_path', '')
        self.merger5_path = self.Read('merger5_path', '')
        self.merger6_path = self.Read('merger6_path', '')


class ConfigView(wx.MiniFrame):

    def __init__(self, parent):
        wx.MiniFrame.__init__(self, parent, -1, 'Preferences', 
                style=wx.DEFAULT_FRAME_STYLE)
        
        self.SetSize((800,500))
        panel = wx.Panel(self)

        caution = """If the paths below are accessed over the network, they should always start with
        '\\\\Computer name' and never with 'Y: (or X: or Z:)\\file or folder'"""
        lbl_path_caution = wx.StaticText(panel, label = caution)
        lbl_db_path = wx.StaticText(panel, label = 'Data path')
        lbl_bt_path = wx.StaticText(panel, label = 'Board Train')
        lbl_list_shops = wx.StaticText(panel, label = 'Shops')
        lbl_default_shop = wx.StaticText(panel, label = 'Default Shop')
        lbl_show_rollovers = wx.StaticText(panel, label = 'Show Rollovers')
        lbl_previewer_path = wx.StaticText(panel, label = 'Previewer path')
        lbl_merger5_path = wx.StaticText(panel, label = 'Merger5 path')
        lbl_merger6_path = wx.StaticText(panel, label = 'Merger6 path')

        self.txt_db_path = wx.FilePickerCtrl(panel, style = wx.FLP_USE_TEXTCTRL)
        self.txt_bt_path = wx.DirPickerCtrl(panel, style = wx.DIRP_USE_TEXTCTRL)
        self.txt_list_shops = wx.TextCtrl(panel)
        self.txt_default_shop = wx.TextCtrl(panel)
        self.chk_show_rollovers = wx.CheckBox(panel)
        self.txt_previewer_path = wx.FilePickerCtrl(panel, style = wx.FLP_USE_TEXTCTRL)
        self.txt_merger5_path = wx.FilePickerCtrl(panel, style = wx.FLP_USE_TEXTCTRL)
        self.txt_merger6_path = wx.FilePickerCtrl(panel, style = wx.FLP_USE_TEXTCTRL)

        self.btn_save = wx.Button(panel, label = 'Save and Quit')

        sizer = wx.GridBagSizer(10, 2)
        sizer.AddGrowableCol(1)

        flag_lbl = wx.TOP|wx.LEFT|wx.BOTTOM|wx.ALIGN_RIGHT
        flag_txt = wx.TOP|wx.LEFT|wx.BOTTOM|wx.EXPAND
        
        sizer.Add(lbl_path_caution, pos = (0,1), flag=wx.TOP|wx.LEFT, border=5)
        sizer.Add(lbl_db_path, pos = (1,0), flag= flag_lbl, border=5)
        sizer.Add(self.txt_db_path, pos = (1,1), flag= flag_txt, border=5)
        sizer.Add(lbl_bt_path, pos = (2,0), flag= flag_lbl, border=5)
        sizer.Add(self.txt_bt_path, pos = (2,1), flag= flag_txt, border=5)
        sizer.Add(lbl_list_shops, pos = (3,0), flag= flag_lbl, border=5)
        sizer.Add(self.txt_list_shops, pos = (3,1), flag= flag_txt, border=5)
        sizer.Add(lbl_default_shop, pos = (4,0), flag= flag_lbl, border=5)
        sizer.Add(self.txt_default_shop, pos = (4,1), flag= flag_txt, border=5)
        sizer.Add(lbl_show_rollovers, pos = (5,0), flag= flag_lbl, border=5)
        sizer.Add(self.chk_show_rollovers, pos = (5,1), flag= flag_txt, border=5)
        sizer.Add(wx.StaticText(panel, label = "Local paths"), pos = (6,1), 
                flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        sizer.Add(lbl_previewer_path, pos = (7,0), flag=flag_lbl, border=5)
        sizer.Add(self.txt_previewer_path, pos = (7,1), flag= flag_txt, border=5)
        sizer.Add(lbl_merger5_path, pos = (8,0), flag=flag_lbl, border=5)
        sizer.Add(self.txt_merger5_path, pos = (8,1), flag= flag_txt, border=5)
        sizer.Add(lbl_merger6_path, pos = (9,0), flag= flag_lbl, border=5)
        sizer.Add(self.txt_merger6_path, pos = (9,1), flag= flag_txt, border=5)

        sizer.Add(self.btn_save, pos = (10,1),
                flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)

        panel.SetSizer(sizer)


class ConfigPresenter(ConfigView):

    def __init__(self, parent):
        ConfigView.__init__(self, parent)
        self.parent = parent # destroyed on save and quit

        self.btn_save.Bind(wx.EVT_BUTTON, self.save)

        self.display()

    def display(self):
        self.txt_db_path.SetPath(settings.db_path)
        self.txt_bt_path.SetPath(settings.bt_path)
        self.txt_list_shops.SetValue(','.join(settings.list_shops)) 
        self.txt_default_shop.SetValue(settings.default_shop) 
        self.chk_show_rollovers.SetValue(settings.show_rollovers) 
        self.txt_previewer_path.SetPath(settings.previewer_path)
        self.txt_merger5_path.SetPath(settings.merger5_path)
        self.txt_merger6_path.SetPath(settings.merger6_path)

    def save(self, evt):
        settings.Write('db_path', self.txt_db_path.GetPath())
        settings.Write('bt_path', self.txt_bt_path.GetPath())
        settings.Write('list_shops', self.txt_list_shops.GetValue())
        settings.Write('default_shop', self.txt_default_shop.GetValue())
        settings.WriteBool('show_rollovers', self.chk_show_rollovers.GetValue())
        settings.Write('previewer_path', self.txt_previewer_path.GetPath())
        settings.Write('merger5_path', self.txt_merger5_path.GetPath())
        settings.Write('merger6_path', self.txt_merger6_path.GetPath())

        self.Destroy()
        try:
            self.parent.Destroy()
        except:
            pass


class TestApp(wx.App):
    def OnInit(self):
        frame = ConfigPresenter(None)
        frame.Show(True)
        return True


if __name__ == '__main__':
    settings = Config('utlsettings-test')
    app = TestApp(False)
    app.MainLoop()
else:
    settings = Config()
