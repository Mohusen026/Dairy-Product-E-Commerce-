
// $('.plus-cart').click(function() {
//     var id=$(this).attr("pid").toString();
//     var eml =this.parentNode.children[2]  //basically these the jquery for the increse and decease the quantity of the product
//     console.log("pid =",id)
//     $.ajax({
//         type:"GET",
//         url:"/pluscart",
//         data:{
//             prod_id:id
//         },
//         success:function(data){
//             console.log("data =",data);
//             eml.innerText=data.quantity
//             document.getElementById("amount").innerText=data.amount
//             document.getElementById("totalamount").innerText=data.totalamount
//         }
//     })
// })  


// $('.minus-cart').click(function() {
//     var id=$(this).attr("pid").toString();
//     var eml =this.parentNode.children[2]  //basically these the jquery for the increse and decease the quantity of the product
//     console.log("pid =",id)
//     $.ajax({
//         type:"GET",
//         url:"/minuscart",
//         data:{
//             prod_id:id
//         },
//         success:function(data){
//             eml.innerText=data.quantity
//             document.getElementById("amount").innerText=data.amount
//             document.getElementById("totalamount").innerText=data.totalamount
//         }
//     })
// })  



// $('.remove-cart').click(function() {
//     var id=$(this).attr("pid").toString();
//     var eml =this  //basically these the jquery for the increse and decease the quantity of the product
//     console.log("pid =",id)
//     $.ajax({
//         type:"GET",
//         url:"/removecart",
//         data:{
//             prod_id:id
//         },
//         success:function(data){            
//             document.getElementById("amount").innerText=data.amount
//             document.getElementById("totalamount").innerText=data.totalamount
//             eml.parentNode.parentNode.parentNode.parentNode.remove()
//         }
//     })
// })  










































$('.plus-cart').click(function() {
    var id = $(this).attr("pid").toString();
    var eml = document.getElementById("quantity-" + id);
    $.ajax({
        type: "GET",
        url: "/pluscart",
        data: {
            prod_id: id
        },
        success: function(data) {
            eml.innerText = data.quantity;
            document.getElementById("amount").innerText = data.amount;
            document.getElementById("totalamount").innerText = data.totalamount;
        }
    })
});

$('.minus-cart').click(function() {
    var id = $(this).attr("pid").toString();
    var eml = document.getElementById("quantity-" + id);
    $.ajax({
        type: "GET",
        url: "/minuscart",
        data: {
            prod_id: id
        },
        success: function(data) {
            eml.innerText = data.quantity;
            document.getElementById("amount").innerText = data.amount;
            document.getElementById("totalamount").innerText = data.totalamount;
        }
    })
});

$('.remove-cart').click(function() {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.parentNode.parentNode.parentNode;
    $.ajax({
        type: "GET",
        url: "/removecart",
        data: {
            prod_id: id
        },
        success: function(data) {
            document.getElementById("amount").innerText = data.amount;
            document.getElementById("totalamount").innerText = data.totalamount;
            eml.remove();
        }
    })
});

