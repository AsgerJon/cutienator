"""
QInputDeviceManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qinputdevicemanager_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QInputDeviceManager to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPoint
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QInputDeviceManager(QObject):
  """
  The cute side of Qt's QInputDeviceManager: a plain Python object standing
  in front of one C++ QInputDeviceManager.

  It is built on the cute 'QObject', as Qt's QInputDeviceManager is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QInputDeviceManager that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'tr', 'deviceCount',
  'setCursorPos', 'keyboardModifiers', 'setKeyboardModifiers'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QInputDeviceManager::~QInputDeviceManager()': the destructor:
    Python never removes a C++ QInputDeviceManager.

  What has no ritual
  ------------------

  8 of the 16 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 2 a signal; 1 a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QInputDeviceManager is created at the first use, not by
    'QInputDeviceManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QInputDeviceManager.
  - Qt tells when it has removed the C++ QInputDeviceManager. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QInputDeviceManager, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class DeviceType(CuteNum):
    """
    The enum 'QInputDeviceManager::DeviceType' of Qt, with the 6 names Qt
    gives in it.
    """

    DeviceTypeUnknown = Kee[int](0)
    DeviceTypePointer = Kee[int](1)
    DeviceTypeKeyboard = Kee[int](2)
    DeviceTypeTouch = Kee[int](3)
    DeviceTypeTablet = Kee[int](4)
    NumDeviceTypes = Kee[int](5)

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
    Calls Qt's 'QString QInputDeviceManager::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputdevicemanager.html#tr

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
    #  QString QInputDeviceManager::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QInputDeviceManager2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QInputDeviceManager'

  #  A C++ QInputDeviceManager Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QInputDeviceManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QInputDeviceManager::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputdevicemanager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QInputDeviceManager::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QInputDeviceManager10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(DeviceType)
  def deviceCount(self, type: DeviceType) -> int:
    """
    Calls Qt's 'int QInputDeviceManager::deviceCount(DeviceType type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputdevicemanager.html#deviceCount

    Parameters
    ----------

    type : DeviceType
      Passed on as its number.
    """
    #  int QInputDeviceManager::deviceCount(DeviceType type) const
    return self.uglySide.call(
        'ritual_ZNK19QInputDeviceManager11deviceCountENS_10DeviceTypeE',
        type.value,
    )

  def keyboardModifiers(self) -> Qt.KeyboardModifiers:
    """
    Calls Qt's 'Qt::KeyboardModifiers
    QInputDeviceManager::keyboardModifiers() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputdevicemanager.html#keyboardModifiers

    Returns
    -------

    Qt.KeyboardModifiers
      The value standing for the combination Qt gave back.
    """
    #  Qt::KeyboardModifiers QInputDeviceManager::keyboardModifiers() const
    return Qt.KeyboardModifiers(self.uglySide.call(
        'ritual_ZNK19QInputDeviceManager17keyboardModifiersEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPoint)
  def setCursorPos(self, pos: QPoint) -> None:
    """
    Calls Qt's 'void QInputDeviceManager::setCursorPos(const QPoint &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputdevicemanager.html#setCursorPos

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QInputDeviceManager::setCursorPos(const QPoint &pos)
    self.uglySide.call(
        'ritual_ZN19QInputDeviceManager12setCursorPosERK6QPoint',
        self._valueOf(pos),
    )

  @overload(Qt.KeyboardModifiers)
  def setKeyboardModifiers(self, mods: Qt.KeyboardModifiers) -> None:
    """
    Calls Qt's 'void
    QInputDeviceManager::setKeyboardModifiers(Qt::KeyboardModifiers mods)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputdevicemanager.html#setKeyboardModifiers

    Parameters
    ----------

    mods : Qt.KeyboardModifiers
      Passed on as its number.
    """
    #  void QInputDeviceManager::setKeyboardModifiers(Qt::KeyboardModifiers
    #      mods)
    self.uglySide.call(
        'ritual_ZN19QInputDeviceManager20setKeyboardModifiersE6QFlagsIN2Qt1'
        '6KeyboardModifierEE',
        mods.value,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QInputDeviceManager::QInputDeviceManager(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputdevicemanager.html#QInputDeviceManager

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QInputDeviceManager::QInputDeviceManager(QObject *parent)
    self._noteCreation(QInputDeviceManager, lambda: Rituals.call(
        'ritual_ZN19QInputDeviceManagerC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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
