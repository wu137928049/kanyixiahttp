// $(
//     function(){
//     //    初始话
//         initTopWheel();
//     }
// )
//
//
// function initTopWheel() {
//     var mySwiper = new Swiper('.swiper-container', {
//         loop: true,
//         // pagination: '.swiper-pagination',
// 	    autoplay: 2000,//可选选项，自动滑动
// })
//
// }

$(
    function () {
        // init top wheel
        initTopWheel();
    }
)

function initTopWheel() {

    var mySwiper = new Swiper('.swiper-container', {
        // loop: true,

        // 如果需要分页器
        pagination: '.swiper-pagination',
	    autoplay: 3000,//可选选项，自动滑动
    })

}