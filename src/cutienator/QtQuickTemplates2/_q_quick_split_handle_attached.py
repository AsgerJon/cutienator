"""
QQuickSplitHandleAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicksplitview_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickSplitHandleAttached to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickSplitHandleAttached(QObject):
  """
  The cute side of Qt's QQuickSplitHandleAttached: a plain Python object
  standing in front of one C++ QQuickSplitHandleAttached.

  It is built on the cute 'QObject', as Qt's QQuickSplitHandleAttached is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickSplitHandleAttached that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'tr', 'isHovered',
  'isPressed', 'qmlAttachedProperties', 'hoveredChanged', 'pressedChanged'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickSplitHandleAttached::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickSplitHandleAttached::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickSplitHandleAttached::qt_qmlMarker_attached()': one of
    Qt's own inner workings.
  - Qt's 'void QQuickSplitHandleAttached::qt_qmlMarker_uncreatable()': one of
    Qt's own inner workings.
  - Qt's 'QQuickSplitHandleAttachedPrivate
    *QQuickSplitHandleAttached::d_func()': gives
    'QQuickSplitHandleAttachedPrivate', which has no cute class yet.
  - Qt's 'const QQuickSplitHandleAttachedPrivate
    *QQuickSplitHandleAttached::d_func() const': gives
    'QQuickSplitHandleAttachedPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 18 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickSplitHandleAttached is created at the first use, not by
    'QQuickSplitHandleAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickSplitHandleAttached.
  - Qt tells when it has removed the C++ QQuickSplitHandleAttached. Every
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
    Calls Qt's 'QString QQuickSplitHandleAttached::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksplithandleattached.html#tr

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
    #  QString QQuickSplitHandleAttached::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QQuickSplitHandleAttached2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      object: Optional[QObject],
  ) -> Optional[QQuickSplitHandleAttached]:
    """
    Calls Qt's 'QQuickSplitHandleAttached
    *QQuickSplitHandleAttached::qmlAttachedProperties(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplithandleattached.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickSplitHandleAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickSplitHandleAttached
    #      *QQuickSplitHandleAttached::qmlAttachedProperties(QObject *object)
    address = Rituals.call(
        'ritual_ZN25QQuickSplitHandleAttached21qmlAttachedPropertiesEP7QObj'
        'ect',
        CuteMixin._addressOf(object, 'QObject'),
    )
    return QQuickSplitHandleAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickSplitHandleAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickSplitHandleAttached::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplithandleattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickSplitHandleAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickSplitHandleAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isHovered(self) -> bool:
    """
    Calls Qt's 'bool QQuickSplitHandleAttached::isHovered() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplithandleattached.html#isHovered
    """
    #  bool QQuickSplitHandleAttached::isHovered() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickSplitHandleAttached9isHoveredEv',
    )

  def isPressed(self) -> bool:
    """
    Calls Qt's 'bool QQuickSplitHandleAttached::isPressed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplithandleattached.html#isPressed
    """
    #  bool QQuickSplitHandleAttached::isPressed() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickSplitHandleAttached9isPressedEv',
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickSplitHandleAttached::QQuickSplitHandleAttached(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplithandleattached.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickSplitHandleAttached::QQuickSplitHandleAttached(QObject *parent)
    self._noteCreation(QQuickSplitHandleAttached, lambda: Rituals.call(
        'ritual_ZN25QQuickSplitHandleAttachedC1EP7QObject',
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

  def hoveredChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSplitHandleAttached::hoveredChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplithandleattached.html#hoveredChanged
    """
    #  void QQuickSplitHandleAttached::hoveredChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickSplitHandleAttached14hoveredChangedEv',
    )

  def pressedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSplitHandleAttached::pressedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplithandleattached.html#pressedChanged
    """
    #  void QQuickSplitHandleAttached::pressedChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickSplitHandleAttached14pressedChangedEv',
    )
