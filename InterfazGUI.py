import time
import os
import wx
import xlrd
from wx.lib.pubsub import pub
from threading import Thread
import CreditPro as cp
wildcard = "Python source (*.xlsx)|*.xlsx|" \
           "All files (*.*)|*.*"
#global arreglo_perfilado

class TestThread(Thread):
    """Test Worker Thread Class."""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.start()  # start the thread

    # ----------------------------------------------------------------------
    def run(self):
        """Run Worker Thread."""
        # This is the code executing in the new thread.
        for i in range(20):
            time.sleep(1)
            wx.CallAfter(pub.sendMessage, "update", msg="")



########################################################################
class PrimerVentana(wx.Frame):

    # ----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,
                          "CreditPRO    Su perfilador de archivos")
        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap("ARPEADOS.jpeg", wx.BITMAP_TYPE_JPEG))
        self.SetIcon(icon)

        panel = wx.Panel(self, wx.ID_ANY)
        panel.SetBackgroundColour("#c9faff")

        self.currentDirectory = os.getcwd()
        # create the buttons and bindings

        global saveFileDlgBtn
        saveFileDlgBtn = wx.Button(panel, label="Guardar Archivo Perfilado", pos=(0, 0), size=(175, 60), style=0)

        openFileDlgBtn = wx.Button(panel, label="Seleccionar archivo(s) .xlsx", pos=(0, 0), size=(175, 60), style=0)
        saveFileDlgBtn.Disable()

        openFileDlgBtn.Bind(wx.EVT_BUTTON, self.onOpenFile)
        saveFileDlgBtn.Bind(wx.EVT_BUTTON, self.onSaveFile)

        # put the buttons in a sizer

        sizer = wx.GridSizer(1,0,0)
        sizer.Add(openFileDlgBtn, 0, wx.ALIGN_CENTRE, 5)
        sizer.Add(saveFileDlgBtn, 0, wx.ALIGN_CENTRE, 5)
        panel.SetSizer(sizer)
    # ----------------------------------------------------------------------
    def onOpenFile(self, event):
        """
        Create and show the Open FileDialog
        """
        dlg = wx.FileDialog(
            self, message="Seleccione los archivo(s) a perfilar",
            defaultDir=self.currentDirectory,
            defaultFile="",
            wildcard=wildcard,
            style=wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR
        )
        if dlg.ShowModal() == wx.ID_OK:
            global arreglo_perfilado
            paths = dlg.GetPaths()
            #print(paths)
            print()
            print(
            "Seleccionó los siguientes archivo(s)")
            progress = self.onQuestion()
            nom_ar=[]
            if progress.ShowModal() == wx.ID_OK:
                for path in paths:
                    nom_xlsx= path.split("\\")
                    archivo = nom_xlsx[-1]
                    nom_ar.append(archivo)
                    print(
                    path)
                print(nom_ar)
                btn = event.GetEventObject()
                btn.Disable()
                saveFileDlgBtn.Enable()
                arreglo_bruto=cp.matrizBases(nom_ar)
                arreglo_perfilado=cp.funcionPuntajes(arreglo_bruto)
                print(arreglo_perfilado)
                return paths



        dlg.Destroy()

    # ----------------------------------------------------------------------
    def onSaveFile(self, event):
        """
        Create and show the Save FileDialog
        """
        dlg = wx.DirDialog(self, "Choose a directory:",
                       style=wx.DD_DEFAULT_STYLE
                       #| wx.DD_DIR_MUST_EXIST
                       #| wx.DD_CHANGE_DIR
                       )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            #print(path)
            print()
            print(
            "You chose the following filename: %s" % path)
            finalizar = self.onInfo(path)
            if finalizar.ShowModal() == wx.ID_OK:
                cp.existsFile(arreglo_perfilado,path)
                self.Close()
            return path

        dlg.Destroy()

    # ----------------------------------------------------------------------
    def onInfo(self,path):
        """
        This method is fired when its corresponding button is pressed
        """
        dlg =self.showMessageDlg("Ha guardado el archivo perfilado en el siguiente directorio:"+path,
                            "Éxito", wx.OK | wx.ICON_INFORMATION)
        return dlg
    # ----------------------------------------------------------------------
    def onQuestion(self):
        """"""
        dlg = self.showMessageDlg("¿Desea Perfilar los archivos seleccionados?", "Validación",
                            wx.OK | wx.CANCEL | wx.ICON_QUESTION)
        return dlg
    # ----------------------------------------------------------------------
    def showMessageDlg(self, msg, title, style):
        """"""
        dlg = wx.MessageDialog(parent=None, message=msg,
                               caption=title, style=style)
        return dlg
        dlg.ShowModal()
        dlg.Destroy()



#Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame1 = PrimerVentana()
    frame1.Show()



    app.MainLoop()