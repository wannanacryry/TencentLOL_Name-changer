# TencentLOL_Name-changer
This program can change Tencent version League of legends in gaming language.
Prerequisites:
1. You need to use the LeagueClient file released by Riot game. You can extract it from the client downloaded by Riot game and directly replace the entire folder of the Tencent version of League of Legends files.
2. In addition to English, your game file must contain the resource file corresponding to the language you want to modify.(Tencent version league of legends client have all English resource file. You can get language files from Riot game released league of legends ).
3. Must be login game by Lolclient.exe. Don't login game by Wegame platfrom , Wegame platfrom will check client file before game running , you can not bypass it.

principle:
Through the normal login method, obtain the startup parameters of LeagueClient.exe. Then change the language part of the startup parameters to the language you want. Then restart LeagueClient.exe with the modified parameters. This way you can skip Riotclientserver.exe's forced locale=zh_CN.
