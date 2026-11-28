"""
QQuickWanderAffector binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickwander_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickWanderAffector to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickItem
from . import QQuickParticleAffector

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickParticleData, WanderData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickParticleData = WAIT['QQuickParticleData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWanderAffector(QQuickParticleAffector):
  """
  The cute side of Qt's QQuickWanderAffector: a plain Python object standing
  in front of one C++ QQuickWanderAffector.

  It is built on the cute 'QQuickParticleAffector', as Qt's
  QQuickWanderAffector is built on Qt's QQuickParticleAffector, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWanderAffector that has a ritual and that
  Python can call so far, 16 names in all: 'metaObject', 'tr', 'xVariance',
  'yVariance', 'pace', 'affectedParameter', 'affectParticle',
  'xVarianceChanged', 'yVarianceChanged', 'paceChanged',
  'affectedParameterChanged', 'setXVariance', 'setYVariance', 'setPace',
  'setAffectedParameter', 'getData'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickWanderAffector::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickWanderAffector::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickWanderAffector::~QQuickWanderAffector()': the destructor:
    Python never removes a C++ QQuickWanderAffector.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickWanderAffector is created at the first use, not by
    'QQuickWanderAffector(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWanderAffector.
  - Qt tells when it has removed the C++ QQuickWanderAffector. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickWanderAffector, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class AffectableParameters(CuteNum):
    """
    The enum 'QQuickWanderAffector::AffectableParameters' of Qt, with the 3
    names Qt gives in it.
    """

    Position = Kee[int](0)
    Velocity = Kee[int](1)
    Acceleration = Kee[int](2)

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
    Calls Qt's 'QString QQuickWanderAffector::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwanderaffector.html#tr

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
    #  QString QQuickWanderAffector::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuickWanderAffector2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWanderAffector'

  #  A C++ QQuickWanderAffector Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickWanderAffector'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickWanderAffector::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwanderaffector.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickWanderAffector::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickWanderAffector10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def xVariance(self) -> float:
    """
    Calls Qt's 'qreal QQuickWanderAffector::xVariance() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwanderaffector.html#xVariance
    """
    #  qreal QQuickWanderAffector::xVariance() const
    return self.uglySide.call('ritual_ZNK20QQuickWanderAffector9xVarianceEv')

  def yVariance(self) -> float:
    """
    Calls Qt's 'qreal QQuickWanderAffector::yVariance() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwanderaffector.html#yVariance
    """
    #  qreal QQuickWanderAffector::yVariance() const
    return self.uglySide.call('ritual_ZNK20QQuickWanderAffector9yVarianceEv')

  def pace(self) -> float:
    """
    Calls Qt's 'qreal QQuickWanderAffector::pace() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwanderaffector.html#pace
    """
    #  qreal QQuickWanderAffector::pace() const
    return self.uglySide.call('ritual_ZNK20QQuickWanderAffector4paceEv')

  def affectedParameter(self) -> AffectableParameters:
    """
    Calls Qt's 'AffectableParameters
    QQuickWanderAffector::affectedParameter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwanderaffector.html#affectedParameter

    Returns
    -------

    AffectableParameters
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'AffectableParameters(number)' gives.
    """
    #  AffectableParameters QQuickWanderAffector::affectedParameter() const
    return QQuickWanderAffector.AffectableParameters(self.uglySide.call(
        'ritual_ZNK20QQuickWanderAffector17affectedParameterEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setXVariance(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickWanderAffector::setXVariance(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwanderaffector.html#setXVariance

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickWanderAffector::setXVariance(qreal arg)
    self.uglySide.call(
        'ritual_ZN20QQuickWanderAffector12setXVarianceEd', arg,
    )

  @overload(float)
  def setYVariance(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickWanderAffector::setYVariance(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwanderaffector.html#setYVariance

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickWanderAffector::setYVariance(qreal arg)
    self.uglySide.call(
        'ritual_ZN20QQuickWanderAffector12setYVarianceEd', arg,
    )

  @overload(float)
  def setPace(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickWanderAffector::setPace(qreal arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwanderaffector.html#setPace

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickWanderAffector::setPace(qreal arg)
    self.uglySide.call('ritual_ZN20QQuickWanderAffector7setPaceEd', arg)

  @overload(AffectableParameters)
  def setAffectedParameter(self, arg: AffectableParameters) -> None:
    """
    Calls Qt's 'void
    QQuickWanderAffector::setAffectedParameter(AffectableParameters arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwanderaffector.html#setAffectedParameter

    Parameters
    ----------

    arg : AffectableParameters
      Passed on as its number.
    """
    #  void QQuickWanderAffector::setAffectedParameter(AffectableParameters
    #      arg)
    self.uglySide.call(
        'ritual_ZN20QQuickWanderAffector20setAffectedParameterENS_20Affecta'
        'bleParametersE',
        arg.value,
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickWanderAffector::QQuickWanderAffector(QQuickItem *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwanderaffector.html#QQuickWanderAffector

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickWanderAffector::QQuickWanderAffector(QQuickItem *parent)
    self._noteCreation(QQuickWanderAffector, lambda: Rituals.call(
        'ritual_ZN20QQuickWanderAffectorC1EP10QQuickItem',
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

  @overload(QQuickParticleData, float)
  @overload(NoneType, float)
  def affectParticle(
      self,
      d: Optional[QQuickParticleData],
      dt: float,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickWanderAffector::affectParticle(QQuickParticleData
    *d, qreal dt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwanderaffector.html#affectParticle

    Parameters
    ----------

    d : Optional[QQuickParticleData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dt : float
      Passed on as it is.
    """
    #  bool QQuickWanderAffector::affectParticle(QQuickParticleData *d, qreal
    #      dt)
    ritual = (
        'ritual_ZN20QQuickWanderAffector14affectParticleEP18QQuickParticleD'
        'atad')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickWanderAffector14affectParticleEP18QQuickPar'
          'ticleDatad')
    return self.uglySide.call(ritual, self._addressOf(d), dt)

  @overload(float)
  def xVarianceChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickWanderAffector::xVarianceChanged(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwanderaffector.html#xVarianceChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickWanderAffector::xVarianceChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN20QQuickWanderAffector16xVarianceChangedEd', arg,
    )

  @overload(float)
  def yVarianceChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickWanderAffector::yVarianceChanged(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwanderaffector.html#yVarianceChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickWanderAffector::yVarianceChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN20QQuickWanderAffector16yVarianceChangedEd', arg,
    )

  @overload(float)
  def paceChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickWanderAffector::paceChanged(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwanderaffector.html#paceChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickWanderAffector::paceChanged(qreal arg)
    self.uglySide.call('ritual_ZN20QQuickWanderAffector11paceChangedEd', arg)

  @overload(AffectableParameters)
  def affectedParameterChanged(self, arg: AffectableParameters) -> None:
    """
    Calls Qt's 'void
    QQuickWanderAffector::affectedParameterChanged(AffectableParameters
    arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwanderaffector.html#affectedParameterChanged

    Parameters
    ----------

    arg : AffectableParameters
      Passed on as its number.
    """
    #  void QQuickWanderAffector::affectedParameterChanged(
    #      AffectableParameters arg)
    self.uglySide.call(
        'ritual_ZN20QQuickWanderAffector24affectedParameterChangedENS_20Aff'
        'ectableParametersE',
        arg.value,
    )

  @overload(int)
  def getData(self, idx: int) -> Optional[WanderData]:
    """
    Calls Qt's 'WanderData *QQuickWanderAffector::getData(int idx)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwanderaffector.html#getData

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    Optional[WanderData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  WanderData *QQuickWanderAffector::getData(int idx)
    address = self.uglySide.call(
        'ritual_ZN20QQuickWanderAffector7getDataEi', idx,
    )
    from . import WanderData
    return WanderData._cuteAt(address)
