from django.http import HttpResponse

def instructions_view(request):
    html = """
    <html>
        <body>
            <!-- HTML -->
            <h1>Instructions</h1>
            <h3>Use the AWSD keys to help you move the sprite</h3>
            <p>A: left</p>
            <p>W: up</p>
            <p>S: down</p>
            <p>D: right</p>

            <h3>You will be entering the RPG food adventure game, where you will obtain different foods through battling different foods while walking around the map.</h3>
            <h3>Directions: The game consist of two main level</h3>
            <ul>
                <li>SEP Map (main Map)</li>
                <li>Software Engineering Program Room (Battle Map)</li>
            </ul>

            <h3>When you are in a battle there will be three different battle buttons on the side of the map</h3>
            <ul>
                <li> Attack </li>
                <li> Jump </li>
                <li> Run </li>
            </ul>
            <button><a href="../game/index.html" class="button">Go Back</a></button>
        </body>
    </html>
    """
    return HttpResponse(html)

