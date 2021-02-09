// function ShirtHover {

// }

function hvr(dom, action)
{
    if (action == 'in')
    {
        $(dom).find("[col=g]").css("display", "none");
        $(dom).find("[col=b]").css("display", "inline-block");
    }

    else
    {
        $(dom).find("[col=b]").css("display", "none");
        $(dom).find("[col=g]").css("display", "inline-block");
    }
}

var updateBtns = document.getElementsByClassName("update-cart")

for (var i=0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function() {
        var productID = this.dataset.product
        var action    = this.dataset.action
        console.log('productID:', productID, 'action:', action)

        console.log('USER:', user)
        if (user === 'AnonymousUser') {
            console.log('Not logged in')
        }
        else {
            updateUserOrder(productID, action)
        }
    })
}


function updateUserOrder(productID, action){
    console.log('User is logged in, sending data...')

    // using the fetch API
    var url = '/update_item/'

    fetch(url, {
        method: 'POST', 
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productID': productID, 'action': action})
    })

    .then((response) => {
        console.log('Got Here first')
        return response.json()
        
    })

    .then((data) => {
        console.log('data:', data)
        location.reload() // to reload our page automatically everytime items gets added to our cart.
    })
}