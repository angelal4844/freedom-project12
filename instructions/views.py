from django.http import HttpResponse

def instructions_view(request):
    html = """
    <html>
        <body>
            <!-- HTML -->
            <h1>Instructions</h1>
            <h2>Use the AWSD keys to help you move the sprite</h2>
            <h3>You will be entering the RPG adventure game with many different adventures.</h3>
            <h3>Directions: The game consist of one main level</h3>
            <ul>
                <li>Restaurant</li>
                <li>Software Engineering Program</li>
            </ul>
            <p>A: left</p>
            <p>W: up</p>
            <p>S: down</p>
            <p>D: right</p>
        </body>
    </html>
    """
    return HttpResponse(html)