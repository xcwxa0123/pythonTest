@ECHO OFF
SETLOCAL ENABLEDELAYEDEXPANSION

@REM 枚举各仓库地址 三期开发git记录选择 四期开发上传ftp

@REM 1、输入时间范围
@REM 2、打印出时间范围内所有提交

ECHO 本程序用于备份所选仓库下git上一次提交的文件,以便上传FTP
ECHO.
ECHO 请选择需要备份的仓库地址,按任意键继续===============^>
pause > nul
FOR /F %%S IN ('MSHTA "%~f0"') DO (
    SET storage_path=%%S
    SET target_storage=%%~dS
)
ECHO 已选择仓库地址: '!storage_path!'

ECHO.
ECHO.
ECHO.
ECHO.

ECHO 请选择备份目标文件夹地址,按任意键继续===============^>
pause > nul
FOR /F %%a IN ('MSHTA "%~f0"') DO (
    SET backup_path=%%a
)
ECHO 已选择目标文件夹地址: '!backup_path!'

SET /P brench_a=请输入分支1(不输时默认HEAD~1):
IF /I "!brench_a!"=="" (
    SET brench_a=HEAD~1
)
ECHO 已设置分支1：!brench_a!

SET /P brench_b=请输入目标分支1(不输时默认HEAD):
IF /I "!brench_b!"=="" (
    SET brench_b=HEAD
)
ECHO 已设置分支2：!brench_b!

CALL:main_func
GOTO:EOF

:main_func
    @REM 目标仓库地址
    !target_storage!
    CD !storage_path!
    SET comment='git diff --name-only !brench_a! !brench_b!'
    @REM explorer .
    ECHO on '!storage_path!'
    @REM FOR /F %%I IN ('git diff --name-only HEAD~ HEAD') DO ECHO %%~nxI
    FOR /F %%I IN (!comment!) DO (
        IF NOT EXIST !backup_path!%%~pI (
            MKDIR !backup_path!%%~pI
        )
        COPY /-Y /V %%~dpnxI !backup_path!%%~pnxI
        ECHO 文件 %%~dpnxI 已复制到: !backup_path!%%~pnxI
    )
    SET /P is_open_explorer=是否打开备份文件夹^(Y/N^):
    IF /I "!is_open_explorer!"=="Y" (
        EXPLORER !backup_path!
    ) ELSE (
        GOTO:EOF
    )
    ECHO 文件备份已完成,请使用备份文件上传FTP避免发生版本问题,按任意键退出
    pause > nul
GOTO:EOF

<script>
var Shell = new ActiveXObject("Shell.Application");
var Folder = Shell.BrowseForFolder(0, "select folder", 0); //起始目录为：桌面
if (Folder != null) {
    Folder = Folder.items();
    Folder = Folder.item();
    Folder = Folder.Path;
    new ActiveXObject('Scripting.FileSystemObject').GetStandardStream(1).Write(Folder);
}
close();
</script>