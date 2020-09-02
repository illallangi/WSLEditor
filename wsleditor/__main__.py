import subprocess

import click


@click.command()
@click.argument('filename', type=click.Path(file_okay=True, dir_okay=False, writable=True, readable=True, resolve_path=True, allow_dash=False), required=True)
@click.option('--distribution', envvar='WSL_DISTRO_NAME')
@click.option('--editor', envvar='WINDOWS_EDITOR', default='/mnt/c/Program Files (x86)/Notepad++/notepad++.exe')
@click.option('--editor-args', envvar='WINDOWS_EDITOR_ARGS', default='-multiInst -notabbar -nosession -noPlugin')
def main(filename, distribution, editor, editor_args):
    windowsFilename = f"\\\\wsl$\\{distribution}{filename}".replace('/', '\\')
    subprocess.call([editor, *editor_args.split(' '), windowsFilename])


if __name__ == "__main__":
    main()
