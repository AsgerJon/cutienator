"""
QDBusUnixFileDescriptor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/qdbusunixfiledescriptor.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QDBusUnixFileDescriptor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDBusUnixFileDescriptor: a plain Python object
  standing in front of one C++ QDBusUnixFileDescriptor.

  C++ hands a QDBusUnixFileDescriptor around as a copy, so every C++
  QDBusUnixFileDescriptor behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDBusUnixFileDescriptor that has a ritual and that
  Python can call so far, 6 names in all: 'isValid', 'fileDescriptor',
  'setFileDescriptor', 'giveFileDescriptor', 'takeFileDescriptor',
  'isSupported'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDBusUnixFileDescriptor
    &QDBusUnixFileDescriptor::operator=(QDBusUnixFileDescriptor &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QDBusUnixFileDescriptor &QDBusUnixFileDescriptor::operator=(const
    QDBusUnixFileDescriptor &other)': assignment: Python binds a name and has
    no operator for it.
  - Qt's 'QDBusUnixFileDescriptor::~QDBusUnixFileDescriptor()': the
    destructor: Python removes its C++ QDBusUnixFileDescriptor by it, and has
    no other use for it.
  - Qt's 'void QDBusUnixFileDescriptor::swap(QDBusUnixFileDescriptor
    &other)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QDBusUnixFileDescriptor is created at the first use, not by
    'QDBusUnixFileDescriptor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDBusUnixFileDescriptor back gives a copy the ritual
    made for Python, in a new cute QDBusUnixFileDescriptor.
  - Each name of Qt's QDBusUnixFileDescriptor that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def isSupported() -> bool:
    """
    Calls Qt's 'bool QDBusUnixFileDescriptor::isSupported()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusunixfiledescriptor.html#isSupported
    """
    #  bool QDBusUnixFileDescriptor::isSupported()
    return Rituals.call('ritual_ZN23QDBusUnixFileDescriptor11isSupportedEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusUnixFileDescriptor'

  #  Qt's '~QDBusUnixFileDescriptor()'. Naming it makes this a value class:
  #  Python owns every C++ QDBusUnixFileDescriptor behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QDBusUnixFileDescriptorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QDBusUnixFileDescriptor::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusunixfiledescriptor.html#isValid
    """
    #  bool QDBusUnixFileDescriptor::isValid() const
    return self.uglySide.call(
        'ritual_ZNK23QDBusUnixFileDescriptor7isValidEv',
    )

  def fileDescriptor(self) -> int:
    """
    Calls Qt's 'int QDBusUnixFileDescriptor::fileDescriptor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusunixfiledescriptor.html#fileDescriptor
    """
    #  int QDBusUnixFileDescriptor::fileDescriptor() const
    return self.uglySide.call(
        'ritual_ZNK23QDBusUnixFileDescriptor14fileDescriptorEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setFileDescriptor(self, fileDescriptor: int) -> None:
    """
    Calls Qt's 'void QDBusUnixFileDescriptor::setFileDescriptor(int
    fileDescriptor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusunixfiledescriptor.html#setFileDescriptor

    Parameters
    ----------

    fileDescriptor : int
      Passed on as it is.
    """
    #  void QDBusUnixFileDescriptor::setFileDescriptor(int fileDescriptor)
    self.uglySide.call(
        'ritual_ZN23QDBusUnixFileDescriptor17setFileDescriptorEi',
        fileDescriptor,
    )

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QDBusUnixFileDescriptor::QDBusUnixFileDescriptor()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusunixfiledescriptor.html
    """
    #  QDBusUnixFileDescriptor::QDBusUnixFileDescriptor()
    self._noteCreation(QDBusUnixFileDescriptor, lambda: Rituals.call(
        'ritual_ZN23QDBusUnixFileDescriptorC1Ev',
    ))

  @overload(int)
  def __init__(self, fileDescriptor: int) -> None:
    """
    Notes what was given, for Qt's
    'QDBusUnixFileDescriptor::QDBusUnixFileDescriptor(int fileDescriptor)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusunixfiledescriptor.html

    Parameters
    ----------

    fileDescriptor : int
      Passed on as it is.
    """
    #  QDBusUnixFileDescriptor::QDBusUnixFileDescriptor(int fileDescriptor)
    self._noteCreation(QDBusUnixFileDescriptor, lambda: Rituals.call(
        'ritual_ZN23QDBusUnixFileDescriptorC1Ei', fileDescriptor,
    ))

  @overload(THIS)
  def __init__(self, other: QDBusUnixFileDescriptor) -> None:
    """
    Notes what was given, for Qt's
    'QDBusUnixFileDescriptor::QDBusUnixFileDescriptor(const
    QDBusUnixFileDescriptor &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusunixfiledescriptor.html

    Parameters
    ----------

    other : QDBusUnixFileDescriptor
      Passed on as a value: Qt reads the C++ QDBusUnixFileDescriptor, which
      stays Python's own.
    """
    #  QDBusUnixFileDescriptor::QDBusUnixFileDescriptor(const
    #      QDBusUnixFileDescriptor &other)
    self._noteCreation(QDBusUnixFileDescriptor, lambda: Rituals.call(
        'ritual_ZN23QDBusUnixFileDescriptorC1ERKS_', self._valueOf(other),
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
  def giveFileDescriptor(self, fileDescriptor: int) -> None:
    """
    Calls Qt's 'void QDBusUnixFileDescriptor::giveFileDescriptor(int
    fileDescriptor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusunixfiledescriptor.html#giveFileDescriptor

    Parameters
    ----------

    fileDescriptor : int
      Passed on as it is.
    """
    #  void QDBusUnixFileDescriptor::giveFileDescriptor(int fileDescriptor)
    self.uglySide.call(
        'ritual_ZN23QDBusUnixFileDescriptor18giveFileDescriptorEi',
        fileDescriptor,
    )

  def takeFileDescriptor(self) -> int:
    """
    Calls Qt's 'int QDBusUnixFileDescriptor::takeFileDescriptor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusunixfiledescriptor.html#takeFileDescriptor
    """
    #  int QDBusUnixFileDescriptor::takeFileDescriptor()
    return self.uglySide.call(
        'ritual_ZN23QDBusUnixFileDescriptor18takeFileDescriptorEv',
    )

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QDBusUnixFileDescriptor::swap(QDBusUnixFileDescriptor
    &other)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDBusUnixFileDescriptor.swap' has no cute function yet. Qt's "
        "'void QDBusUnixFileDescriptor::swap(QDBusUnixFileDescriptor "
        "&other)': takes a type Python has no way to hand over yet.")
