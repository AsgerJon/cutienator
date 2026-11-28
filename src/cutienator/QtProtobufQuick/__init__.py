"""
The 'cutienator.QtProtobufQuick' package provides the cute classes of
the part of Qt named QtProtobufQuick, under the name PySide6 has for it.

  from cutienator.QtProtobufQuick import QQmlProtobufBoolListForeign, QQmlProtobufDoubleListForeign

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
    'QQmlProtobufBoolListForeign',
    'QQmlProtobufDoubleListForeign',
    'QQmlProtobufFixed32Foreign',
    'QQmlProtobufFixed32ListForeign',
    'QQmlProtobufFixed64Foreign',
    'QQmlProtobufFixed64ListForeign',
    'QQmlProtobufFloatListForeign',
    'QQmlProtobufInt32Foreign',
    'QQmlProtobufInt32ListForeign',
    'QQmlProtobufInt64Foreign',
    'QQmlProtobufInt64ListForeign',
    'QQmlProtobufSFixed32Foreign',
    'QQmlProtobufSFixed32ListForeign',
    'QQmlProtobufSFixed64Foreign',
    'QQmlProtobufSFixed64ListForeign',
    'QQmlProtobufSInt32Foreign',
    'QQmlProtobufSInt32ListForeign',
    'QQmlProtobufSInt64Foreign',
    'QQmlProtobufSInt64ListForeign',
    'QQmlProtobufUInt32Foreign',
    'QQmlProtobufUInt32ListForeign',
    'QQmlProtobufUInt64Foreign',
    'QQmlProtobufUInt64ListForeign',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_qml_protobuf_bool_list_foreign import QQmlProtobufBoolListForeign
  from ._q_qml_protobuf_double_list_foreign import QQmlProtobufDoubleListForeign
  from ._q_qml_protobuf_fixed32_foreign import QQmlProtobufFixed32Foreign
  from ._q_qml_protobuf_fixed32_list_foreign import QQmlProtobufFixed32ListForeign
  from ._q_qml_protobuf_fixed64_foreign import QQmlProtobufFixed64Foreign
  from ._q_qml_protobuf_fixed64_list_foreign import QQmlProtobufFixed64ListForeign
  from ._q_qml_protobuf_float_list_foreign import QQmlProtobufFloatListForeign
  from ._q_qml_protobuf_int32_foreign import QQmlProtobufInt32Foreign
  from ._q_qml_protobuf_int32_list_foreign import QQmlProtobufInt32ListForeign
  from ._q_qml_protobuf_int64_foreign import QQmlProtobufInt64Foreign
  from ._q_qml_protobuf_int64_list_foreign import QQmlProtobufInt64ListForeign
  from ._q_qml_protobuf_s_fixed32_foreign import QQmlProtobufSFixed32Foreign
  from ._q_qml_protobuf_s_fixed32_list_foreign import QQmlProtobufSFixed32ListForeign
  from ._q_qml_protobuf_s_fixed64_foreign import QQmlProtobufSFixed64Foreign
  from ._q_qml_protobuf_s_fixed64_list_foreign import QQmlProtobufSFixed64ListForeign
  from ._q_qml_protobuf_s_int32_foreign import QQmlProtobufSInt32Foreign
  from ._q_qml_protobuf_s_int32_list_foreign import QQmlProtobufSInt32ListForeign
  from ._q_qml_protobuf_s_int64_foreign import QQmlProtobufSInt64Foreign
  from ._q_qml_protobuf_s_int64_list_foreign import QQmlProtobufSInt64ListForeign
  from ._q_qml_protobuf_u_int32_foreign import QQmlProtobufUInt32Foreign
  from ._q_qml_protobuf_u_int32_list_foreign import QQmlProtobufUInt32ListForeign
  from ._q_qml_protobuf_u_int64_foreign import QQmlProtobufUInt64Foreign
  from ._q_qml_protobuf_u_int64_list_foreign import QQmlProtobufUInt64ListForeign
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QQmlProtobufBoolListForeign': '_q_qml_protobuf_bool_list_foreign',
      'QQmlProtobufDoubleListForeign': '_q_qml_protobuf_double_list_foreign',
      'QQmlProtobufFixed32Foreign': '_q_qml_protobuf_fixed32_foreign',
      'QQmlProtobufFixed32ListForeign': '_q_qml_protobuf_fixed32_list_foreign',
      'QQmlProtobufFixed64Foreign': '_q_qml_protobuf_fixed64_foreign',
      'QQmlProtobufFixed64ListForeign': '_q_qml_protobuf_fixed64_list_foreign',
      'QQmlProtobufFloatListForeign': '_q_qml_protobuf_float_list_foreign',
      'QQmlProtobufInt32Foreign': '_q_qml_protobuf_int32_foreign',
      'QQmlProtobufInt32ListForeign': '_q_qml_protobuf_int32_list_foreign',
      'QQmlProtobufInt64Foreign': '_q_qml_protobuf_int64_foreign',
      'QQmlProtobufInt64ListForeign': '_q_qml_protobuf_int64_list_foreign',
      'QQmlProtobufSFixed32Foreign': '_q_qml_protobuf_s_fixed32_foreign',
      'QQmlProtobufSFixed32ListForeign': '_q_qml_protobuf_s_fixed32_list_foreign',
      'QQmlProtobufSFixed64Foreign': '_q_qml_protobuf_s_fixed64_foreign',
      'QQmlProtobufSFixed64ListForeign': '_q_qml_protobuf_s_fixed64_list_foreign',
      'QQmlProtobufSInt32Foreign': '_q_qml_protobuf_s_int32_foreign',
      'QQmlProtobufSInt32ListForeign': '_q_qml_protobuf_s_int32_list_foreign',
      'QQmlProtobufSInt64Foreign': '_q_qml_protobuf_s_int64_foreign',
      'QQmlProtobufSInt64ListForeign': '_q_qml_protobuf_s_int64_list_foreign',
      'QQmlProtobufUInt32Foreign': '_q_qml_protobuf_u_int32_foreign',
      'QQmlProtobufUInt32ListForeign': '_q_qml_protobuf_u_int32_list_foreign',
      'QQmlProtobufUInt64Foreign': '_q_qml_protobuf_u_int64_foreign',
      'QQmlProtobufUInt64ListForeign': '_q_qml_protobuf_u_int64_list_foreign',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtProtobufQuick import QQmlProtobufUInt64ListForeign'. Python calls
    this for a name the package does not hold yet. The file of the
    class is brought in, which brings in the files that class needs
    and no others, and the class is kept here for the next time.

    Raises
    ------

    AttributeError
      The part has no class of that name.
    """
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
