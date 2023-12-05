from tkinter import *
from tkinter import ttk
from tkinter import messagebox

agenda = [
    {"nome": "Jonas", "telefone": "85 98888 3333", "categoria": "Amigos"}
]
index = None
def atualizarTabela():
    for linha in tabela.get_children():
        tabela.delete(linha)

    for contato in agenda:
        tabela.insert("", END, values=(contato["nome"], contato['telefone'],
                                       contato["categoria"]))

def limpasCampos():
    txtNome.delete(0, END)
    txtTelefone.delete(0, END)
    comboCategoria.set('')

def adicionarContato():
    nome = txtNome.get()
    telefone = txtTelefone.get()
    categoria = comboCategoria.get()
    contato = {
        "nome": nome,
        "telefone": telefone,
        "categoria": categoria
    }
    agenda.append(contato)
    messagebox.showinfo('Sucesso!', 'Contado Adicionado com Sucesso!')
    atualizarTabela()
    limpasCampos()

def tabelaClique(event):
    linhaSelecionada = tabela.selection()[0]
    global index
    index = tabela.index(linhaSelecionada)
    contato = agenda[index]
    limpasCampos()
    txtNome.insert(0, contato['nome'])
    txtTelefone.insert(0, contato['telefone'])
    comboCategoria.set(contato['categoria'])

def editarContato():
    agenda[index] = {
        "nome": txtNome.get(),
        "telefone": txtTelefone.get(),
        "categoria": comboCategoria.get()
    }
    limpasCampos()
    atualizarTabela()
    messagebox.showinfo('Sucesso!', 'Dados Alterado com Sucesso!')

def excluirContato():
    opcao = messagebox.askyesno('Tem certeza?', 'Deseja Exluir o Contato?')
    if opcao:
        agenda.remove(agenda[index])
        messagebox.showinfo('Sucesso!', 'Contato Exlcluído com Sucesso!')
        limpasCampos()
        atualizarTabela()



janela = Tk()
janela.title('Agenda Telefônica')

labelNome = Label(janela, text='Nome:', fg='navy', font='Tahoma 14 bold')
labelNome.grid(row=0, column=0)
txtNome = Entry(janela, font='Tahoma 14', width=27)
txtNome.grid(row=0, column=1)

labelTelefone = Label(janela, text='Telefone:', fg='navy', font='Tahoma 14 bold')
labelTelefone.grid(row=1, column=0)
txtTelefone = Entry(janela, font='Tahoma 14', width=27)
txtTelefone.grid(row=1, column=1)

labelCategorias = Label(janela, text='Categoria:', fg='navy', font='Tahoma 14 bold')
labelCategorias.grid(row=2, column=0)

categorias = ['Amigos', 'Trabalho', 'Família']
comboCategoria = ttk.Combobox(janela, values=categorias, font='Tahoma 14', width=25)
comboCategoria.grid(row=2, column=1)


btnAdicionar = Button(janela, text='Adicionar', bg='navy', fg='white',
                   font='Tahoma 12 bold', width=8, activebackground='white',
                   activeforeground='navy', command=adicionarContato)
btnAdicionar.grid(row=3, column=0)

btnEditar = Button(janela, text='Editar', bg='navy', fg='white',
                   font='Tahoma 12 bold', width=8, activebackground='white',
                   activeforeground='navy', command=editarContato)
btnEditar.grid(row=3, column=1)

btnExcluir = Button(janela, text='Excluir', bg='navy', fg='white',
                   font='Tahoma 12 bold', width=8, activebackground='white',
                   activeforeground='navy', command=excluirContato)
btnExcluir.grid(row=3, column=2)

colunas = ['Nome', 'Tefefone', 'Categoria']
tabela = ttk.Treeview(janela, columns=colunas, show='headings')

for coluna in colunas:
    tabela.heading(coluna, text=coluna)
tabela.grid(row=4, columnspan=3)
tabela.bind('<ButtonRelease-1>', tabelaClique)


atualizarTabela()
janela.mainloop()

