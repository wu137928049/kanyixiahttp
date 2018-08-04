$(function () {
   $('#all_sort').click(
       function(){
           $('#sort_list').show();
           $('#all_sort_icon').attr('class','glyphicon glyphicon-chevron-down');
       }
   )
});
$(function () {
   $('#sort_list') .click(
       function () {
           $('#sort_list').hide();
           $('#all_sort_icon').attr('class','glyphicon glyphicon-chevron-up');
       }
   )
});
$(function () {
    $('#all_type').click(
        function () {
            $('#type_list').show();
            $('#all_type_icon').attr('class','glyphicon glyphicon-chevron-down');
        }
    )
});
$(function () {
   $('#type_list').click(
       function () {
           $('#type_list').hide();
           $('#all_type_icon').attr('class','glyphicon glyphicon-chevron-up');
       }
   )
});
