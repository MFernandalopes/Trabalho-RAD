import tkinter as tk
from tkinter import ttk, messagebox
from database import BancoRAD
banco = BancoRAD()
banco.conectar()

root = tk.Tk()
root.title("RAD Control - Sistema de Gestão de Solicitações")
root.geometry('750x750')


frame_form = tk.LabelFrame(root, text="Dados da Solicitação")
frame_form.pack(padx=10, pady=10, fill="x")

tk.Label(frame_form, text="Nome do Aluno:").grid(row=0, column=0, padx=5, pady=5)
entry_nome = tk.Entry(frame_form, width=40)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Matrícula").grid(row=1, column=0, padx=5, pady=5)
entry_matricula = tk.Entry(frame_form, width=40)
entry_matricula.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Prazo").grid(row=2, column=0, padx=5, pady=5)
entry_prazo = tk.Entry(frame_form, width=40)
entry_prazo.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Tipo:").grid(row=3, column=0, padx=5, pady=5)
combo_tipo = ttk.Combobox(frame_form, values=["Dúvida", "Entrega", "Correção", "Orientação", "Revisão", "Outro"])
combo_tipo.grid(row=3, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Prioridade:").grid(row=4, column=0, padx=5, pady=5)
combo_prioridade = ttk.Combobox(frame_form, values=["Baixa", "Média", "Alta"])
combo_prioridade.grid(row=4, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Status:").grid(row=5, column=0, padx=5, pady=5)
combo_status = ttk.Combobox(frame_form, values=["Aberto", "Em andamento", "Concluído", "Cancelado"])
combo_status.grid(row=5, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Descrição:").grid(row=6, column=0, padx=5, pady=5)
text_descricao = tk.Text(frame_form, width=40, height=4)
text_descricao.grid(row=6, column=1, padx=5, pady=5)

frame_botoes = tk.LabelFrame(root, text="Ações")
frame_botoes.pack(padx=10, pady=5, fill="x")


def cadastrar():
    nome = entry_nome.get()
    matricula = entry_matricula.get()
    tipo = combo_tipo.get()
    prioridade = combo_prioridade.get()
    status = combo_status.get()
    descricao = text_descricao.get("1.0", "end-1c")
    prazo = entry_prazo.get() or None

    if not nome or not matricula or not tipo or not prioridade or not status or not descricao:
        messagebox.showwarning("Aviso", "Preencha todos os campos obrigatórios!")
        return
    
    banco.inserir(nome, matricula, tipo, prioridade, status, descricao, prazo)
    limpar()
    recarregar()
    messagebox.showinfo("Sucesso", "Solicitação cadastrada com sucesso!")

def atualizar():
    nome = entry_nome.get()
    matricula = entry_matricula.get()
    tipo = combo_tipo.get()
    prioridade = combo_prioridade.get()
    status = combo_status.get()
    descricao = text_descricao.get("1.0", "end-1c")
    prazo = entry_prazo.get() or None

    if not nome or not matricula or not tipo or not prioridade or not status or not descricao:
        messagebox.showwarning(
        "Aviso",
        "Preencha todos os campos obrigatórios!"
        )
        return

    selecionado = tree.focus()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione um registro!")
        return
    id_registro = tree.item(selecionado)["values"][0]
    banco.atualizar(id_registro, nome, matricula, tipo, prioridade, status, descricao, prazo)
    recarregar()
    limpar()

def selecionar(event):
    selecionado = tree.focus()
    if selecionado:
        valores = tree.item(selecionado)["values"]  
        entry_nome.delete(0, "end")
        entry_nome.insert(0, valores[1])
        entry_matricula.delete(0, "end")
        entry_matricula.insert(0, valores[2])
        combo_tipo.set(valores[3])
        combo_prioridade.set(valores[4])
        combo_status.set(valores[5])
        text_descricao.delete("1.0", "end")
        text_descricao.insert("1.0", valores[6])
        entry_prazo.delete(0, "end")
        entry_prazo.insert(0, str(valores[8] or ""))
    
def excluir():
    selecionado = tree.focus()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione um registro!")
        return
    confirmar = messagebox.askyesno("Confirmar", "Deseja excluir?")
    if confirmar:
        id_registro = tree.item(selecionado)["values"][0]
        banco.excluir(id_registro)
        recarregar()         

def pesquisar():
    nome = entry_nome.get().strip()
    prioridade = combo_prioridade.get()
    status = combo_status.get()
    
    # Descobrindo qual deles o usuário preencheu para usar como busca
    if nome:
        termo = nome
    elif status:
        termo = status
    elif prioridade:
        termo = prioridade
    else:
        # Se tudo estiver vazio avisamos ao usuário
        messagebox.showwarning("Aviso", "Preencha o Nome, Status ou Prioridade para pesquisar!")
        return

    tree.delete(*tree.get_children())  
    registros = banco.pesquisar(termo)         
    if registros:
        for registro in registros:
            tree.insert("", "end", values=registro) 

def limpar():
    entry_nome.delete(0, "end")
    entry_matricula.delete(0, "end")
    entry_prazo.delete(0, "end")
    combo_tipo.set("")
    combo_prioridade.set("")
    combo_status.set("")
    text_descricao.delete("1.0", "end")
     
    for item in tree.selection():
        tree.selection_remove(item)

def recarregar():
    tree.delete(*tree.get_children())  
    registros = banco.listar()
    if registros:       
        for registro in registros:
            tree.insert("", "end", values=registro)  

tk.Button(frame_botoes, text="Cadastrar", command=cadastrar).pack(side="left", padx=5, pady=5)
tk.Button(frame_botoes, text="Atualizar", command=atualizar).pack(side="left", padx=5, pady=5)
tk.Button(frame_botoes, text="Excluir", command=excluir).pack(side="left", padx=5, pady=5)
tk.Button(frame_botoes, text="Pesquisar", command=pesquisar).pack(side="left", padx=5, pady=5)
tk.Button(frame_botoes, text="Limpar", command=limpar).pack(side="left", padx=5, pady=5)
tk.Button(frame_botoes, text="Recarregar", command=recarregar).pack(side="left", padx=5, pady=5)


frame_lista = tk.LabelFrame(root, text="Registros")
frame_lista.pack(padx=10, pady=10, fill="both", expand=True)

colunas = ("id", "nome", "matricula", "tipo", "prioridade", "status", "descricao", "data", "prazo")
tree = ttk.Treeview(frame_lista, columns=colunas, show="headings")
tree.pack(fill="both", expand=True)

tree.heading("id", text="ID")
tree.heading("nome", text="Nome")
tree.heading("matricula", text="Matrícula")
tree.heading("tipo", text="Tipos")
tree.heading("prioridade", text="Prioridade")
tree.heading("status", text="Status")
tree.heading("descricao", text="Descricao")
tree.heading("data", text="Data")
tree.heading("prazo", text="Prazo")

tree.column("id", width=50)
tree.column("nome", width=150)
tree.column("matricula", width=100)
tree.column("tipo", width=100)
tree.column("prioridade", width=80)
tree.column("status", width=100)
tree.column("descricao", width=200)
tree.column("data", width=120)
tree.column("prazo", width=100)


tree.bind("<<TreeviewSelect>>", selecionar)





recarregar()
root.mainloop()