import plotly.graph_objects as go

# Définition des données de l'organigramme
data = [
    go.Node(
        name="Président",
        x=0,
        y=0,
        text="Président",
        color="#4d4d4d"
    ),
    go.Node(
        name="Directeur général",
        x=0,
        y=1,
        text="Directeur général",
        color="#4d4d4d"
    ),
    go.Node(
        name="Directeur des ventes",
        x=-1,
        y=2,
        text="Directeur des ventes",
        color="#4d4d4d"
    ),
    go.Node(
        name="Directeur de la production",
        x=1,
        y=2,
        text="Directeur de la production",
        color="#4d4d4d"
    ),
    go.Node(
        name="Directeur financier",
        x=0,
        y=3,
        text="Directeur financier",
        color="#4d4d4d"
    ),
    go.Edge(
        source="Président",
        target="Directeur général",
        color="#cccccc"
    ),
    go.Edge(
        source="Directeur général",
        target="Directeur des ventes",
        color="#cccccc"
    ),
    go.Edge(
        source="Directeur général",
        target="Directeur de la production",
        color="#cccccc"
    ),
    go.Edge(
        source="Directeur général",
        target="Directeur financier",
        color="#cccccc"
    )
]

# Création de la figure
figure = go.Figure(
    data=data,
    layout=go.Layout(
        title="Organigramme",
        font={"color": "#333333"}
    )
)

# Affichage de la figure
figure.show()
