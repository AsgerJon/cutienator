"""
QDebug binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtCore/qdebug.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from . import QIODeviceBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QByteArray, QChar, QIODevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QChar = WAIT['QChar']
  QIODevice = WAIT['QIODevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDebug(QIODeviceBase):
  """
  The cute side of Qt's QDebug: a plain Python object standing in front of
  one C++ QDebug.

  It is built on the cute 'QIODeviceBase', as Qt's QDebug is built on Qt's
  QIODeviceBase, and has everything that class has.

  C++ hands a QDebug around as a copy, so every C++ QDebug behind a cute one
  is Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDebug that has a ritual and that Python can call so
  far, 9 names in all: 'putUcs4', 'putString', 'putTimeUnit', 'verbosity',
  'setVerbosity', 'autoInsertSpaces', 'setAutoInsertSpaces', 'quoteStrings',
  'setQuoteStrings'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QDebug::putByteArray(const char *begin, size_t length,
    Latin1Content content)': names the enum 'QDebug::Latin1Content', whose
    class cannot be named here.
  - Qt's 'QDebug::QDebug(QString *string)': names 'QString', which has no
    cute class yet.
  - Qt's 'QDebug::QDebug(QtMsgType t)': names the enum 'QtMsgType', whose
    class cannot be named here.
  - Qt's 'QDebug::~QDebug()': the destructor: Python removes its C++ QDebug
    by it, and has no other use for it.

  What has no ritual
  ------------------

  63 of the 79 functions Qt declares: 47 takes or gives a type that cannot be
  passed yet; 16 a template.

  What to expect
  --------------

  - The C++ QDebug is created at the first use, not by 'QDebug(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDebug back gives a copy the ritual made for Python,
    in a new cute QDebug.
  """

  #  The enums Qt writes inside QDebug, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class VerbosityLevel(CuteNum):
    """
    The enum 'QDebug::VerbosityLevel' of Qt, with the 3 names Qt gives in it.
    """

    MinimumVerbosity = Kee[int](0)
    DefaultVerbosity = Kee[int](2)
    MaximumVerbosity = Kee[int](7)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDebug'

  #  Qt's '~QDebug()'. Naming it makes this a value class: Python owns every
  #  C++ QDebug behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN6QDebugD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def verbosity(self) -> int:
    """
    Calls Qt's 'int QDebug::verbosity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdebug.html#verbosity
    """
    #  int QDebug::verbosity() const
    return self.uglySide.call('ritual_ZNK6QDebug9verbosityEv')

  def autoInsertSpaces(self) -> bool:
    """
    Calls Qt's 'bool QDebug::autoInsertSpaces() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdebug.html#autoInsertSpaces
    """
    #  bool QDebug::autoInsertSpaces() const
    return self.uglySide.call('ritual_ZNK6QDebug16autoInsertSpacesEv')

  def quoteStrings(self) -> bool:
    """
    Calls Qt's 'bool QDebug::quoteStrings() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdebug.html#quoteStrings
    """
    #  bool QDebug::quoteStrings() const
    return self.uglySide.call('ritual_ZNK6QDebug12quoteStringsEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setVerbosity(self, verbosityLevel: int) -> None:
    """
    Calls Qt's 'void QDebug::setVerbosity(int verbosityLevel)'.

    Qt's own words: https://doc.qt.io/qt-6/qdebug.html#setVerbosity

    Parameters
    ----------

    verbosityLevel : int
      Passed on as it is.
    """
    #  void QDebug::setVerbosity(int verbosityLevel)
    self.uglySide.call('ritual_ZN6QDebug12setVerbosityEi', verbosityLevel)

  @overload(bool)
  def setAutoInsertSpaces(self, b: bool) -> None:
    """
    Calls Qt's 'void QDebug::setAutoInsertSpaces(bool b)'.

    Qt's own words: https://doc.qt.io/qt-6/qdebug.html#setAutoInsertSpaces

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QDebug::setAutoInsertSpaces(bool b)
    self.uglySide.call('ritual_ZN6QDebug19setAutoInsertSpacesEb', b)

  @overload(bool)
  def setQuoteStrings(self, b: bool) -> None:
    """
    Calls Qt's 'void QDebug::setQuoteStrings(bool b)'.

    Qt's own words: https://doc.qt.io/qt-6/qdebug.html#setQuoteStrings

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QDebug::setQuoteStrings(bool b)
    self.uglySide.call('ritual_ZN6QDebug15setQuoteStringsEb', b)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QIODevice)
  @overload(NoneType)
  def __init__(self, device: Optional[QIODevice]) -> None:
    """
    Notes what was given, for Qt's 'QDebug::QDebug(QIODevice *device)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdebug.html#QDebug

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDebug::QDebug(QIODevice *device)
    self._noteCreation(QDebug, lambda: Rituals.call(
        'ritual_ZN6QDebugC1EP9QIODevice', self._addressOf(device),
    ))

  @overload(QByteArray)
  def __init__(self, bytes: Optional[QByteArray]) -> None:
    """
    Notes what was given, for Qt's 'QDebug::QDebug(QByteArray *bytes)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdebug.html#QDebug

    Parameters
    ----------

    bytes : Optional[QByteArray]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDebug::QDebug(QByteArray *bytes)
    self._noteCreation(QDebug, lambda: Rituals.call(
        'ritual_ZN6QDebugC1EP10QByteArray', self._addressOf(bytes),
    ))

  @overload(THIS)
  def __init__(self, o: QDebug) -> None:
    """
    Notes what was given, for Qt's 'QDebug::QDebug(const QDebug &o)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdebug.html#QDebug

    Parameters
    ----------

    o : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.
    """
    #  QDebug::QDebug(const QDebug &o)
    self._noteCreation(QDebug, lambda: Rituals.call(
        'ritual_ZN6QDebugC1ERKS_', self._valueOf(o),
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

  @overload(int)
  def putUcs4(self, ucs4: int) -> None:
    """
    Calls Qt's 'void QDebug::putUcs4(uint ucs4)'.

    Qt's own words: https://doc.qt.io/qt-6/qdebug.html#putUcs4

    Parameters
    ----------

    ucs4 : int
      Passed on as it is.
    """
    #  void QDebug::putUcs4(uint ucs4)
    self.uglySide.call('ritual_ZN6QDebug7putUcs4Ej', ucs4)

  @overload(QChar, int)
  @overload(NoneType, int)
  def putString(self, begin: Optional[QChar], length: int) -> None:
    """
    Calls Qt's 'void QDebug::putString(const QChar *begin, size_t length)'.

    Qt's own words: https://doc.qt.io/qt-6/qdebug.html#putString

    Parameters
    ----------

    begin : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    length : int
      Passed on as it is.
    """
    #  void QDebug::putString(const QChar *begin, size_t length)
    self.uglySide.call(
        'ritual_ZN6QDebug9putStringEPK5QCharm',
        self._addressOf(begin), length,
    )

  @overload(int, int)
  def putTimeUnit(self, num: int, den: int) -> None:
    """
    Calls Qt's 'void QDebug::putTimeUnit(qint64 num, qint64 den)'.

    Qt's own words: https://doc.qt.io/qt-6/qdebug.html#putTimeUnit

    Parameters
    ----------

    num : int
      Passed on as it is.

    den : int
      Passed on as it is.
    """
    #  void QDebug::putTimeUnit(qint64 num, qint64 den)
    self.uglySide.call('ritual_ZN6QDebug11putTimeUnitExx', num, den)
