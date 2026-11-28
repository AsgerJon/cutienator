"""
QQuickFlickableVisibleArea binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickflickable_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickFlickableVisibleArea to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickFlickable
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickFlickable = WAIT['QQuickFlickable']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickFlickableVisibleArea(QObject):
  """
  The cute side of Qt's QQuickFlickableVisibleArea: a plain Python object
  standing in front of one C++ QQuickFlickableVisibleArea.

  It is built on the cute 'QObject', as Qt's QQuickFlickableVisibleArea is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickFlickableVisibleArea that has a ritual and
  that Python can call so far, 11 names in all: 'metaObject', 'tr',
  'xPosition', 'widthRatio', 'yPosition', 'heightRatio', 'updateVisible',
  'xPositionChanged', 'yPositionChanged', 'widthRatioChanged',
  'heightRatioChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickFlickableVisibleArea::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickFlickableVisibleArea::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickFlickableVisibleArea::qt_qmlMarker_anonymous()': one of
    Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickFlickableVisibleArea is created at the first use, not by
    'QQuickFlickableVisibleArea(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFlickableVisibleArea.
  - Qt tells when it has removed the C++ QQuickFlickableVisibleArea. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickFlickableVisibleArea::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickablevisiblearea.html#tr

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
    #  QString QQuickFlickableVisibleArea::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QQuickFlickableVisibleArea2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFlickableVisibleArea'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickFlickableVisibleArea::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickablevisiblearea.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickFlickableVisibleArea::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickFlickableVisibleArea10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def xPosition(self) -> float:
    """
    Calls Qt's 'qreal QQuickFlickableVisibleArea::xPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickablevisiblearea.html#xPosition
    """
    #  qreal QQuickFlickableVisibleArea::xPosition() const
    return self.uglySide.call(
        'ritual_ZNK26QQuickFlickableVisibleArea9xPositionEv',
    )

  def widthRatio(self) -> float:
    """
    Calls Qt's 'qreal QQuickFlickableVisibleArea::widthRatio() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickablevisiblearea.html#widthRatio
    """
    #  qreal QQuickFlickableVisibleArea::widthRatio() const
    return self.uglySide.call(
        'ritual_ZNK26QQuickFlickableVisibleArea10widthRatioEv',
    )

  def yPosition(self) -> float:
    """
    Calls Qt's 'qreal QQuickFlickableVisibleArea::yPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickablevisiblearea.html#yPosition
    """
    #  qreal QQuickFlickableVisibleArea::yPosition() const
    return self.uglySide.call(
        'ritual_ZNK26QQuickFlickableVisibleArea9yPositionEv',
    )

  def heightRatio(self) -> float:
    """
    Calls Qt's 'qreal QQuickFlickableVisibleArea::heightRatio() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickablevisiblearea.html#heightRatio
    """
    #  qreal QQuickFlickableVisibleArea::heightRatio() const
    return self.uglySide.call(
        'ritual_ZNK26QQuickFlickableVisibleArea11heightRatioEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
  @overload(QQuickFlickable)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickFlickable] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickFlickableVisibleArea::QQuickFlickableVisibleArea(QQuickFlickable
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickablevisiblearea.html

    Parameters
    ----------

    parent : Optional[QQuickFlickable]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickFlickableVisibleArea::QQuickFlickableVisibleArea(QQuickFlickable
    #      *parent)
    self._noteCreation(QQuickFlickableVisibleArea, lambda: Rituals.call(
        'ritual_ZN26QQuickFlickableVisibleAreaC1EP15QQuickFlickable',
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

  def updateVisible(self) -> None:
    """
    Calls Qt's 'void QQuickFlickableVisibleArea::updateVisible()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickablevisiblearea.html#updateVisible
    """
    #  void QQuickFlickableVisibleArea::updateVisible()
    self.uglySide.call(
        'ritual_ZN26QQuickFlickableVisibleArea13updateVisibleEv',
    )

  @overload(float)
  def xPositionChanged(self, xPosition: float) -> None:
    """
    Calls Qt's 'void QQuickFlickableVisibleArea::xPositionChanged(qreal
    xPosition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickablevisiblearea.html#xPositionChanged

    Parameters
    ----------

    xPosition : float
      Passed on as it is.
    """
    #  void QQuickFlickableVisibleArea::xPositionChanged(qreal xPosition)
    self.uglySide.call(
        'ritual_ZN26QQuickFlickableVisibleArea16xPositionChangedEd',
        xPosition,
    )

  @overload(float)
  def yPositionChanged(self, yPosition: float) -> None:
    """
    Calls Qt's 'void QQuickFlickableVisibleArea::yPositionChanged(qreal
    yPosition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickablevisiblearea.html#yPositionChanged

    Parameters
    ----------

    yPosition : float
      Passed on as it is.
    """
    #  void QQuickFlickableVisibleArea::yPositionChanged(qreal yPosition)
    self.uglySide.call(
        'ritual_ZN26QQuickFlickableVisibleArea16yPositionChangedEd',
        yPosition,
    )

  @overload(float)
  def widthRatioChanged(self, widthRatio: float) -> None:
    """
    Calls Qt's 'void QQuickFlickableVisibleArea::widthRatioChanged(qreal
    widthRatio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickablevisiblearea.html#widthRatioChanged

    Parameters
    ----------

    widthRatio : float
      Passed on as it is.
    """
    #  void QQuickFlickableVisibleArea::widthRatioChanged(qreal widthRatio)
    self.uglySide.call(
        'ritual_ZN26QQuickFlickableVisibleArea17widthRatioChangedEd',
        widthRatio,
    )

  @overload(float)
  def heightRatioChanged(self, heightRatio: float) -> None:
    """
    Calls Qt's 'void QQuickFlickableVisibleArea::heightRatioChanged(qreal
    heightRatio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickablevisiblearea.html#heightRatioChanged

    Parameters
    ----------

    heightRatio : float
      Passed on as it is.
    """
    #  void QQuickFlickableVisibleArea::heightRatioChanged(qreal heightRatio)
    self.uglySide.call(
        'ritual_ZN26QQuickFlickableVisibleArea18heightRatioChangedEd',
        heightRatio,
    )
