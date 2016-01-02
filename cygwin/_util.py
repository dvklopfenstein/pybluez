
import os
import sys
import re

def find_SDK_cygwin(SDK):
    candidate_roots = (os.getenv('ProgramFiles'), os.getenv('ProgramW6432'),
                       os.getenv('ProgramFiles(x86)'))
    if SDK == "MS":
        return get_MS_SDK_dir(candidate_roots)
    elif SDK == "BT":
        return get_BT_SDK_dir(candidate_roots)

def get_BT_SDK_dir(candidate_roots):
    """Return dir for MicroSoft Design Kit, if found."""
    WC_BASE = os.path.join(os.getenv('ProgramFiles (x86)'), "Widcomm", "BTW DK", "SDK")

def get_MS_SDK_dir(candidate_roots):
    """Return dir for MicroSoft Design Kit, if found."""
    dir_base = get_MS_SDK_dir_base(candidate_roots)
    sys_version = get_sys_version()
    MS_SDK = get_MS_SDK_dir_ver(dir_base, sys_version)
    if os.path.exists(MS_SDK):
        return MS_SDK
    return get_SDK_dir(candidate_roots)

def get_MS_SDK_dir_base(candidate_roots):
    """Get 'Microsoft SDKs' directories."""
    for rootdir in candidate_roots:
        if rootdir is not None:
            for name in os.listdir(rootdir):
                if name == "Microsoft SDKs":
                    base_dir = os.path.join(rootdir, name, "Windows")
                    if os.path.exists(base_dir):
                        return base_dir
    raise Exception("NO 'Microsoft SDKs' DIRECTORY FOUND:\n{}".format('\n  '.join(candidate_roots)))

def get_sys_version():
    """Extract the version number from sys.version."""
    sys_mtch = re.match(r'([\d\.]+)', sys.version)
    if sys_mtch:
        return sys_mtch.group(1)
    raise Exception("NO VERSION FOR {} FOUND".format(MS_SDK_basedir))

def get_MS_SDK_dir_ver(MS_SDK_basedir, sys_version):
    if sys_version >= '2.7.10':
        return os.path.join(MS_SDK_basedir, 'v10.0A')  # Visual Studio 14
    # TBD: Not sure which 'MS SDK' version to use for anything other than 2.7.10
    else:
        raise Exception(
          "TIME TO IMPLEMENT WHICH 'Visual Studio' TO USE WITH sys.version({})".format(sys_version))
    #elif sys_version < '3.3':
    #    MS_SDK = r'Microsoft SDKs\Windows\v6.0A'  # Visual Studio 9
    #elif '3.3' <= sys_version < '3.5':
    #    MS_SDK = r'Microsoft SDKs\Windows\v7.0A'  # Visual Studio 10


def get_SDK_dir(candidate_roots):
    candidate_paths = ('Microsoft Platform SDK for Windows XP',
                       'Microsoft Platform SDK')

    for candidate_root in candidate_roots:
        if candidate_root is not None:
            for candidate_path in candidate_paths:
                candidate_sdk = os.path.join(candidate_root, candidate_path)
                if os.path.exists(candidate_sdk):
                    return candidate_sdk
    raise Exception("NO PATH TO MICROSOFT SDK FOUND")
