"""
Qt3DRender::QRayCaster binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qraycaster.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRayCaster(Qt3DRender.QAbstractRayCaster):
  """
  The cute side of Qt's Qt3DRender::QRayCaster: a plain Python object
  standing in front of one C++ Qt3DRender::QRayCaster.

  It is built on the cute 'Qt3DRender::QAbstractRayCaster', as Qt's
  Qt3DRender::QRayCaster is built on Qt's Qt3DRender::QAbstractRayCaster, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QRayCaster that has a ritual and that
  Python can call so far, 12 names in all: 'metaObject', 'tr', 'origin',
  'direction', 'length', 'setOrigin', 'setDirection', 'setLength', 'trigger',
  'originChanged', 'directionChanged', 'lengthChanged'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QRayCaster::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DRender::QRayCaster::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QRayCaster::~QRayCaster()': the destructor: Python
    never removes a C++ Qt3DRender::QRayCaster.
  - Qt's 'Qt3DRender::QAbstractRayCaster::Hits
    Qt3DRender::QRayCaster::pick(const QVector3D &origin, const QVector3D
    &direction, float length)': gives a type Python has no way to take yet.
  - Qt's 'Qt3DRender::QRayCaster::QRayCaster(QAbstractRayCasterPrivate &dd,
    QNode *parent)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QRayCaster is created at the first use, not by
    'Qt3DRender::QRayCaster(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QRayCaster.
  - Qt tells when it has removed the C++ Qt3DRender::QRayCaster. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DRender::QRayCaster that has no cute function yet,
    'pick', holds a function that raises 'NotImplementedError', and its
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
    Calls Qt's 'QString Qt3DRender::QRayCaster::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qraycaster.html#tr

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
    #  QString Qt3DRender::QRayCaster::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender10QRayCaster2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QRayCaster'

  #  A C++ Qt3DRender::QRayCaster Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QRayCaster'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QRayCaster::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qraycaster.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QRayCaster::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QRayCaster10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def origin(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DRender::QRayCaster::origin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qraycaster.html#origin

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DRender::QRayCaster::origin() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QRayCaster6originEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def direction(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DRender::QRayCaster::direction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qraycaster.html#direction

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DRender::QRayCaster::direction() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QRayCaster9directionEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def length(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QRayCaster::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qraycaster.html#length
    """
    #  float Qt3DRender::QRayCaster::length() const
    return self.uglySide.call('ritual_ZNK10Qt3DRender10QRayCaster6lengthEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector3D)
  def setOrigin(self, origin: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRayCaster::setOrigin(const QVector3D
    &origin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qraycaster.html#setOrigin

    Parameters
    ----------

    origin : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DRender::QRayCaster::setOrigin(const QVector3D &origin)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QRayCaster9setOriginERK9QVector3D',
        self._valueOf(origin),
    )

  @overload(QVector3D)
  def setDirection(self, direction: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRayCaster::setDirection(const QVector3D
    &direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qraycaster.html#setDirection

    Parameters
    ----------

    direction : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DRender::QRayCaster::setDirection(const QVector3D &direction)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QRayCaster12setDirectionERK9QVector3D',
        self._valueOf(direction),
    )

  @overload(float)
  def setLength(self, length: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRayCaster::setLength(float length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qraycaster.html#setLength

    Parameters
    ----------

    length : float
      Passed on as it is.
    """
    #  void Qt3DRender::QRayCaster::setLength(float length)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QRayCaster9setLengthEf', length,
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
    Notes what was given, for Qt's 'Qt3DRender::QRayCaster::QRayCaster(QNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qraycaster.html#QRayCaster

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QRayCaster::QRayCaster(QNode *parent)
    self._noteCreation(QRayCaster, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender10QRayCasterC1EPN8Qt3DCore5QNodeE',
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
    Calls Qt's 'void Qt3DRender::QRayCaster::trigger()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qraycaster.html#trigger
    """
    #  void Qt3DRender::QRayCaster::trigger()
    self.uglySide.call('ritual_ZN10Qt3DRender10QRayCaster7triggerEv')

  @overload(QVector3D, QVector3D, float)
  def trigger(
      self,
      origin: QVector3D,
      direction: QVector3D,
      length: float,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRayCaster::trigger(const QVector3D &origin,
    const QVector3D &direction, float length)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qraycaster.html#trigger

    Parameters
    ----------

    origin : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    direction : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    length : float
      Passed on as it is.
    """
    #  void Qt3DRender::QRayCaster::trigger(const QVector3D &origin, const
    #      QVector3D &direction, float length)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QRayCaster7triggerERK9QVector3DS3_f',
        self._valueOf(origin), self._valueOf(direction), length,
    )

  @overload(QVector3D)
  def originChanged(self, origin: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRayCaster::originChanged(const QVector3D
    &origin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qraycaster.html#originChanged

    Parameters
    ----------

    origin : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DRender::QRayCaster::originChanged(const QVector3D &origin)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QRayCaster13originChangedERK9QVector3D',
        self._valueOf(origin),
    )

  @overload(QVector3D)
  def directionChanged(self, direction: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRayCaster::directionChanged(const QVector3D
    &direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qraycaster.html#directionChanged

    Parameters
    ----------

    direction : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DRender::QRayCaster::directionChanged(const QVector3D
    #      &direction)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QRayCaster16directionChangedERK9QVector3D',
        self._valueOf(direction),
    )

  @overload(float)
  def lengthChanged(self, length: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRayCaster::lengthChanged(float length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qraycaster.html#lengthChanged

    Parameters
    ----------

    length : float
      Passed on as it is.
    """
    #  void Qt3DRender::QRayCaster::lengthChanged(float length)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QRayCaster13lengthChangedEf', length,
    )

  @staticmethod
  def pick(*__, **_) -> Never:
    """
    Qt's 'Qt3DRender::QAbstractRayCaster::Hits
    Qt3DRender::QRayCaster::pick(const QVector3D &origin, const QVector3D
    &direction, float length)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QRayCaster.pick' has no cute function yet. Qt's "
        "'Qt3DRender::QAbstractRayCaster::Hits "
        "Qt3DRender::QRayCaster::pick(const QVector3D &origin, const "
        "QVector3D &direction, float length)': gives a type Python has no "
        "way to take yet.")
