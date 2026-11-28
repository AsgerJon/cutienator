"""
Qt3DInput::QAbstractAxisInput binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/qabstractaxisinput.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DInput

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractAxisInput(Qt3DCore.QNode):
  """
  The cute side of Qt's Qt3DInput::QAbstractAxisInput: a plain Python object
  standing in front of one C++ Qt3DInput::QAbstractAxisInput.

  It is built on the cute 'Qt3DCore::QNode', as Qt's
  Qt3DInput::QAbstractAxisInput is built on Qt's Qt3DCore::QNode, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::QAbstractAxisInput that has a ritual and
  that Python can call so far, 6 names in all: 'metaObject', 'tr',
  'sourceDevice', 'setSourceDevice', 'sourceDeviceChanged', 'd_func'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DInput::QAbstractAxisInput::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DInput::QAbstractAxisInput::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DInput::QAbstractAxisInput::~QAbstractAxisInput()': the
    destructor: Python never removes a C++ Qt3DInput::QAbstractAxisInput.
  - Qt's 'Qt3DInput::QAbstractAxisInput::QAbstractAxisInput(
    QAbstractAxisInputPrivate &dd, QNode *parent)': takes a type Python has
    no way to hand over yet.
  - Qt's 'const QAbstractAxisInputPrivate
    *Qt3DInput::QAbstractAxisInput::d_func() const': takes in Python what
    'QAbstractAxisInputPrivate *Qt3DInput::QAbstractAxisInput::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DInput::QAbstractAxisInput is created at the first use, not by
    'Qt3DInput::QAbstractAxisInput(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::QAbstractAxisInput.
  - Qt tells when it has removed the C++ Qt3DInput::QAbstractAxisInput. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DInput::QAbstractAxisInput that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
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
    Calls Qt's 'QString Qt3DInput::QAbstractAxisInput::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractaxisinput.html#tr

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
    #  QString Qt3DInput::QAbstractAxisInput::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN9Qt3DInput18QAbstractAxisInput2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::QAbstractAxisInput'

  #  A C++ Qt3DInput::QAbstractAxisInput Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DInput_QAbstractAxisInput'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *Qt3DInput::QAbstractAxisInput::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractaxisinput.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DInput::QAbstractAxisInput::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput18QAbstractAxisInput10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sourceDevice(self) -> Optional[Qt3DInput.QAbstractPhysicalDevice]:
    """
    Calls Qt's 'QAbstractPhysicalDevice
    *Qt3DInput::QAbstractAxisInput::sourceDevice() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractaxisinput.html#sourceDevice

    Returns
    -------

    Optional[Qt3DInput.QAbstractPhysicalDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractPhysicalDevice *Qt3DInput::QAbstractAxisInput::sourceDevice()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput18QAbstractAxisInput12sourceDeviceEv',
    )
    return Qt3DInput.QAbstractPhysicalDevice._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DInput.QAbstractPhysicalDevice'])
  @overload(NoneType)
  def setSourceDevice(
      self,
      sourceDevice: Optional[Qt3DInput.QAbstractPhysicalDevice],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QAbstractAxisInput::setSourceDevice(QAbstractPhysicalDevice
    *sourceDevice)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractaxisinput.html#setSourceDevice

    Parameters
    ----------

    sourceDevice : Optional[Qt3DInput.QAbstractPhysicalDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QAbstractAxisInput::setSourceDevice(
    #      QAbstractPhysicalDevice *sourceDevice)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput18QAbstractAxisInput15setSourceDeviceEPNS_23QAb'
        'stractPhysicalDeviceE',
        self._addressOf(sourceDevice),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'Qt3DInput::QAbstractAxisInput::QAbstractAxisInput(
    QAbstractAxisInputPrivate &dd, QNode *parent)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DInput.QAbstractAxisInput.__init__' has no cute function yet. "
        "Qt's "
        "'Qt3DInput::QAbstractAxisInput::QAbstractAxisInput(QAbstractAxisInp"
        "utPrivate &dd, QNode *parent)': takes a type Python has no way to "
        "hand over yet.")

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

  @overload(WAIT['Qt3DInput.QAbstractPhysicalDevice'])
  @overload(NoneType)
  def sourceDeviceChanged(
      self,
      sourceDevice: Optional[Qt3DInput.QAbstractPhysicalDevice],
  ) -> None:
    """
    Calls Qt's 'void Qt3DInput::QAbstractAxisInput::sourceDeviceChanged(
    QAbstractPhysicalDevice *sourceDevice)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractaxisinput.html

    Parameters
    ----------

    sourceDevice : Optional[Qt3DInput.QAbstractPhysicalDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QAbstractAxisInput::sourceDeviceChanged(
    #      QAbstractPhysicalDevice *sourceDevice)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput18QAbstractAxisInput19sourceDeviceChangedEPNS_2'
        '3QAbstractPhysicalDeviceE',
        self._addressOf(sourceDevice),
    )

  def d_func(self) -> Optional[Qt3DInput.QAbstractAxisInputPrivate]:
    """
    Calls Qt's 'QAbstractAxisInputPrivate
    *Qt3DInput::QAbstractAxisInput::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractaxisinput.html#d_func

    Returns
    -------

    Optional[Qt3DInput.QAbstractAxisInputPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxisInputPrivate *Qt3DInput::QAbstractAxisInput::d_func()
    address = self.uglySide.call(
        'ritual_ZN9Qt3DInput18QAbstractAxisInput6d_funcEv',
    )
    return Qt3DInput.QAbstractAxisInputPrivate._cuteAt(address)
