/* ajax call to retrieve array of x (howmany) items */
var gettweet = function (id) {
    console.log(id)
    $.ajax({
        type: "GET",
        url: "https://api.twitter.com/1.1/statuses/show.json?id="+id,
        dataType: "json",
        contentType: "application/json;charset=utf-8",
        data: id,
        success: function (result) {
            console.log(result)
        },
        error: function (request, status, error) {
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    })
}


$(document).ready(function () {
  console.log("whattup")

  gettweet(1240818722626920448)
  //console.log(tweetObject.tweet)
})
