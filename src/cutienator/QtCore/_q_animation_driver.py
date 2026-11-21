"""
QAnimationDriver binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qabstractanimation.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from . import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAnimationDriver(QObject):
  """
  The cute side of Qt's QAnimationDriver: a plain Python object standing in
  front of one C++ QAnimationDriver.

  It is built on the cute 'QObject', as Qt's QAnimationDriver is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAnimationDriver that has a ritual and that Python
  can call so far, 7 names in all: 'metaObject', 'tr', 'advance', 'install',
  'uninstall', 'isRunning', 'elapsed'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAnimationDriver::~QAnimationDriver()': the destructor: Python
    never removes a C++ QAnimationDriver.

  What has no ritual
  ------------------

  12 of the 21 functions Qt declares: 4 protected; 3 private; 2 takes or
  gives a type that cannot be passed yet; 2 a signal; 1 a template.

  What to expect
  --------------

  - The C++ QAnimationDriver is created at the first use, not by
    'QAnimationDriver(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAnimationDriver.
  - Qt tells when it has removed the C++ QAnimationDriver. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QAnimationDriver::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qanimationdriver.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAnimationDriver::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QAnimationDriver2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAnimationDriver'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAnimationDriver::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qanimationdriver.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAnimationDriver::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QAnimationDriver10metaObjectEv',
    )
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def isRunning(self) -> bool:
    """
    Calls Qt's 'bool QAnimationDriver::isRunning() const'.

    Qt's own words: https://doc.qt.io/qt-6/qanimationdriver.html#isRunning
    """
    #  bool QAnimationDriver::isRunning() const
    return self.uglySide.call('ritual_ZNK16QAnimationDriver9isRunningEv')

  def elapsed(self) -> int:
    """
    Calls Qt's 'qint64 QAnimationDriver::elapsed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qanimationdriver.html#elapsed
    """
    #  qint64 QAnimationDriver::elapsed() const
    return self.uglySide.call('ritual_ZNK16QAnimationDriver7elapsedEv')

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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QAnimationDriver::QAnimationDriver(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationdriver.html#QAnimationDriver

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAnimationDriver::QAnimationDriver(QObject *parent)
    self._noteCreation(QAnimationDriver, lambda: Rituals.call(
        'ritual_ZN16QAnimationDriverC1EP7QObject', self._addressOf(parent),
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

  def advance(self) -> None:
    """
    Calls Qt's 'void QAnimationDriver::advance()'.

    Qt's own words: https://doc.qt.io/qt-6/qanimationdriver.html#advance
    """
    #  void QAnimationDriver::advance()
    self.uglySide.call('ritual_ZN16QAnimationDriver7advanceEv')

  def install(self) -> None:
    """
    Calls Qt's 'void QAnimationDriver::install()'.

    Qt's own words: https://doc.qt.io/qt-6/qanimationdriver.html#install
    """
    #  void QAnimationDriver::install()
    self.uglySide.call('ritual_ZN16QAnimationDriver7installEv')

  def uninstall(self) -> None:
    """
    Calls Qt's 'void QAnimationDriver::uninstall()'.

    Qt's own words: https://doc.qt.io/qt-6/qanimationdriver.html#uninstall
    """
    #  void QAnimationDriver::uninstall()
    self.uglySide.call('ritual_ZN16QAnimationDriver9uninstallEv')
