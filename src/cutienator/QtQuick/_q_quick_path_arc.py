"""
QQuickPathArc binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpath_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickPathArc to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickCurve

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPathArc(QQuickCurve):
  """
  The cute side of Qt's QQuickPathArc: a plain Python object standing in
  front of one C++ QQuickPathArc.

  It is built on the cute 'QQuickCurve', as Qt's QQuickPathArc is built on
  Qt's QQuickCurve, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPathArc that has a ritual and that Python can
  call so far, 17 names in all: 'metaObject', 'tr', 'radiusX', 'setRadiusX',
  'radiusY', 'setRadiusY', 'useLargeArc', 'setUseLargeArc', 'direction',
  'setDirection', 'xAxisRotation', 'setXAxisRotation', 'radiusXChanged',
  'radiusYChanged', 'useLargeArcChanged', 'directionChanged',
  'xAxisRotationChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPathArc::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickPathArc::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickPathArc::addToPath(QPainterPath &path, const
    QQuickPathData &a1)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickPathArc is created at the first use, not by
    'QQuickPathArc(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPathArc.
  - Qt tells when it has removed the C++ QQuickPathArc. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickPathArc, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ArcDirection(CuteNum):
    """
    The enum 'QQuickPathArc::ArcDirection' of Qt, with the 2 names Qt gives
    in it.
    """

    Clockwise = Kee[int](0)
    Counterclockwise = Kee[int](1)

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
    Calls Qt's 'QString QQuickPathArc::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpatharc.html#tr

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
    #  QString QQuickPathArc::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QQuickPathArc2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPathArc'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPathArc::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpatharc.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPathArc::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QQuickPathArc10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def radiusX(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathArc::radiusX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpatharc.html#radiusX
    """
    #  qreal QQuickPathArc::radiusX() const
    return self.uglySide.call('ritual_ZNK13QQuickPathArc7radiusXEv')

  def radiusY(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathArc::radiusY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpatharc.html#radiusY
    """
    #  qreal QQuickPathArc::radiusY() const
    return self.uglySide.call('ritual_ZNK13QQuickPathArc7radiusYEv')

  def useLargeArc(self) -> bool:
    """
    Calls Qt's 'bool QQuickPathArc::useLargeArc() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpatharc.html#useLargeArc
    """
    #  bool QQuickPathArc::useLargeArc() const
    return self.uglySide.call('ritual_ZNK13QQuickPathArc11useLargeArcEv')

  def direction(self) -> ArcDirection:
    """
    Calls Qt's 'ArcDirection QQuickPathArc::direction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpatharc.html#direction

    Returns
    -------

    ArcDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ArcDirection(number)'
      gives.
    """
    #  ArcDirection QQuickPathArc::direction() const
    return QQuickPathArc.ArcDirection(self.uglySide.call(
        'ritual_ZNK13QQuickPathArc9directionEv',
    ))

  def xAxisRotation(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathArc::xAxisRotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpatharc.html#xAxisRotation
    """
    #  qreal QQuickPathArc::xAxisRotation() const
    return self.uglySide.call('ritual_ZNK13QQuickPathArc13xAxisRotationEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setRadiusX(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickPathArc::setRadiusX(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpatharc.html#setRadiusX

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickPathArc::setRadiusX(qreal a0)
    self.uglySide.call('ritual_ZN13QQuickPathArc10setRadiusXEd', a0)

  @overload(float)
  def setRadiusY(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickPathArc::setRadiusY(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpatharc.html#setRadiusY

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickPathArc::setRadiusY(qreal a0)
    self.uglySide.call('ritual_ZN13QQuickPathArc10setRadiusYEd', a0)

  @overload(bool)
  def setUseLargeArc(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickPathArc::setUseLargeArc(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpatharc.html#setUseLargeArc

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickPathArc::setUseLargeArc(bool a0)
    self.uglySide.call('ritual_ZN13QQuickPathArc14setUseLargeArcEb', a0)

  @overload(ArcDirection)
  def setDirection(self, direction: ArcDirection) -> None:
    """
    Calls Qt's 'void QQuickPathArc::setDirection(ArcDirection direction)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpatharc.html#setDirection

    Parameters
    ----------

    direction : ArcDirection
      Passed on as its number.
    """
    #  void QQuickPathArc::setDirection(ArcDirection direction)
    self.uglySide.call(
        'ritual_ZN13QQuickPathArc12setDirectionENS_12ArcDirectionE',
        direction.value,
    )

  @overload(float)
  def setXAxisRotation(self, rotation: float) -> None:
    """
    Calls Qt's 'void QQuickPathArc::setXAxisRotation(qreal rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpatharc.html#setXAxisRotation

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void QQuickPathArc::setXAxisRotation(qreal rotation)
    self.uglySide.call(
        'ritual_ZN13QQuickPathArc16setXAxisRotationEd', rotation,
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
    Notes what was given, for Qt's 'QQuickPathArc::QQuickPathArc(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickpatharc.html#QQuickPathArc

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickPathArc::QQuickPathArc(QObject *parent)
    self._noteCreation(QQuickPathArc, lambda: Rituals.call(
        'ritual_ZN13QQuickPathArcC1EP7QObject',
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

  def radiusXChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathArc::radiusXChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpatharc.html#radiusXChanged
    """
    #  void QQuickPathArc::radiusXChanged()
    self.uglySide.call('ritual_ZN13QQuickPathArc14radiusXChangedEv')

  def radiusYChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathArc::radiusYChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpatharc.html#radiusYChanged
    """
    #  void QQuickPathArc::radiusYChanged()
    self.uglySide.call('ritual_ZN13QQuickPathArc14radiusYChangedEv')

  def useLargeArcChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathArc::useLargeArcChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpatharc.html#useLargeArcChanged
    """
    #  void QQuickPathArc::useLargeArcChanged()
    self.uglySide.call('ritual_ZN13QQuickPathArc18useLargeArcChangedEv')

  def directionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathArc::directionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpatharc.html#directionChanged
    """
    #  void QQuickPathArc::directionChanged()
    self.uglySide.call('ritual_ZN13QQuickPathArc16directionChangedEv')

  def xAxisRotationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathArc::xAxisRotationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpatharc.html#xAxisRotationChanged
    """
    #  void QQuickPathArc::xAxisRotationChanged()
    self.uglySide.call('ritual_ZN13QQuickPathArc20xAxisRotationChangedEv')
