"""
QQuickActionGroupAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickactiongroup_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickActionGroupAttached to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickActionGroup
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickActionGroup = WAIT['QQuickActionGroup']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickActionGroupAttached(QObject):
  """
  The cute side of Qt's QQuickActionGroupAttached: a plain Python object
  standing in front of one C++ QQuickActionGroupAttached.

  It is built on the cute 'QObject', as Qt's QQuickActionGroupAttached is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickActionGroupAttached that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject', 'tr', 'group',
  'setGroup', 'groupChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickActionGroupAttached::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickActionGroupAttached::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickActionGroupAttachedPrivate
    *QQuickActionGroupAttached::d_func()': gives
    'QQuickActionGroupAttachedPrivate', which has no cute class yet.
  - Qt's 'const QQuickActionGroupAttachedPrivate
    *QQuickActionGroupAttached::d_func() const': gives
    'QQuickActionGroupAttachedPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 14 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickActionGroupAttached is created at the first use, not by
    'QQuickActionGroupAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickActionGroupAttached.
  - Qt tells when it has removed the C++ QQuickActionGroupAttached. Every
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
    Calls Qt's 'QString QQuickActionGroupAttached::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickactiongroupattached.html#tr

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
    #  QString QQuickActionGroupAttached::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QQuickActionGroupAttached2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickActionGroupAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickActionGroupAttached::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickactiongroupattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickActionGroupAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickActionGroupAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def group(self) -> Optional[QQuickActionGroup]:
    """
    Calls Qt's 'QQuickActionGroup *QQuickActionGroupAttached::group() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickactiongroupattached.html#group

    Returns
    -------

    Optional[QQuickActionGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickActionGroup *QQuickActionGroupAttached::group() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickActionGroupAttached5groupEv',
    )
    from . import QQuickActionGroup
    return QQuickActionGroup._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickActionGroup)
  @overload(NoneType)
  def setGroup(self, group: Optional[QQuickActionGroup]) -> None:
    """
    Calls Qt's 'void QQuickActionGroupAttached::setGroup(QQuickActionGroup
    *group)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickactiongroupattached.html#setGroup

    Parameters
    ----------

    group : Optional[QQuickActionGroup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickActionGroupAttached::setGroup(QQuickActionGroup *group)
    self.uglySide.call(
        'ritual_ZN25QQuickActionGroupAttached8setGroupEP17QQuickActionGroup',
        self._addressOf(group),
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
    'QQuickActionGroupAttached::QQuickActionGroupAttached(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickactiongroupattached.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickActionGroupAttached::QQuickActionGroupAttached(QObject *parent)
    self._noteCreation(QQuickActionGroupAttached, lambda: Rituals.call(
        'ritual_ZN25QQuickActionGroupAttachedC1EP7QObject',
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

  def groupChanged(self) -> None:
    """
    Calls Qt's 'void QQuickActionGroupAttached::groupChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickactiongroupattached.html#groupChanged
    """
    #  void QQuickActionGroupAttached::groupChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickActionGroupAttached12groupChangedEv',
    )
