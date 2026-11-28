"""
QWebEngineUrlScheme binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebengineurlscheme.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QWebEngineUrlScheme(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebEngineUrlScheme: a plain Python object standing
  in front of one C++ QWebEngineUrlScheme.

  C++ hands a QWebEngineUrlScheme around as a copy, so every C++
  QWebEngineUrlScheme behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QWebEngineUrlScheme that has a ritual and that
  Python can call so far, 13 names in all: '__eq__', '__ne__', 'name',
  'setName', 'syntax', 'setSyntax', 'defaultPort', 'setDefaultPort', 'flags',
  'setFlags', 'registerScheme', 'schemeByName', 'lockSchemes'. It can be made
  from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWebEngineUrlScheme &QWebEngineUrlScheme::operator=(const
    QWebEngineUrlScheme &that)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QWebEngineUrlScheme::QWebEngineUrlScheme(QWebEngineUrlScheme
    &&that)': takes a type Python has no way to hand over yet.
  - Qt's 'QWebEngineUrlScheme
    &QWebEngineUrlScheme::operator=(QWebEngineUrlScheme &&that)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QWebEngineUrlScheme::~QWebEngineUrlScheme()': the destructor:
    Python removes its C++ QWebEngineUrlScheme by it, and has no other use
    for it.
  - Qt's 'QWebEngineUrlScheme::QWebEngineUrlScheme(QWebEngineUrlSchemePrivate
    *d)': names 'QWebEngineUrlSchemePrivate', which has no cute class yet.

  What has no ritual
  ------------------

  3 of the 24 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QWebEngineUrlScheme is created at the first use, not by
    'QWebEngineUrlScheme(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWebEngineUrlScheme back gives a copy the ritual made
    for Python, in a new cute QWebEngineUrlScheme.
  """

  #  The enums Qt writes inside QWebEngineUrlScheme, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Flag(CuteFlags):
    """
    The flags enum 'QWebEngineUrlScheme::Flag' of Qt, with the 9 names Qt
    gives in it. Qt names the type of its combinations
    'QWebEngineUrlScheme::Flags'.
    """

    SecureScheme = 0x1
    LocalScheme = 0x2
    LocalAccessAllowed = 0x4
    NoAccessAllowed = 0x8
    ServiceWorkersAllowed = 0x10
    ViewSourceAllowed = 0x20
    ContentSecurityPolicyIgnored = 0x40
    CorsEnabled = 0x80
    FetchApiAllowed = 0x100

  Flags = Flag

  class SpecialPort(CuteNum):
    """
    The enum 'QWebEngineUrlScheme::SpecialPort' of Qt, with the 1 names Qt
    gives in it.
    """

    PortUnspecified = Kee[int](-1)

  class Syntax(CuteNum, scoped=True):
    """
    The enum 'QWebEngineUrlScheme::Syntax' of Qt, with the 4 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    HostPortAndUserInformation = Kee[int](0)
    HostAndPort = Kee[int](1)
    Host = Kee[int](2)
    Path = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS)
  def registerScheme(scheme: QWebEngineUrlScheme) -> None:
    """
    Calls Qt's 'void QWebEngineUrlScheme::registerScheme(const
    QWebEngineUrlScheme &scheme)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlscheme.html#registerScheme

    Parameters
    ----------

    scheme : QWebEngineUrlScheme
      Passed on as a value: Qt reads the C++ QWebEngineUrlScheme, which stays
      Python's own.
    """
    #  void QWebEngineUrlScheme::registerScheme(const QWebEngineUrlScheme
    #      &scheme)
    Rituals.call(
        'ritual_ZN19QWebEngineUrlScheme14registerSchemeERKS_',
        CuteMixin._valueOf(scheme),
    )

  @staticmethod
  @overload(QByteArray)
  def schemeByName(name: QByteArray) -> QWebEngineUrlScheme:
    """
    Calls Qt's 'QWebEngineUrlScheme QWebEngineUrlScheme::schemeByName(const
    QByteArray &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlscheme.html#schemeByName

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QWebEngineUrlScheme
      A new cute QWebEngineUrlScheme around the copy Qt gave back. Python
      owns it.
    """
    #  QWebEngineUrlScheme QWebEngineUrlScheme::schemeByName(const QByteArray
    #      &name)
    address = Rituals.call(
        'ritual_ZN19QWebEngineUrlScheme12schemeByNameERK10QByteArray',
        CuteMixin._valueOf(name),
    )
    return QWebEngineUrlScheme._cuteOwning(address)

  @staticmethod
  def lockSchemes() -> None:
    """
    Calls Qt's 'void QWebEngineUrlScheme::lockSchemes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlscheme.html#lockSchemes
    """
    #  void QWebEngineUrlScheme::lockSchemes()
    Rituals.call('ritual_ZN19QWebEngineUrlScheme11lockSchemesEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineUrlScheme'

  #  Qt's '~QWebEngineUrlScheme()'. Naming it makes this a value class:
  #  Python owns every C++ QWebEngineUrlScheme behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QWebEngineUrlSchemeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QWebEngineUrlScheme::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineurlscheme.html#name

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QWebEngineUrlScheme::name() const
    address = self.uglySide.call('ritual_ZNK19QWebEngineUrlScheme4nameEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def syntax(self) -> Syntax:
    """
    Calls Qt's 'Syntax QWebEngineUrlScheme::syntax() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineurlscheme.html#syntax

    Returns
    -------

    Syntax
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Syntax(number)' gives.
    """
    #  Syntax QWebEngineUrlScheme::syntax() const
    return QWebEngineUrlScheme.Syntax(self.uglySide.call(
        'ritual_ZNK19QWebEngineUrlScheme6syntaxEv',
    ))

  def defaultPort(self) -> int:
    """
    Calls Qt's 'int QWebEngineUrlScheme::defaultPort() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlscheme.html#defaultPort
    """
    #  int QWebEngineUrlScheme::defaultPort() const
    return self.uglySide.call(
        'ritual_ZNK19QWebEngineUrlScheme11defaultPortEv',
    )

  def flags(self) -> Flags:
    """
    Calls Qt's 'Flags QWebEngineUrlScheme::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineurlscheme.html#flags

    Returns
    -------

    Flags
      The value standing for the combination Qt gave back.
    """
    #  Flags QWebEngineUrlScheme::flags() const
    return QWebEngineUrlScheme.Flags(self.uglySide.call(
        'ritual_ZNK19QWebEngineUrlScheme5flagsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  def setName(self, newValue: QByteArray) -> None:
    """
    Calls Qt's 'void QWebEngineUrlScheme::setName(const QByteArray
    &newValue)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineurlscheme.html#setName

    Parameters
    ----------

    newValue : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QWebEngineUrlScheme::setName(const QByteArray &newValue)
    self.uglySide.call(
        'ritual_ZN19QWebEngineUrlScheme7setNameERK10QByteArray',
        self._valueOf(newValue),
    )

  @overload(Syntax)
  def setSyntax(self, newValue: Syntax) -> None:
    """
    Calls Qt's 'void QWebEngineUrlScheme::setSyntax(Syntax newValue)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineurlscheme.html#setSyntax

    Parameters
    ----------

    newValue : Syntax
      Passed on as its number.
    """
    #  void QWebEngineUrlScheme::setSyntax(Syntax newValue)
    self.uglySide.call(
        'ritual_ZN19QWebEngineUrlScheme9setSyntaxENS_6SyntaxE',
        newValue.value,
    )

  @overload(int)
  def setDefaultPort(self, newValue: int) -> None:
    """
    Calls Qt's 'void QWebEngineUrlScheme::setDefaultPort(int newValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlscheme.html#setDefaultPort

    Parameters
    ----------

    newValue : int
      Passed on as it is.
    """
    #  void QWebEngineUrlScheme::setDefaultPort(int newValue)
    self.uglySide.call(
        'ritual_ZN19QWebEngineUrlScheme14setDefaultPortEi', newValue,
    )

  @overload(Flags)
  def setFlags(self, newValue: Flags) -> None:
    """
    Calls Qt's 'void QWebEngineUrlScheme::setFlags(Flags newValue)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebengineurlscheme.html#setFlags

    Parameters
    ----------

    newValue : Flags
      Passed on as its number.
    """
    #  void QWebEngineUrlScheme::setFlags(Flags newValue)
    self.uglySide.call(
        'ritual_ZN19QWebEngineUrlScheme8setFlagsE6QFlagsINS_4FlagEE',
        newValue.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, that: QWebEngineUrlScheme) -> bool:
    """
    Calls Qt's 'bool QWebEngineUrlScheme::operator==(const
    QWebEngineUrlScheme &that) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlscheme.html#operator==

    Parameters
    ----------

    that : QWebEngineUrlScheme
      Passed on as a value: Qt reads the C++ QWebEngineUrlScheme, which stays
      Python's own.
    """
    #  bool QWebEngineUrlScheme::operator==(const QWebEngineUrlScheme &that)
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QWebEngineUrlSchemeeqERKS_', self._valueOf(that),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, that: QWebEngineUrlScheme) -> bool:
    """
    Calls Qt's 'bool QWebEngineUrlScheme::operator!=(const
    QWebEngineUrlScheme &that) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlscheme.html#operator!=

    Parameters
    ----------

    that : QWebEngineUrlScheme
      Passed on as a value: Qt reads the C++ QWebEngineUrlScheme, which stays
      Python's own.
    """
    #  bool QWebEngineUrlScheme::operator!=(const QWebEngineUrlScheme &that)
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QWebEngineUrlSchemeneERKS_', self._valueOf(that),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QWebEngineUrlScheme::QWebEngineUrlScheme()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlscheme.html#QWebEngineUrlScheme
    """
    #  QWebEngineUrlScheme::QWebEngineUrlScheme()
    self._noteCreation(QWebEngineUrlScheme, lambda: Rituals.call(
        'ritual_ZN19QWebEngineUrlSchemeC1Ev',
    ))

  @overload(QByteArray)
  def __init__(self, name: QByteArray) -> None:
    """
    Notes what was given, for Qt's
    'QWebEngineUrlScheme::QWebEngineUrlScheme(const QByteArray &name)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlscheme.html#QWebEngineUrlScheme

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  QWebEngineUrlScheme::QWebEngineUrlScheme(const QByteArray &name)
    self._noteCreation(QWebEngineUrlScheme, lambda: Rituals.call(
        'ritual_ZN19QWebEngineUrlSchemeC1ERK10QByteArray',
        self._valueOf(name),
    ))

  @overload(THIS)
  def __init__(self, that: QWebEngineUrlScheme) -> None:
    """
    Notes what was given, for Qt's
    'QWebEngineUrlScheme::QWebEngineUrlScheme(const QWebEngineUrlScheme
    &that)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineurlscheme.html#QWebEngineUrlScheme

    Parameters
    ----------

    that : QWebEngineUrlScheme
      Passed on as a value: Qt reads the C++ QWebEngineUrlScheme, which stays
      Python's own.
    """
    #  QWebEngineUrlScheme::QWebEngineUrlScheme(const QWebEngineUrlScheme
    #      &that)
    self._noteCreation(QWebEngineUrlScheme, lambda: Rituals.call(
        'ritual_ZN19QWebEngineUrlSchemeC1ERKS_', self._valueOf(that),
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
