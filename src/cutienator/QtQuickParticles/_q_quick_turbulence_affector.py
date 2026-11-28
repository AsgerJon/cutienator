"""
QQuickTurbulenceAffector binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickturbulence_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickTurbulenceAffector to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickItem
from . import QQuickParticleAffector

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF, QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTurbulenceAffector(QQuickParticleAffector):
  """
  The cute side of Qt's QQuickTurbulenceAffector: a plain Python object
  standing in front of one C++ QQuickTurbulenceAffector.

  It is built on the cute 'QQuickParticleAffector', as Qt's
  QQuickTurbulenceAffector is built on Qt's QQuickParticleAffector, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTurbulenceAffector that has a ritual and that
  Python can call so far, 13 names in all: 'metaObject', 'tr',
  'affectSystem', 'strength', 'noiseSource', 'strengthChanged',
  'noiseSourceChanged', 'setStrength', 'setNoiseSource', 'geometryChange',
  'ensureInit', 'initializeGrid', 'boundsRespectingField'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickTurbulenceAffector::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickTurbulenceAffector::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickTurbulenceAffector::~QQuickTurbulenceAffector()': the
    destructor: Python never removes a C++ QQuickTurbulenceAffector.

  What has no ritual
  ------------------

  3 of the 20 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQuickTurbulenceAffector is created at the first use, not by
    'QQuickTurbulenceAffector(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTurbulenceAffector.
  - Qt tells when it has removed the C++ QQuickTurbulenceAffector. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickTurbulenceAffector::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickturbulenceaffector.html#tr

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
    #  QString QQuickTurbulenceAffector::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QQuickTurbulenceAffector2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTurbulenceAffector'

  #  A C++ QQuickTurbulenceAffector Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickTurbulenceAffector'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickTurbulenceAffector::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickturbulenceaffector.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTurbulenceAffector::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickTurbulenceAffector10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def strength(self) -> float:
    """
    Calls Qt's 'qreal QQuickTurbulenceAffector::strength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickturbulenceaffector.html#strength
    """
    #  qreal QQuickTurbulenceAffector::strength() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickTurbulenceAffector8strengthEv',
    )

  def noiseSource(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickTurbulenceAffector::noiseSource() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickturbulenceaffector.html#noiseSource

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickTurbulenceAffector::noiseSource() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickTurbulenceAffector11noiseSourceEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setStrength(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickTurbulenceAffector::setStrength(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickturbulenceaffector.html#setStrength

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickTurbulenceAffector::setStrength(qreal arg)
    self.uglySide.call(
        'ritual_ZN24QQuickTurbulenceAffector11setStrengthEd', arg,
    )

  @overload(QUrl)
  def setNoiseSource(self, arg: QUrl) -> None:
    """
    Calls Qt's 'void QQuickTurbulenceAffector::setNoiseSource(const QUrl
    &arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickturbulenceaffector.html#setNoiseSource

    Parameters
    ----------

    arg : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickTurbulenceAffector::setNoiseSource(const QUrl &arg)
    self.uglySide.call(
        'ritual_ZN24QQuickTurbulenceAffector14setNoiseSourceERK4QUrl',
        self._valueOf(arg),
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
    'QQuickTurbulenceAffector::QQuickTurbulenceAffector(QQuickItem *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickturbulenceaffector.html

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickTurbulenceAffector::QQuickTurbulenceAffector(QQuickItem *parent)
    self._noteCreation(QQuickTurbulenceAffector, lambda: Rituals.call(
        'ritual_ZN24QQuickTurbulenceAffectorC1EP10QQuickItem',
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

  @overload(float)
  def affectSystem(self, dt: float) -> None:
    """
    Calls Qt's 'void QQuickTurbulenceAffector::affectSystem(qreal dt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickturbulenceaffector.html#affectSystem

    Parameters
    ----------

    dt : float
      Passed on as it is.
    """
    #  void QQuickTurbulenceAffector::affectSystem(qreal dt)
    ritual = 'ritual_ZN24QQuickTurbulenceAffector12affectSystemEd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QQuickTurbulenceAffector12affectSystemEd'
    self.uglySide.call(ritual, dt)

  @overload(float)
  def strengthChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickTurbulenceAffector::strengthChanged(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickturbulenceaffector.html#strengthChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickTurbulenceAffector::strengthChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN24QQuickTurbulenceAffector15strengthChangedEd', arg,
    )

  @overload(QUrl)
  def noiseSourceChanged(self, arg: QUrl) -> None:
    """
    Calls Qt's 'void QQuickTurbulenceAffector::noiseSourceChanged(const QUrl
    &arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickturbulenceaffector.html#noiseSourceChanged

    Parameters
    ----------

    arg : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickTurbulenceAffector::noiseSourceChanged(const QUrl &arg)
    self.uglySide.call(
        'ritual_ZN24QQuickTurbulenceAffector18noiseSourceChangedERK4QUrl',
        self._valueOf(arg),
    )

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickTurbulenceAffector::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickturbulenceaffector.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickTurbulenceAffector::geometryChange(const QRectF
    #      &newGeometry, const QRectF &oldGeometry)
    ritual = (
        'ritual_ZN24QQuickTurbulenceAffector14geometryChangeERK6QRectFS2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickTurbulenceAffector14geometryChangeERK6QRect'
          'FS2_')
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  def ensureInit(self) -> None:
    """
    Calls Qt's 'void QQuickTurbulenceAffector::ensureInit()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickturbulenceaffector.html#ensureInit
    """
    #  void QQuickTurbulenceAffector::ensureInit()
    self.uglySide.call('ritual_ZN24QQuickTurbulenceAffector10ensureInitEv')

  def initializeGrid(self) -> None:
    """
    Calls Qt's 'void QQuickTurbulenceAffector::initializeGrid()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickturbulenceaffector.html#initializeGrid
    """
    #  void QQuickTurbulenceAffector::initializeGrid()
    self.uglySide.call(
        'ritual_ZN24QQuickTurbulenceAffector14initializeGridEv',
    )

  @overload(int, int)
  def boundsRespectingField(self, x: int, y: int) -> float:
    """
    Calls Qt's 'qreal QQuickTurbulenceAffector::boundsRespectingField(int x,
    int y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickturbulenceaffector.html

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  qreal QQuickTurbulenceAffector::boundsRespectingField(int x, int y)
    return self.uglySide.call(
        'ritual_ZN24QQuickTurbulenceAffector21boundsRespectingFieldEii',
        x, y,
    )
