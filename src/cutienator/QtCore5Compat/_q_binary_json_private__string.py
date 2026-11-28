"""
QBinaryJsonPrivate::String binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QBinaryJsonPrivate::String to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class String(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QBinaryJsonPrivate::String: a plain Python object
  standing in front of one C++ QBinaryJsonPrivate::String.

  C++ hands a QBinaryJsonPrivate::String around as a copy, so every C++
  QBinaryJsonPrivate::String behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QBinaryJsonPrivate::String that has a ritual and
  that Python can call so far, 5 names in all: 'byteSize', 'isValid',
  'fillTrailingZeros', '__eq__', 'toString'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QBinaryJsonPrivate::String::copy(char *dest, QStringView
    str)': names 'char', which has no cute class yet.
  - Qt's 'QBinaryJsonPrivate::String::~String()': the destructor: Python
    removes its C++ QBinaryJsonPrivate::String by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QBinaryJsonPrivate::String is created at the first use, not by
    'QBinaryJsonPrivate::String(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QBinaryJsonPrivate::String back gives a copy the
    ritual made for Python, in a new cute QBinaryJsonPrivate::String.
  - Each name of Qt's QBinaryJsonPrivate::String that has no cute function
    yet, 'copy', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The classes Qt writes inside QBinaryJsonPrivate::String, each a class in
  #  here as in C++.

  class Data(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QBinaryJsonPrivate::String::Data: a plain Python
    object standing in front of one C++ QBinaryJsonPrivate::String::Data.

    C++ hands a QBinaryJsonPrivate::String::Data around as a copy, so every
    C++ QBinaryJsonPrivate::String::Data behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QBinaryJsonPrivate::String::Data yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QBinaryJsonPrivate::String::Data::~Data()': the destructor:
      Python removes its C++ QBinaryJsonPrivate::String::Data by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QBinaryJsonPrivate::String::Data is created at the first use,
      not by 'QBinaryJsonPrivate::String::Data(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QBinaryJsonPrivate::String::Data back gives a copy
      the ritual made for Python, in a new cute
      QBinaryJsonPrivate::String::Data.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QBinaryJsonPrivate::String::Data'

    #  Qt's '~QBinaryJsonPrivate::String::Data()'. Naming it makes this a
    #  value class: Python owns every C++ QBinaryJsonPrivate::String::Data
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN18QBinaryJsonPrivate6String4DataD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(Data)
  @overload(NoneType)
  def fillTrailingZeros(data: Optional[Data]) -> None:
    """
    Calls Qt's 'void QBinaryJsonPrivate::String::fillTrailingZeros(Data
    *data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-string.html#fillTrailingZeros

    Parameters
    ----------

    data : Optional[Data]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBinaryJsonPrivate::String::fillTrailingZeros(Data *data)
    Rituals.call(
        'ritual_ZN18QBinaryJsonPrivate6String17fillTrailingZerosEPNS0_4Data'
        'E',
        CuteMixin._addressOf(data),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBinaryJsonPrivate::String'

  #  Qt's '~QBinaryJsonPrivate::String()'. Naming it makes this a value
  #  class: Python owns every C++ QBinaryJsonPrivate::String behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN18QBinaryJsonPrivate6StringD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def byteSize(self) -> int:
    """
    Calls Qt's 'uint QBinaryJsonPrivate::String::byteSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-string.html#byteSize
    """
    #  uint QBinaryJsonPrivate::String::byteSize() const
    return self.uglySide.call(
        'ritual_ZNK18QBinaryJsonPrivate6String8byteSizeEv',
    )

  @overload(int)
  def isValid(self, maxSize: int) -> bool:
    """
    Calls Qt's 'bool QBinaryJsonPrivate::String::isValid(uint maxSize)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-string.html#isValid

    Parameters
    ----------

    maxSize : int
      Passed on as it is.
    """
    #  bool QBinaryJsonPrivate::String::isValid(uint maxSize) const
    return self.uglySide.call(
        'ritual_ZNK18QBinaryJsonPrivate6String7isValidEj', maxSize,
    )

  def toString(self) -> str:
    """
    Calls Qt's 'QString QBinaryJsonPrivate::String::toString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-string.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBinaryJsonPrivate::String::toString() const
    return self.uglySide.call(
        'ritual_ZNK18QBinaryJsonPrivate6String8toStringEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def __eq__(self, str: str) -> bool:
    """
    Calls Qt's 'bool QBinaryJsonPrivate::String::operator==(QStringView str)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-string.html#operator==

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QBinaryJsonPrivate::String::operator==(QStringView str) const
    return self.uglySide.call(
        'ritual_ZNK18QBinaryJsonPrivate6StringeqE11QStringView', str,
    )

  @overload(THIS)
  def __eq__(self, str: String) -> bool:
    """
    Calls Qt's 'bool QBinaryJsonPrivate::String::operator==(const String
    &str) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-string.html#operator==

    Parameters
    ----------

    str : String
      Passed on as a value: Qt reads the C++ QBinaryJsonPrivate::String,
      which stays Python's own.
    """
    #  bool QBinaryJsonPrivate::String::operator==(const String &str) const
    return self.uglySide.call(
        'ritual_ZNK18QBinaryJsonPrivate6StringeqERKS0_', self._valueOf(str),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  @overload(NoneType)
  def __init__(self, data: Optional[str]) -> None:
    """
    Notes what was given, for Qt's 'QBinaryJsonPrivate::String::String(const
    char *data)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-string.html#String

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  QBinaryJsonPrivate::String::String(const char *data)
    self._noteCreation(String, lambda: Rituals.call(
        'ritual_ZN18QBinaryJsonPrivate6StringC1EPKc', self._bytesOf(data),
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
  def copy(*__, **_) -> Never:
    """
    Qt's 'void QBinaryJsonPrivate::String::copy(char *dest, QStringView
    str)': names 'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QBinaryJsonPrivate.String.copy' has no cute function yet. Qt's "
        "'void QBinaryJsonPrivate::String::copy(char *dest, QStringView "
        "str)': names 'char', which has no cute class yet.")
