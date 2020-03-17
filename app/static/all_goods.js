var goodsRequest = new XMLHttpRequest();
goodsRequest.open('GET','')
goodsRequest.onload = function () {
    var ourData = JSON.parse(goodsRequest.responseText);
    console.log(ourData[0])

};
goodsRequest.send();
