"""
QBinaryJsonPrivate::MutableData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QBinaryJsonPrivate::MutableData to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QJsonValue
from . import QBinaryJsonPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class MutableData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QBinaryJsonPrivate::MutableData: a plain Python
  object standing in front of one C++ QBinaryJsonPrivate::MutableData.

  What exists
  -----------

  Every function of Qt's QBinaryJsonPrivate::MutableData that has a ritual
  and that Python can call so far, 2 names in all: 'clone', 'compact'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QBinaryJsonPrivate::MutableData::MutableData(char *raw, uint a)':
    names 'char', which has no cute class yet.
  - Qt's 'QBinaryJsonPrivate::MutableData::~MutableData()': the destructor:
    Python never removes a C++ QBinaryJsonPrivate::MutableData.
  - Qt's 'char *QBinaryJsonPrivate::MutableData::takeRawData(uint *size)':
    takes a number to change where it is.

  What has no ritual
  ------------------

  4 of the 10 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QBinaryJsonPrivate::MutableData is created at the first use, not
    by 'QBinaryJsonPrivate::MutableData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBinaryJsonPrivate::MutableData.
  - Each name of Qt's QBinaryJsonPrivate::MutableData that has no cute
    function yet, 'takeRawData', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBinaryJsonPrivate::MutableData'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload(int, QJsonValue.Type)
  def __init__(self, reserved: int, valueType: QJsonValue.Type) -> None:
    """
    Notes what was given, for Qt's
    'QBinaryJsonPrivate::MutableData::MutableData(uint reserved,
    QJsonValue::Type valueType)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-mutabledata.html#MutableData

    Parameters
    ----------

    reserved : int
      Passed on as it is.

    valueType : QJsonValue.Type
      Passed on as its number.
    """
    #  QBinaryJsonPrivate::MutableData::MutableData(uint reserved,
    #      QJsonValue::Type valueType)
    self._noteCreation(MutableData, lambda: Rituals.call(
        'ritual_ZN18QBinaryJsonPrivate11MutableDataC1EjN10QJsonValue4TypeE',
        reserved, valueType.value,
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

  @overload(WAIT['QBinaryJsonPrivate.Base'])
  @overload(NoneType)
  @overload(WAIT['QBinaryJsonPrivate.Base'], int)
  @overload(NoneType, int)
  def clone(
      self,
      b: Optional[QBinaryJsonPrivate.Base],
      reserve: int = 0,
  ) -> Optional[MutableData]:
    """
    Calls Qt's 'MutableData *QBinaryJsonPrivate::MutableData::clone(const
    Base *b, uint reserve)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-mutabledata.html#clone

    Parameters
    ----------

    b : Optional[QBinaryJsonPrivate.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    reserve : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    Optional[MutableData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  MutableData *QBinaryJsonPrivate::MutableData::clone(const Base *b,
    #      uint reserve)
    address = self.uglySide.call(
        'ritual_ZN18QBinaryJsonPrivate11MutableData5cloneEPKNS_4BaseEj',
        self._addressOf(b), reserve,
    )
    return MutableData._cuteAt(address)

  def compact(self) -> None:
    """
    Calls Qt's 'void QBinaryJsonPrivate::MutableData::compact()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-mutabledata.html#compact
    """
    #  void QBinaryJsonPrivate::MutableData::compact()
    self.uglySide.call(
        'ritual_ZN18QBinaryJsonPrivate11MutableData7compactEv',
    )

  @staticmethod
  def takeRawData(*__, **_) -> Never:
    """
    Qt's 'char *QBinaryJsonPrivate::MutableData::takeRawData(uint *size)':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QBinaryJsonPrivate.MutableData.takeRawData' has no cute function "
        "yet. Qt's 'char *QBinaryJsonPrivate::MutableData::takeRawData(uint "
        "*size)': takes a number to change where it is.")
