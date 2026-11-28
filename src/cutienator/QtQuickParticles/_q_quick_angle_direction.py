"""
QQuickAngleDirection binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickangledirection_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickAngleDirection to be private: it declares the class in a
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
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickAngleDirection(QQuickDirection):
  """
  The cute side of Qt's QQuickAngleDirection: a plain Python object standing
  in front of one C++ QQuickAngleDirection.

  It is built on the cute 'QQuickDirection', as Qt's QQuickAngleDirection is
  built on Qt's QQuickDirection, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickAngleDirection that has a ritual and that
  Python can call so far, 15 names in all: 'metaObject', 'tr', 'sample',
  'angle', 'magnitude', 'angleVariation', 'magnitudeVariation',
  'angleChanged', 'magnitudeChanged', 'angleVariationChanged',
  'magnitudeVariationChanged', 'setAngle', 'setMagnitude',
  'setAngleVariation', 'setMagnitudeVariation'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickAngleDirection::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickAngleDirection::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickAngleDirection is created at the first use, not by
    'QQuickAngleDirection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickAngleDirection.
  - Qt tells when it has removed the C++ QQuickAngleDirection. Every call on
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
    Calls Qt's 'QString QQuickAngleDirection::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickangledirection.html#tr

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
    #  QString QQuickAngleDirection::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuickAngleDirection2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickAngleDirection'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickAngleDirection::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickangledirection.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickAngleDirection::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickAngleDirection10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def angle(self) -> float:
    """
    Calls Qt's 'qreal QQuickAngleDirection::angle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickangledirection.html#angle
    """
    #  qreal QQuickAngleDirection::angle() const
    return self.uglySide.call('ritual_ZNK20QQuickAngleDirection5angleEv')

  def magnitude(self) -> float:
    """
    Calls Qt's 'qreal QQuickAngleDirection::magnitude() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickangledirection.html#magnitude
    """
    #  qreal QQuickAngleDirection::magnitude() const
    return self.uglySide.call('ritual_ZNK20QQuickAngleDirection9magnitudeEv')

  def angleVariation(self) -> float:
    """
    Calls Qt's 'qreal QQuickAngleDirection::angleVariation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickangledirection.html#angleVariation
    """
    #  qreal QQuickAngleDirection::angleVariation() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickAngleDirection14angleVariationEv',
    )

  def magnitudeVariation(self) -> float:
    """
    Calls Qt's 'qreal QQuickAngleDirection::magnitudeVariation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickangledirection.html#magnitudeVariation
    """
    #  qreal QQuickAngleDirection::magnitudeVariation() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickAngleDirection18magnitudeVariationEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setAngle(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickAngleDirection::setAngle(qreal arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickangledirection.html#setAngle

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickAngleDirection::setAngle(qreal arg)
    self.uglySide.call('ritual_ZN20QQuickAngleDirection8setAngleEd', arg)

  @overload(float)
  def setMagnitude(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickAngleDirection::setMagnitude(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickangledirection.html#setMagnitude

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickAngleDirection::setMagnitude(qreal arg)
    self.uglySide.call(
        'ritual_ZN20QQuickAngleDirection12setMagnitudeEd', arg,
    )

  @overload(float)
  def setAngleVariation(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickAngleDirection::setAngleVariation(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickangledirection.html#setAngleVariation

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickAngleDirection::setAngleVariation(qreal arg)
    self.uglySide.call(
        'ritual_ZN20QQuickAngleDirection17setAngleVariationEd', arg,
    )

  @overload(float)
  def setMagnitudeVariation(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickAngleDirection::setMagnitudeVariation(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickangledirection.html#setMagnitudeVariation

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickAngleDirection::setMagnitudeVariation(qreal arg)
    self.uglySide.call(
        'ritual_ZN20QQuickAngleDirection21setMagnitudeVariationEd', arg,
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
    'QQuickAngleDirection::QQuickAngleDirection(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickangledirection.html#QQuickAngleDirection

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickAngleDirection::QQuickAngleDirection(QObject *parent)
    self._noteCreation(QQuickAngleDirection, lambda: Rituals.call(
        'ritual_ZN20QQuickAngleDirectionC1EP7QObject',
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
    Calls Qt's 'QPointF QQuickAngleDirection::sample(const QPointF &from)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickangledirection.html#sample

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
    #  QPointF QQuickAngleDirection::sample(const QPointF &from)
    ritual = 'ritual_ZN20QQuickAngleDirection6sampleERK7QPointF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickAngleDirection6sampleERK7QPointF'
    address = self.uglySide.call(ritual, self._valueOf(from_, 'QPointF'))
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(float)
  def angleChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickAngleDirection::angleChanged(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickangledirection.html#angleChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickAngleDirection::angleChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN20QQuickAngleDirection12angleChangedEd', arg,
    )

  @overload(float)
  def magnitudeChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickAngleDirection::magnitudeChanged(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickangledirection.html#magnitudeChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickAngleDirection::magnitudeChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN20QQuickAngleDirection16magnitudeChangedEd', arg,
    )

  @overload(float)
  def angleVariationChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickAngleDirection::angleVariationChanged(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickangledirection.html#angleVariationChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickAngleDirection::angleVariationChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN20QQuickAngleDirection21angleVariationChangedEd', arg,
    )

  @overload(float)
  def magnitudeVariationChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickAngleDirection::magnitudeVariationChanged(qreal
    arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickangledirection.html

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickAngleDirection::magnitudeVariationChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN20QQuickAngleDirection25magnitudeVariationChangedEd', arg,
    )
