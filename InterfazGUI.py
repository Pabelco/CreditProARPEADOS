import time
import os
import wx

from wx.lib.pubsub import pub
from threading import Thread
import CreditPro as cp
wildcard = "Python source (*.xlsx)|*.xlsx|" \
           "All files (*.*)|*.*"
global lista_parametros
lista_parametros = [None, None, None, None,
                  None, None, None, None,
                  None, None, None, None,
                  None, None, None, None,
                  None, None, None, None,
                  None, None, None, None,
                  None, None, None]
global list_lista_parametros
list_lista_parametros=[]

class Mywin(wx.Frame):
    def __init__(self, parent):
        super(Mywin, self).__init__(parent, title="CreditPRO    Su perfilador de archivos", size=(1000, 400))
        #icon = wx.Icon()
        #icon.CopyFromBitmap(wx.Bitmap("ARPEADOS.jpeg", wx.BITMAP_TYPE_JPEG))
        #self.SetIcon(icon)
        self.currentDirectory = os.getcwd()
        panel = wx.Panel(self, wx.ID_ANY)
        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        hbox7 = wx.BoxSizer(wx.HORIZONTAL)
        hbox8 = wx.BoxSizer(wx.HORIZONTAL)
        hbox9 = wx.BoxSizer(wx.HORIZONTAL)
        hbox10 = wx.BoxSizer(wx.HORIZONTAL)

        l1 = wx.StaticText(panel, -1, "Tipo de Cédula:")
        l11 = wx.StaticText(panel, -1,"C:")
        l12 = wx.StaticText(panel, -1, "R:")
        l13 = wx.StaticText(panel, -1, "P:")
        l2 = wx.StaticText(panel, -1, "Tipo de Pago:")
        l21 = wx.StaticText(panel, -1, "Tarjeta:")
        l22 = wx.StaticText(panel, -1, "Banco:")
        l23 = wx.StaticText(panel, -1, "Cooperativa:")
        l3 = wx.StaticText(panel, -1, "Estado Civil:")
        l31 = wx.StaticText(panel, -1, "Casado:")
        l32 = wx.StaticText(panel, -1, "Soltero:")
        l4 = wx.StaticText(panel, -1, "Negocio propio:")
        l41 = wx.StaticText(panel, -1, "SI:")
        l42 = wx.StaticText(panel, -1, "NO:")
        l5 = wx.StaticText(panel, -1, "Ingresos:")
        l51 = wx.StaticText(panel, -1, "De 374 a 500:")
        l52 = wx.StaticText(panel, -1, "De 501 a 700:")
        l53 = wx.StaticText(panel, -1, "De 701 a 900:")
        l54 = wx.StaticText(panel, -1, "Mayor a 900:")
        l6 = wx.StaticText(panel, -1, "Sexo:")
        l61 = wx.StaticText(panel, -1, "Masculino:")
        l62 = wx.StaticText(panel, -1, "Femenino:")
        l7 = wx.StaticText(panel, -1, "Vehículo propio:")
        l71 = wx.StaticText(panel, -1, "SI:")
        l72 = wx.StaticText(panel, -1, "NO:")
        l8 = wx.StaticText(panel, -1, "Casa propia:")
        l81 = wx.StaticText(panel, -1, "SI:")
        l82 = wx.StaticText(panel, -1, "NO:")
        l9 = wx.StaticText(panel, -1, "Edad:")
        l91 = wx.StaticText(panel, -1, "De 18 a 25:")
        l92 = wx.StaticText(panel, -1, "De 26 a 30:")
        l93 = wx.StaticText(panel, -1, "De 31 a 35:")
        l94 = wx.StaticText(panel, -1, "De 36 a 40:")
        l95 = wx.StaticText(panel, -1, "Mayor a 41:")
        l10 = wx.StaticText(panel, -1, "Trabajo con R. de Dependencia:")
        l101 = wx.StaticText(panel, -1, "SI:")
        l102 = wx.StaticText(panel, -1, "NO:")

        #Parámetros de Cédula
        hbox1.Add(l1, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox1.Add(l11, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.t11 = wx.TextCtrl(panel)
        self.t12 = wx.TextCtrl(panel)
        self.t13 = wx.TextCtrl(panel)



        hbox1.Add(self.t11, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox1.Add(l12, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox1.Add(self.t12, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox1.Add(l13, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox1.Add(self.t13, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)


        self.t11.Bind(wx.EVT_TEXT, self.OnKeyTyped)
        self.t12.Bind(wx.EVT_TEXT, self.OnKeyTyped)
        self.t13.Bind(wx.EVT_TEXT, self.OnKeyTyped)
        vbox.Add(hbox1)

        #Parámetros de pago
        hbox2.Add(l2, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox2.Add(l21, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.t21 = wx.TextCtrl(panel)
        self.t22 = wx.TextCtrl(panel)
        self.t23 = wx.TextCtrl(panel)

        hbox2.Add(self.t21, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox2.Add(l22, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox2.Add(self.t22, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox2.Add(l23, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox2.Add(self.t23, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.t21.Bind(wx.EVT_TEXT, self.OnKeyTyped)
        self.t22.Bind(wx.EVT_TEXT, self.OnKeyTyped)
        self.t23.Bind(wx.EVT_TEXT, self.OnKeyTyped)

        vbox.Add(hbox2)

        # Parámetros de Esctado Civil
        hbox3.Add(l3, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox3.Add(l31, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.t31 = wx.TextCtrl(panel)
        self.t32 = wx.TextCtrl(panel)


        hbox3.Add(self.t31, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox3.Add(l32, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox3.Add(self.t32, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)


        self.t31.Bind(wx.EVT_TEXT, self.OnKeyTyped)
        self.t32.Bind(wx.EVT_TEXT, self.OnKeyTyped)

        vbox.Add(hbox3)

        #Parámetros de Relación Dependecia
        hbox4.Add(l4, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox4.Add(l41, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.t41 = wx.TextCtrl(panel)
        self.t42 = wx.TextCtrl(panel)

        hbox4.Add(self.t41, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox4.Add(l42, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox4.Add(self.t42, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.t41.Bind(wx.EVT_TEXT, self.OnKeyTyped)
        self.t42.Bind(wx.EVT_TEXT, self.OnKeyTyped)

        vbox.Add(hbox4)

        # Parámetros de Ingresos
        hbox5.Add(l5, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox5.Add(l51, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.t51 = wx.TextCtrl(panel)
        self.t52 = wx.TextCtrl(panel)
        self.t53 = wx.TextCtrl(panel)
        self.t54 = wx.TextCtrl(panel)

        hbox5.Add(self.t51, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox5.Add(l52, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox5.Add(self.t52, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox5.Add(l53, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox5.Add(self.t53, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox5.Add(l54, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox5.Add(self.t54, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.t51.Bind(wx.EVT_TEXT, self.OnKeyTyped)
        self.t52.Bind(wx.EVT_TEXT, self.OnKeyTyped)
        self.t53.Bind(wx.EVT_TEXT, self.OnKeyTyped)
        self.t54.Bind(wx.EVT_TEXT, self.OnKeyTyped)
        vbox.Add(hbox5)

        # Parámetros de Sexo
        hbox6.Add(l6, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox6.Add(l61, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.t61 = wx.TextCtrl(panel)
        self.t62 = wx.TextCtrl(panel)


        hbox6.Add(self.t61, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox6.Add(l62, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox6.Add(self.t62, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.t61.Bind(wx.EVT_TEXT, self.OnKeyTyped)
        self.t62.Bind(wx.EVT_TEXT, self.OnKeyTyped)

        vbox.Add(hbox6)

        # Parámetros de Vehiculo
        hbox7.Add(l7, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox7.Add(l71, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.t71 = wx.TextCtrl(panel)
        self.t72 = wx.TextCtrl(panel)

        hbox7.Add(self.t71, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox7.Add(l72, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox7.Add(self.t72, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.t71.Bind(wx.EVT_TEXT, self.OnKeyTyped)
        self.t72.Bind(wx.EVT_TEXT, self.OnKeyTyped)

        vbox.Add(hbox7)

        # Parámetros de Casa
        hbox8.Add(l8, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox8.Add(l81, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.t81 = wx.TextCtrl(panel)
        self.t82 = wx.TextCtrl(panel)

        hbox8.Add(self.t81, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox8.Add(l82, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox8.Add(self.t82, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.t81.Bind(wx.EVT_TEXT, self.OnKeyTyped)
        self.t82.Bind(wx.EVT_TEXT, self.OnKeyTyped)

        vbox.Add(hbox8)

        # Parámetros de Edad
        hbox9.Add(l9, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox9.Add(l91, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.t91 = wx.TextCtrl(panel)
        self.t92 = wx.TextCtrl(panel)
        self.t93 = wx.TextCtrl(panel)
        self.t94 = wx.TextCtrl(panel)
        self.t95 = wx.TextCtrl(panel)

        hbox9.Add(self.t91, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox9.Add(l92, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox9.Add(self.t92, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox9.Add(l93, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox9.Add(self.t93, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox9.Add(l94, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox9.Add(self.t94, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox9.Add(l95, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox9.Add(self.t95, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.t91.Bind(wx.EVT_TEXT, self.OnKeyTyped)
        self.t92.Bind(wx.EVT_TEXT, self.OnKeyTyped)
        self.t93.Bind(wx.EVT_TEXT, self.OnKeyTyped)
        self.t94.Bind(wx.EVT_TEXT, self.OnKeyTyped)
        self.t95.Bind(wx.EVT_TEXT, self.OnKeyTyped)
        vbox.Add(hbox9)

        # Parámetros de Sexo
        hbox10.Add(l10, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox10.Add(l101, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.t101 = wx.TextCtrl(panel)
        self.t102 = wx.TextCtrl(panel)

        hbox10.Add(self.t101, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox10.Add(l102, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        hbox10.Add(self.t102, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)

        self.t101.Bind(wx.EVT_TEXT, self.OnKeyTyped)
        self.t102.Bind(wx.EVT_TEXT, self.OnKeyTyped)

        vbox.Add(hbox10)

        hbox11 = wx.BoxSizer(wx.HORIZONTAL)
        saveParametros = wx.Button(panel, label="Guardar cambios", pos=(1,1), size=(120, 60), style=0)
        saveParametros.Bind(wx.EVT_BUTTON, self.guardarCambiosdeParametros)
        discardParametros = wx.Button(panel, label="Cancelar", pos=(1, 1), size=(120, 60), style=0)
        discardParametros.Bind(wx.EVT_BUTTON, self.cancelarCambiosdeParametros)

        hbox11.Add(saveParametros)
        hbox11.Add(discardParametros)
        vbox.Add(hbox11,1,wx.EXPAND | wx.ALIGN_CENTER | wx.ALL,5)

        panel.SetSizer(vbox)

        self.Centre()
        self.Show()
        self.Fit()


    def cancelarCambiosdeParametros(self,event):
        (print("Se canceló"))
        lista_parametros1=[None, None, None, None,
                  None, None, None, None,
                  None, None, None, None,
                  None, None, None, None,
                  None, None, None, None,
                  None, None, None, None,
                  None, None, None]
        global arre
        arre = cp.funcionPuntajes(arreglo_bruto,lista_parametros1)
        self.Close()

    def guardarCambiosdeParametros(self,event):

        print(lista_parametros)
        print(len(lista_parametros))
        list_lista_parametros.append(lista_parametros)
        global arre
        #arre = cp.funcionPuntajes(arreglo_bruto, list_lista_parametros[0])
        arre = cp.funcionPuntajes(arreglo_bruto, lista_parametros)
        self.Close()

    def OnKeyTyped(self, event):

        print(event.GetString())
        print(event.Id)

        if (event.Id == -31957):
            lista_parametros[0]=event.GetString()
        elif (event.Id == -31956):
            lista_parametros[1]=event.GetString()
        elif (event.Id == -31955):
            lista_parametros[2]=event.GetString()
        elif (event.Id == -31954):
            lista_parametros[3]=event.GetString()
        elif (event.Id == -31953):
            lista_parametros[4]=event.GetString()
        elif (event.Id == -31952):
            lista_parametros[5]=event.GetString()
        elif (event.Id == -31951):
            lista_parametros[6]=event.GetString()
        elif (event.Id == -31950):
            lista_parametros[7]=event.GetString()
        elif (event.Id == -31949):
            lista_parametros[8]=event.GetString()
        elif (event.Id == -31948):
            lista_parametros[9]=event.GetString()
        elif (event.Id == -31947):
            lista_parametros[10]=event.GetString()
        elif (event.Id == -31946):
            lista_parametros[11]=event.GetString()
        elif (event.Id == -31945):
            lista_parametros[12]=event.GetString()
        elif (event.Id == -31944):
            lista_parametros[13]=event.GetString()
        elif (event.Id == -31943):
            lista_parametros[14]=event.GetString()
        elif (event.Id == -31942):
            lista_parametros[15]=event.GetString()
        elif (event.Id == -31941):
            lista_parametros[16]=event.GetString()
        elif (event.Id == -31940):
            lista_parametros[17]=event.GetString()
        elif (event.Id == -31939):
            lista_parametros[18]=event.GetString()
        elif (event.Id == -31938):
            lista_parametros[19]=event.GetString()
        elif (event.Id == -31937):
            lista_parametros[20]=event.GetString()
        elif (event.Id == -31936):
            lista_parametros[21]=event.GetString()
        elif (event.Id == -31935):
            lista_parametros[22]=event.GetString()
        elif (event.Id == -31934):
            lista_parametros[23]=event.GetString()
        elif (event.Id == -31933):
            lista_parametros[24]=event.GetString()
        elif (event.Id == -31932):
            lista_parametros[25]=event.GetString()
        else:
            lista_parametros[26]=event.GetString()

############################################################################


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
    """
    def guardarCambiosdeParametros(self,event):

        print(lista_parametros)
        print(len(lista_parametros))
        list_lista_parametros.append(lista_parametros)
    """
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
                global arreglo_bruto
                arreglo_bruto = cp.matrizBases(nom_ar)
                global cambio_parametros
                cambio_parametros=self.onCambioParam()

                #global arre
                #arre = cp.funcionPuntajes(arreglo_bruto, lista_parametros)
                if cambio_parametros.ShowModal() == wx.ID_OK:
                    Mywin(None)
                    #global arre
                    #arre= cp.funcionPuntajes(arreglo_bruto,list_lista_parametros[0])
                else:
                    lista_cancel=[None, None, None, None,
                  None, None, None, None,
                  None, None, None, None,
                  None, None, None, None,
                  None, None, None, None,
                  None, None, None, None,
                  None, None, None]
                    global arre
                    arre= cp.funcionPuntajes(arreglo_bruto,lista_cancel)


                    #print(arr)




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
                print(arre)
                nuevopath = path+ '\\' + 'Archivo_Perfilado.xlsx'
                if os.path.exists(nuevopath):
                        cp.existsFile(arre,path)
                else:
                        cp.createFile(arre,path)
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
    def onCambioParam(self):
        """"""
        dlg = self.showMessageDlg("¿Desea Cambiar los valores para la Perfilación?", "Cambio de parámetros",
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

#Hasta que al fin


    app.MainLoop()