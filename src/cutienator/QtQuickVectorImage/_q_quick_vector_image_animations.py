"""
QQuickVectorImageAnimations binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickVectorImage/6.12.0/QtQuickVectorImage/private/qquickvectorimage_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickVectorImageAnimations to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickVectorImageAnimations(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickVectorImageAnimations: a plain Python object
  standing in front of one C++ QQuickVectorImageAnimations.

  What exists
  -----------

  Every function of Qt's QQuickVectorImageAnimations that has a ritual and
  that Python can call so far, 10 names in all: 'metaObject', 'tr', 'loops',
  'setLoops', 'paused', 'setPaused', 'restart', 'loopsChanged',
  'enabledChanged', 'pausedChanged'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickVectorImageAnimations::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuickVectorImageAnimations::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickVectorImageAnimations::qt_qmlMarker_anonymous()': one of
    Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickVectorImageAnimations is created at the first use, not by
    'QQuickVectorImageAnimations(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickVectorImageAnimations.
  - Qt tells when it has removed the C++ QQuickVectorImageAnimations. Every
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
    Calls Qt's 'QString QQuickVectorImageAnimations::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimageanimations.html#tr

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
    #  QString QQuickVectorImageAnimations::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN27QQuickVectorImageAnimations2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickVectorImageAnimations'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickVectorImageAnimations::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimageanimations.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickVectorImageAnimations::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QQuickVectorImageAnimations10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def loops(self) -> int:
    """
    Calls Qt's 'int QQuickVectorImageAnimations::loops() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimageanimations.html#loops
    """
    #  int QQuickVectorImageAnimations::loops() const
    return self.uglySide.call(
        'ritual_ZNK27QQuickVectorImageAnimations5loopsEv',
    )

  def paused(self) -> bool:
    """
    Calls Qt's 'bool QQuickVectorImageAnimations::paused() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimageanimations.html#paused
    """
    #  bool QQuickVectorImageAnimations::paused() const
    return self.uglySide.call(
        'ritual_ZNK27QQuickVectorImageAnimations6pausedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setLoops(self, loops: int) -> None:
    """
    Calls Qt's 'void QQuickVectorImageAnimations::setLoops(int loops)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimageanimations.html#setLoops

    Parameters
    ----------

    loops : int
      Passed on as it is.
    """
    #  void QQuickVectorImageAnimations::setLoops(int loops)
    self.uglySide.call(
        'ritual_ZN27QQuickVectorImageAnimations8setLoopsEi', loops,
    )

  @overload(bool)
  def setPaused(self, paused: bool) -> None:
    """
    Calls Qt's 'void QQuickVectorImageAnimations::setPaused(bool paused)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimageanimations.html#setPaused

    Parameters
    ----------

    paused : bool
      Passed on as it is.
    """
    #  void QQuickVectorImageAnimations::setPaused(bool paused)
    self.uglySide.call(
        'ritual_ZN27QQuickVectorImageAnimations9setPausedEb', paused,
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
    'QQuickVectorImageAnimations::QQuickVectorImageAnimations(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimageanimations.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickVectorImageAnimations::QQuickVectorImageAnimations(QObject
    #      *parent)
    self._noteCreation(QQuickVectorImageAnimations, lambda: Rituals.call(
        'ritual_ZN27QQuickVectorImageAnimationsC1EP7QObject',
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

  def restart(self) -> None:
    """
    Calls Qt's 'void QQuickVectorImageAnimations::restart()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimageanimations.html#restart
    """
    #  void QQuickVectorImageAnimations::restart()
    self.uglySide.call('ritual_ZN27QQuickVectorImageAnimations7restartEv')

  def loopsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickVectorImageAnimations::loopsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimageanimations.html#loopsChanged
    """
    #  void QQuickVectorImageAnimations::loopsChanged()
    self.uglySide.call(
        'ritual_ZN27QQuickVectorImageAnimations12loopsChangedEv',
    )

  def enabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickVectorImageAnimations::enabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimageanimations.html#enabledChanged
    """
    #  void QQuickVectorImageAnimations::enabledChanged()
    self.uglySide.call(
        'ritual_ZN27QQuickVectorImageAnimations14enabledChangedEv',
    )

  def pausedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickVectorImageAnimations::pausedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickvectorimageanimations.html#pausedChanged
    """
    #  void QQuickVectorImageAnimations::pausedChanged()
    self.uglySide.call(
        'ritual_ZN27QQuickVectorImageAnimations13pausedChangedEv',
    )
