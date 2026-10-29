import turtle
import random

# Configuração da tela
tela = turtle.Screen()
tela.bgcolor("#0a0a2a")          # céu noturno escuro
tela.title("Cidade Noturna")
tela.setup(1200, 700)
tela.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

# ========== FUNÇÕES ==========

def desenhar_predio(x, y, largura, altura, cor):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(cor)
    t.begin_fill()
    
    # Corpo do prédio
    t.setheading(90)
    t.forward(altura)
    t.right(90)
    t.forward(largura)
    t.right(90)
    t.forward(altura)
    t.right(90)
    t.forward(largura)
    t.end_fill()
    
    # Janelas
    t.color("#ffd700")          # amarelo das luzes
    for i in range(4, altura - 10, 25):
        for j in range(8, largura - 8, 18):
            if random.random() > 0.25:   # algumas janelas apagadas
                t.penup()
                t.goto(x + j, y + i)
                t.pendown()
                t.begin_fill()
                for _ in range(4):
                    t.forward(10)
                    t.right(90)
                t.end_fill()

def desenhar_lua(x, y, raio):
    t.penup()
    t.goto(x, y - raio)
    t.pendown()
    t.color("#f5f5dc")
    t.begin_fill()
    t.circle(raio)
    t.end_fill()
    
    # Cratera simples
    t.penup()
    t.goto(x + 15, y + 10)
    t.pendown()
    t.color("#e8e8d0")
    t.begin_fill()
    t.circle(8)
    t.end_fill()

def desenhar_estrelas(quantidade):
    t.color("white")
    for _ in range(quantidade):
        x = random.randint(-580, 580)
        y = random.randint(50, 320)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.begin_fill()
        t.circle(random.randint(1, 2))
        t.end_fill()

# ========== DESENHO ==========

# Estrelas
desenhar_estrelas(80)

# Lua
desenhar_lua(420, 250, 45)

# Chão
t.penup()
t.goto(-600, -280)
t.pendown()
t.color("#1a1a1a")
t.begin_fill()
t.setheading(0)
t.forward(1200)
t.right(90)
t.forward(80)
t.right(90)
t.forward(1200)
t.right(90)
t.forward(80)
t.end_fill()

# Prédios (posição x, base y, largura, altura, cor)
predios = [
    (-520, -280, 70, 180, "#2c3e50"),
    (-440, -280, 90, 260, "#34495e"),
    (-340, -280, 60, 150, "#2c3e50"),
    (-270, -280, 110, 320, "#1c2833"),
    (-150, -280, 80, 210, "#2c3e50"),
    (-60,  -280, 100, 280, "#34495e"),
    (50,   -280, 70, 190, "#2c3e50"),
    (130,  -280, 120, 350, "#1a252f"),
    (260,  -280, 85, 230, "#2c3e50"),
    (355,  -280, 95, 290, "#34495e"),
    (460,  -280, 75, 170, "#2c3e50"),
]

for p in predios:
    desenhar_predio(*p)

# Antenas em alguns prédios
t.color("#aaaaaa")
t.pensize(2)
antenas = [(-225, 40), (190, 70), (400, 10)]
for x, y in antenas:
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(90)
    t.forward(40)
    t.forward(8)
    t.backward(8)
    t.right(30)
    t.forward(12)
    t.backward(12)
    t.left(60)
    t.forward(12)

tela.update()
tela.mainloop()