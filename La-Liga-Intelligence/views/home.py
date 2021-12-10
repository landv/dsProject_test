import inspect
import os
import sys
import webbrowser
from pathlib import Path
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from graphics.main import *
from reports.pontuacao import criarPDF_pont
from reports.gols import criarPDF_gols
from controllers.atualizarCSV import updateEquipe
from models.times import getDados

p = Path(os.getcwd())


class App:
    def __init__(self, root, posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv):
        logo = PhotoImage(file=str(p) + "\\assets\\img\\logo.png")
        lbl1 = Label(root, image=logo, bg="#FFFFFF")
        lbl1.place(x=30, y=30)

        self.tv = ttk.Treeview(root, columns=(
        "posicao", "time", "pontos", "partidas", "vitorias", "empates", "derrotas", "golsPro", "golsContra", "saldo",
        "ca", "cv"), show="headings", height=20)
        self.tv.column("posicao", minwidth=0, width=50)
        self.tv.column("time", minwidth=0, width=150)
        self.tv.column("pontos", minwidth=0, width=50)
        self.tv.column("partidas", minwidth=0, width=100)
        self.tv.column("vitorias", minwidth=0, width=70)
        self.tv.column("empates", minwidth=0, width=70)
        self.tv.column("derrotas", minwidth=0, width=70)
        self.tv.column("golsPro", minwidth=0, width=70)
        self.tv.column("golsContra", minwidth=0, width=70)
        self.tv.column("saldo", minwidth=0, width=70)
        self.tv.column("ca", minwidth=0, width=70)
        self.tv.column("cv", minwidth=0, width=70)
        self.tv.heading("posicao", text="Posição")
        self.tv.heading("time", text="Time")
        self.tv.heading("pontos", text="Pontos")
        self.tv.heading("partidas", text="Partidas Jogadas")
        self.tv.heading("vitorias", text="Vitórias")
        self.tv.heading("empates", text="Empates")
        self.tv.heading("derrotas", text="Derrotas")
        self.tv.heading("golsPro", text="Gols Pró")
        self.tv.heading("golsContra", text="Gols Sofridos")
        self.tv.heading("saldo", text="Saldo de Gols")
        self.tv.heading("ca", text="CA")
        self.tv.heading("cv", text="CV")
        self.tv.bind('<ButtonRelease-1>', self.selectItem)
        self.tv.grid(column=0, row=4, columnspan=3, padx=30, pady=120)

        for i in posicao:
            self.tv.insert("", "end", values=(
            str(posicao[i - 1]), nome[i - 1], str(pontos[i - 1]), str(partidas[i - 1]), str(vitorias[i - 1]),
            str(empates[i - 1]), str(derrotas[i - 1]),
            str(gp[i - 1]), str(gc[i - 1]), str(saldo[i - 1]), str(ca[i - 1]), str(cv[i - 1])))

        framePontuacao = LabelFrame(root, text="Gráficos da Pontuação", padx=10, pady=10, font="Helvetica 16 bold",
                                    bg="#FFFFFF")
        framePontuacao.place(x=30, y=575, width=915)

        btn2 = Button(framePontuacao, text="Barras", command=lambda: self.call("pt_ba",
                                                                               posicao, nome, pontos, partidas,
                                                                               vitorias, empates, derrotas, gp, gc,
                                                                               saldo, ca, cv))
        btn2.pack(side="left", padx=10, pady=10)

        btn3 = Button(framePontuacao, text="Pizza", command=lambda: self.call("pt_pi",
                                                                              posicao, nome, pontos, partidas, vitorias,
                                                                              empates, derrotas, gp, gc, saldo, ca, cv))
        btn3.pack(side="left", padx=10, pady=10)

        btn4 = Button(framePontuacao, text="Histograma", command=lambda: self.call("pt_hi",
                                                                                   posicao, nome, pontos, partidas,
                                                                                   vitorias, empates, derrotas, gp, gc,
                                                                                   saldo, ca, cv))
        btn4.pack(side="left", padx=10, pady=10)

        btn4 = Button(framePontuacao, text="Plot", command=lambda: self.call("pt_pl",
                                                                             posicao, nome, pontos, partidas, vitorias,
                                                                             empates, derrotas, gp, gc, saldo, ca, cv))
        btn4.pack(side="left", padx=10, pady=10)

        btn5 = Button(framePontuacao, text="ScatterPlot", command=lambda: self.call("pt_sp",
                                                                                    posicao, nome, pontos, partidas,
                                                                                    vitorias, empates, derrotas, gp, gc,
                                                                                    saldo, ca, cv))
        btn5.pack(side="left", padx=10, pady=10)

        btn6 = Button(framePontuacao, text="Pontuação-Gols Pró", command=lambda: self.call("pt_gp",
                                                                                           posicao, nome, pontos,
                                                                                           partidas, vitorias, empates,
                                                                                           derrotas, gp, gc, saldo, ca,
                                                                                           cv))
        btn6.pack(side="left", padx=10, pady=10)

        btn6 = Button(framePontuacao, text="Relação Pontuação-Gols Contra", command=lambda: self.call("pt_gc",
                                                                                                      posicao, nome,
                                                                                                      pontos, partidas,
                                                                                                      vitorias, empates,
                                                                                                      derrotas, gp, gc,
                                                                                                      saldo, ca, cv))
        btn6.pack(side="left", padx=10, pady=10)

        btn7 = Button(framePontuacao, text="Relação Pontuação-Saldo", command=lambda: self.call("pt_sl",
                                                                                                posicao, nome, pontos,
                                                                                                partidas, vitorias,
                                                                                                empates, derrotas, gp,
                                                                                                gc, saldo, ca, cv))
        btn7.pack(side="left", padx=10, pady=10)

        frameGols = LabelFrame(root, text="Gráficos dos Gols", padx=10, pady=10, font="Helvetica 16 bold", bg="#FFFFFF")
        frameGols.place(x=30, y=700, width=915, height=150)

        btn7 = Button(frameGols, text="Relação de Gols", command=lambda: self.call("gp_gc",
                                                                                   posicao, nome, pontos, partidas,
                                                                                   vitorias, empates, derrotas, gp, gc,
                                                                                   saldo, ca, cv))
        btn7.place(x=10, y=10)

        btn8 = Button(frameGols, text="Barras (Gols Pró)", command=lambda: self.call("gp_ba",
                                                                                     posicao, nome, pontos, partidas,
                                                                                     vitorias, empates, derrotas, gp,
                                                                                     gc, saldo, ca, cv))
        btn8.place(x=120, y=10)

        btn9 = Button(frameGols, text="Barras (Gols Sofridos)", command=lambda: self.call("gs_ba",
                                                                                          posicao, nome, pontos,
                                                                                          partidas, vitorias, empates,
                                                                                          derrotas, gp, gc, saldo, ca,
                                                                                          cv))
        btn9.place(x=230, y=10)

        btn10 = Button(frameGols, text="Pizza (Gols Pró)", command=lambda: self.call("gp_pi",
                                                                                     posicao, nome, pontos, partidas,
                                                                                     vitorias, empates, derrotas, gp,
                                                                                     gc, saldo, ca, cv))
        btn10.place(x=365, y=10)

        btn11 = Button(frameGols, text="Pizza (Gols Sofridos)", command=lambda: self.call("gs_pi",
                                                                                          posicao, nome, pontos,
                                                                                          partidas, vitorias, empates,
                                                                                          derrotas, gp, gc, saldo, ca,
                                                                                          cv))
        btn11.place(x=470, y=10)

        btn12 = Button(frameGols, text="Histograma (Gols Pró)", command=lambda: self.call("gp_hi",
                                                                                          posicao, nome, pontos,
                                                                                          partidas, vitorias, empates,
                                                                                          derrotas, gp, gc, saldo, ca,
                                                                                          cv))
        btn12.place(x=600, y=10)

        btn13 = Button(frameGols, text="Histograma (Gols Sofridos)", command=lambda: self.call("gc_hi",
                                                                                               posicao, nome, pontos,
                                                                                               partidas, vitorias,
                                                                                               empates, derrotas, gp,
                                                                                               gc, saldo, ca, cv))
        btn13.place(x=10, y=50)

        btn14 = Button(frameGols, text="Plot (Gols Pró)", command=lambda: self.call("gp_pl",
                                                                                    posicao, nome, pontos, partidas,
                                                                                    vitorias, empates, derrotas, gp, gc,
                                                                                    saldo, ca, cv))
        btn14.place(x=750, y=10)

        btn15 = Button(frameGols, text="Plot (Gols Sofridos)", command=lambda: self.call("gc_pl",
                                                                                         posicao, nome, pontos,
                                                                                         partidas, vitorias, empates,
                                                                                         derrotas, gp, gc, saldo, ca,
                                                                                         cv))
        btn15.place(x=180, y=50)

        btn16 = Button(frameGols, text="ScatterPlot (Gols Pró)", command=lambda: self.call("gp_sp",
                                                                                           posicao, nome, pontos,
                                                                                           partidas, vitorias, empates,
                                                                                           derrotas, gp, gc, saldo, ca,
                                                                                           cv))
        btn16.place(x=300, y=50)

        btn17 = Button(frameGols, text="ScatterPlot (Gols Sofridos)", command=lambda: self.call("gc_sp",
                                                                                                posicao, nome, pontos,
                                                                                                partidas, vitorias,
                                                                                                empates, derrotas, gp,
                                                                                                gc, saldo, ca, cv))
        btn17.place(x=430, y=50)

        btn18 = Button(frameGols, text="Relação Gols Pró - Gols Sofridos", command=lambda: self.call("r_gpc",
                                                                                                     posicao, nome,
                                                                                                     pontos, partidas,
                                                                                                     vitorias, empates,
                                                                                                     derrotas, gp, gc,
                                                                                                     saldo, ca, cv))
        btn18.place(x=595, y=50)

        frameResultados = LabelFrame(root, text="Gráficos das Vitórias, Empates e Derrotas", padx=10, pady=10,
                                     font="Helvetica 16 bold", bg="#FFFFFF")
        frameResultados.place(x=30, y=875, width=915, height=150)

        btn19 = Button(frameResultados, text="Relação de Resultados", command=lambda: self.call("re_ba",
                                                                                                posicao, nome, pontos,
                                                                                                partidas, vitorias,
                                                                                                empates, derrotas, gp,
                                                                                                gc, saldo, ca, cv))
        btn19.place(x=10, y=10)

        btn20 = Button(frameResultados, text="Barras (Vitórias)", command=lambda: self.call("vi_ba",
                                                                                            posicao, nome, pontos,
                                                                                            partidas, vitorias, empates,
                                                                                            derrotas, gp, gc, saldo, ca,
                                                                                            cv))
        btn20.place(x=143, y=10)

        btn21 = Button(frameResultados, text="Barras (Derrotas)", command=lambda: self.call("de_ba",
                                                                                            posicao, nome, pontos,
                                                                                            partidas, vitorias, empates,
                                                                                            derrotas, gp, gc, saldo, ca,
                                                                                            cv))
        btn21.place(x=241, y=10)

        btn22 = Button(frameResultados, text="Barras (Empates)", command=lambda: self.call("em_ba",
                                                                                           posicao, nome, pontos,
                                                                                           partidas, vitorias, empates,
                                                                                           derrotas, gp, gc, saldo, ca,
                                                                                           cv))
        btn22.place(x=344, y=10)

        btn23 = Button(frameResultados, text="Pizza (Vitórias)", command=lambda: self.call("vi_pi",
                                                                                           posicao, nome, pontos,
                                                                                           partidas, vitorias, empates,
                                                                                           derrotas, gp, gc, saldo, ca,
                                                                                           cv))
        btn23.place(x=447, y=10)

        btn24 = Button(frameResultados, text="Pizza (Derrotas)", command=lambda: self.call("de_pi",
                                                                                           posicao, nome, pontos,
                                                                                           partidas, vitorias, empates,
                                                                                           derrotas, gp, gc, saldo, ca,
                                                                                           cv))
        btn24.place(x=535, y=10)

        btn25 = Button(frameResultados, text="Pizza (Empates)", command=lambda: self.call("em_pi",
                                                                                          posicao, nome, pontos,
                                                                                          partidas, vitorias, empates,
                                                                                          derrotas, gp, gc, saldo, ca,
                                                                                          cv))
        btn25.place(x=630, y=10)

        btn26 = Button(frameResultados, text="Plot (Vitórias)", command=lambda: self.call("vi_pl",
                                                                                          posicao, nome, pontos,
                                                                                          partidas, vitorias, empates,
                                                                                          derrotas, gp, gc, saldo, ca,
                                                                                          cv))
        btn26.place(x=725, y=10)

        btn27 = Button(frameResultados, text="Plot (Derrotas)", command=lambda: self.call("de_pl",
                                                                                          posicao, nome, pontos,
                                                                                          partidas, vitorias, empates,
                                                                                          derrotas, gp, gc, saldo, ca,
                                                                                          cv))
        btn27.place(x=810, y=10)

        btn28 = Button(frameResultados, text="Plot (Empates)", command=lambda: self.call("em_pl",
                                                                                         posicao, nome, pontos,
                                                                                         partidas, vitorias, empates,
                                                                                         derrotas, gp, gc, saldo, ca,
                                                                                         cv))
        btn28.place(x=10, y=50)

        btn29 = Button(frameResultados, text="Histograma (Vitórias)", command=lambda: self.call("vi_hi",
                                                                                                posicao, nome, pontos,
                                                                                                partidas, vitorias,
                                                                                                empates, derrotas, gp,
                                                                                                gc, saldo, ca, cv))
        btn29.place(x=110, y=50)

        btn30 = Button(frameResultados, text="Histograma (Derrotas)", command=lambda: self.call("de_hi",
                                                                                                posicao, nome, pontos,
                                                                                                partidas, vitorias,
                                                                                                empates, derrotas, gp,
                                                                                                gc, saldo, ca, cv))
        btn30.place(x=240, y=50)

        btn31 = Button(frameResultados, text="Histograma (Empates)", command=lambda: self.call("em_hi",
                                                                                               posicao, nome, pontos,
                                                                                               partidas, vitorias,
                                                                                               empates, derrotas, gp,
                                                                                               gc, saldo, ca, cv))
        btn31.place(x=375, y=50)

        btn32 = Button(frameResultados, text="ScatterPlot (Vitórias)", command=lambda: self.call("vi_sp",
                                                                                                 posicao, nome, pontos,
                                                                                                 partidas, vitorias,
                                                                                                 empates, derrotas, gp,
                                                                                                 gc, saldo, ca, cv))
        btn32.place(x=510, y=50)

        btn33 = Button(frameResultados, text="ScatterPlot (Derrotas)", command=lambda: self.call("de_sp",
                                                                                                 posicao, nome, pontos,
                                                                                                 partidas, vitorias,
                                                                                                 empates, derrotas, gp,
                                                                                                 gc, saldo, ca, cv))
        btn33.place(x=640, y=50)

        btn34 = Button(frameResultados, text="ScatterPlot (Empates)", command=lambda: self.call("em_sp",
                                                                                                posicao, nome, pontos,
                                                                                                partidas, vitorias,
                                                                                                empates, derrotas, gp,
                                                                                                gc, saldo, ca, cv))
        btn34.place(x=772, y=50)

        frameEdit = LabelFrame(root, text="Editar a Tabela", padx=10, pady=10, font="Helvetica 16 bold", bg="#FFFFFF")
        frameEdit.place(x=980, y=108, width=905, height=440)

        lbl8 = Label(frameEdit, text="Time", bg="#FFFFFF")
        lbl8.place(x=10, y=10)

        self.vequipe = StringVar()
        select = ttk.Combobox(frameEdit, values=nome, textvariable=self.vequipe)
        select.set("Equipe")
        select.place(x=10, y=35)

        lbl9 = Label(frameEdit, text="Pontos", bg="#FFFFFF")
        lbl9.place(x=10, y=80)

        self.vpontos = StringVar()
        en1 = Entry(frameEdit, width=10, textvariable=self.vpontos)
        en1.place(x=10, y=105)

        lbl10 = Label(frameEdit, text="Partidas", bg="#FFFFFF")
        lbl10.place(x=10, y=150)

        self.vpartidas = StringVar()
        en2 = Entry(frameEdit, width=10, textvariable=self.vpartidas)
        en2.place(x=10, y=175)

        lbl11 = Label(frameEdit, text="Vitórias", bg="#FFFFFF")
        lbl11.place(x=10, y=220)

        self.vvitorias = StringVar()
        en3 = Entry(frameEdit, width=10, textvariable=self.vvitorias)
        en3.place(x=10, y=245)

        lbl12 = Label(frameEdit, text="Empates", bg="#FFFFFF")
        lbl12.place(x=10, y=290)

        self.vempates = StringVar()
        en4 = Entry(frameEdit, width=10, textvariable=self.vempates)
        en4.place(x=10, y=315)

        lbl13 = Label(frameEdit, text="Derrotas", bg="#FFFFFF")
        lbl13.place(x=240, y=10)

        self.vderrotas = StringVar()
        en5 = Entry(frameEdit, width=10, textvariable=self.vderrotas)
        en5.place(x=240, y=35)

        lbl14 = Label(frameEdit, text="Gols Pró", bg="#FFFFFF")
        lbl14.place(x=240, y=80)

        self.vgp = StringVar()
        en6 = Entry(frameEdit, width=10, textvariable=self.vgp)
        en6.place(x=240, y=105)

        lbl15 = Label(frameEdit, text="Gols Sofridos", bg="#FFFFFF")
        lbl15.place(x=240, y=150)

        self.vgc = StringVar()
        en7 = Entry(frameEdit, width=10, textvariable=self.vgc)
        en7.place(x=240, y=175)

        lbl16 = Label(frameEdit, text="Cartões Amarelos", bg="#FFFFFF")
        lbl16.place(x=240, y=220)

        self.vca = StringVar()
        en8 = Entry(frameEdit, width=10, textvariable=self.vca)
        en8.place(x=240, y=245)

        lbl17 = Label(frameEdit, text="Cartões Vermelhos", bg="#FFFFFF")
        lbl17.place(x=240, y=290)

        self.vcv = StringVar()
        en9 = Entry(frameEdit, width=10, textvariable=self.vcv)
        en9.place(x=240, y=315)

        btn45 = Button(frameEdit, text="Atualizar os Dados",
                       command=lambda: self.updateDate(self.vequipe.get(), self.vpontos.get(), self.vpartidas.get(),
                                                       self.vvitorias.get(), self.vempates.get(), self.vderrotas.get(),
                                                       self.vgp.get(), self.vgc.get(), self.vca.get(), self.vcv.get()))
        btn45.place(x=470, y=300)

        lbl18 = Label(frameEdit, text="Para manter a confiabilidade dos dados é necessário que você", bg="#FFFFFF")
        lbl19 = Label(frameEdit, text="esteja ciente das regras da La Liga e do sistema de pontuação.", bg="#FFFFFF")
        lbl18.place(x=510, y=10)
        lbl19.place(x=510, y=27)

        frameCartoes = LabelFrame(root, text="Gráficos dos Cartões", padx=10, pady=10, font="Helvetica 16 bold",
                                  bg="#FFFFFF")
        frameCartoes.place(x=980, y=575, width=905, height=150)

        btn35 = Button(frameCartoes, text="Relação de Cartões", command=lambda: self.call("ca_cv",
                                                                                          posicao, nome, pontos,
                                                                                          partidas, vitorias, empates,
                                                                                          derrotas, gp, gc, saldo, ca,
                                                                                          cv))
        btn35.place(x=10, y=10)

        btn36 = Button(frameCartoes, text="Barra (Cartões Amarelos)", command=lambda: self.call("ca_ba",
                                                                                                posicao, nome, pontos,
                                                                                                partidas, vitorias,
                                                                                                empates, derrotas, gp,
                                                                                                gc, saldo, ca, cv))
        btn36.place(x=125, y=10)

        btn37 = Button(frameCartoes, text="Barra (Cartões Vermelhos)", command=lambda: self.call("cv_ba",
                                                                                                 posicao, nome, pontos,
                                                                                                 partidas, vitorias,
                                                                                                 empates, derrotas, gp,
                                                                                                 gc, saldo, ca, cv))
        btn37.place(x=270, y=10)

        btn37 = Button(frameCartoes, text="Pizza (Cartões Amarelos)", command=lambda: self.call("ca_pi",
                                                                                                posicao, nome, pontos,
                                                                                                partidas, vitorias,
                                                                                                empates, derrotas, gp,
                                                                                                gc, saldo, ca, cv))
        btn37.place(x=420, y=10)

        btn37 = Button(frameCartoes, text="Pizza (Cartões Vermelhos)", command=lambda: self.call("cv_pi",
                                                                                                 posicao, nome, pontos,
                                                                                                 partidas, vitorias,
                                                                                                 empates, derrotas, gp,
                                                                                                 gc, saldo, ca, cv))
        btn37.place(x=562, y=10)

        btn38 = Button(frameCartoes, text="Histograma (Cartões Amarelos)", command=lambda: self.call("ca_hi",
                                                                                                     posicao, nome,
                                                                                                     pontos, partidas,
                                                                                                     vitorias, empates,
                                                                                                     derrotas, gp, gc,
                                                                                                     saldo, ca, cv))
        btn38.place(x=712, y=10)

        btn39 = Button(frameCartoes, text="Histograma (Cartões Vermelhos)", command=lambda: self.call("cv_hi",
                                                                                                      posicao, nome,
                                                                                                      pontos, partidas,
                                                                                                      vitorias, empates,
                                                                                                      derrotas, gp, gc,
                                                                                                      saldo, ca, cv))
        btn39.place(x=10, y=50)

        btn40 = Button(frameCartoes, text="Plot (Cartões Amarelos)", command=lambda: self.call("ca_pl",
                                                                                               posicao, nome, pontos,
                                                                                               partidas, vitorias,
                                                                                               empates, derrotas, gp,
                                                                                               gc, saldo, ca, cv))
        btn40.place(x=205, y=50)

        btn41 = Button(frameCartoes, text="Plot (Cartões Vermelhos)", command=lambda: self.call("cv_pl",
                                                                                                posicao, nome, pontos,
                                                                                                partidas, vitorias,
                                                                                                empates, derrotas, gp,
                                                                                                gc, saldo, ca, cv))
        btn41.place(x=355, y=50)

        btn42 = Button(frameCartoes, text="ScatterPlot (Cartões Amarelos)", command=lambda: self.call("ca_sp",
                                                                                                      posicao, nome,
                                                                                                      pontos, partidas,
                                                                                                      vitorias, empates,
                                                                                                      derrotas, gp, gc,
                                                                                                      saldo, ca, cv))
        btn42.place(x=515, y=50)

        btn43 = Button(frameCartoes, text="ScatterPlot (Cartões Vermelhos)", command=lambda: self.call("cv_sp",
                                                                                                       posicao, nome,
                                                                                                       pontos, partidas,
                                                                                                       vitorias,
                                                                                                       empates,
                                                                                                       derrotas, gp, gc,
                                                                                                       saldo, ca, cv))
        btn43.place(x=700, y=50)

        framePDF = LabelFrame(root, text="Criar Relatórios PDF", padx=10, pady=10, font="Helvetica 16 bold",
                              bg="#FFFFFF")
        framePDF.place(x=980, y=755, width=905)

        btn44 = Button(framePDF, text="Relatório de Pontuação", command=lambda: self.call("pdf_pont",
                                                                                          posicao, nome, pontos,
                                                                                          partidas, vitorias, empates,
                                                                                          derrotas, gp, gc, saldo, ca,
                                                                                          cv))
        btn44.pack(side="left", padx=10, pady=10)

        btn44 = Button(framePDF, text="Relatório de Gols", command=lambda: self.call("pdf_gols",
                                                                                     posicao, nome, pontos, partidas,
                                                                                     vitorias, empates, derrotas, gp,
                                                                                     gc, saldo, ca, cv))
        btn44.pack(side="left", padx=10, pady=10)

        frameSobre = LabelFrame(root, text="Sobre", padx=10, pady=10, font="Helvetica 16 bold", bg="#FFFFFF")
        frameSobre.place(x=980, y=875, width=905, height=150)

        lbl2 = Label(frameSobre, text="Desenvolvedor:", bg="#FFFFFF", font="Helvetica 13 bold")
        lbl2.place(x=15, y=5)

        lbl3 = Label(frameSobre, text="Leonardo Vasconcelos Paulino", bg="#FFFFFF", font="Helvetica 13")
        lbl3.place(x=145, y=5)

        lbl4 = Label(frameSobre, text="GitHub:", bg="#FFFFFF", font="Helvetica 13 bold")
        lbl4.place(x=15, y=35)

        lbl5 = Button(frameSobre, text="Acessar GitHub do desenvolvedor", cursor="hand2",
                      command=lambda: webbrowser.open('https://github.com/leovasc5/'))
        lbl5.place(x=90, y=35)

        lbl6 = Label(frameSobre, text="Código:", bg="#FFFFFF", font="Helvetica 13 bold")
        lbl6.place(x=15, y=65)

        lbl7 = Button(frameSobre, text="Acessar Repositório", cursor="hand2",
                      command=lambda: webbrowser.open('https://github.com/leovasc5/La-Liga-Intelligence'))
        lbl7.place(x=90, y=65)

        root.mainloop()

    def call(self, modo, posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv):
        pt_ba(nome, pontos) if modo == "pt_ba" else None
        pt_pi(nome, pontos) if modo == "pt_pi" else None
        pt_hi(pontos) if modo == "pt_hi" else None
        pt_pl(nome, pontos) if modo == "pt_pl" else None
        pt_sp(nome, pontos) if modo == "pt_sp" else None
        pt_gp(pontos, gp) if modo == "pt_gp" else None
        pt_gc(pontos, gc) if modo == "pt_gc" else None
        pt_sl(pontos, saldo) if modo == "pt_sl" else None
        gp_gc(gp, gc, nome) if modo == "gp_gc" else None
        gp_ba(nome, gp) if modo == "gp_ba" else None
        gs_ba(nome, gc) if modo == "gs_ba" else None
        gp_pi(nome, gp) if modo == "gp_pi" else None
        gs_pi(nome, gc) if modo == "gs_pi" else None
        gp_hi(gp) if modo == "gp_hi" else None
        gc_hi(gc) if modo == "gc_hi" else None
        gp_pl(nome, gp) if modo == "gp_pl" else None
        gc_pl(nome, gc) if modo == "gc_pl" else None
        gp_sp(nome, gp) if modo == "gp_sp" else None
        gc_sp(nome, gc) if modo == "gc_sp" else None
        r_gpc(nome, gp, gc) if modo == "r_gpc" else None
        re_ba(nome, vitorias, empates, derrotas) if modo == "re_ba" else None
        vi_ba(nome, vitorias) if modo == "vi_ba" else None
        de_ba(nome, derrotas) if modo == "de_ba" else None
        em_ba(nome, empates) if modo == "em_ba" else None
        vi_pi(nome, vitorias) if modo == "vi_pi" else None
        de_pi(nome, derrotas) if modo == "de_pi" else None
        em_pi(nome, empates) if modo == "em_pi" else None
        vi_pl(nome, vitorias) if modo == "vi_pl" else None
        de_pl(nome, derrotas) if modo == "de_pl" else None
        em_pl(nome, empates) if modo == "em_pl" else None
        vi_hi(vitorias) if modo == "vi_hi" else None
        de_hi(derrotas) if modo == "de_hi" else None
        em_hi(empates) if modo == "em_hi" else None
        vi_sp(nome, vitorias) if modo == "vi_sp" else None
        de_sp(nome, derrotas) if modo == "de_sp" else None
        em_sp(nome, empates) if modo == "em_sp" else None
        ca_cv(nome, ca, cv) if modo == "ca_cv" else None
        ca_ba(nome, ca) if modo == "ca_ba" else None
        cv_ba(nome, cv) if modo == "cv_ba" else None
        ca_pi(nome, ca) if modo == "ca_pi" else None
        cv_pi(nome, cv) if modo == "cv_pi" else None
        ca_hi(ca) if modo == "ca_hi" else None
        cv_hi(cv) if modo == "cv_hi" else None
        ca_pl(nome, ca) if modo == "ca_pl" else None
        cv_pl(nome, cv) if modo == "cv_pl" else None
        ca_sp(nome, ca) if modo == "ca_sp" else None
        cv_sp(nome, cv) if modo == "cv_sp" else None
        criarPDF_pont() if modo == "pdf_pont" else None
        criarPDF_gols() if modo == "pdf_gols" else None

    def updateDate(self, equipe, pontos, partidas, vitorias, empates, derrotas, gp, gc, ca, cv):
        if equipe == "Equipe":
            return self.escape("error", "Não foi selecionada nenhuma equipe!")
        try:
            partidas = int(partidas)
            pontos = int(pontos)
            vitorias = int(vitorias)
            empates = int(empates)
            derrotas = int(derrotas)
            gp = int(gp)
            gc = int(gc)
            ca = int(ca)
            cv = int(cv)
        except:
            return self.escape("error", "É preciso que os valores sejam números inteiros!")

        if partidas > 38:
            return self.escape("error", "Não é possível que o time dispute mais de 38 partidas!")

        if (
                partidas or vitorias or empates or derrotas or gp or gc or ca or cv) < 0:  # Exceto pontos por conta da possibilidade de punições
            return self.escape("error", "Não é possível aceitar números negativos!")

        updateEquipe(equipe, pontos, partidas, vitorias, empates, derrotas, gp, gc, ca, cv)
        self.sincronizar()
        self.vca.set(""), self.vcv.set(""), self.vderrotas.set(""), self.vempates.set(""), self.vvitorias.set(
            ""), self.vgp.set("")
        self.vgc.set(""), self.vequipe.set(""), self.vpartidas.set(""), self.vpontos.set("")

    def escape(self, modo, msg):
        if modo == "error":
            messagebox.showerror(title="Erro", message=msg)

    def selectItem(self, a):
        curItem = self.tv.focus()
        b = self.tv.item(curItem)
        b = list(b.values())
        nome = b[2][1]
        pontos = b[2][2]
        partidas = b[2][3]
        vitorias = b[2][4]
        empates = b[2][5]
        derrotas = b[2][6]
        gp = b[2][7]
        gc = b[2][8]
        ca = b[2][10]
        cv = b[2][11]
        self.vequipe.set(nome)
        self.vpontos.set(str(pontos))
        self.vpartidas.set(partidas)
        self.vvitorias.set(str(vitorias))
        self.vempates.set(str(empates))
        self.vderrotas.set(str(derrotas))
        self.vgp.set(str(gp))
        self.vgc.set(str(gc))
        self.vca.set(str(ca))
        self.vcv.set(str(cv))

    def sincronizar(self):
        for i in self.tv.get_children():
            self.tv.delete(i)

        dados = getDados()

        for i in dados["posicao"]:
            self.tv.insert("", "end", values=(
            str(dados["posicao"][i - 1]), dados["nome"][i - 1], str(dados["pontos"][i - 1]),
            str(dados["partidas"][i - 1]), str(dados["vitorias"][i - 1]),
            str(dados["empates"][i - 1]), str(dados["derrotas"][i - 1]), str(dados["gp"][i - 1]),
            str(dados["gc"][i - 1]), str(dados["saldo"][i - 1]), str(dados["ca"][i - 1]), str(dados["cv"][i - 1])))
