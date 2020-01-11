$(document).ready(function () {
    socket = io(location.origin);
    socket.emit('add_user',{
        username : $('p').text()
    });

    $('.send').on('click',()=>{
        var name = $('#name').val();
        socket.emit('private_message',{
            username:name
        });
    });

    socket.on('private_message',(data)=>{
        alert(data)
    });
});