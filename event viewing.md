### event viewing

We are given a .evtx file, which is a Windows logs file

Being honest, I've never touched one of these before so for the first hour or so I either stared at the screen having no idea what to do or looked up on what to look for, which doesn't really help in the end

My teammate, tsumu, said that they have got 2/3 parts of the flag, one in installer the other in registry event.

With that clue in mind, I start scouring through the whole log, at first unfiltered (I hate myself), but then I excluded irrelevant event types `Filter: -4702, -5158, -5156, -5154, -4658, -4656,-4624,-4648,-4690, -4672, -4663, -5152, -10000, -10001`

So these are the base64 I found, which are the 2 parts of the flag. Now to find the third and final part.
``` cGljb0NURntFdjNudF92aTN3djNyXw==
MXNfYV9wcjN0dHlfdXMzZnVsXw==
```

Looking through the logs and when the shut downs (event code 1074) happen, the first instance of instant shutdown is at 2:59:18. I found first part during installer part at 1:55:55 and registry value update at 1:56:19. User created an account named N/A (or log couldn't get the account?)

Afterwards, they installed Visual Studio, so there's lots of legitimate msiinstaller logs, then they restarted and again lots of logs of restarting. After logging in again, at 2:47:12 they accessed the credential manager for user, DESKTOP-EKVR84B$. They are accessed again at 3:00:12 and at 3:02:22. I think this is part of the login process, but at 3:02:30 someone tried to login with blank password on users Administrator, DefaultAccount, Guest, WDAGUtilityAccount.

Oh, at 3:02:25 at the User32 shutdown log, there's a comment containing the third part of the flag `dDAwbF84MWJhM2ZlOX0=`. The answer I guess is to just scour the logs?