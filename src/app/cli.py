import typer
from typing_extensions import Annotated

app = typer.Typer(help="RouteSage : compiled RAG with optimized routing")

@app.command()
def ask(
    question : Annotated[str, typer.Argument(help="The question to ask to the RAG system")],
    k : Annotated[int, typer.Option(help="The number of documents to retrieve")] = 5,

):

    """
    Ask a question and get an answer with citations
    """

    typer.echo(f"Searching for {question}, (top-k : {k})")
    # later we will call our DSPy program here
    typer.echo("Ready for retrieval")

@app.command()
def version():
    """
    Print the version of RouteSage.
    """
    typer.echo("RouteSage : v0.1.0")

if __name__=="__main__":
    app()