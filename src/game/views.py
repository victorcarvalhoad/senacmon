from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required
def start_view(request):
    # futura lógica: escolher o starter e criar a partida
    messages.info(request, "Tela de início de partida, escolha do Pokémon e criação da partida.")
    return render(request, "game/start.html")

@login_required
def state_view(request):
    # futura lógica: mostrar o estado atual da partida
    return render(request, "game/board.html", {"state": None})

@login_required
def roll_view(request):
    if request.method == "POST":
        messages.error(request, "Ação inválida")
        return redirect("game:state")

    # futura lógica: consumir captura, rolar dado, resolver zona
    messages.success(request, "Rolagem efetuada, zona resolvida no placeholder")
    return redirect("game:state")

"""
Lógica futura:
- Receber a requisição GET.
- Lançar uma mensagem "tela de início...".
- Renderizar a página start.html ou board.html.
- E, para a rota roll
- Lançar mensagem de dados rolando.
- E redirecionar para o estado.
"""