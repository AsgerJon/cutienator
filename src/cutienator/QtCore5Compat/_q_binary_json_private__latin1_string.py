"""
QBinaryJsonPrivate::Latin1String binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QBinaryJsonPrivate::Latin1String to be private: it declares the
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

  from ..QtCore import QLatin1String

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Latin1String(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QBinaryJsonPrivate::Latin1String: a plain Python
  object standing in front of one C++ QBinaryJsonPrivate::Latin1String.

  C++ hands a QBinaryJsonPrivate::Latin1String around as a copy, so every C++
  QBinaryJsonPrivate::Latin1String behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QBinaryJsonPrivate::Latin1String that has a ritual
  and that Python can call so far, 4 names in all: 'byteSize', 'isValid',
  'toQLatin1String', 'toString'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QBinaryJsonPrivate::Latin1String::copy(char *dest, QStringView
    src)': names 'char', which has no cute class yet.
  - Qt's 'QBinaryJsonPrivate::Latin1String::~Latin1String()': the destructor:
    Python removes its C++ QBinaryJsonPrivate::Latin1String by it, and has no
    other use for it.

  What to expect
  --------------

  - The C++ QBinaryJsonPrivate::Latin1String is created at the first use, not
    by 'QBinaryJsonPrivate::Latin1String(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QBinaryJsonPrivate::Latin1String back gives a copy
    the ritual made for Python, in a new cute
    QBinaryJsonPrivate::Latin1String.
  - Each name of Qt's QBinaryJsonPrivate::Latin1String that has no cute
    function yet, 'copy', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The classes Qt writes inside QBinaryJsonPrivate::Latin1String, each a
  #  class in here as in C++.

  class Data(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QBinaryJsonPrivate::Latin1String::Data: a plain
    Python object standing in front of one C++
    QBinaryJsonPrivate::Latin1String::Data.

    C++ hands a QBinaryJsonPrivate::Latin1String::Data around as a copy, so
    every C++ QBinaryJsonPrivate::Latin1String::Data behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QBinaryJsonPrivate::Latin1String::Data yet. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QBinaryJsonPrivate::Latin1String::Data::~Data()': the destructor:
      Python removes its C++ QBinaryJsonPrivate::Latin1String::Data by it,
      and has no other use for it.

    What to expect
    --------------

    - The C++ QBinaryJsonPrivate::Latin1String::Data is created at the first
      use, not by 'QBinaryJsonPrivate::Latin1String::Data(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QBinaryJsonPrivate::Latin1String::Data back gives a
      copy the ritual made for Python, in a new cute
      QBinaryJsonPrivate::Latin1String::Data.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QBinaryJsonPrivate::Latin1String::Data'

    #  Qt's '~QBinaryJsonPrivate::Latin1String::Data()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QBinaryJsonPrivate::Latin1String::Data behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN18QBinaryJsonPrivate12Latin1String4DataD1Ev')

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBinaryJsonPrivate::Latin1String'

  #  Qt's '~QBinaryJsonPrivate::Latin1String()'. Naming it makes this a value
  #  class: Python owns every C++ QBinaryJsonPrivate::Latin1String behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN18QBinaryJsonPrivate12Latin1StringD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def byteSize(self) -> int:
    """
    Calls Qt's 'uint QBinaryJsonPrivate::Latin1String::byteSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-latin1string.html#byteSize
    """
    #  uint QBinaryJsonPrivate::Latin1String::byteSize() const
    return self.uglySide.call(
        'ritual_ZNK18QBinaryJsonPrivate12Latin1String8byteSizeEv',
    )

  @overload(int)
  def isValid(self, maxSize: int) -> bool:
    """
    Calls Qt's 'bool QBinaryJsonPrivate::Latin1String::isValid(uint maxSize)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-latin1string.html#isValid

    Parameters
    ----------

    maxSize : int
      Passed on as it is.
    """
    #  bool QBinaryJsonPrivate::Latin1String::isValid(uint maxSize) const
    return self.uglySide.call(
        'ritual_ZNK18QBinaryJsonPrivate12Latin1String7isValidEj', maxSize,
    )

  def toQLatin1String(self) -> QLatin1String:
    """
    Calls Qt's 'QLatin1String
    QBinaryJsonPrivate::Latin1String::toQLatin1String() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-latin1string.html

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  QLatin1String QBinaryJsonPrivate::Latin1String::toQLatin1String()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QBinaryJsonPrivate12Latin1String15toQLatin1StringEv',
    )
    from ..QtCore import QLatin1String
    return QLatin1String._cuteOwning(address)

  def toString(self) -> str:
    """
    Calls Qt's 'QString QBinaryJsonPrivate::Latin1String::toString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-latin1string.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBinaryJsonPrivate::Latin1String::toString() const
    return self.uglySide.call(
        'ritual_ZNK18QBinaryJsonPrivate12Latin1String8toStringEv',
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  @overload(NoneType)
  def __init__(self, data: Optional[str]) -> None:
    """
    Notes what was given, for Qt's
    'QBinaryJsonPrivate::Latin1String::Latin1String(const char *data)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-latin1string.html#Latin1String

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  QBinaryJsonPrivate::Latin1String::Latin1String(const char *data)
    self._noteCreation(Latin1String, lambda: Rituals.call(
        'ritual_ZN18QBinaryJsonPrivate12Latin1StringC1EPKc',
        self._bytesOf(data),
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
    Qt's 'void QBinaryJsonPrivate::Latin1String::copy(char *dest, QStringView
    src)': names 'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QBinaryJsonPrivate.Latin1String.copy' has no cute function yet. "
        "Qt's 'void QBinaryJsonPrivate::Latin1String::copy(char *dest, "
        "QStringView src)': names 'char', which has no cute class yet.")
