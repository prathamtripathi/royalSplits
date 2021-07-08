var updateBtns = document.getElementsByClassName('update-cart');

for(i=0; i < updateBtns.length;i++){
  updateBtns[i].addEventListener('click',function(){
    var productId = this.dataset.product;
    var action = this.dataset.action;
    console.log('productId',productId,'action',action);
    console.log('User':user);
  })
}























// function getCookie(name) {
//   var cookieArr = document.cookie.split(";");
//   for (var i = 0; i < cookieArr.length; i++) {
//     var cookiePair = cookieArr[i].split("=");

//     if(name == cookiePair[0].trim()){
//       return decodeURIComponent(cookiePair[1]);
//     }
//     // body...
//   }
//   return null;

  
// }
// var cart = JSON.parse(getCookie('cart'))
// if(cart == undefined){
//   cart = {}
//   console.log("cart Was created");
//   document.cookie = 'cart='+ JSON.stringify(cart) + ";domain=;path=/"
// }
// console.log('cart:',cart)


















// function addToCart(pid){
//   var cartTitle = document.querySelector('#rowCartPrice');
//   var cartImage = document.querySelector('#rowSideBarCart');
//   productTitleId = '#productTitle' + pid;
//   productPriceId = '#productPrice' + pid;
//   var radio = '#productThumb' +pid;
//   var title = document.querySelector(productTitleId).innerHTML;
//   var price = document.querySelector(productPriceId).innerHTML;
//   var th = document.getElementsByName(radio);
//   var thumb;
//   if(th[0].checked){
//   	thumb = th[0].value;
//   }else if(th[1].checked){
//   	thumb = th[1].value;
//   }else if(th[2].checked){
//   	thumb = th[2].value;
//   }else if(th[3].checked){
//   	thumb = th[3].value;
//   }else if(th[4].checked){
//   	thumb = th[4].value;
//   }else if(th[5].checked){
//   	thumb = th[5].value;
//   }else if(th[6].checked){
//   	thumb = th[6].value;
//   }else{
//   	thumb = th[7].value;
//   }

  

  
  
// }
