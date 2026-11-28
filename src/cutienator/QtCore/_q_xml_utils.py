"""
QXmlUtils binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qxmlutils_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QXmlUtils to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QChar
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChar = WAIT['QChar']


class QXmlUtils(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QXmlUtils: a plain Python object standing in front of
  one C++ QXmlUtils.

  C++ hands a QXmlUtils around as a copy, so every C++ QXmlUtils behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QXmlUtils that has a ritual and that Python can call
  so far, 11 names in all: 'isEncName', 'isChar', 'isNameChar', 'isLetter',
  'isNCName', 'isPublicID', 'isBaseChar', 'isDigit', 'isExtender',
  'isIdeographic', 'isCombiningChar'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QXmlUtils::rangeContains(RangeIter begin, RangeIter end, const
    QChar c)': names 'QXmlCharRange', which has no cute class yet.
  - Qt's 'QXmlUtils::~QXmlUtils()': the destructor: Python removes its C++
    QXmlUtils by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QXmlUtils is created at the first use, not by 'QXmlUtils(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QXmlUtils back gives a copy the ritual made for
    Python, in a new cute QXmlUtils.
  - Each name of Qt's QXmlUtils that has no cute function yet,
    'rangeContains', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def isEncName(encName: str) -> bool:
    """
    Calls Qt's 'bool QXmlUtils::isEncName(QStringView encName)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlutils.html#isEncName

    Parameters
    ----------

    encName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlUtils::isEncName(QStringView encName)
    return Rituals.call(
        'ritual_ZN9QXmlUtils9isEncNameE11QStringView', encName,
    )

  @staticmethod
  @overload(int)
  def isChar(c: int) -> bool:
    """
    Calls Qt's 'bool QXmlUtils::isChar(const char32_t c)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlutils.html#isChar

    Parameters
    ----------

    c : int
      Passed on as it is.
    """
    #  bool QXmlUtils::isChar(const char32_t c)
    return Rituals.call('ritual_ZN9QXmlUtils6isCharEDi', c)

  @staticmethod
  @overload(QChar)
  def isNameChar(c: QChar) -> bool:
    """
    Calls Qt's 'bool QXmlUtils::isNameChar(const QChar c)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlutils.html#isNameChar

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool QXmlUtils::isNameChar(const QChar c)
    return Rituals.call(
        'ritual_ZN9QXmlUtils10isNameCharE5QChar', CuteMixin._valueOf(c),
    )

  @staticmethod
  @overload(QChar)
  def isLetter(c: QChar) -> bool:
    """
    Calls Qt's 'bool QXmlUtils::isLetter(const QChar c)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlutils.html#isLetter

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool QXmlUtils::isLetter(const QChar c)
    return Rituals.call(
        'ritual_ZN9QXmlUtils8isLetterE5QChar', CuteMixin._valueOf(c),
    )

  @staticmethod
  @overload(str)
  def isNCName(ncName: str) -> bool:
    """
    Calls Qt's 'bool QXmlUtils::isNCName(QStringView ncName)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlutils.html#isNCName

    Parameters
    ----------

    ncName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlUtils::isNCName(QStringView ncName)
    return Rituals.call('ritual_ZN9QXmlUtils8isNCNameE11QStringView', ncName)

  @staticmethod
  @overload(str)
  def isPublicID(candidate: str) -> bool:
    """
    Calls Qt's 'bool QXmlUtils::isPublicID(QStringView candidate)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlutils.html#isPublicID

    Parameters
    ----------

    candidate : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlUtils::isPublicID(QStringView candidate)
    return Rituals.call(
        'ritual_ZN9QXmlUtils10isPublicIDE11QStringView', candidate,
    )

  @staticmethod
  @overload(QChar)
  def isBaseChar(c: QChar) -> bool:
    """
    Calls Qt's 'bool QXmlUtils::isBaseChar(const QChar c)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlutils.html#isBaseChar

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool QXmlUtils::isBaseChar(const QChar c)
    return Rituals.call(
        'ritual_ZN9QXmlUtils10isBaseCharE5QChar', CuteMixin._valueOf(c),
    )

  @staticmethod
  @overload(QChar)
  def isDigit(c: QChar) -> bool:
    """
    Calls Qt's 'bool QXmlUtils::isDigit(const QChar c)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlutils.html#isDigit

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool QXmlUtils::isDigit(const QChar c)
    return Rituals.call(
        'ritual_ZN9QXmlUtils7isDigitE5QChar', CuteMixin._valueOf(c),
    )

  @staticmethod
  @overload(QChar)
  def isExtender(c: QChar) -> bool:
    """
    Calls Qt's 'bool QXmlUtils::isExtender(const QChar c)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlutils.html#isExtender

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool QXmlUtils::isExtender(const QChar c)
    return Rituals.call(
        'ritual_ZN9QXmlUtils10isExtenderE5QChar', CuteMixin._valueOf(c),
    )

  @staticmethod
  @overload(QChar)
  def isIdeographic(c: QChar) -> bool:
    """
    Calls Qt's 'bool QXmlUtils::isIdeographic(const QChar c)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlutils.html#isIdeographic

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool QXmlUtils::isIdeographic(const QChar c)
    return Rituals.call(
        'ritual_ZN9QXmlUtils13isIdeographicE5QChar', CuteMixin._valueOf(c),
    )

  @staticmethod
  @overload(QChar)
  def isCombiningChar(c: QChar) -> bool:
    """
    Calls Qt's 'bool QXmlUtils::isCombiningChar(const QChar c)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlutils.html#isCombiningChar

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  bool QXmlUtils::isCombiningChar(const QChar c)
    return Rituals.call(
        'ritual_ZN9QXmlUtils15isCombiningCharE5QChar', CuteMixin._valueOf(c),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QXmlUtils'

  #  Qt's '~QXmlUtils()'. Naming it makes this a value class: Python owns
  #  every C++ QXmlUtils behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QXmlUtilsD1Ev'

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
  def rangeContains(*__, **_) -> Never:
    """
    Qt's 'bool QXmlUtils::rangeContains(RangeIter begin, RangeIter end, const
    QChar c)': names 'QXmlCharRange', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QXmlUtils.rangeContains' has no cute function yet. Qt's 'bool "
        "QXmlUtils::rangeContains(RangeIter begin, RangeIter end, const "
        "QChar c)': names 'QXmlCharRange', which has no cute class yet.")
