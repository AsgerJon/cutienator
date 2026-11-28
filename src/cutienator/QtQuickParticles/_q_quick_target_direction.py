"""
QQuickTargetDirection binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickParticles/6.12.0/QtQuickParticles/private/qquicktargetdirection_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickTargetDirection to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickDirection

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF
  from ..QtQuick import QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTargetDirection(QQuickDirection):
  """
  The cute side of Qt's QQuickTargetDirection: a plain Python object standing
  in front of one C++ QQuickTargetDirection.

  It is built on the cute 'QQuickDirection', as Qt's QQuickTargetDirection is
  built on Qt's QQuickDirection, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTargetDirection that has a ritual and that
  Python can call so far, 24 names in all: 'metaObject', 'tr', 'sample',
  'targetX', 'targetY', 'targetVariation', 'magnitude',
  'proportionalMagnitude', 'magnitudeVariation', 'targetItem',
  'targetXChanged', 'targetYChanged', 'targetVariationChanged',
  'magnitudeChanged', 'proprotionalMagnitudeChanged',
  'magnitudeVariationChanged', 'targetItemChanged', 'setTargetX',
  'setTargetY', 'setTargetVariation', 'setMagnitude',
  'setProportionalMagnitude', 'setMagnitudeVariation', 'setTargetItem'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickTargetDirection::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickTargetDirection::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 29 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickTargetDirection is created at the first use, not by
    'QQuickTargetDirection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTargetDirection.
  - Qt tells when it has removed the C++ QQuickTargetDirection. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickTargetDirection::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktargetdirection.html#tr

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
    #  QString QQuickTargetDirection::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQuickTargetDirection2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTargetDirection'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickTargetDirection::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktargetdirection.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTargetDirection::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickTargetDirection10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def targetX(self) -> float:
    """
    Calls Qt's 'qreal QQuickTargetDirection::targetX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktargetdirection.html#targetX
    """
    #  qreal QQuickTargetDirection::targetX() const
    return self.uglySide.call('ritual_ZNK21QQuickTargetDirection7targetXEv')

  def targetY(self) -> float:
    """
    Calls Qt's 'qreal QQuickTargetDirection::targetY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktargetdirection.html#targetY
    """
    #  qreal QQuickTargetDirection::targetY() const
    return self.uglySide.call('ritual_ZNK21QQuickTargetDirection7targetYEv')

  def targetVariation(self) -> float:
    """
    Calls Qt's 'qreal QQuickTargetDirection::targetVariation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktargetdirection.html#targetVariation
    """
    #  qreal QQuickTargetDirection::targetVariation() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickTargetDirection15targetVariationEv',
    )

  def magnitude(self) -> float:
    """
    Calls Qt's 'qreal QQuickTargetDirection::magnitude() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktargetdirection.html#magnitude
    """
    #  qreal QQuickTargetDirection::magnitude() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickTargetDirection9magnitudeEv',
    )

  def proportionalMagnitude(self) -> bool:
    """
    Calls Qt's 'bool QQuickTargetDirection::proportionalMagnitude() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktargetdirection.html#proportionalMagnitude
    """
    #  bool QQuickTargetDirection::proportionalMagnitude() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickTargetDirection21proportionalMagnitudeEv',
    )

  def magnitudeVariation(self) -> float:
    """
    Calls Qt's 'qreal QQuickTargetDirection::magnitudeVariation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktargetdirection.html#magnitudeVariation
    """
    #  qreal QQuickTargetDirection::magnitudeVariation() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickTargetDirection18magnitudeVariationEv',
    )

  def targetItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickTargetDirection::targetItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktargetdirection.html#targetItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickTargetDirection::targetItem() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickTargetDirection10targetItemEv',
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setTargetX(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickTargetDirection::setTargetX(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktargetdirection.html#setTargetX

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickTargetDirection::setTargetX(qreal arg)
    self.uglySide.call('ritual_ZN21QQuickTargetDirection10setTargetXEd', arg)

  @overload(float)
  def setTargetY(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickTargetDirection::setTargetY(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktargetdirection.html#setTargetY

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickTargetDirection::setTargetY(qreal arg)
    self.uglySide.call('ritual_ZN21QQuickTargetDirection10setTargetYEd', arg)

  @overload(float)
  def setTargetVariation(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickTargetDirection::setTargetVariation(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktargetdirection.html#setTargetVariation

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickTargetDirection::setTargetVariation(qreal arg)
    self.uglySide.call(
        'ritual_ZN21QQuickTargetDirection18setTargetVariationEd', arg,
    )

  @overload(float)
  def setMagnitude(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickTargetDirection::setMagnitude(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktargetdirection.html#setMagnitude

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickTargetDirection::setMagnitude(qreal arg)
    self.uglySide.call(
        'ritual_ZN21QQuickTargetDirection12setMagnitudeEd', arg,
    )

  @overload(bool)
  def setProportionalMagnitude(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickTargetDirection::setProportionalMagnitude(bool
    arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktargetdirection.html

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickTargetDirection::setProportionalMagnitude(bool arg)
    self.uglySide.call(
        'ritual_ZN21QQuickTargetDirection24setProportionalMagnitudeEb', arg,
    )

  @overload(float)
  def setMagnitudeVariation(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickTargetDirection::setMagnitudeVariation(qreal
    arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktargetdirection.html#setMagnitudeVariation

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickTargetDirection::setMagnitudeVariation(qreal arg)
    self.uglySide.call(
        'ritual_ZN21QQuickTargetDirection21setMagnitudeVariationEd', arg,
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setTargetItem(self, arg: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickTargetDirection::setTargetItem(QQuickItem *arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktargetdirection.html#setTargetItem

    Parameters
    ----------

    arg : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTargetDirection::setTargetItem(QQuickItem *arg)
    self.uglySide.call(
        'ritual_ZN21QQuickTargetDirection13setTargetItemEP10QQuickItem',
        self._addressOf(arg),
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
    'QQuickTargetDirection::QQuickTargetDirection(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktargetdirection.html#QQuickTargetDirection

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickTargetDirection::QQuickTargetDirection(QObject *parent)
    self._noteCreation(QQuickTargetDirection, lambda: Rituals.call(
        'ritual_ZN21QQuickTargetDirectionC1EP7QObject',
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

  @overload(QPointF)
  def sample(self, from_: QPointF) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickTargetDirection::sample(const QPointF &from)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktargetdirection.html#sample

    Parameters
    ----------

    from_ : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickTargetDirection::sample(const QPointF &from)
    ritual = 'ritual_ZN21QQuickTargetDirection6sampleERK7QPointF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuickTargetDirection6sampleERK7QPointF'
    address = self.uglySide.call(ritual, self._valueOf(from_, 'QPointF'))
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(float)
  def targetXChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickTargetDirection::targetXChanged(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktargetdirection.html#targetXChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickTargetDirection::targetXChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN21QQuickTargetDirection14targetXChangedEd', arg,
    )

  @overload(float)
  def targetYChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickTargetDirection::targetYChanged(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktargetdirection.html#targetYChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickTargetDirection::targetYChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN21QQuickTargetDirection14targetYChangedEd', arg,
    )

  @overload(float)
  def targetVariationChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickTargetDirection::targetVariationChanged(qreal
    arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktargetdirection.html#targetVariationChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickTargetDirection::targetVariationChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN21QQuickTargetDirection22targetVariationChangedEd', arg,
    )

  @overload(float)
  def magnitudeChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickTargetDirection::magnitudeChanged(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktargetdirection.html#magnitudeChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickTargetDirection::magnitudeChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN21QQuickTargetDirection16magnitudeChangedEd', arg,
    )

  @overload(bool)
  def proprotionalMagnitudeChanged(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickTargetDirection::proprotionalMagnitudeChanged(bool
    arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktargetdirection.html

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickTargetDirection::proprotionalMagnitudeChanged(bool arg)
    self.uglySide.call(
        'ritual_ZN21QQuickTargetDirection28proprotionalMagnitudeChangedEb',
        arg,
    )

  @overload(float)
  def magnitudeVariationChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickTargetDirection::magnitudeVariationChanged(qreal
    arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktargetdirection.html

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickTargetDirection::magnitudeVariationChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN21QQuickTargetDirection25magnitudeVariationChangedEd', arg,
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def targetItemChanged(self, arg: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickTargetDirection::targetItemChanged(QQuickItem
    *arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktargetdirection.html#targetItemChanged

    Parameters
    ----------

    arg : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTargetDirection::targetItemChanged(QQuickItem *arg)
    self.uglySide.call(
        'ritual_ZN21QQuickTargetDirection17targetItemChangedEP10QQuickItem',
        self._addressOf(arg),
    )
