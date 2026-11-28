"""
QQuickMaskExtruder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickmaskextruder_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickMaskExtruder to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickParticleExtruder

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF, QRectF, QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickMaskExtruder(QQuickParticleExtruder):
  """
  The cute side of Qt's QQuickMaskExtruder: a plain Python object standing in
  front of one C++ QQuickMaskExtruder.

  It is built on the cute 'QQuickParticleExtruder', as Qt's
  QQuickMaskExtruder is built on Qt's QQuickParticleExtruder, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickMaskExtruder that has a ritual and that Python
  can call so far, 10 names in all: 'metaObject', 'tr', 'extrude',
  'contains', 'source', 'sourceChanged', 'setSource', 'startMaskLoading',
  'finishMaskLoading', 'ensureInitialized'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickMaskExtruder::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickMaskExtruder::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickMaskExtruder is created at the first use, not by
    'QQuickMaskExtruder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickMaskExtruder.
  - Qt tells when it has removed the C++ QQuickMaskExtruder. Every call on
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
    Calls Qt's 'QString QQuickMaskExtruder::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmaskextruder.html#tr

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
    #  QString QQuickMaskExtruder::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QQuickMaskExtruder2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickMaskExtruder'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickMaskExtruder::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmaskextruder.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickMaskExtruder::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickMaskExtruder10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickMaskExtruder::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmaskextruder.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickMaskExtruder::source() const
    address = self.uglySide.call('ritual_ZNK18QQuickMaskExtruder6sourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, arg: QUrl) -> None:
    """
    Calls Qt's 'void QQuickMaskExtruder::setSource(const QUrl &arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmaskextruder.html#setSource

    Parameters
    ----------

    arg : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickMaskExtruder::setSource(const QUrl &arg)
    self.uglySide.call(
        'ritual_ZN18QQuickMaskExtruder9setSourceERK4QUrl',
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickMaskExtruder::QQuickMaskExtruder(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaskextruder.html#QQuickMaskExtruder

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickMaskExtruder::QQuickMaskExtruder(QObject *parent)
    self._noteCreation(QQuickMaskExtruder, lambda: Rituals.call(
        'ritual_ZN18QQuickMaskExtruderC1EP7QObject',
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

  @overload(QRectF)
  def extrude(self, a0: QRectF) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickMaskExtruder::extrude(const QRectF &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmaskextruder.html#extrude

    Parameters
    ----------

    a0 : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickMaskExtruder::extrude(const QRectF &a0)
    ritual = 'ritual_ZN18QQuickMaskExtruder7extrudeERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickMaskExtruder7extrudeERK6QRectF'
    address = self.uglySide.call(ritual, self._valueOf(a0))
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(QRectF, QPointF)
  def contains(self, bounds: QRectF, point: QPointF) -> bool:
    """
    Calls Qt's 'bool QQuickMaskExtruder::contains(const QRectF &bounds, const
    QPointF &point)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmaskextruder.html#contains

    Parameters
    ----------

    bounds : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QQuickMaskExtruder::contains(const QRectF &bounds, const QPointF
    #      &point)
    ritual = 'ritual_ZN18QQuickMaskExtruder8containsERK6QRectFRK7QPointF'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuickMaskExtruder8containsERK6QRectFRK7QPointF')
    return self.uglySide.call(
        ritual, self._valueOf(bounds), self._valueOf(point, 'QPointF'),
    )

  @overload(QUrl)
  def sourceChanged(self, arg: QUrl) -> None:
    """
    Calls Qt's 'void QQuickMaskExtruder::sourceChanged(const QUrl &arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaskextruder.html#sourceChanged

    Parameters
    ----------

    arg : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickMaskExtruder::sourceChanged(const QUrl &arg)
    self.uglySide.call(
        'ritual_ZN18QQuickMaskExtruder13sourceChangedERK4QUrl',
        self._valueOf(arg),
    )

  def startMaskLoading(self) -> None:
    """
    Calls Qt's 'void QQuickMaskExtruder::startMaskLoading()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaskextruder.html#startMaskLoading
    """
    #  void QQuickMaskExtruder::startMaskLoading()
    self.uglySide.call('ritual_ZN18QQuickMaskExtruder16startMaskLoadingEv')

  def finishMaskLoading(self) -> None:
    """
    Calls Qt's 'void QQuickMaskExtruder::finishMaskLoading()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaskextruder.html#finishMaskLoading
    """
    #  void QQuickMaskExtruder::finishMaskLoading()
    self.uglySide.call('ritual_ZN18QQuickMaskExtruder17finishMaskLoadingEv')

  @overload(QRectF)
  def ensureInitialized(self, r: QRectF) -> None:
    """
    Calls Qt's 'void QQuickMaskExtruder::ensureInitialized(const QRectF &r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmaskextruder.html#ensureInitialized

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickMaskExtruder::ensureInitialized(const QRectF &r)
    self.uglySide.call(
        'ritual_ZN18QQuickMaskExtruder17ensureInitializedERK6QRectF',
        self._valueOf(r),
    )
