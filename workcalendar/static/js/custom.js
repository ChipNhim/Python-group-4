$(function () {
    fade_alerts();
    // Set default date range of week from Monday to Sunday
    const date_range = get_date_range_in_week(new Date());
    const date_range_approve = get_date_range_in_week(new Date(), 7);
    set_date_range(date_range[0], date_range[1]);
    set_date_range_1(date_range_approve[0], date_range_approve[1]);
    current_href = window.location.href
    if (current_href.includes("car/list_approve")&&
        !current_href.includes("date_from"))
    {
        test=window.location.origin + '/car/list_approve?date_from=' +
          date_range[0] + '&date_to=' + date_range[1];
        window.location.href = test
        // history.pushState({},"", test)
    };
    if (current_href.includes("dashboard/list_calendar") &&
        !current_href.includes("date_from=")) {
        test = window.location.origin + 
            '/dashboard/list_calendar?date_from=' +
            date_range[0] + '&date_to=' + date_range[1];
        window.location.href = test
    };
  });
  
  function fade_alerts() {
    var alerts = document.getElementsByClassName('msg');
    var i = alerts.length;
    for (let elem of alerts) {
      i--;
      time = 3250 + 1000 * i;
      setTimeout(function () {
        $(elem).fadeOut('slow');
      }, time);
    }
  }
  
  function get_date_range_in_week(rnd_date, step = 0) {
    const curr = format_date(rnd_date);
  
    var monday_date = format_date();
  
    const monday = 1 - curr.getDay(); // monday: 1 (day of week)
    monday_date.setDate(monday_date.getDate() + monday + step);
  
    var sunday_date = format_date();
  
    const sunday = 7 - curr.getDay(); // sunday: 0 (day of week)
    sunday_date.setDate(sunday_date.getDate() + sunday + step);
  
    return [monday_date.toISOString().split('T')[0], sunday_date.toISOString().split('T')[0]];
  }
  
  // Set default date range of week from Monday to Sunday
  function set_date_range(date_from, date_end) {
    $('#date-from').val(date_from);
    $('#date-to').val(date_end);
    // const url = window.location.href; 
  }
  function set_date_range_1(date_from, date_end) {
    $('#date-from-approve').val(date_from);
    $('#date-to-approve').val(date_end);
    // const url = window.location.href; 
  }  
  function format_date(value = new Date()) {
    return new Date(value.toISOString().split('T')[0]);
  }