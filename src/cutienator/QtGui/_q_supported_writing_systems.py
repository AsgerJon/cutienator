"""
QSupportedWritingSystems binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformfontdatabase.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QFontDatabase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QDebug
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']


class QSupportedWritingSystems(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSupportedWritingSystems: a plain Python object
  standing in front of one C++ QSupportedWritingSystems.

  C++ hands a QSupportedWritingSystems around as a copy, so every C++
  QSupportedWritingSystems behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSupportedWritingSystems that has a ritual and that
  Python can call so far, 6 names in all: 'setSupported', 'supported',
  'detach', '__eq__', '__ne__', '__rlshift__'. It can be made from Python, in
  2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSupportedWritingSystems &QSupportedWritingSystems::operator=(const
    QSupportedWritingSystems &other)': assignment: Python binds a name and
    has no operator for it.
  - Qt's 'QSupportedWritingSystems::~QSupportedWritingSystems()': the
    destructor: Python removes its C++ QSupportedWritingSystems by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QSupportedWritingSystems is created at the first use, not by
    'QSupportedWritingSystems(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSupportedWritingSystems back gives a copy the ritual
    made for Python, in a new cute QSupportedWritingSystems.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSupportedWritingSystems'

  #  Qt's '~QSupportedWritingSystems()'. Naming it makes this a value class:
  #  Python owns every C++ QSupportedWritingSystems behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QSupportedWritingSystemsD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QFontDatabase.WritingSystem)
  def supported(self, a0: QFontDatabase.WritingSystem) -> bool:
    """
    Calls Qt's 'bool
    QSupportedWritingSystems::supported(QFontDatabase::WritingSystem a0)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsupportedwritingsystems.html#supported

    Parameters
    ----------

    a0 : QFontDatabase.WritingSystem
      Passed on as its number.
    """
    #  bool QSupportedWritingSystems::supported(QFontDatabase::WritingSystem
    #      a0) const
    return self.uglySide.call(
        'ritual_ZNK24QSupportedWritingSystems9supportedEN13QFontDatabase13W'
        'ritingSystemE',
        a0.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QFontDatabase.WritingSystem)
  @overload(QFontDatabase.WritingSystem, bool)
  def setSupported(
      self,
      a0: QFontDatabase.WritingSystem,
      supported: bool = True,
  ) -> None:
    """
    Calls Qt's 'void
    QSupportedWritingSystems::setSupported(QFontDatabase::WritingSystem a0,
    bool supported)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsupportedwritingsystems.html#setSupported

    Parameters
    ----------

    a0 : QFontDatabase.WritingSystem
      Passed on as its number.

    supported : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QSupportedWritingSystems::setSupported(QFontDatabase::
    #      WritingSystem a0, bool supported)
    self.uglySide.call(
        'ritual_ZN24QSupportedWritingSystems12setSupportedEN13QFontDatabase'
        '13WritingSystemEb',
        a0.value, supported,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, a1: QSupportedWritingSystems) -> bool:
    """
    Calls Qt's 'bool operator==(const QSupportedWritingSystems &a0, const
    QSupportedWritingSystems &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsupportedwritingsystems.html#operator==

    Parameters
    ----------

    a1 : QSupportedWritingSystems
      Passed on as a value: Qt reads the C++ QSupportedWritingSystems, which
      stays Python's own.
    """
    #  bool operator==(const QSupportedWritingSystems &a0, const
    #      QSupportedWritingSystems &a1)
    return Rituals.call(
        'ritual_ZeqRK24QSupportedWritingSystemsS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(a1),
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
  def __ne__(self, a1: QSupportedWritingSystems) -> bool:
    """
    Calls Qt's 'bool operator!=(const QSupportedWritingSystems &a0, const
    QSupportedWritingSystems &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsupportedwritingsystems.html#operator!=

    Parameters
    ----------

    a1 : QSupportedWritingSystems
      Passed on as a value: Qt reads the C++ QSupportedWritingSystems, which
      stays Python's own.
    """
    #  bool operator!=(const QSupportedWritingSystems &a0, const
    #      QSupportedWritingSystems &a1)
    return Rituals.call(
        'ritual_ZneRK24QSupportedWritingSystemsS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(a1),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(QDebug)
  def __rlshift__(self, a0: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug a0, const QSupportedWritingSystems
    &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsupportedwritingsystems.html#operator<<

    Parameters
    ----------

    a0 : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug a0, const QSupportedWritingSystems &a1)
    address = Rituals.call(
        'ritual_Zls6QDebugRK24QSupportedWritingSystems',
        CuteMixin._valueOf(a0), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
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
    'QSupportedWritingSystems::QSupportedWritingSystems()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsupportedwritingsystems.html
    """
    #  QSupportedWritingSystems::QSupportedWritingSystems()
    self._noteCreation(QSupportedWritingSystems, lambda: Rituals.call(
        'ritual_ZN24QSupportedWritingSystemsC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QSupportedWritingSystems) -> None:
    """
    Notes what was given, for Qt's
    'QSupportedWritingSystems::QSupportedWritingSystems(const
    QSupportedWritingSystems &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsupportedwritingsystems.html

    Parameters
    ----------

    other : QSupportedWritingSystems
      Passed on as a value: Qt reads the C++ QSupportedWritingSystems, which
      stays Python's own.
    """
    #  QSupportedWritingSystems::QSupportedWritingSystems(const
    #      QSupportedWritingSystems &other)
    self._noteCreation(QSupportedWritingSystems, lambda: Rituals.call(
        'ritual_ZN24QSupportedWritingSystemsC1ERKS_', self._valueOf(other),
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

  def detach(self) -> None:
    """
    Calls Qt's 'void QSupportedWritingSystems::detach()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsupportedwritingsystems.html#detach
    """
    #  void QSupportedWritingSystems::detach()
    self.uglySide.call('ritual_ZN24QSupportedWritingSystems6detachEv')
