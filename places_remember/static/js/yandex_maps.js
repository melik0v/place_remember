ymaps.ready(init);

    function init() {
        // Создание карты.
        // https://tech.yandex.ru/maps/doc/jsapi/2.1/dg/concepts/map-docpage/
        let center = [56.010566, 92.852571]

        if (document.getElementById("id_place").value)
                {
                    try {
                        center = [...document.getElementById("id_place").value.split(',')]
                    } catch(e) {
                        center = [56.010566, 92.852571]
                    }

                    var myPlacemark = new ymaps.Placemark(center);
                    myCollection.add(myPlacemark)
                    myMap.geoObjects.add(myCollection);
                }

        var myMap = new ymaps.Map("map", {

            // Координаты центра карты.
            // Порядок по умолчнию: «широта, долгота».
            center: center,

            // Уровень масштабирования. Допустимые значения:
            // от 0 (весь мир) до 19.
            zoom: 12,
            // Элементы управления
            // https://tech.yandex.ru/maps/doc/jsapi/2.1/dg/concepts/controls/standard-docpage/
            controls: [

                'zoomControl', // Ползунок масштаба
                'rulerControl', // Линейка
                'routeButtonControl', // Панель маршрутизации
                'trafficControl', // Пробки
                'typeSelector', // Переключатель слоев карты
                'fullscreenControl', // Полноэкранный режим

                // Поисковая строка
                new ymaps.control.SearchControl({
                    options: {
                        // вид - поисковая строка
                        size: 'medium',
                        // Включим возможность искать не только топонимы, но и организации.
                        provider: 'yandex#search'
                    }
                })

            ]
        });
        var myCollection = new ymaps.GeoObjectCollection();



        myMap.events.add('click', function (e) {

            myCollection.removeAll();
            // Получение координат щелчка
            var coords = e.get('coords');
            // for (i = 0; i < coords.length; ++i) {
            //     coords[i] = coords[i].toFixed(6);
            // }
            //alert(coords.join(', '));
            var myPlacemark = new ymaps.Placemark([...coords]);
            myCollection.add(myPlacemark)
            myMap.geoObjects.add(myCollection);

            document.getElementById("id_place").value = coords.reverse().join(',');

        });

    }
