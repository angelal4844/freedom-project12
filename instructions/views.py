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

            <h2>Here are some others:</h2>
            <p>Y: spawn the enemy</p>
            <h2>There will be buttons that appear when you will be able to select</h2>

            <h2>To go back, click on the button</h2>
            <button type="button" onclick="https://angelal4844.github.io/freedom-project12/instructions/instructions.html">Click Me!</button>


        </body>
    </html>
    """
    return HttpResponse(html)

