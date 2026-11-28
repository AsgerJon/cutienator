"""
QBinaryJsonPrivate::ConstData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QBinaryJsonPrivate::ConstData to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QJsonDocument

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ConstData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QBinaryJsonPrivate::ConstData: a plain Python object
  standing in front of one C++ QBinaryJsonPrivate::ConstData.

  What exists
  -----------

  Every function of Qt's QBinaryJsonPrivate::ConstData that has a ritual and
  that Python can call so far, 1 name in all: 'toJsonDocument'. It can be
  made from Python, in 1 way; see '__init__'.

  What has no ritual
  ------------------

  5 of the 7 functions Qt declares: 4 forbidden; 1 leans on
  'QBinaryJsonPrivate.

  What to expect
  --------------

  - The C++ QBinaryJsonPrivate::ConstData is created at the first use, not by
    'QBinaryJsonPrivate::ConstData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBinaryJsonPrivate::ConstData.
  - Each name of Qt's QBinaryJsonPrivate::ConstData that has no cute function
    yet, 'isValid', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBinaryJsonPrivate::ConstData'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toJsonDocument(self) -> QJsonDocument:
    """
    Calls Qt's 'QJsonDocument QBinaryJsonPrivate::ConstData::toJsonDocument()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-constdata.html#toJsonDocument

    Returns
    -------

    QJsonDocument
      A new cute QJsonDocument around the copy Qt gave back. Python owns it.
    """
    #  QJsonDocument QBinaryJsonPrivate::ConstData::toJsonDocument() const
    address = self.uglySide.call(
        'ritual_ZNK18QBinaryJsonPrivate9ConstData14toJsonDocumentEv',
    )
    from ..QtCore import QJsonDocument
    return QJsonDocument._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, int)
  @overload(NoneType, int)
  def __init__(self, raw: Optional[str], a: int) -> None:
    """
    Notes what was given, for Qt's
    'QBinaryJsonPrivate::ConstData::ConstData(const char *raw, uint a)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-constdata.html#ConstData

    Parameters
    ----------

    raw : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    a : int
      Passed on as it is.
    """
    #  QBinaryJsonPrivate::ConstData::ConstData(const char *raw, uint a)
    self._noteCreation(ConstData, lambda: Rituals.call(
        'ritual_ZN18QBinaryJsonPrivate9ConstDataC1EPKcj',
        self._bytesOf(raw), a,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def isValid(*__, **_) -> Never:
    """
    Qt's 'bool QBinaryJsonPrivate::ConstData::isValid() const': leans on
    'QBinaryJsonPrivate::Value::isValidHelper(QBinaryJsonPrivate::Base
    const*, QVarLengthArray<QBinaryJsonPrivate::IsValidFrame, 16ll>&) const',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QBinaryJsonPrivate.ConstData.isValid' has no cute function yet. "
        "Qt's 'bool QBinaryJsonPrivate::ConstData::isValid() const': leans "
        "on "
        "'QBinaryJsonPrivate::Value::isValidHelper(QBinaryJsonPrivate::Base "
        "const*, QVarLengthArray<QBinaryJsonPrivate::IsValidFrame, 16ll>&) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")
