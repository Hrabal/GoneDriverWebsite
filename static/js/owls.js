$( document ).ready(function() {
    
    var posEyeLeft = $('.left.eyes .retina').offset();
    var posEyeRight = $('.right.eyes .retina').offset();

    var RposEyeLeft = $('.left.eyes .retina').position();
    var RposEyeRight = $('.right.eyes .retina').position();

    $('.square').mousemove(function(e){
        var this_owl = '#' + $(this).attr('id') + ' '

        var posEyeLeft = $(this_owl+'.left.eyes .retina').offset();
        var posEyeRight = $(this_owl+'.right.eyes .retina').offset();

        var RposEyeLeft = $(this_owl+'.left.eyes .retina').position();
        var RposEyeRight = $(this_owl+'.right.eyes .retina').position();

        var posX = e.pageX;
        var posY = e.pageY;
        var posXrelLeft = posX - posEyeLeft.left - 15;
        var posYrelLeft = posY - posEyeLeft.top - 15;
        var posXrelRight = posX - posEyeRight.left - 15;
        var posYrelRight = posY - posEyeRight.top - 15;
        
        var moveXLeft = ( posXrelLeft * 30 ) / $('.square').width(); 
        var moveYLeft = ( posYrelLeft * 30 ) / $('.square').height();
        var moveXRight = ( posXrelRight * 30 ) / $('.square').width(); 
        var moveYRight = ( posYrelRight * 30 ) / $('.square').height();
        
        $(this_owl+'.left.eyes .retina').css('left',RposEyeLeft.left + moveXLeft);
        $(this_owl+'.left.eyes .retina').css('top',RposEyeLeft.top + moveYLeft);
        $(this_owl+'.right.eyes .retina').css('left',RposEyeLeft.left + moveXRight);
        $(this_owl+'.right.eyes .retina').css('top',RposEyeLeft.top + moveYRight);
    });
    $('.square').mouseleave(function(e){
        var this_owl = '#' + $(this).attr('id') + ' '
        $(this_owl+'.left.eyes .retina').css('left',RposEyeLeft.left).css('top',RposEyeLeft.top);
        $(this_owl+'.right.eyes .retina').css('left',RposEyeRight.left).css('top',RposEyeRight.top);
        $(this_owl+'.eyes').toggleClass('closed');
    });

    $('.square').mouseenter(function(e) {
        var this_owl = '#' + $(this).attr('id') + ' '
        $(this_owl+'.eyes').removeClass('closed');
    });


    function randRange(data) {
       var newTime = data[Math.floor(data.length * Math.random())];
       return newTime;
    };

    function toggleSomething() {
        var timeArray = new Array(2000, 2500, 750, 950, 2000, 100, 1000, 1500);
        var owlsArray = [
            '#luca ',
            '#giova ',
            '#fede '
        ];
        var randOwl = owlsArray[Math.floor(Math.random()*owlsArray.length)];

        var eyeArray = ['.left', '.right']
        var randEye = eyeArray[Math.floor(Math.random()*eyeArray.length)];

        $(randOwl+randEye+'.eyes').toggleClass("closed");

        clearInterval(timer);
        timer = setInterval(toggleSomething, randRange(timeArray));
    };

    var timer = setInterval(toggleSomething, 1000);
});