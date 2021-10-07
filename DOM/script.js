// Thay đổi màu sắc tiêu đề h1
function changePageColor() {
  var color = document.querySelectorAll("p")
  color[0].style.color = "green";
  color[1].style.color = "yellow";
  color[2].style.color = "red";
}

//Thay đổi màu nền trang
function changeBgColor(color){
  document.body.style.backgroundColor = color;
}

// Thay đổi nội dung của đoạn văn paragraph1 thành giống nội dung của đoạn văn paragraph2 (tham số truyền vào là id của 2 đoạn văn hoặc thứ tự của đoạn văn).
function copyContent(id1, id2)
{
  //var content_list = document.querySelectorAll("p")
  var content1 = document.getElementById(id2).innerHTML;
  document.getElementById(id1).textContent = content1
  


}
//changeFontSize(x): Thay đổi kích thước font chữ của cả 3 đoạn văn thành x pixels (x là một số nguyên).
function changeFontSize(x)
{
  content_list = document.querySelectorAll("p")

  for (let index = 0; index < content_list.length; index++) {
    content_list[index].style.fontSize = x + 'px'
  }
}
//increaseFontSize(paragraph): Tăng kích thước font chữ của đoạn văn mong muốn (tham số truyền vào là id đoạn văn hoặc thứ tự đoạn văn) lên 1 pixel so với kích thước hiện tại, kích thước tăng lên không được vượt quá 30 pixels (Sử dụng sau khi gọi hàm changeFontSize() hoặc dùng window.getComputedStyle).
function increaseFontSize(id_paragraph)
{ 
  var element = document.getElementById(id_paragraph);
  style = window.getComputedStyle(element, null).getPropertyValue('font-size');
  currentSize = parseFloat(style);
  if (currentSize < 30) {
    element.style.fontSize = (currentSize + 1) + 'px';
  }
  
  
}

//decreaseFontSize(paragraph): Giảm kích thước font chữ của đoạn văn mong muốn (tham số truyền vào là id đoạn văn hoặc thứ tự đoạn văn) xuống 1 pixels so với kích thước hiện tại, kích thước giảm xuống không vượt quá 10 pixels.
function decreaseFontSize(id_paragraph){
  var element = document.getElementById(id_paragraph);
  style = window.getComputedStyle(element, null).getPropertyValue('font-size');
  currentSize = parseFloat(style);
  if (currentSize > 10) {
    element.style.fontSize = (currentSize - 1) + 'px';
  }
}
