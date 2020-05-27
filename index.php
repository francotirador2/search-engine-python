<html>

    <head>
        <title>Search Engine</title>
    </head>

    <body>

        <form action='index.php' method='GET'>

            <label for='queryBox'>Enter query here</label></br>
            <input type='text' name='query' id='queryBox'>
            <input type='submit' name='search' value='Search'><br>
            
        </form>

        <button id='upload' onclick='upload()'>Upload</button>

        <p id='results'>
            <?php
                if ($_GET['query']) {
                    echo 'Showing results for query: ' . $_GET['query'] . '<br>';
                    $command = 'python3 search.py 3 ' . $_GET['query'];
                    $results = exec($command);
                    $results = explode(',',$results);
                    //$results = json_decode($results);
                    foreach ($results as $result) {
                        echo '<a href="docs_test/' . $result . '">' . $result . '</a></br>';
                    }
                }
           ?>
        </p>

        <script>
            function upload() {
                document.getElementById('results').innerHTML = 'uploading...';
            }
        </script>

    </body>
</html>