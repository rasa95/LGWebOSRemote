# LGWebOSRemote
Command line webOS remote for LGTVs. This tool uses a connection via websockets to port 3000 on newer LG TVs, there are other tools which use a restful connection to port 8080 however that port is closed on newer firmware versions.

## Supported models

### Tested with

  * UF830V
  * UH650V
  * UJ635V
  * UF776V
  * HU80KG.AEU (CineBeam 4K)
  * OLED55B7
  * SK8500PLA
  * 49UK6300MLB
  * [please add more!]

Tested with python 2.7.2 on windows and works fine, expect fiew things mentioned in Bugs.

### Likely supports

All devices 

## Available Commands
    scan
    auth                  Hostname/IP     Authenticate and exit, creates initial config .lgtv.json
    audioStatus           
    audioVolume           
    closeApp              appid
    getTVChannel          
    input3DOff            
    input3DOn             
    inputChannelDown      
    inputChannelUp        
    inputMediaFastForward  
    inputMediaPause       
    inputMediaPlay        
    inputMediaRewind      
    inputMediaStop        
    listApps              
    listChannels          
    listInputs            
    listServices          
    mute                  {muted}
    notification          {message}
    off                   
    on                    
    openAppWithPayload    {payload}
    openBrowserAt         {url}
    openYoutubeId         {videoid}
    openYoutubeURL        {url}
    setInput              {input_id}
    setTVChannel          {channel}
    setVolume             {level}
    startApp              {appid}
    swInfo                
    volumeDown            
    volumeUp

## Install

Requires wakeonlan, websocket for python and arp (in Debian/Ubuntu: apt-get install net-tools)
    
    pip install git+https://github.com/rasa95/LGWebOSRemote

## Example usage
    # Scan/Authenticate
    $ lgtv scan 
    {
        "count": 1, 
        "list": [
            {
                "address": "192.168.1.231", 
                "model": "UF830V", 
                "uuid": "10f34f86-0664-f223-4b8f-d16a772d9baf"
            }
        ], 
        "result": "ok"
    }
    $ lgtv auth 192.168.1.231
    
    $ lgtv on
    $ lgtv off

    # If you have the youtube plugin
    $ lgtv openYoutubeURL https://www.youtube.com/watch?v=dQw4w9WgXcQ

    # Otherwise, this works reasonably well
    $ lgtv openBrowserAt https://www.youtube.com/tv#/watch?v=dQw4w9WgXcQ

## Caveats

You need to auth with the TV before being able to use the on command as it requires the mac address.

## Bugs

Scan is not working  
Auth is only working with predefined parameters
