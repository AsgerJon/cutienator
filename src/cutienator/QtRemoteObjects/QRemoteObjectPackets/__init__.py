"""
The namespace 'QRemoteObjectPackets' of Qt, a package of 'cutienator.QtRemoteObjects':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtRemoteObjects import QRemoteObjectPackets
  QRemoteObjectPackets.ObjectInfo

A class is brought in the first time it is asked for.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.PackageGenerator. Changes made here are
#  lost.
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

from .._q_remote_object_packets import QRemoteObjectPackets as _Enums

#  The enums of the namespace, and the names of their
#  members, as names of the package itself, where C++ has
#  them: 'Qt.AlignLeft'.
globals().update({
    name: value for name, value in _Enums.__dict__.items()
    if not name.startswith('_')})

__all__ = (
    'ObjectInfo',
    'DataStreamPacket',
    'QAS_',
    'QSQ_',
    'QRO_',
    'CodecBase',
    'QDataStreamCodec',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._q_remote_object_packets__object_info import ObjectInfo
  from .._q_remote_object_packets__data_stream_packet import DataStreamPacket
  from .._q_remote_object_packets__q_a_s_ import QAS_
  from .._q_remote_object_packets__q_s_q_ import QSQ_
  from .._q_remote_object_packets__q_r_o_ import QRO_
  from .._q_remote_object_packets__codec_base import CodecBase
  from .._q_remote_object_packets__q_data_stream_codec import QDataStreamCodec
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'ObjectInfo': '_q_remote_object_packets__object_info',
      'DataStreamPacket': '_q_remote_object_packets__data_stream_packet',
      'QAS_': '_q_remote_object_packets__q_a_s_',
      'QSQ_': '_q_remote_object_packets__q_s_q_',
      'QRO_': '_q_remote_object_packets__q_r_o_',
      'CodecBase': '_q_remote_object_packets__codec_base',
      'QDataStreamCodec': '_q_remote_object_packets__q_data_stream_codec',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'QRemoteObjectPackets.ObjectInfo'. Python calls this for
    a name the package does not hold yet, and what it gives is kept here for
    the next time.

    Raises
    ------

    AttributeError
      The namespace has nothing of that name.
    """
    if name in __space_packages__:
      value = importlib.import_module('.%s' % name, __name__)
    else:
      try:
        fileName = __class_files__[name]
      except KeyError:
        infoSpec = """module '%s' has no attribute '%s'"""
        raise AttributeError(infoSpec % (__name__, name)) from None
      module = importlib.import_module('..%s' % fileName, __name__)
      value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names everything of the namespace, brought in or not."""
    return [*__all__, *(
        name for name in _Enums.__dict__ if not name.startswith('_'))]
