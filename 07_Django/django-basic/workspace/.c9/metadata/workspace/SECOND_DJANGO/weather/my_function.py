{"changed":true,"filter":false,"title":"my_function.py","tooltip":"/SECOND_DJANGO/weather/my_function.py","value":"from IPython import embed # 얘는 함수 안에 없어도 된다, 디버깅 잡아주는 애\n\ndef get_weather(input_location):\n    \n    from darksky import forecast\n    from geopy.geocoders import Nominatim\n\n    API_KEY = 'd47b16e36ef06715e86efaf2f8753fb4'\n    geo = Nominatim(user_agent='dr weather app')\n    \n    \n    l = geo.geocode(input_location)\n    # geo_data = (l.latitude, l.longitude)\n    lat = l.latitude\n    lon = l.longitude\n    location = forecast(API_KEY, lat, lon)\n    temp = round((float(location.currently['temperature']) -32) * 5 / 9, 2)\n    summary = location.currently['summary']\n    time = location.time\n    \n    return (lat, lon, temp, summary, time)\n    \n# get_weather('멀티캠퍼스')\n# embed()\n","undoManager":{"mark":96,"position":100,"stack":[[{"start":{"row":14,"column":19},"end":{"row":14,"column":20},"action":"insert","lines":["."],"id":276},{"start":{"row":14,"column":20},"end":{"row":14,"column":21},"action":"insert","lines":["c"]},{"start":{"row":14,"column":21},"end":{"row":14,"column":22},"action":"insert","lines":["u"]},{"start":{"row":14,"column":22},"end":{"row":14,"column":23},"action":"insert","lines":["r"]},{"start":{"row":14,"column":23},"end":{"row":14,"column":24},"action":"insert","lines":["r"]},{"start":{"row":14,"column":24},"end":{"row":14,"column":25},"action":"insert","lines":["e"]},{"start":{"row":14,"column":25},"end":{"row":14,"column":26},"action":"insert","lines":["n"]},{"start":{"row":14,"column":26},"end":{"row":14,"column":27},"action":"insert","lines":["t"]}],[{"start":{"row":14,"column":26},"end":{"row":14,"column":27},"action":"remove","lines":["t"],"id":277}],[{"start":{"row":14,"column":26},"end":{"row":14,"column":27},"action":"insert","lines":["t"],"id":278},{"start":{"row":14,"column":27},"end":{"row":14,"column":28},"action":"insert","lines":["l"]},{"start":{"row":14,"column":28},"end":{"row":14,"column":29},"action":"insert","lines":["y"]}],[{"start":{"row":14,"column":29},"end":{"row":14,"column":31},"action":"insert","lines":["[]"],"id":279}],[{"start":{"row":14,"column":30},"end":{"row":14,"column":32},"action":"insert","lines":["''"],"id":280}],[{"start":{"row":14,"column":31},"end":{"row":14,"column":32},"action":"insert","lines":["t"],"id":281},{"start":{"row":14,"column":32},"end":{"row":14,"column":33},"action":"insert","lines":["e"]},{"start":{"row":14,"column":33},"end":{"row":14,"column":34},"action":"insert","lines":["m"]},{"start":{"row":14,"column":34},"end":{"row":14,"column":35},"action":"insert","lines":["p"]}],[{"start":{"row":14,"column":35},"end":{"row":14,"column":36},"action":"insert","lines":["e"],"id":282},{"start":{"row":14,"column":36},"end":{"row":14,"column":37},"action":"insert","lines":["r"]},{"start":{"row":14,"column":37},"end":{"row":14,"column":38},"action":"insert","lines":["a"]},{"start":{"row":14,"column":38},"end":{"row":14,"column":39},"action":"insert","lines":["t"]},{"start":{"row":14,"column":39},"end":{"row":14,"column":40},"action":"insert","lines":["u"]},{"start":{"row":14,"column":40},"end":{"row":14,"column":41},"action":"insert","lines":["r"]}],[{"start":{"row":14,"column":41},"end":{"row":14,"column":42},"action":"insert","lines":["e"],"id":283}],[{"start":{"row":14,"column":44},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":284},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]},{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"insert","lines":["s"]},{"start":{"row":15,"column":5},"end":{"row":15,"column":6},"action":"insert","lines":["u"]},{"start":{"row":15,"column":6},"end":{"row":15,"column":7},"action":"insert","lines":["m"]},{"start":{"row":15,"column":7},"end":{"row":15,"column":8},"action":"insert","lines":["m"]}],[{"start":{"row":15,"column":8},"end":{"row":15,"column":9},"action":"insert","lines":["a"],"id":285}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":9},"action":"remove","lines":["summa"],"id":286},{"start":{"row":15,"column":4},"end":{"row":15,"column":11},"action":"insert","lines":["summary"]}],[{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"insert","lines":[" "],"id":287},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"insert","lines":["="]}],[{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"insert","lines":[" "],"id":288},{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"insert","lines":["l"]},{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"insert","lines":["o"]},{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"insert","lines":["c"]},{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"insert","lines":["a"]},{"start":{"row":15,"column":18},"end":{"row":15,"column":19},"action":"insert","lines":["i"]}],[{"start":{"row":15,"column":18},"end":{"row":15,"column":19},"action":"remove","lines":["i"],"id":289}],[{"start":{"row":15,"column":18},"end":{"row":15,"column":19},"action":"insert","lines":["t"],"id":290},{"start":{"row":15,"column":19},"end":{"row":15,"column":20},"action":"insert","lines":["i"]},{"start":{"row":15,"column":20},"end":{"row":15,"column":21},"action":"insert","lines":["o"]},{"start":{"row":15,"column":21},"end":{"row":15,"column":22},"action":"insert","lines":["n"]},{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"insert","lines":["."]},{"start":{"row":15,"column":23},"end":{"row":15,"column":24},"action":"insert","lines":["c"]},{"start":{"row":15,"column":24},"end":{"row":15,"column":25},"action":"insert","lines":["u"]}],[{"start":{"row":15,"column":23},"end":{"row":15,"column":25},"action":"remove","lines":["cu"],"id":291},{"start":{"row":15,"column":23},"end":{"row":15,"column":32},"action":"insert","lines":["currently"]}],[{"start":{"row":15,"column":32},"end":{"row":15,"column":33},"action":"insert","lines":["'"],"id":292}],[{"start":{"row":15,"column":32},"end":{"row":15,"column":33},"action":"remove","lines":["'"],"id":293}],[{"start":{"row":15,"column":32},"end":{"row":15,"column":34},"action":"insert","lines":["[]"],"id":294}],[{"start":{"row":15,"column":33},"end":{"row":15,"column":35},"action":"insert","lines":["''"],"id":295}],[{"start":{"row":15,"column":34},"end":{"row":15,"column":35},"action":"insert","lines":["s"],"id":296},{"start":{"row":15,"column":35},"end":{"row":15,"column":36},"action":"insert","lines":["u"]}],[{"start":{"row":15,"column":34},"end":{"row":15,"column":36},"action":"remove","lines":["su"],"id":297},{"start":{"row":15,"column":34},"end":{"row":15,"column":37},"action":"insert","lines":["sum"]}],[{"start":{"row":15,"column":37},"end":{"row":15,"column":38},"action":"insert","lines":["m"],"id":298}],[{"start":{"row":15,"column":34},"end":{"row":15,"column":38},"action":"remove","lines":["summ"],"id":299},{"start":{"row":15,"column":34},"end":{"row":15,"column":41},"action":"insert","lines":["summary"]}],[{"start":{"row":15,"column":43},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":300},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":301}],[{"start":{"row":16,"column":43},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":302},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":5},"action":"insert","lines":["r"],"id":303},{"start":{"row":17,"column":5},"end":{"row":17,"column":6},"action":"insert","lines":["e"]},{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"insert","lines":["t"]},{"start":{"row":17,"column":7},"end":{"row":17,"column":8},"action":"insert","lines":["u"]},{"start":{"row":17,"column":8},"end":{"row":17,"column":9},"action":"insert","lines":["r"]},{"start":{"row":17,"column":9},"end":{"row":17,"column":10},"action":"insert","lines":["n"]}],[{"start":{"row":17,"column":10},"end":{"row":17,"column":11},"action":"insert","lines":[" "],"id":304}],[{"start":{"row":17,"column":11},"end":{"row":17,"column":13},"action":"insert","lines":["()"],"id":305}],[{"start":{"row":17,"column":12},"end":{"row":17,"column":13},"action":"insert","lines":["l"],"id":306},{"start":{"row":17,"column":13},"end":{"row":17,"column":14},"action":"insert","lines":[","]}],[{"start":{"row":17,"column":13},"end":{"row":17,"column":14},"action":"remove","lines":[","],"id":307}],[{"start":{"row":17,"column":13},"end":{"row":17,"column":14},"action":"insert","lines":["."],"id":308}],[{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"insert","lines":["l"],"id":309},{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"insert","lines":["a"]},{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"insert","lines":["t"]}],[{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"insert","lines":[" "],"id":310},{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"insert","lines":["="]}],[{"start":{"row":13,"column":9},"end":{"row":13,"column":10},"action":"insert","lines":[" "],"id":311},{"start":{"row":13,"column":10},"end":{"row":13,"column":11},"action":"insert","lines":["l"]},{"start":{"row":13,"column":11},"end":{"row":13,"column":12},"action":"insert","lines":["."]}],[{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"insert","lines":["l"],"id":312},{"start":{"row":13,"column":13},"end":{"row":13,"column":14},"action":"insert","lines":["a"]}],[{"start":{"row":13,"column":12},"end":{"row":13,"column":14},"action":"remove","lines":["la"],"id":313},{"start":{"row":13,"column":12},"end":{"row":13,"column":20},"action":"insert","lines":["latitude"]}],[{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"insert","lines":[";"],"id":314}],[{"start":{"row":13,"column":21},"end":{"row":13,"column":22},"action":"insert","lines":[" "],"id":315},{"start":{"row":13,"column":22},"end":{"row":13,"column":23},"action":"insert","lines":["l"]},{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"insert","lines":["o"]}],[{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"insert","lines":["n"],"id":316}],[{"start":{"row":13,"column":25},"end":{"row":13,"column":26},"action":"insert","lines":[" "],"id":317},{"start":{"row":13,"column":26},"end":{"row":13,"column":27},"action":"insert","lines":["="]}],[{"start":{"row":13,"column":27},"end":{"row":13,"column":28},"action":"insert","lines":[" "],"id":318},{"start":{"row":13,"column":28},"end":{"row":13,"column":29},"action":"insert","lines":["l"]},{"start":{"row":13,"column":29},"end":{"row":13,"column":30},"action":"insert","lines":["."]},{"start":{"row":13,"column":30},"end":{"row":13,"column":31},"action":"insert","lines":["l"]},{"start":{"row":13,"column":31},"end":{"row":13,"column":32},"action":"insert","lines":["o"]}],[{"start":{"row":13,"column":30},"end":{"row":13,"column":32},"action":"remove","lines":["lo"],"id":319},{"start":{"row":13,"column":30},"end":{"row":13,"column":39},"action":"insert","lines":["longitude"]}],[{"start":{"row":14,"column":33},"end":{"row":14,"column":43},"action":"remove","lines":["l.latitude"],"id":320}],[{"start":{"row":14,"column":33},"end":{"row":14,"column":34},"action":"insert","lines":["a"],"id":321},{"start":{"row":14,"column":34},"end":{"row":14,"column":35},"action":"insert","lines":["t"]}],[{"start":{"row":14,"column":34},"end":{"row":14,"column":35},"action":"remove","lines":["t"],"id":322},{"start":{"row":14,"column":33},"end":{"row":14,"column":34},"action":"remove","lines":["a"]}],[{"start":{"row":14,"column":33},"end":{"row":14,"column":34},"action":"insert","lines":["l"],"id":323},{"start":{"row":14,"column":34},"end":{"row":14,"column":35},"action":"insert","lines":["a"]},{"start":{"row":14,"column":35},"end":{"row":14,"column":36},"action":"insert","lines":["t"]}],[{"start":{"row":14,"column":38},"end":{"row":14,"column":49},"action":"remove","lines":["l.longitude"],"id":324}],[{"start":{"row":14,"column":38},"end":{"row":14,"column":39},"action":"insert","lines":["l"],"id":325},{"start":{"row":14,"column":39},"end":{"row":14,"column":40},"action":"insert","lines":["o"]},{"start":{"row":14,"column":40},"end":{"row":14,"column":41},"action":"insert","lines":["n"]}],[{"start":{"row":17,"column":13},"end":{"row":17,"column":14},"action":"remove","lines":["."],"id":326}],[{"start":{"row":17,"column":13},"end":{"row":17,"column":14},"action":"insert","lines":["a"],"id":327},{"start":{"row":17,"column":14},"end":{"row":17,"column":15},"action":"insert","lines":["t"]},{"start":{"row":17,"column":15},"end":{"row":17,"column":16},"action":"insert","lines":[","]}],[{"start":{"row":17,"column":16},"end":{"row":17,"column":17},"action":"insert","lines":[" "],"id":328},{"start":{"row":17,"column":17},"end":{"row":17,"column":18},"action":"insert","lines":["l"]},{"start":{"row":17,"column":18},"end":{"row":17,"column":19},"action":"insert","lines":["o"]},{"start":{"row":17,"column":19},"end":{"row":17,"column":20},"action":"insert","lines":["n"]},{"start":{"row":17,"column":20},"end":{"row":17,"column":21},"action":"insert","lines":[","]}],[{"start":{"row":17,"column":21},"end":{"row":17,"column":22},"action":"insert","lines":[" "],"id":329},{"start":{"row":17,"column":22},"end":{"row":17,"column":23},"action":"insert","lines":["t"]},{"start":{"row":17,"column":23},"end":{"row":17,"column":24},"action":"insert","lines":["e"]},{"start":{"row":17,"column":24},"end":{"row":17,"column":25},"action":"insert","lines":["m"]},{"start":{"row":17,"column":25},"end":{"row":17,"column":26},"action":"insert","lines":["p"]},{"start":{"row":17,"column":26},"end":{"row":17,"column":27},"action":"insert","lines":[","]}],[{"start":{"row":17,"column":27},"end":{"row":17,"column":28},"action":"insert","lines":[" "],"id":330},{"start":{"row":17,"column":28},"end":{"row":17,"column":29},"action":"insert","lines":["s"]},{"start":{"row":17,"column":29},"end":{"row":17,"column":30},"action":"insert","lines":["u"]},{"start":{"row":17,"column":30},"end":{"row":17,"column":31},"action":"insert","lines":["m"]},{"start":{"row":17,"column":31},"end":{"row":17,"column":32},"action":"insert","lines":["m"]}],[{"start":{"row":17,"column":28},"end":{"row":17,"column":32},"action":"remove","lines":["summ"],"id":331},{"start":{"row":17,"column":28},"end":{"row":17,"column":35},"action":"insert","lines":["summary"]}],[{"start":{"row":16,"column":43},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":332},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]},{"start":{"row":17,"column":4},"end":{"row":17,"column":5},"action":"insert","lines":["t"]},{"start":{"row":17,"column":5},"end":{"row":17,"column":6},"action":"insert","lines":["i"]},{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"insert","lines":["m"]},{"start":{"row":17,"column":7},"end":{"row":17,"column":8},"action":"insert","lines":["e"]}],[{"start":{"row":17,"column":8},"end":{"row":17,"column":9},"action":"insert","lines":[" "],"id":333},{"start":{"row":17,"column":9},"end":{"row":17,"column":10},"action":"insert","lines":["="]}],[{"start":{"row":17,"column":10},"end":{"row":17,"column":11},"action":"insert","lines":[" "],"id":334},{"start":{"row":17,"column":11},"end":{"row":17,"column":12},"action":"insert","lines":["l"]},{"start":{"row":17,"column":12},"end":{"row":17,"column":13},"action":"insert","lines":["o"]},{"start":{"row":17,"column":13},"end":{"row":17,"column":14},"action":"insert","lines":["c"]},{"start":{"row":17,"column":14},"end":{"row":17,"column":15},"action":"insert","lines":["a"]},{"start":{"row":17,"column":15},"end":{"row":17,"column":16},"action":"insert","lines":["t"]},{"start":{"row":17,"column":16},"end":{"row":17,"column":17},"action":"insert","lines":["i"]},{"start":{"row":17,"column":17},"end":{"row":17,"column":18},"action":"insert","lines":["o"]}],[{"start":{"row":17,"column":18},"end":{"row":17,"column":19},"action":"insert","lines":["n"],"id":335},{"start":{"row":17,"column":19},"end":{"row":17,"column":20},"action":"insert","lines":[","]}],[{"start":{"row":17,"column":19},"end":{"row":17,"column":20},"action":"remove","lines":[","],"id":336}],[{"start":{"row":17,"column":19},"end":{"row":17,"column":20},"action":"insert","lines":["."],"id":337},{"start":{"row":17,"column":20},"end":{"row":17,"column":21},"action":"insert","lines":["t"]},{"start":{"row":17,"column":21},"end":{"row":17,"column":22},"action":"insert","lines":["i"]},{"start":{"row":17,"column":22},"end":{"row":17,"column":23},"action":"insert","lines":["m"]},{"start":{"row":17,"column":23},"end":{"row":17,"column":24},"action":"insert","lines":["e"]}],[{"start":{"row":18,"column":35},"end":{"row":18,"column":36},"action":"insert","lines":[","],"id":338}],[{"start":{"row":18,"column":36},"end":{"row":18,"column":37},"action":"insert","lines":[" "],"id":339},{"start":{"row":18,"column":37},"end":{"row":18,"column":38},"action":"insert","lines":["t"]},{"start":{"row":18,"column":38},"end":{"row":18,"column":39},"action":"insert","lines":["i"]},{"start":{"row":18,"column":39},"end":{"row":18,"column":40},"action":"insert","lines":["m"]},{"start":{"row":18,"column":40},"end":{"row":18,"column":41},"action":"insert","lines":["e"]}],[{"start":{"row":17,"column":24},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":340},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":13,"column":21},"end":{"row":13,"column":22},"action":"remove","lines":[" "],"id":341},{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"remove","lines":[";"]}],[{"start":{"row":13,"column":20},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":342},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":21,"column":4},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":343},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"remove","lines":["    "],"id":344}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":1},"action":"insert","lines":["g"],"id":345},{"start":{"row":22,"column":1},"end":{"row":22,"column":2},"action":"insert","lines":["e"]},{"start":{"row":22,"column":2},"end":{"row":22,"column":3},"action":"insert","lines":["t"]},{"start":{"row":22,"column":3},"end":{"row":22,"column":4},"action":"insert","lines":["_"]}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"remove","lines":["get_"],"id":346},{"start":{"row":22,"column":0},"end":{"row":22,"column":13},"action":"insert","lines":["get_weather()"]}],[{"start":{"row":22,"column":12},"end":{"row":22,"column":14},"action":"insert","lines":["''"],"id":347}],[{"start":{"row":22,"column":13},"end":{"row":22,"column":14},"action":"insert","lines":["a"],"id":348},{"start":{"row":22,"column":14},"end":{"row":22,"column":15},"action":"insert","lines":["j"]},{"start":{"row":22,"column":15},"end":{"row":22,"column":16},"action":"insert","lines":["f"]},{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"insert","lines":["x"]}],[{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"remove","lines":["x"],"id":349},{"start":{"row":22,"column":15},"end":{"row":22,"column":16},"action":"remove","lines":["f"]},{"start":{"row":22,"column":14},"end":{"row":22,"column":15},"action":"remove","lines":["j"]},{"start":{"row":22,"column":13},"end":{"row":22,"column":14},"action":"remove","lines":["a"]}],[{"start":{"row":22,"column":13},"end":{"row":22,"column":14},"action":"insert","lines":["멀"],"id":354}],[{"start":{"row":22,"column":14},"end":{"row":22,"column":15},"action":"insert","lines":["티"],"id":357}],[{"start":{"row":22,"column":15},"end":{"row":22,"column":16},"action":"insert","lines":["캠"],"id":359}],[{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"insert","lines":["퍼"],"id":363}],[{"start":{"row":22,"column":17},"end":{"row":22,"column":18},"action":"insert","lines":["스"],"id":364}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":2},"action":"insert","lines":["# "],"id":365}],[{"start":{"row":23,"column":0},"end":{"row":23,"column":2},"action":"remove","lines":["# "],"id":366}],[{"start":{"row":16,"column":44},"end":{"row":16,"column":45},"action":"insert","lines":[" "],"id":367},{"start":{"row":16,"column":45},"end":{"row":16,"column":46},"action":"insert","lines":["-"]},{"start":{"row":16,"column":46},"end":{"row":16,"column":47},"action":"insert","lines":["3"]},{"start":{"row":16,"column":47},"end":{"row":16,"column":48},"action":"insert","lines":["2"]}],[{"start":{"row":16,"column":48},"end":{"row":16,"column":49},"action":"insert","lines":[")"],"id":368}],[{"start":{"row":16,"column":11},"end":{"row":16,"column":12},"action":"insert","lines":["("],"id":369}],[{"start":{"row":16,"column":50},"end":{"row":16,"column":51},"action":"insert","lines":[" "],"id":370},{"start":{"row":16,"column":51},"end":{"row":16,"column":52},"action":"insert","lines":["*"]}],[{"start":{"row":16,"column":52},"end":{"row":16,"column":53},"action":"insert","lines":[" "],"id":371},{"start":{"row":16,"column":53},"end":{"row":16,"column":54},"action":"insert","lines":["5"]}],[{"start":{"row":16,"column":54},"end":{"row":16,"column":55},"action":"insert","lines":[" "],"id":372},{"start":{"row":16,"column":55},"end":{"row":16,"column":56},"action":"insert","lines":["/"]}],[{"start":{"row":16,"column":56},"end":{"row":16,"column":57},"action":"insert","lines":[" "],"id":373},{"start":{"row":16,"column":57},"end":{"row":16,"column":58},"action":"insert","lines":["9"]}],[{"start":{"row":16,"column":12},"end":{"row":16,"column":13},"action":"insert","lines":["리"],"id":375}],[{"start":{"row":16,"column":12},"end":{"row":16,"column":13},"action":"remove","lines":["리"],"id":377}],[{"start":{"row":16,"column":12},"end":{"row":16,"column":13},"action":"insert","lines":["f"],"id":378},{"start":{"row":16,"column":13},"end":{"row":16,"column":14},"action":"insert","lines":["l"]},{"start":{"row":16,"column":14},"end":{"row":16,"column":15},"action":"insert","lines":["o"]},{"start":{"row":16,"column":15},"end":{"row":16,"column":16},"action":"insert","lines":["a"]},{"start":{"row":16,"column":16},"end":{"row":16,"column":17},"action":"insert","lines":["t"]}],[{"start":{"row":16,"column":17},"end":{"row":16,"column":18},"action":"insert","lines":["("],"id":379}],[{"start":{"row":16,"column":51},"end":{"row":16,"column":52},"action":"insert","lines":[")"],"id":380}],[{"start":{"row":16,"column":11},"end":{"row":16,"column":12},"action":"insert","lines":["r"],"id":384},{"start":{"row":16,"column":12},"end":{"row":16,"column":13},"action":"insert","lines":["o"]},{"start":{"row":16,"column":13},"end":{"row":16,"column":14},"action":"insert","lines":["u"]},{"start":{"row":16,"column":14},"end":{"row":16,"column":15},"action":"insert","lines":["n"]},{"start":{"row":16,"column":15},"end":{"row":16,"column":16},"action":"insert","lines":["d"]}],[{"start":{"row":16,"column":70},"end":{"row":16,"column":71},"action":"insert","lines":[","],"id":385}],[{"start":{"row":16,"column":71},"end":{"row":16,"column":72},"action":"insert","lines":[" "],"id":386},{"start":{"row":16,"column":72},"end":{"row":16,"column":73},"action":"insert","lines":["2"]},{"start":{"row":16,"column":73},"end":{"row":16,"column":74},"action":"insert","lines":[")"]}],[{"start":{"row":16,"column":17},"end":{"row":16,"column":18},"action":"insert","lines":["("],"id":387}],[{"start":{"row":23,"column":0},"end":{"row":23,"column":2},"action":"insert","lines":["# "],"id":388}],[{"start":{"row":0,"column":43},"end":{"row":0,"column":44},"action":"insert","lines":[","],"id":389}],[{"start":{"row":23,"column":9},"end":{"row":23,"column":10},"action":"insert","lines":[" "],"id":390}],[{"start":{"row":23,"column":9},"end":{"row":23,"column":10},"action":"remove","lines":[" "],"id":391}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":23,"column":9},"end":{"row":23,"column":9},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1548743284869}