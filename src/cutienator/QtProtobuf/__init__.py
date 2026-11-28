"""
The 'cutienator.QtProtobuf' package provides the cute classes of the
part of Qt named QtProtobuf, under the name PySide6 has for it.

  from cutienator.QtProtobuf import QProtobufRepeatedIterator, QProtobufSerializerPrivate

A class is brought in the first time it is asked for, with the files it
needs and no others. So bringing in the package costs nothing, and a
program pays for the classes it uses.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

__all__ = (
    'QProtobufRepeatedIterator',
    'QProtobufSerializerPrivate',
    'QProtobufSelfcheckIterator',
    'QAbstractProtobufSerializer',
    'QProtobufMessage',
    'QProtobufMessagePrivate',
    'QProtobufDeserializerBase',
    'QProtobufJsonSerializer',
    'QProtobufMapEntryBase',
    'QProtobufMessageDeleter',
    'QProtobufSerializer',
    'QProtobufSerializerBase',
    'QProtobufDeserializerImpl',
    'QProtobufSerializerImpl',
    'QtProtobuf',
    'QtProtobufPrivate',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_protobuf_repeated_iterator import QProtobufRepeatedIterator
  from ._q_protobuf_serializer_private import QProtobufSerializerPrivate
  from ._q_protobuf_selfcheck_iterator import QProtobufSelfcheckIterator
  from ._q_abstract_protobuf_serializer import QAbstractProtobufSerializer
  from ._q_protobuf_message import QProtobufMessage
  from ._q_protobuf_message_private import QProtobufMessagePrivate
  from ._q_protobuf_deserializer_base import QProtobufDeserializerBase
  from ._q_protobuf_json_serializer import QProtobufJsonSerializer
  from ._q_protobuf_map_entry_base import QProtobufMapEntryBase
  from ._q_protobuf_message_deleter import QProtobufMessageDeleter
  from ._q_protobuf_serializer import QProtobufSerializer
  from ._q_protobuf_serializer_base import QProtobufSerializerBase
  from ._q_protobuf_deserializer_impl import QProtobufDeserializerImpl
  from ._q_protobuf_serializer_impl import QProtobufSerializerImpl
  from . import QtProtobuf
  from . import QtProtobufPrivate
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QProtobufRepeatedIterator': '_q_protobuf_repeated_iterator',
      'QProtobufSerializerPrivate': '_q_protobuf_serializer_private',
      'QProtobufSelfcheckIterator': '_q_protobuf_selfcheck_iterator',
      'QAbstractProtobufSerializer': '_q_abstract_protobuf_serializer',
      'QProtobufMessage': '_q_protobuf_message',
      'QProtobufMessagePrivate': '_q_protobuf_message_private',
      'QProtobufDeserializerBase': '_q_protobuf_deserializer_base',
      'QProtobufJsonSerializer': '_q_protobuf_json_serializer',
      'QProtobufMapEntryBase': '_q_protobuf_map_entry_base',
      'QProtobufMessageDeleter': '_q_protobuf_message_deleter',
      'QProtobufSerializer': '_q_protobuf_serializer',
      'QProtobufSerializerBase': '_q_protobuf_serializer_base',
      'QProtobufDeserializerImpl': '_q_protobuf_deserializer_impl',
      'QProtobufSerializerImpl': '_q_protobuf_serializer_impl',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('QtProtobuf', 'QtProtobufPrivate',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtProtobuf import QProtobufSerializerImpl'. Python calls
    this for a name the package does not hold yet. The file of the
    class is brought in, which brings in the files that class needs
    and no others, and the class is kept here for the next time.

    Raises
    ------

    AttributeError
      The part has no class of that name.
    """
    if name in __space_packages__:
      value = importlib.import_module('.%s' % name, __name__)
      globals()[name] = value
      return value
    try:
      fileName = __class_files__[name]
    except KeyError:
      infoSpec = """module '%s' has no attribute '%s'"""
      raise AttributeError(infoSpec % (__name__, name)) from None
    module = importlib.import_module('.%s' % fileName, __name__)
    value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names every class of the part, brought in or not."""
    return [*__all__]
