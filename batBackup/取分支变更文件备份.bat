@ECHO OFF
SETLOCAL ENABLEDELAYEDEXPANSION

@REM ö�ٸ��ֿ��ַ ���ڿ���git��¼ѡ�� ���ڿ����ϴ�ftp

@REM 1������ʱ�䷶Χ
@REM 2����ӡ��ʱ�䷶Χ�������ύ

ECHO ���������ڱ�����ѡ�ֿ���git��һ���ύ���ļ�,�Ա��ϴ�FTP
ECHO.
ECHO ��ѡ����Ҫ���ݵĲֿ��ַ,�����������===============^>
pause > nul
FOR /F %%S IN ('MSHTA "%~f0"') DO (
    SET storage_path=%%S
    SET target_storage=%%~dS
)
ECHO ��ѡ��ֿ��ַ: '!storage_path!'

ECHO.
ECHO.
ECHO.
ECHO.

ECHO ��ѡ�񱸷�Ŀ���ļ��е�ַ,�����������===============^>
pause > nul
FOR /F %%a IN ('MSHTA "%~f0"') DO (
    SET backup_path=%%a
)
ECHO ��ѡ��Ŀ���ļ��е�ַ: '!backup_path!'

SET /P brench_a=�������֧1(����ʱĬ��HEAD~1):
IF /I "!brench_a!"=="" (
    SET brench_a=HEAD~1
)
ECHO �����÷�֧1��!brench_a!

SET /P brench_b=������Ŀ���֧1(����ʱĬ��HEAD):
IF /I "!brench_b!"=="" (
    SET brench_b=HEAD
)
ECHO �����÷�֧2��!brench_b!

CALL:main_func
GOTO:EOF

:main_func
    @REM Ŀ��ֿ��ַ
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
        ECHO �ļ� %%~dpnxI �Ѹ��Ƶ�: !backup_path!%%~pnxI
    )
    SET /P is_open_explorer=�Ƿ�򿪱����ļ���^(Y/N^):
    IF /I "!is_open_explorer!"=="Y" (
        EXPLORER !backup_path!
    ) ELSE (
        GOTO:EOF
    )
    ECHO �ļ����������,��ʹ�ñ����ļ��ϴ�FTP���ⷢ���汾����,��������˳�
    pause > nul
GOTO:EOF

<script>
var Shell = new ActiveXObject("Shell.Application");
var Folder = Shell.BrowseForFolder(0, "select folder", 0); //��ʼĿ¼Ϊ������
if (Folder != null) {
    Folder = Folder.items();
    Folder = Folder.item();
    Folder = Folder.Path;
    new ActiveXObject('Scripting.FileSystemObject').GetStandardStream(1).Write(Folder);
}
close();
</script>