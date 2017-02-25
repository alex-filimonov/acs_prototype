function refresh_device(device_id){
    $.ajax({
        url:'/device_info/index?device_id='+device_id,
        dataType:"text",
        success:function(data,textStatus){
            $('#panel_mng').html(data)
        }
    })
}

function refresh_net(device_id){
    $.ajax({
        url:'/device_info/net_status?device_id='+device_id,
        dataType:"text",
        success:function(data,textStatus){
            $('#panel_net').html(data)
        }
    })
}


function save_main_param(device_id){
    $('#button_save_main_param').addClass( 'disabled' )
    var msg=$('#main_param_form').serialize();
    $.ajax({
        type:"POST",
        url:"/param/save_main",
        data:msg,
        success:function(data,textStatus){
            $('#panel_device_main_param').html(data)
        }

    })
}

function refresh_device_command(device_id){
    $.ajax({
        url:'/device_command/index?device_id='+device_id,
        dataType:"text",
        success:function(data,textStatus){
            $('#panel_device_command').html(data)
        }
    })
}

function refresh_device_main_param(device_id){
    $.ajax({
        url:'/param/index?device_id='+device_id,
        dataType:"text",
        success:function(data,textStatus){
            $('#panel_device_main_param').html(data)
        }
    })
}

function refresh_device_all_param(device_id){
    $.ajax({
        url:'/param/all?device_id='+device_id,
        dataType:"text",
        success:function(data,textStatus){
            $('#panel_device_all_param').html(data)
        }
    })
}

function save_param(device_id,param_name){

    var msg=$('#param_form').serialize();
    $.ajax({
        type:"POST",
        url:"/param/save",
        data:msg,
        success:function(data,textStatus){
            $('#panel_device_all_param').html(data)
        }

    })
}

var time_id=0;

function start_time_refresh(device_id){
    if (time_id==0){
        $('#start_stop_time_button').removeClass('btn-warning');
        $('#start_stop_time_button').addClass('btn-success');
        time_id=setInterval(function() {
                refresh_device(device_id);
                refresh_device_command (device_id);
                refresh_net(device_id)
                }, 2000);
    } else {
        $('#start_stop_time_button').removeClass('btn-success');
        $('#start_stop_time_button').addClass('btn-warning');
        clearInterval(time_id);        
        time_id=0
    }
}


function refresh_all_for_device(device_id){
    refresh_device(device_id);
    refresh_device_command (device_id);
    refresh_device_main_param (device_id);
    refresh_device_all_param(device_id);
    refresh_net(device_id)
}


function power_on(device_id){
    $.ajax({
        url:'/device_command/power_on?device_id='+device_id,
        dataType:"text",
        success:function(data,textStatus){
            $('#panel_mng').html(data)
        }
    })
}

function power_off(device_id){
    $.ajax({
        url:'/device_command/power_off?device_id='+device_id,
        dataType:"text",
        success:function(data,textStatus){
            $('#panel_mng').html(data)
        }
    })
}


function refresh_client_log(device_id){
    $.ajax({
        url:'/netlog/client_log?device_id='+device_id,
        dataType:"text",
        success:function(data,textStatus){
            $('#client_log').html(data)
        }
    })
}

function refresh_listner_log(device_id){
    $.ajax({
        url:'/netlog/listner_log?device_id='+device_id,
        dataType:"text",
        success:function(data,textStatus){
            $('#listner_request_log').html(data)
        }
    })
}



