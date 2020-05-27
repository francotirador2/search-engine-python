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

        <form action='index.php' method='POST' enctype="multipart/form-data">
            <!--<button id='upload' onclick='upload()'>Upload</button>-->
            <input type='file' name='doc'><br>
            <input type='submit' name='uploadDoc' value='Submit'>
        </form>

        <p id='results'>
            <?php

                if ($_GET['query']) {

                    echo 'Showing results for query: ' . $_GET['query'] . '<br>';
                    $command = 'python3 search.py 3 ' . $_GET['query'];
                    $results = exec($command);
                    $results = explode(',',$results);
                    foreach ($results as $result) {
                        echo '<a href="docs_test/' . $result . '">' . $result . '</a></br>';
                    }

                } else if (isset($_POST['uploadDoc'])) {

                    echo json_encode($_FILES);
                    
                    $target_dir = "docs_test/";
                    $target_file = $target_dir . basename($_FILES['doc']['name']);
                    //$uploadOk = 1;
                    $imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
                    
                    if (move_uploaded_file($_FILES['doc']['tmp_name'], $target_file)) {
                        echo 'The file ' . basename( $_FILES['doc']['name']). ' has been uploaded.';
                    } else {
                        echo 'Sorry, there was an error uploading your file.';
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