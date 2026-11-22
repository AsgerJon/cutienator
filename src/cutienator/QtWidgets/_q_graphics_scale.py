"""
QGraphicsScale binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgraphicstransform.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QGraphicsTransform

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QMatrix4x4, QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsScale(QGraphicsTransform):
  """
  The cute side of Qt's QGraphicsScale: a plain Python object standing in
  front of one C++ QGraphicsScale.

  It is built on the cute 'QGraphicsTransform', as Qt's QGraphicsScale is
  built on Qt's QGraphicsTransform, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsScale that has a ritual and that Python can
  call so far, 11 names in all: 'metaObject', 'tr', 'origin', 'setOrigin',
  'xScale', 'setXScale', 'yScale', 'setYScale', 'zScale', 'setZScale',
  'applyTo'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsScale::~QGraphicsScale()': the destructor: Python never
    removes a C++ QGraphicsScale.

  What has no ritual
  ------------------

  11 of the 24 functions Qt declares: 5 a signal; 3 private; 2 takes or gives
  a type that cannot be passed yet; 1 a template.

  What to expect
  --------------

  - The C++ QGraphicsScale is created at the first use, not by
    'QGraphicsScale(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsScale.
  - Qt tells when it has removed the C++ QGraphicsScale. Every call on the
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
    Calls Qt's 'QString QGraphicsScale::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscale.html#tr

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
    #  QString QGraphicsScale::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QGraphicsScale2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsScale'

  #  A C++ QGraphicsScale Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsScale'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGraphicsScale::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscale.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGraphicsScale::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QGraphicsScale10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def origin(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QGraphicsScale::origin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscale.html#origin

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QGraphicsScale::origin() const
    address = self.uglySide.call('ritual_ZNK14QGraphicsScale6originEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def xScale(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsScale::xScale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscale.html#xScale
    """
    #  qreal QGraphicsScale::xScale() const
    return self.uglySide.call('ritual_ZNK14QGraphicsScale6xScaleEv')

  def yScale(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsScale::yScale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscale.html#yScale
    """
    #  qreal QGraphicsScale::yScale() const
    return self.uglySide.call('ritual_ZNK14QGraphicsScale6yScaleEv')

  def zScale(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsScale::zScale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscale.html#zScale
    """
    #  qreal QGraphicsScale::zScale() const
    return self.uglySide.call('ritual_ZNK14QGraphicsScale6zScaleEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector3D)
  def setOrigin(self, point: QVector3D) -> None:
    """
    Calls Qt's 'void QGraphicsScale::setOrigin(const QVector3D &point)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscale.html#setOrigin

    Parameters
    ----------

    point : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QGraphicsScale::setOrigin(const QVector3D &point)
    self.uglySide.call(
        'ritual_ZN14QGraphicsScale9setOriginERK9QVector3D',
        self._valueOf(point),
    )

  @overload(float)
  def setXScale(self, a0: float) -> None:
    """
    Calls Qt's 'void QGraphicsScale::setXScale(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscale.html#setXScale

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QGraphicsScale::setXScale(qreal a0)
    self.uglySide.call('ritual_ZN14QGraphicsScale9setXScaleEd', a0)

  @overload(float)
  def setYScale(self, a0: float) -> None:
    """
    Calls Qt's 'void QGraphicsScale::setYScale(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscale.html#setYScale

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QGraphicsScale::setYScale(qreal a0)
    self.uglySide.call('ritual_ZN14QGraphicsScale9setYScaleEd', a0)

  @overload(float)
  def setZScale(self, a0: float) -> None:
    """
    Calls Qt's 'void QGraphicsScale::setZScale(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscale.html#setZScale

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QGraphicsScale::setZScale(qreal a0)
    self.uglySide.call('ritual_ZN14QGraphicsScale9setZScaleEd', a0)

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
    Notes what was given, for Qt's 'QGraphicsScale::QGraphicsScale(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscale.html#QGraphicsScale

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsScale::QGraphicsScale(QObject *parent)
    self._noteCreation(QGraphicsScale, lambda: Rituals.call(
        'ritual_ZN14QGraphicsScaleC1EP7QObject', self._addressOf(parent),
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

  @overload(QMatrix4x4)
  @overload(NoneType)
  def applyTo(self, matrix: Optional[QMatrix4x4]) -> None:
    """
    Calls Qt's 'void QGraphicsScale::applyTo(QMatrix4x4 *matrix) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscale.html#applyTo

    Parameters
    ----------

    matrix : Optional[QMatrix4x4]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsScale::applyTo(QMatrix4x4 *matrix) const
    ritual = 'ritual_ZNK14QGraphicsScale7applyToEP10QMatrix4x4'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QGraphicsScale7applyToEP10QMatrix4x4'
    self.uglySide.call(ritual, self._addressOf(matrix))
