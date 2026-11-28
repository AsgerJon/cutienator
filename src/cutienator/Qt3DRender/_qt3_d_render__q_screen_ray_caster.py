"""
Qt3DRender::QScreenRayCaster binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qscreenraycaster.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPoint
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScreenRayCaster(Qt3DRender.QAbstractRayCaster):
  """
  The cute side of Qt's Qt3DRender::QScreenRayCaster: a plain Python object
  standing in front of one C++ Qt3DRender::QScreenRayCaster.

  It is built on the cute 'Qt3DRender::QAbstractRayCaster', as Qt's
  Qt3DRender::QScreenRayCaster is built on Qt's
  Qt3DRender::QAbstractRayCaster, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QScreenRayCaster that has a ritual and
  that Python can call so far, 6 names in all: 'metaObject', 'tr',
  'position', 'setPosition', 'trigger', 'positionChanged'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QScreenRayCaster::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QScreenRayCaster::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QScreenRayCaster::~QScreenRayCaster()': the destructor:
    Python never removes a C++ Qt3DRender::QScreenRayCaster.
  - Qt's 'Qt3DRender::QAbstractRayCaster::Hits
    Qt3DRender::QScreenRayCaster::pick(const QPoint &position)': gives a type
    Python has no way to take yet.
  - Qt's
    'Qt3DRender::QScreenRayCaster::QScreenRayCaster(QAbstractRayCasterPrivate
    &dd, QNode *parent)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QScreenRayCaster is created at the first use, not by
    'Qt3DRender::QScreenRayCaster(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QScreenRayCaster.
  - Qt tells when it has removed the C++ Qt3DRender::QScreenRayCaster. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DRender::QScreenRayCaster that has no cute function
    yet, 'pick', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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
    Calls Qt's 'QString Qt3DRender::QScreenRayCaster::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qscreenraycaster.html#tr

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
    #  QString Qt3DRender::QScreenRayCaster::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender16QScreenRayCaster2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QScreenRayCaster'

  #  A C++ Qt3DRender::QScreenRayCaster Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QScreenRayCaster'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QScreenRayCaster::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qscreenraycaster.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QScreenRayCaster::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QScreenRayCaster10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def position(self) -> QPoint:
    """
    Calls Qt's 'QPoint Qt3DRender::QScreenRayCaster::position() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qscreenraycaster.html#position

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint Qt3DRender::QScreenRayCaster::position() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QScreenRayCaster8positionEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPoint)
  def setPosition(self, position: QPoint) -> None:
    """
    Calls Qt's 'void Qt3DRender::QScreenRayCaster::setPosition(const QPoint
    &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qscreenraycaster.html#setPosition

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void Qt3DRender::QScreenRayCaster::setPosition(const QPoint &position)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QScreenRayCaster11setPositionERK6QPoint',
        self._valueOf(position),
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QScreenRayCaster::QScreenRayCaster(QNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qscreenraycaster.html#QScreenRayCaster

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QScreenRayCaster::QScreenRayCaster(QNode *parent)
    self._noteCreation(QScreenRayCaster, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender16QScreenRayCasterC1EPN8Qt3DCore5QNodeE',
        self._addressOf(parent),
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

  @overload()
  def trigger(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::QScreenRayCaster::trigger()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qscreenraycaster.html#trigger
    """
    #  void Qt3DRender::QScreenRayCaster::trigger()
    self.uglySide.call('ritual_ZN10Qt3DRender16QScreenRayCaster7triggerEv')

  @overload(QPoint)
  def trigger(self, position: QPoint) -> None:
    """
    Calls Qt's 'void Qt3DRender::QScreenRayCaster::trigger(const QPoint
    &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qscreenraycaster.html#trigger

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void Qt3DRender::QScreenRayCaster::trigger(const QPoint &position)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QScreenRayCaster7triggerERK6QPoint',
        self._valueOf(position),
    )

  @overload(QPoint)
  def positionChanged(self, position: QPoint) -> None:
    """
    Calls Qt's 'void Qt3DRender::QScreenRayCaster::positionChanged(const
    QPoint &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qscreenraycaster.html#positionChanged

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void Qt3DRender::QScreenRayCaster::positionChanged(const QPoint
    #      &position)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QScreenRayCaster15positionChangedERK6QPoint',
        self._valueOf(position),
    )

  @staticmethod
  def pick(*__, **_) -> Never:
    """
    Qt's 'Qt3DRender::QAbstractRayCaster::Hits
    Qt3DRender::QScreenRayCaster::pick(const QPoint &position)': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QScreenRayCaster.pick' has no cute function yet. Qt's "
        "'Qt3DRender::QAbstractRayCaster::Hits "
        "Qt3DRender::QScreenRayCaster::pick(const QPoint &position)': gives "
        "a type Python has no way to take yet.")
