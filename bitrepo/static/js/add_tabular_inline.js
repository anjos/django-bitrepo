function increment_form_ids(el, to) {
  var from = to-1;
  $(':input', $(el)).each(function(i,e){
      var old_name = $(e).attr('name')
      var old_id = $(e).attr('id')
      $(e).attr('name', old_name.replace(from, to))
      $(e).attr('id', old_id.replace(from, to))
      $(e).val('')
      })
}

function add_inline_button() {
  $(".inline-group p.tools").bind("click", function(e) {
      var rows = $(this).parents("div.inline-group").find("tr");
      var last = $(rows[rows.length-1]);
      var copy = last.clone(true);
      if (last.hasClass("row1")) {
      copy.attr("class", "row2");
      } else {
      copy.attr("class", "row1");
      }
      last.after(copy);
      $($(this).parents("div.inline-group").find("input")[0]).val(rows.length);
      increment_form_ids(copy, rows.length-1);
      return false;
      });
}

$(document).ready(add_inline_button);
