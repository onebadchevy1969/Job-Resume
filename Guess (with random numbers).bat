@echo off
:beginning
set /a rnd=%random% %% 100 + 1 
echo I'm thinking of a number between 1-100
pause  
set /p NUM= Pick a number.
if %NUM%==%rnd% (
echo You're right!
pause
goto end
) else echo you are wrong!It was %rnd%!
pause

:again 
cls 
set /p AGA=Play again? (y/n)
if %AGA%==y (
goto start
) 

if %AGA%== Y (
goto start
)

if %AGA%== N (
goto end
)

if %AGA%==n (
goto end
) else echo pick y or n please.
pause 
goto again 

:start
cls  
set /a rnd=%random% %% 100 + 1 
set /p NUM= Pick a number.
if %NUM%==%rnd% (
echo You're right!
pause
goto end
) else echo you are wrong!It was %rnd%!
pause
goto start 


:end 
echo Goodbye!
timeout 5
close 