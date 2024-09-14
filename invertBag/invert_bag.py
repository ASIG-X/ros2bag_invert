"""Example: Register type from definition string."""

from __future__ import annotations
from pathlib import Path
from collections.abc import Sequence

from rosbags.typesys import Stores, get_types_from_msg, get_typestore
from rosbags.convert.converter import convert

def guess_msgtype(path: Path) -> str:
    """Guess message type name from path."""
    name = path.relative_to(path.parents[2]).with_suffix('')
    if 'msg' not in name.parts:
        name = name.parent / 'msg' / name.name
    return str(name)

def invert_bag(src: Sequence[Path], dst: Path, msg_paths: Sequence[str]) -> None:
    typestore1 = get_typestore(Stores.ROS1_NOETIC)
    typestore2 = get_typestore(Stores.ROS2_HUMBLE)
    add_types = {}

    for pathstr in msg_paths:
        msgpath = Path(pathstr)
        msgdef = msgpath.read_text(encoding='utf-8')
        add_types.update(get_types_from_msg(msgdef, guess_msgtype(msgpath)))

    typestore1.register(add_types)
    typestore2.register(add_types)

    convert(src, dst, dst_version=None, default_typestore=typestore2, typestore=typestore1, exclude_topics='', include_topics='',exclude_msgtypes='',include_msgtypes='')
