/*
 * requestAnimationFrame polyfill
 */
if (!window.requestAnimationFrame)
{
    window.requestAnimationFrame = (window.webkitRequestAnimationFrame || window.mozRequestAnimationFrame || window.msRequestAnimationFrame || window.oRequestAnimationFrame || function (callback)
    {
        'use strict';
        return window.setTimeout(callback, 1000 / 60);
    });
}

/*!
 * Mantis.js / jQuery / Zepto.js plugin for Constellation
 * @author Acauã Montiel (significantly modified by Greg Olmschenk)
 * @license http://acaua.mit-license.org/
 */
(function ($, window)
{
    'use strict';
    /**
     * Makes a nice constellation on canvas
     * @constructor Constellation
     */
    function Constellation(canvas, options)
    {
        var $canvas = $(canvas),
            context = canvas.getContext('2d'),
            defaults = {
                star: {
                    color: 'rgba(255, 255, 255, 0.5)',
                    width: 2.0
                },
                line: {
                    color: 'rgba(255, 255, 255, 0.2)',
                    width: 1.0
                },
                position: {
                    x: 0, // This value will be overwritten at startup
                    y: 0 // This value will be overwritten at startup
                },
                width: window.innerWidth,
                height: window.innerHeight,
                velocity: 0.2,
                numberOfStars: 15 + 0.030 * (window.innerWidth + window.innerHeight),
                distanceBetweenStars: 10 + 0.044 * (window.innerWidth + window.innerHeight),
                distanceFromMouse: 10 + 0.077 * (window.innerWidth + window.innerHeight),
                stars: []
            },
            config = $.extend(true, {}, defaults, options);

        function Star()
        {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;

            this.vx = (config.velocity * (Math.random() - 0.5) * 2.0);
            this.vy = (config.velocity * (Math.random() - 0.5) * 2.0);

            this.radius = Math.random() * config.star.width;
        }

        Star.prototype = {
            create: function ()
            {
                context.beginPath();
                context.arc(this.x, this.y, this.radius, 0, Math.PI * 2, false);
                context.fill();
            },

            animate: function ()
            {
                var i, star;

                for (i = 0; i < config.numberOfStars; i++)
                {

                    star = config.stars[i];

                    if (star.y < 0 || star.y > canvas.height)
                    {
                        star.vy = -star.vy;
                    }
                    else if (star.x < 0 || star.x > canvas.width)
                    {
                        star.vx = -star.vx;
                    }

                    star.x += star.vx;
                    star.y += star.vy;
                }
            },

            line: function ()
            {
                var numberOfStars = config.numberOfStars,
                    iStar,
                    jStar,
                    i,
                    j;

                for (i = 0; i < numberOfStars; i++)
                {
                    iStar = config.stars[i];
                    if (
                        (iStar.x - config.position.x) < config.distanceFromMouse &&
                        (iStar.y - config.position.y) < config.distanceFromMouse &&
                        (iStar.x - config.position.x) > -config.distanceFromMouse &&
                        (iStar.y - config.position.y) > -config.distanceFromMouse
                    )
                    {
                        for (j = 0; j < numberOfStars; j++)
                        {
                            jStar = config.stars[j];

                            if (
                                (iStar.x - jStar.x) < config.distanceBetweenStars &&
                                (iStar.y - jStar.y) < config.distanceBetweenStars &&
                                (iStar.x - jStar.x) > -config.distanceBetweenStars &&
                                (iStar.y - jStar.y) > -config.distanceBetweenStars
                            )
                            {
                                context.beginPath();
                                context.moveTo(iStar.x, iStar.y);
                                context.lineTo(jStar.x, jStar.y);
                                context.stroke();
                                context.closePath();
                            }
                        }
                    }
                }
            }
        };

        this.createStars = function ()
        {
            var numberOfStars = config.numberOfStars,
                star,
                i;

            context.clearRect(0, 0, canvas.width, canvas.height);

            for (i = 0; i < numberOfStars; i++)
            {
                config.stars.push(new Star());
                star = config.stars[i];

                star.create();
            }

            star.line();
            star.animate();
        };

        this.setCanvas = function ()
        {
            canvas.width = config.width;
            canvas.height = config.height;
        };

        this.setContext = function ()
        {
            context.fillStyle = config.star.color;
            context.strokeStyle = config.line.color;
            context.lineWidth = config.line.width;
        };

        this.setInitialPosition = function ()
        {
            if (!options || !options.hasOwnProperty('position'))
            {
                config.position = {
                    x: canvas.width * 0.5,
                    y: canvas.height * 0.5
                };
            }
        };

        this.loop = function (callback)
        {
            callback();

            window.requestAnimationFrame(function ()
            {
                this.loop(callback);
            }.bind(this));
        };

        this.bind = function ()
        {
            $('body').on('mousemove', function (e)
            {
                config.position.x = e.pageX - $canvas.offset().left;
                config.position.y = e.pageY - $canvas.offset().top;
            });
        };

        this.init = function ()
        {
            this.setCanvas();
            this.setContext();
            this.setInitialPosition();
            this.loop(this.createStars);
            this.bind();
        };
    }

    $.fn.constellation = function (options)
    {
        return $(this).each(function ()
        {
            var c = new Constellation(this, options);
            c.init();
        });
    };
})($, window);

// Init plugin
$('canvas').constellation({});
