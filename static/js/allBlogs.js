// onclick lisner for ajax call 
// spinner and loadmore btn and alert 
var spinner = document.getElementById('spinner');
var btn = document.getElementById('loadMoreBtn');
var alertNoMore = document.getElementById('noMoreAlert');
// update insert to append data from js to html
var updateInsert = document.getElementById('Blogs');
// current number of updates avaliable
var currentNoUpdates = 6;
var BlogsOver = false;
// loadmore function to handle ajax
if (BlogsOver == true) {
    console.log('no more blogs to load now')
}
else {
    
    document.getElementById('loadMoreBtn').onclick = () => {
        
        var url = '../GetMoreBlog/' + currentNoUpdates;
        console.log("clicked");
        document.getElementById('loadMoreBtn_Span').innerHTML=`<button class=" btn btn-user-primary" id="loadMoreBtn" hx-get="${url}" hx-target="#Blogs" hx-trigger="click" hx-swap="beforeend" >Load More</button>`
        currentNoUpdates += 6;
        console.log(document.getElementById('loadMoreBtn_Span').innerHTML);

    }
}

