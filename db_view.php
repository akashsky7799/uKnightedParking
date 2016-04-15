<?php
// array for JSON response
$response = array();

// make sure we have the connect file
require_once __DIR__ . '/db_connect.php';

// make a connection
$db = new DB_CONNECT();

// get all products from parking table (table name must match table in database)
$result = mysql_query("SELECT * FROM parking") or die(mysql_error());

// check for empty result
if (mysql_num_rows($result) > 0) {
    // looping through all results
    $response["parking"] = array();

    while ($row = mysql_fetch_array($result)) {
        // temp user array
        $Part = array();
        $Part["id"] = $row["id"];
        $Part["name"] = $row["name"];
        $Part["openspots"] = $row["openspots"];

        // push data into final response array
        array_push($response["parking"], $Part);
    }
    // success
    $response["success"] = 1;

    // echoing JSON response
    echo json_encode($response);
} else {
    // no data found
    $response["success"] = 0;
    $response["message"] = "No parts inserted";

    // echo no users JSON
    echo json_encode($response);
}
?>
