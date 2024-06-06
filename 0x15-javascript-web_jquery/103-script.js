$(document).ready(() => {
  const callback = () => {
    const code = $('INPUT#language_code').val();
    $.get(`https://stefanbohacek.com/hellosalut/?lang=${code}`, (data) => {
      $('DIV#hello').text(data.hello);
    });
  };

  $('INPUT#language_code').keypress((e) => {
    if (e.keyCode === 13) callback();
  });

  $('INPUT#btn_translate').click(callback);
});
