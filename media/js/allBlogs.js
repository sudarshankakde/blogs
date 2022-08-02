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
    document.getElementById('loadMoreBtn').addEventListener('click', loadMoreUpdates);
    window.onscroll = () => {
        const scrollable = document.documentElement.scrollHeight - window.innerHeight;
        const scrolled = window.scrollY;
        if (BlogsOver == false) {
            if (scrolled <= scrollable - 400) {
            }
            else {
                loadMoreUpdates();
            }
        }
        else{
        }
    }
}

function loadMoreUpdates() {
    // spiner visible and load more hidden
    spinner.style.visibility = "visible";
    btn.style.visibility = "hidden";
    // ajax variable
    var getData = new XMLHttpRequest();
    getData.open("GET", "GetMoreBlog/" + (currentNoUpdates), true);
    getData.onload = () => {
        // spiner hidden and load more vissible
        spinner.style.visibility = "hidden";
        btn.style.visibility = "visible";
        // status ok : 200
        if (getData.status == 200) {
            // update current no of updates 
            currentNoUpdates += 6;
            var data = JSON.parse(getData.response);
            if (data.data[0] == null) {
                btn.style.visibility = "hidden";
                alertNoMore.style.visibility = "visible";
                BlogsOver = true;
            }
            console.log(data);
            for (var i in data.data) {
                var post = data.data[i].fields;
                // inner html insert in updateInsert 
                // card
                const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
                ];
                var summary = post.summary.slice(650);
                var dateVar = new Date(post.publish_date);
                var CalenderDate = dateVar.getUTCDate();
                if (CalenderDate < 10) CalenderDate = '0' + CalenderDate;
                var date = String(CalenderDate) + " " + monthNames[dateVar.getMonth()] + " " + String(dateVar.getFullYear());


                const tagOt = [];
                for (var i in data.tags) {
                    tagOt[data.tags[i].id] = data.tags[i].tag;
                }
                function callHtml(t) {
                    t = tagOt[t]
                    return (`<a href='search?query=${t}' class='badge badge-Theme-Primary bi bi-tag-fill w-auto my-1 mr-2'>${t}</a>`)
                }
                updateInsert.innerHTML += `<div class="col-lg-6 col-sm-6 col-12 my-lg-3 my-sm-3 my-2 ">
            <div class="card-deck">
                <div class="card">
                    <img class="card-img-top" src="${post.image}" alt=${post.title} style="max-height: 250px;">
                    <div class="card-body">
                        <h5 class="card-title">${post.title}</h5>
                        <p class="card-text"></i>${post.summary}</p>
                        <span class="tags my-2 d-flex  flex-wrap  justify-content-start ">               
                            ${post.tags.map((t) => callHtml(t))}
                        </span >
                        <span class="my-auto d-flex justify-content-between pt-2">
                            <span class="bi bi-eye-fill  my-auto"
                                style="font-size: medium;opacity: 0.9; cursor: default;" title='${post.views} views'
                                data-toggle="tooltip" data-placement="bottom">&nbsp;${post.views}</span>
                            <!-- Link -->
                            <a href=${post.slug} class="Hover2">
                                Read more
                            </a>
                        </span>
                    </div >
                        <div class="card-footer d-flex justify-content-between">
                            <small class="text-user">Last updated ${date}</small>
                            <small class="text-user "><i class="bi bi-person-fill"></i> Author - ${post.author}</small>
                        </div>
                </div >
            </div >
        </div >`;
            }

        }
        else {
            alertNoMore.innerHTML = "Can't Load More Blogs";
            alertNoMore.style.visibility = "visible";
            btn.style.visibility = "hidden";
            console.clear();
        }
    }
    getData.send();
}


