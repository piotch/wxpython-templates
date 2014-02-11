import wx
from wx.lib.pubsub import setupkwargs
from wx.lib.pubsub import pub


class Config(wx.Config):

    def __init__(self):
        wx.Config.__init__(self, 'BoardTrain2')

        self.db_path = self.Read('db_path', 'data/UTL5_data.mdb')
        self.bt_path = self.Read('bt_path', 
                'C:/Users/Admin/Documents/utl/BoardTrain2/test')
        self.list_shops = self.Read('list_shops', 'Bricklane,Battersea').split(',')
        self.default_shop = self.Read('default_shop', 'Bricklane')
        self.show_rollovers = self.ReadBool('show_rollovers', False)
        self.previewer_path = self.Read('previewer_path', '')
        self.merger5_path = self.Read('merger5_path', '')
        self.merger6_path = self.Read('merger6_path', '')


class ConfigEditor(wx.MiniFrame):

    def __init__(self, parent):
        wx.MiniFrame.__init__(self, parent, -1,
                'Preferences', style=wx.DEFAULT_FRAME_STYLE)
        
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

        self.txt_db_path = wx.TextCtrl(panel, style = wx.TE_READONLY)
        self.txt_bt_path = wx.TextCtrl(panel, style = wx.TE_READONLY)
        self.txt_list_shops = wx.TextCtrl(panel)
        self.txt_default_shop = wx.TextCtrl(panel)
        self.chk_show_rollovers = wx.CheckBox(panel)
        self.txt_previewer_path = wx.TextCtrl(panel, style = wx.TE_READONLY)
        self.txt_merger5_path = wx.TextCtrl(panel, style = wx.TE_READONLY)
        self.txt_merger6_path = wx.TextCtrl(panel, style = wx.TE_READONLY)

        self.btn_browse_db = wx.Button(panel, label = 'Choose...')
        self.btn_browse_bt = wx.Button(panel, label = 'Choose...')
        self.btn_browse_pre = wx.Button(panel, label = 'Choose...')
        self.btn_browse_m5= wx.Button(panel, label = 'Choose...')
        self.btn_browse_m6 = wx.Button(panel, label = 'Choose...')
        self.btn_save = wx.Button(panel, label = 'Save and Quit')

        sizer = wx.GridBagSizer(10, 3)
        sizer.AddGrowableCol(1)
        
        sizer.Add(lbl_path_caution,
                pos = (0,1),
                flag=wx.TOP|wx.LEFT, border=5)
        sizer.Add(lbl_db_path,
                pos = (1,0),
                flag=wx.TOP|wx.LEFT|wx.BOTTOM|wx.ALIGN_RIGHT, border=5)
        sizer.Add(self.txt_db_path,
                pos = (1,1),
                flag=wx.TOP|wx.LEFT|wx.BOTTOM|wx.EXPAND, border=5)
        sizer.Add(self.btn_browse_db,
                pos = (1,2),
                flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        sizer.Add(lbl_bt_path,
                pos = (2,0),
                flag=wx.TOP|wx.LEFT|wx.BOTTOM|wx.ALIGN_RIGHT, border=5)
        sizer.Add(self.txt_bt_path,
                pos = (2,1),
                flag=wx.TOP|wx.LEFT|wx.BOTTOM|wx.EXPAND, border=5)
        sizer.Add(self.btn_browse_bt,
                pos = (2,2),
                flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        sizer.Add(lbl_list_shops,
                pos = (3,0),
                flag=wx.TOP|wx.LEFT|wx.BOTTOM|wx.ALIGN_RIGHT, border=5)
        sizer.Add(self.txt_list_shops,
                pos = (3,1),
                flag=wx.TOP|wx.LEFT|wx.BOTTOM|wx.EXPAND, border=5)
        sizer.Add(lbl_default_shop,
                pos = (4,0),
                flag=wx.TOP|wx.LEFT|wx.BOTTOM|wx.ALIGN_RIGHT, border=5)
        sizer.Add(self.txt_default_shop,
                pos = (4,1),
                flag=wx.TOP|wx.LEFT|wx.BOTTOM|wx.EXPAND, border=5)
        sizer.Add(lbl_show_rollovers,
                pos = (5,0),
                flag=wx.TOP|wx.LEFT|wx.BOTTOM|wx.ALIGN_RIGHT, border=5)
        sizer.Add(self.chk_show_rollovers,
                pos = (5,1),
                flag=wx.TOP|wx.LEFT|wx.BOTTOM|wx.EXPAND, border=5)
        sizer.Add(wx.StaticText(panel, label = "Local paths"),
                pos = (6,1),
                flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        sizer.Add(lbl_previewer_path,
                pos = (7,0),
                flag=wx.TOP|wx.LEFT|wx.BOTTOM|wx.ALIGN_RIGHT, border=5)
        sizer.Add(self.txt_previewer_path,
                pos = (7,1),
                flag=wx.TOP|wx.LEFT|wx.BOTTOM|wx.EXPAND, border=5)
        sizer.Add(self.btn_browse_pre,
                pos = (7,2),
                flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        sizer.Add(lbl_merger5_path,
                pos = (8,0),
                flag=wx.TOP|wx.LEFT|wx.BOTTOM|wx.ALIGN_RIGHT|wx.ALIGN_RIGHT, border=5)
        sizer.Add(self.txt_merger5_path,
                pos = (8,1),
                flag=wx.TOP|wx.LEFT|wx.BOTTOM|wx.EXPAND, border=5)
        sizer.Add(self.btn_browse_m5,
                pos = (8,2),
                flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        sizer.Add(lbl_merger6_path,
                pos = (9,0),
                flag=wx.TOP|wx.LEFT|wx.BOTTOM|wx.ALIGN_RIGHT, border=5)
        sizer.Add(self.txt_merger6_path,
                pos = (9,1),
                flag=wx.TOP|wx.LEFT|wx.BOTTOM|wx.EXPAND, border=5)
        sizer.Add(self.btn_browse_m6,
                pos = (9,2),
                flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)

        sizer.Add(self.btn_save,
                pos = (10,1),
                flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)

        panel.SetSizer(sizer)


class ConfigPresenter(ConfigEditor):

    def __init__(self, parent):
        ConfigEditor.__init__(self, parent)
        self.parent = parent

        self.btn_browse_db.Bind(wx.EVT_BUTTON, self.browse_db)
        self.btn_browse_bt.Bind(wx.EVT_BUTTON, self.browse_bt)
        self.btn_browse_pre.Bind(wx.EVT_BUTTON, self.browse_pre)
        self.btn_browse_m5.Bind(wx.EVT_BUTTON, self.browse_m5)
        self.btn_browse_m6.Bind(wx.EVT_BUTTON, self.browse_m6)
        self.btn_save.Bind(wx.EVT_BUTTON, self.save)
 
        self.txt_db_path.SetValue(config.db_path)
        self.txt_bt_path.SetValue(config.bt_path)
        self.txt_list_shops.SetValue(','.join(config.list_shops)) 
        self.txt_default_shop.SetValue(config.default_shop) 
        self.chk_show_rollovers.SetValue(config.show_rollovers) 
        self.txt_previewer_path.SetValue(config.previewer_path)
        self.txt_merger5_path.SetValue(config.merger5_path)
        self.txt_merger6_path.SetValue(config.merger6_path)

    def browse_db(self, evt):
        dialog = wx.FileDialog(None, 
                message = 'Data', style = wx.OPEN) 
        if dialog.ShowModal() == wx.ID_OK:
            new_path = dialog.GetPath()
            self.txt_db_path.SetLabel(new_path)

    def browse_pre(self, evt):
        dialog = wx.FileDialog(None, 
                message = 'Previewer.exe', style = wx.OPEN) 
        if dialog.ShowModal() == wx.ID_OK:
            new_path = dialog.GetPath()
            self.txt_previewer_path.SetLabel(new_path)

    def browse_m5(self, evt):
        dialog = wx.FileDialog(None, 
                message = 'Merger5 .exe file', style = wx.OPEN) 
        if dialog.ShowModal() == wx.ID_OK:
            new_path = dialog.GetPath()
            self.txt_merger5_path.SetLabel(new_path)

    def browse_m6(self, evt):
        dialog = wx.FileDialog(None, 
                message = 'Merger6 .exe file', style = wx.OPEN) 
        if dialog.ShowModal() == wx.ID_OK:
            new_path = dialog.GetPath()
            self.txt_merger6_path.SetLabel(new_path)

    def browse_bt(self, evt):
        dialog = wx.DirDialog(None, 
                message = 'Board Train Folder', style = wx.OPEN) 
        if dialog.ShowModal() == wx.ID_OK:
            new_path = dialog.GetPath()
            self.txt_bt_path.SetLabel(new_path)

    def save(self, evt):
        config.Write('db_path', self.txt_db_path.GetValue())
        config.Write('bt_path', self.txt_bt_path.GetValue())
        config.Write('list_shops', self.txt_list_shops.GetValue())
        config.Write('default_shop', self.txt_default_shop.GetValue())
        config.WriteBool('show_rollovers', self.chk_show_rollovers.GetValue())
        config.Write('previewer_path', self.txt_previewer_path.GetValue())
        config.Write('merger5_path', self.txt_merger5_path.GetValue())
        config.Write('merger6_path', self.txt_merger6_path.GetValue())

        self.Destroy()
        self.parent.Destroy()


class App(wx.App):
    def OnInit(self):
        frame = ConfigPresenter(None)
        frame.Show(True)
        return True


if __name__ == '__main__':
    config = Config()
    app = App(False)
    app.MainLoop()
