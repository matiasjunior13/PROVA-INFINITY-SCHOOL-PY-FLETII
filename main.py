
import flet as ft

def main(page: ft.Page):
    page.title = "Formulário de Contato"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 500
    page.window_height = 700
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 40
    page.update()
    
    titulo = ft.Text("Formulário de Contato", size=32, weight="bold")
    subtitulo = ft.Text("Preencha os campos abaixo e clique em Enviar", size=16)
    
    campo_nome = ft.TextField(
        label="Nome completo",
        hint_text="Digite seu nome completo",
        border="underline",
        prefix_icon="person",
        expand=True
    )
    
    campo_email = ft.TextField(
        label="E-mail",
        hint_text="Digite seu e-mail",
        border="underline",
        prefix_icon="email",
        keyboard_type=ft.KeyboardType.EMAIL,
        expand=True
    )
    
    campo_mensagem = ft.TextField(
        label="Mensagem",
        hint_text="Digite sua mensagem",
        border="underline",
        prefix_icon="message",
        multiline=True,
        min_lines=3,
        max_lines=5,
        expand=True
    )
    
    confirmacao = ft.Container(
        content=ft.Column([
            ft.Icon("check_circle", color="green", size=64),
            ft.Text("Formulário enviado com sucesso!", size=20, weight="bold", color="green"),
            ], 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
        alignment=ft.alignment.center,
        padding=20,
        visible=False
    )
    
    def enviar_formulario(e):
        if not campo_nome.value:
            campo_nome.error_text = "Por favor, informe seu nome"
            page.update()
            return
        
        if not campo_email.value:
            campo_email.error_text = "Por favor, informe seu e-mail"
            page.update()
            return
        elif "@" not in campo_email.value or "." not in campo_email.value:
            campo_email.error_text = "Por favor, informe um e-mail válido"
            page.update()
            return
        
        if not campo_mensagem.value:
            campo_mensagem.error_text = "Por favor, digite sua mensagem"
            page.update()
            return
        
        dados = {
            "nome": campo_nome.value,
            "email": campo_email.value,
            "mensagem": campo_mensagem.value
        }
        
        print("Dados do formulário:")
        print(f"Nome: {dados['nome']}")
        print(f"Email: {dados['email']}")
        print(f"Mensagem: {dados['mensagem']}")
        
        formulario.visible = False
        confirmacao.visible = True
        page.update()
    
    botao_enviar = ft.ElevatedButton(
        text="Enviar",
        icon="send",
        on_click=enviar_formulario,
        bgcolor="blue",
        color="white",
        width=200
    )    
    formulario = ft.Container(
        content=ft.Column([
            titulo,
            subtitulo,
            ft.Divider(height=30, color="transparent"),
            campo_nome,
            ft.Container(height=20),
            campo_email,
            ft.Container(height=20),
            campo_mensagem,
            ft.Container(height=40),
            ft.Row([botao_enviar], alignment=ft.MainAxisAlignment.CENTER)
        ], spacing=5),
        visible=True
    )
    page.add(
        ft.Card(
            content=ft.Container(
                content=ft.Stack([formulario, confirmacao]),
                padding=30
            ),
            elevation=5
        )
    )
    campo_nome.focus()
    page.update()

ft.app(target=main)
