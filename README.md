# CardManager
```
  ______        __        _______   ________   ___      ___       __      _____  ___        __       _______    _______   _______   
 /" _  "\      /""\      /"      \ |"      "\ |"  \    /"  |     /""\    (\"   \|"  \      /""\     /" _   "|  /"     "| /"      \  
(: ( \___)    /    \    |:        |(.  ___  :) \   \  //   |    /    \   |.\\   \    |    /    \   (: ( \___) (: ______)|:        | 
 \/ \        /' /\  \   |_____/   )|: \   ) || /\\  \/.    |   /' /\  \  |: \.   \\  |   /' /\  \   \/ \       \/    |  |_____/   ) 
 //  \ _    //  __'  \   //      / (| (___\ |||: \.        |  //  __'  \ |.  \    \. |  //  __'  \  //  \ ___  // ___)_  //      /  
(:   _) \  /   /  \\  \ |:  __   \ |:       :)|.  \    /:  | /   /  \\  \|    \    \ | /   /  \\  \(:   _(  _|(:      "||:  __   \  
 \_______)(___/    \___)|__|  \___)(________/ |___|\__/|___|(___/    \___)\___|\____\)(___/    \___)\_______)  \_______)|__|  \___) 
                                                                                                                                    
```

## Requirements
- python 3.9

## Installation
```bash
git clone https://github.com/yurijGagarin/Cardmanager.git
cd Cardmanager
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp cardmanager/local_settings.py.example  cardmanager/local_settings.py
# edit local_settings.py
```

## Apply migrations
```bash
python manage.py migrate
```

## Apply fixtures

```bash
python manage.py loaddata card/fixtures.json
```

##  Run app

```bash
python manage.py runserver
```