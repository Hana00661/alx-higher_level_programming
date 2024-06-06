$(document).ready(() => {
  $('INPUT#btn_translate').click(() => {
    const code = $('INPUT#language_code').val();
    $.get(`https://stefanbohacek.com/hellosalut/?lang=${code}`, (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
});
