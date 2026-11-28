"""
QQuickSplitViewAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicksplitview_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickSplitViewAttached to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickSplitView

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickSplitViewAttached(QObject):
  """
  The cute side of Qt's QQuickSplitViewAttached: a plain Python object
  standing in front of one C++ QQuickSplitViewAttached.

  It is built on the cute 'QObject', as Qt's QQuickSplitViewAttached is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickSplitViewAttached that has a ritual and that
  Python can call so far, 34 names in all: 'metaObject', 'tr', 'view',
  'minimumWidth', 'setMinimumWidth', 'resetMinimumWidth', 'minimumHeight',
  'setMinimumHeight', 'resetMinimumHeight', 'preferredWidth',
  'setPreferredWidth', 'resetPreferredWidth', 'preferredHeight',
  'setPreferredHeight', 'resetPreferredHeight', 'maximumWidth',
  'setMaximumWidth', 'resetMaximumWidth', 'maximumHeight',
  'setMaximumHeight', 'resetMaximumHeight', 'fillWidth', 'setFillWidth',
  'fillHeight', 'setFillHeight', 'viewChanged', 'minimumWidthChanged',
  'minimumHeightChanged', 'preferredWidthChanged', 'preferredHeightChanged',
  'maximumWidthChanged', 'maximumHeightChanged', 'fillWidthChanged',
  'fillHeightChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickSplitViewAttached::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickSplitViewAttached::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickSplitViewAttachedPrivate *QQuickSplitViewAttached::d_func()':
    gives 'QQuickSplitViewAttachedPrivate', which has no cute class yet.
  - Qt's 'const QQuickSplitViewAttachedPrivate
    *QQuickSplitViewAttached::d_func() const': gives
    'QQuickSplitViewAttachedPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 43 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickSplitViewAttached is created at the first use, not by
    'QQuickSplitViewAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickSplitViewAttached.
  - Qt tells when it has removed the C++ QQuickSplitViewAttached. Every call
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
    Calls Qt's 'QString QQuickSplitViewAttached::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksplitviewattached.html#tr

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
    #  QString QQuickSplitViewAttached::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QQuickSplitViewAttached2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickSplitViewAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickSplitViewAttached::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitviewattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickSplitViewAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickSplitViewAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def view(self) -> Optional[QQuickSplitView]:
    """
    Calls Qt's 'QQuickSplitView *QQuickSplitViewAttached::view() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksplitviewattached.html#view

    Returns
    -------

    Optional[QQuickSplitView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickSplitView *QQuickSplitViewAttached::view() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickSplitViewAttached4viewEv',
    )
    from . import QQuickSplitView
    return QQuickSplitView._cuteAt(address)

  def minimumWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickSplitViewAttached::minimumWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitviewattached.html#minimumWidth
    """
    #  qreal QQuickSplitViewAttached::minimumWidth() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickSplitViewAttached12minimumWidthEv',
    )

  def minimumHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickSplitViewAttached::minimumHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitviewattached.html#minimumHeight
    """
    #  qreal QQuickSplitViewAttached::minimumHeight() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickSplitViewAttached13minimumHeightEv',
    )

  def preferredWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickSplitViewAttached::preferredWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitviewattached.html#preferredWidth
    """
    #  qreal QQuickSplitViewAttached::preferredWidth() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickSplitViewAttached14preferredWidthEv',
    )

  def preferredHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickSplitViewAttached::preferredHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitviewattached.html#preferredHeight
    """
    #  qreal QQuickSplitViewAttached::preferredHeight() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickSplitViewAttached15preferredHeightEv',
    )

  def maximumWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickSplitViewAttached::maximumWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitviewattached.html#maximumWidth
    """
    #  qreal QQuickSplitViewAttached::maximumWidth() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickSplitViewAttached12maximumWidthEv',
    )

  def maximumHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickSplitViewAttached::maximumHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitviewattached.html#maximumHeight
    """
    #  qreal QQuickSplitViewAttached::maximumHeight() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickSplitViewAttached13maximumHeightEv',
    )

  def fillWidth(self) -> bool:
    """
    Calls Qt's 'bool QQuickSplitViewAttached::fillWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitviewattached.html#fillWidth
    """
    #  bool QQuickSplitViewAttached::fillWidth() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickSplitViewAttached9fillWidthEv',
    )

  def fillHeight(self) -> bool:
    """
    Calls Qt's 'bool QQuickSplitViewAttached::fillHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitviewattached.html#fillHeight
    """
    #  bool QQuickSplitViewAttached::fillHeight() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickSplitViewAttached10fillHeightEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setMinimumWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QQuickSplitViewAttached::setMinimumWidth(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitviewattached.html#setMinimumWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QQuickSplitViewAttached::setMinimumWidth(qreal width)
    self.uglySide.call(
        'ritual_ZN23QQuickSplitViewAttached15setMinimumWidthEd', width,
    )

  @overload(float)
  def setMinimumHeight(self, height: float) -> None:
    """
    Calls Qt's 'void QQuickSplitViewAttached::setMinimumHeight(qreal
    height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitviewattached.html#setMinimumHeight

    Parameters
    ----------

    height : float
      Passed on as it is.
    """
    #  void QQuickSplitViewAttached::setMinimumHeight(qreal height)
    self.uglySide.call(
        'ritual_ZN23QQuickSplitViewAttached16setMinimumHeightEd', height,
    )

  @overload(float)
  def setPreferredWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QQuickSplitViewAttached::setPreferredWidth(qreal
    width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitviewattached.html#setPreferredWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QQuickSplitViewAttached::setPreferredWidth(qreal width)
    self.uglySide.call(
        'ritual_ZN23QQuickSplitViewAttached17setPreferredWidthEd', width,
    )

  @overload(float)
  def setPreferredHeight(self, height: float) -> None:
    """
    Calls Qt's 'void QQuickSplitViewAttached::setPreferredHeight(qreal
    height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitviewattached.html#setPreferredHeight

    Parameters
    ----------

    height : float
      Passed on as it is.
    """
    #  void QQuickSplitViewAttached::setPreferredHeight(qreal height)
    self.uglySide.call(
        'ritual_ZN23QQuickSplitViewAttached18setPreferredHeightEd', height,
    )

  @overload(float)
  def setMaximumWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QQuickSplitViewAttached::setMaximumWidth(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitviewattached.html#setMaximumWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QQuickSplitViewAttached::setMaximumWidth(qreal width)
    self.uglySide.call(
        'ritual_ZN23QQuickSplitViewAttached15setMaximumWidthEd', width,
    )

  @overload(float)
  def setMaximumHeight(self, height: float) -> None:
    """
    Calls Qt's 'void QQuickSplitViewAttached::setMaximumHeight(qreal
    height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitviewattached.html#setMaximumHeight

    Parameters
    ----------

    height : float
      Passed on as it is.
    """
    #  void QQuickSplitViewAttached::setMaximumHeight(qreal height)
    self.uglySide.call(
        'ritual_ZN23QQuickSplitViewAttached16setMaximumHeightEd', height,
    )

  @overload(bool)
  def setFillWidth(self, fill: bool) -> None:
    """
    Calls Qt's 'void QQuickSplitViewAttached::setFillWidth(bool fill)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitviewattached.html#setFillWidth

    Parameters
    ----------

    fill : bool
      Passed on as it is.
    """
    #  void QQuickSplitViewAttached::setFillWidth(bool fill)
    self.uglySide.call(
        'ritual_ZN23QQuickSplitViewAttached12setFillWidthEb', fill,
    )

  @overload(bool)
  def setFillHeight(self, fill: bool) -> None:
    """
    Calls Qt's 'void QQuickSplitViewAttached::setFillHeight(bool fill)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitviewattached.html#setFillHeight

    Parameters
    ----------

    fill : bool
      Passed on as it is.
    """
    #  void QQuickSplitViewAttached::setFillHeight(bool fill)
    self.uglySide.call(
        'ritual_ZN23QQuickSplitViewAttached13setFillHeightEb', fill,
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
    'QQuickSplitViewAttached::QQuickSplitViewAttached(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitviewattached.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickSplitViewAttached::QQuickSplitViewAttached(QObject *parent)
    self._noteCreation(QQuickSplitViewAttached, lambda: Rituals.call(
        'ritual_ZN23QQuickSplitViewAttachedC1EP7QObject',
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

  def resetMinimumWidth(self) -> None:
    """
    Calls Qt's 'void QQuickSplitViewAttached::resetMinimumWidth()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitviewattached.html#resetMinimumWidth
    """
    #  void QQuickSplitViewAttached::resetMinimumWidth()
    self.uglySide.call(
        'ritual_ZN23QQuickSplitViewAttached17resetMinimumWidthEv',
    )

  def resetMinimumHeight(self) -> None:
    """
    Calls Qt's 'void QQuickSplitViewAttached::resetMinimumHeight()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitviewattached.html#resetMinimumHeight
    """
    #  void QQuickSplitViewAttached::resetMinimumHeight()
    self.uglySide.call(
        'ritual_ZN23QQuickSplitViewAttached18resetMinimumHeightEv',
    )

  def resetPreferredWidth(self) -> None:
    """
    Calls Qt's 'void QQuickSplitViewAttached::resetPreferredWidth()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitviewattached.html#resetPreferredWidth
    """
    #  void QQuickSplitViewAttached::resetPreferredWidth()
    self.uglySide.call(
        'ritual_ZN23QQuickSplitViewAttached19resetPreferredWidthEv',
    )

  def resetPreferredHeight(self) -> None:
    """
    Calls Qt's 'void QQuickSplitViewAttached::resetPreferredHeight()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitviewattached.html#resetPreferredHeight
    """
    #  void QQuickSplitViewAttached::resetPreferredHeight()
    self.uglySide.call(
        'ritual_ZN23QQuickSplitViewAttached20resetPreferredHeightEv',
    )

  def resetMaximumWidth(self) -> None:
    """
    Calls Qt's 'void QQuickSplitViewAttached::resetMaximumWidth()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitviewattached.html#resetMaximumWidth
    """
    #  void QQuickSplitViewAttached::resetMaximumWidth()
    self.uglySide.call(
        'ritual_ZN23QQuickSplitViewAttached17resetMaximumWidthEv',
    )

  def resetMaximumHeight(self) -> None:
    """
    Calls Qt's 'void QQuickSplitViewAttached::resetMaximumHeight()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitviewattached.html#resetMaximumHeight
    """
    #  void QQuickSplitViewAttached::resetMaximumHeight()
    self.uglySide.call(
        'ritual_ZN23QQuickSplitViewAttached18resetMaximumHeightEv',
    )

  def viewChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSplitViewAttached::viewChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitviewattached.html#viewChanged
    """
    #  void QQuickSplitViewAttached::viewChanged()
    self.uglySide.call('ritual_ZN23QQuickSplitViewAttached11viewChangedEv')

  def minimumWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSplitViewAttached::minimumWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitviewattached.html#minimumWidthChanged
    """
    #  void QQuickSplitViewAttached::minimumWidthChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickSplitViewAttached19minimumWidthChangedEv',
    )

  def minimumHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSplitViewAttached::minimumHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitviewattached.html#minimumHeightChanged
    """
    #  void QQuickSplitViewAttached::minimumHeightChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickSplitViewAttached20minimumHeightChangedEv',
    )

  def preferredWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSplitViewAttached::preferredWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitviewattached.html#preferredWidthChanged
    """
    #  void QQuickSplitViewAttached::preferredWidthChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickSplitViewAttached21preferredWidthChangedEv',
    )

  def preferredHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSplitViewAttached::preferredHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitviewattached.html
    """
    #  void QQuickSplitViewAttached::preferredHeightChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickSplitViewAttached22preferredHeightChangedEv',
    )

  def maximumWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSplitViewAttached::maximumWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitviewattached.html#maximumWidthChanged
    """
    #  void QQuickSplitViewAttached::maximumWidthChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickSplitViewAttached19maximumWidthChangedEv',
    )

  def maximumHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSplitViewAttached::maximumHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitviewattached.html#maximumHeightChanged
    """
    #  void QQuickSplitViewAttached::maximumHeightChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickSplitViewAttached20maximumHeightChangedEv',
    )

  def fillWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSplitViewAttached::fillWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitviewattached.html#fillWidthChanged
    """
    #  void QQuickSplitViewAttached::fillWidthChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickSplitViewAttached16fillWidthChangedEv',
    )

  def fillHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSplitViewAttached::fillHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitviewattached.html#fillHeightChanged
    """
    #  void QQuickSplitViewAttached::fillHeightChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickSplitViewAttached17fillHeightChangedEv',
    )
