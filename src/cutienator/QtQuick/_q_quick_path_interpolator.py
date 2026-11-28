"""
QQuickPathInterpolator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpathinterpolator_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickPathInterpolator to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickPath
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickPath = WAIT['QQuickPath']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPathInterpolator(QObject):
  """
  The cute side of Qt's QQuickPathInterpolator: a plain Python object
  standing in front of one C++ QQuickPathInterpolator.

  It is built on the cute 'QObject', as Qt's QQuickPathInterpolator is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPathInterpolator that has a ritual and that
  Python can call so far, 15 names in all: 'metaObject', 'tr', 'path',
  'setPath', 'progress', 'setProgress', 'x', 'y', 'angle', 'pathChanged',
  'progressChanged', 'xChanged', 'yChanged', 'angleChanged',
  '_q_pathUpdated'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPathInterpolator::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickPathInterpolator::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickPathInterpolator is created at the first use, not by
    'QQuickPathInterpolator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPathInterpolator.
  - Qt tells when it has removed the C++ QQuickPathInterpolator. Every call
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
    Calls Qt's 'QString QQuickPathInterpolator::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathinterpolator.html#tr

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
    #  QString QQuickPathInterpolator::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QQuickPathInterpolator2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPathInterpolator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPathInterpolator::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathinterpolator.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPathInterpolator::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickPathInterpolator10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def path(self) -> Optional[QQuickPath]:
    """
    Calls Qt's 'QQuickPath *QQuickPathInterpolator::path() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathinterpolator.html#path

    Returns
    -------

    Optional[QQuickPath]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPath *QQuickPathInterpolator::path() const
    address = self.uglySide.call('ritual_ZNK22QQuickPathInterpolator4pathEv')
    from . import QQuickPath
    return QQuickPath._cuteAt(address)

  def progress(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathInterpolator::progress() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathinterpolator.html#progress
    """
    #  qreal QQuickPathInterpolator::progress() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickPathInterpolator8progressEv',
    )

  def x(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathInterpolator::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathinterpolator.html#x
    """
    #  qreal QQuickPathInterpolator::x() const
    return self.uglySide.call('ritual_ZNK22QQuickPathInterpolator1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathInterpolator::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathinterpolator.html#y
    """
    #  qreal QQuickPathInterpolator::y() const
    return self.uglySide.call('ritual_ZNK22QQuickPathInterpolator1yEv')

  def angle(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathInterpolator::angle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathinterpolator.html#angle
    """
    #  qreal QQuickPathInterpolator::angle() const
    return self.uglySide.call('ritual_ZNK22QQuickPathInterpolator5angleEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickPath)
  @overload(NoneType)
  def setPath(self, path: Optional[QQuickPath]) -> None:
    """
    Calls Qt's 'void QQuickPathInterpolator::setPath(QQuickPath *path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathinterpolator.html#setPath

    Parameters
    ----------

    path : Optional[QQuickPath]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPathInterpolator::setPath(QQuickPath *path)
    self.uglySide.call(
        'ritual_ZN22QQuickPathInterpolator7setPathEP10QQuickPath',
        self._addressOf(path),
    )

  @overload(float)
  def setProgress(self, progress: float) -> None:
    """
    Calls Qt's 'void QQuickPathInterpolator::setProgress(qreal progress)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathinterpolator.html#setProgress

    Parameters
    ----------

    progress : float
      Passed on as it is.
    """
    #  void QQuickPathInterpolator::setProgress(qreal progress)
    self.uglySide.call(
        'ritual_ZN22QQuickPathInterpolator11setProgressEd', progress,
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
    'QQuickPathInterpolator::QQuickPathInterpolator(QObject *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathinterpolator.html#QQuickPathInterpolator

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickPathInterpolator::QQuickPathInterpolator(QObject *parent)
    self._noteCreation(QQuickPathInterpolator, lambda: Rituals.call(
        'ritual_ZN22QQuickPathInterpolatorC1EP7QObject',
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

  def pathChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathInterpolator::pathChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathinterpolator.html#pathChanged
    """
    #  void QQuickPathInterpolator::pathChanged()
    self.uglySide.call('ritual_ZN22QQuickPathInterpolator11pathChangedEv')

  def progressChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathInterpolator::progressChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathinterpolator.html#progressChanged
    """
    #  void QQuickPathInterpolator::progressChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickPathInterpolator15progressChangedEv',
    )

  def xChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathInterpolator::xChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathinterpolator.html#xChanged
    """
    #  void QQuickPathInterpolator::xChanged()
    self.uglySide.call('ritual_ZN22QQuickPathInterpolator8xChangedEv')

  def yChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathInterpolator::yChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathinterpolator.html#yChanged
    """
    #  void QQuickPathInterpolator::yChanged()
    self.uglySide.call('ritual_ZN22QQuickPathInterpolator8yChangedEv')

  def angleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathInterpolator::angleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathinterpolator.html#angleChanged
    """
    #  void QQuickPathInterpolator::angleChanged()
    self.uglySide.call('ritual_ZN22QQuickPathInterpolator12angleChangedEv')

  def _q_pathUpdated(self) -> None:
    """
    Calls Qt's 'void QQuickPathInterpolator::_q_pathUpdated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathinterpolator.html#_q_pathUpdated
    """
    #  void QQuickPathInterpolator::_q_pathUpdated()
    self.uglySide.call('ritual_ZN22QQuickPathInterpolator14_q_pathUpdatedEv')
