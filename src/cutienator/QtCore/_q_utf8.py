"""
QUtf8 binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qstringconverter_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QUtf8 to be private: it declares the class in a header it calls
#  private. cutienator does not care. Qt hands objects of the class out all
#  the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QByteArray, QByteArrayView, QChar, QLatin1String
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArrayView = WAIT['QByteArrayView']
  QChar = WAIT['QChar']
  QLatin1String = WAIT['QLatin1String']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QUtf8(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QUtf8: a plain Python object standing in front of one
  C++ QUtf8.

  C++ hands a QUtf8 around as a copy, so every C++ QUtf8 behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QUtf8 that has a ritual and that Python can call so
  far, 3 names in all: 'convertToUnicode', 'convertFromUnicode',
  'compareUtf8'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QString QUtf8::convertToUnicode(QByteArrayView in,
    QStringConverter::State *state)': names 'QStringConverter::State', which
    has no cute class yet.
  - Qt's 'QChar *QUtf8::convertToUnicode(QChar *out, QByteArrayView in,
    QStringConverter::State *state)': names 'QStringConverter::State', which
    has no cute class yet.
  - Qt's 'char *QUtf8::convertFromUnicode(char *dst, QStringView in)': names
    'char', which has no cute class yet.
  - Qt's 'QByteArray QUtf8::convertFromUnicode(QStringView in,
    QStringConverter::State *state)': names 'QStringConverter::State', which
    has no cute class yet.
  - Qt's 'char *QUtf8::convertFromLatin1(char *out, QLatin1StringView in)':
    names 'char', which has no cute class yet.
  - Qt's 'QUtf8::~QUtf8()': the destructor: Python removes its C++ QUtf8 by
    it, and has no other use for it.

  What has no ritual
  ------------------

  8 of the 18 functions Qt declares: 4 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 takes or
  gives a type that cannot be passed yet; 2 a template.

  What to expect
  --------------

  - The C++ QUtf8 is created at the first use, not by 'QUtf8(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QUtf8 back gives a copy the ritual made for Python,
    in a new cute QUtf8.
  - Each name of Qt's QUtf8 that has no cute function yet,
    'convertFromLatin1', 'isValidUtf8', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QUtf8, each a class in here as in C++.

  class ValidUtf8Result(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QUtf8::ValidUtf8Result: a plain Python object
    standing in front of one C++ QUtf8::ValidUtf8Result.

    C++ hands a QUtf8::ValidUtf8Result around as a copy, so every C++
    QUtf8::ValidUtf8Result behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QUtf8::ValidUtf8Result yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QUtf8::ValidUtf8Result::~ValidUtf8Result()': the destructor:
      Python removes its C++ QUtf8::ValidUtf8Result by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QUtf8::ValidUtf8Result is created at the first use, not by
      'QUtf8::ValidUtf8Result(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QUtf8::ValidUtf8Result back gives a copy the ritual
      made for Python, in a new cute QUtf8::ValidUtf8Result.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QUtf8::ValidUtf8Result'

    #  Qt's '~QUtf8::ValidUtf8Result()'. Naming it makes this a value class:
    #  Python owns every C++ QUtf8::ValidUtf8Result behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN5QUtf815ValidUtf8ResultD1Ev'

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
  @overload(QChar, QByteArrayView)
  @overload(NoneType, QByteArrayView)
  def convertToUnicode(
      buffer: Optional[QChar],
      in_: QByteArrayView,
  ) -> Optional[QChar]:
    """
    Calls Qt's 'QChar *QUtf8::convertToUnicode(QChar *buffer, QByteArrayView
    in)'.

    Qt's own words: https://doc.qt.io/qt-6/qutf8.html#convertToUnicode

    Parameters
    ----------

    buffer : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    in_ : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    Returns
    -------

    Optional[QChar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QChar *QUtf8::convertToUnicode(QChar *buffer, QByteArrayView in)
    address = Rituals.call(
        'ritual_ZN5QUtf816convertToUnicodeEP5QChar14QByteArrayView',
        CuteMixin._addressOf(buffer), CuteMixin._valueOf(in_),
    )
    from . import QChar
    return QChar._cuteAt(address)

  @staticmethod
  @overload(QByteArrayView)
  def convertToUnicode(in_: QByteArrayView) -> str:
    """
    Calls Qt's 'QString QUtf8::convertToUnicode(QByteArrayView in)'.

    Qt's own words: https://doc.qt.io/qt-6/qutf8.html#convertToUnicode

    Parameters
    ----------

    in_ : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QUtf8::convertToUnicode(QByteArrayView in)
    return Rituals.call(
        'ritual_ZN5QUtf816convertToUnicodeE14QByteArrayView',
        CuteMixin._valueOf(in_),
    )

  @staticmethod
  @overload(str)
  def convertFromUnicode(in_: str) -> QByteArray:
    """
    Calls Qt's 'QByteArray QUtf8::convertFromUnicode(QStringView in)'.

    Qt's own words: https://doc.qt.io/qt-6/qutf8.html#convertFromUnicode

    Parameters
    ----------

    in_ : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QUtf8::convertFromUnicode(QStringView in)
    address = Rituals.call(
        'ritual_ZN5QUtf818convertFromUnicodeE11QStringView', in_,
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  @staticmethod
  @overload(QByteArrayView, QLatin1String)
  @overload(QByteArrayView, QLatin1String, Qt.CaseSensitivity)
  def compareUtf8(
      utf8: QByteArrayView,
      s: QLatin1String,
      cs: Qt.CaseSensitivity = Qt.CaseSensitivity.CaseSensitive,
  ) -> int:
    """
    Calls Qt's 'int QUtf8::compareUtf8(QByteArrayView utf8, QLatin1StringView
    s, Qt::CaseSensitivity cs)'.

    Qt's own words: https://doc.qt.io/qt-6/qutf8.html#compareUtf8

    Parameters
    ----------

    utf8 : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    s : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    cs : Qt.CaseSensitivity
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CaseSensitivity.CaseSensitive.
    """
    #  int QUtf8::compareUtf8(QByteArrayView utf8, QLatin1StringView s,
    #      Qt::CaseSensitivity cs)
    return Rituals.call(
        'ritual_ZN5QUtf811compareUtf8E14QByteArrayView13QLatin1StringN2Qt15'
        'CaseSensitivityE',
        CuteMixin._valueOf(utf8), CuteMixin._valueOf(s), cs.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QUtf8'

  #  Qt's '~QUtf8()'. Naming it makes this a value class: Python owns every
  #  C++ QUtf8 behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN5QUtf8D1Ev'

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
  def convertFromLatin1(*__, **_) -> Never:
    """
    Qt's 'char *QUtf8::convertFromLatin1(char *out, QLatin1StringView in)':
    names 'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QUtf8.convertFromLatin1' has no cute function yet. Qt's 'char "
        "*QUtf8::convertFromLatin1(char *out, QLatin1StringView in)': names "
        "'char', which has no cute class yet.")

  @staticmethod
  def isValidUtf8(*__, **_) -> Never:
    """
    Qt's 'ValidUtf8Result QUtf8::isValidUtf8(QByteArrayView in)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'QUtf8NoOutputTraits'.
    """
    raise NotImplementedError(
        "'QUtf8.isValidUtf8' has no cute function yet. Qt's "
        "'ValidUtf8Result QUtf8::isValidUtf8(QByteArrayView in)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'QUtf8NoOutputTraits'.")
