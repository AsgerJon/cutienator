"""
QQuickTableViewAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktableview_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickTableViewAttached to be private: it declares the class in a
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
  from ..QtQml import QQmlComponent
  from . import QQuickTableView
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlComponent = WAIT['QQmlComponent']
  QQuickTableView = WAIT['QQuickTableView']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTableViewAttached(QObject):
  """
  The cute side of Qt's QQuickTableViewAttached: a plain Python object
  standing in front of one C++ QQuickTableViewAttached.

  It is built on the cute 'QObject', as Qt's QQuickTableViewAttached is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTableViewAttached that has a ritual and that
  Python can call so far, 11 names in all: 'metaObject', 'tr', 'view',
  'setView', 'editDelegate', 'setEditDelegate', 'viewChanged', 'pooled',
  'reused', 'editDelegateChanged', 'commit'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickTableViewAttached::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickTableViewAttached::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickTableViewAttached is created at the first use, not by
    'QQuickTableViewAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTableViewAttached.
  - Qt tells when it has removed the C++ QQuickTableViewAttached. Every call
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
    Calls Qt's 'QString QQuickTableViewAttached::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableviewattached.html#tr

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
    #  QString QQuickTableViewAttached::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QQuickTableViewAttached2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTableViewAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickTableViewAttached::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTableViewAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickTableViewAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def view(self) -> Optional[QQuickTableView]:
    """
    Calls Qt's 'QQuickTableView *QQuickTableViewAttached::view() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableviewattached.html#view

    Returns
    -------

    Optional[QQuickTableView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTableView *QQuickTableViewAttached::view() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickTableViewAttached4viewEv',
    )
    from . import QQuickTableView
    return QQuickTableView._cuteAt(address)

  def editDelegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickTableViewAttached::editDelegate()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewattached.html#editDelegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickTableViewAttached::editDelegate() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickTableViewAttached12editDelegateEv',
    )
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickTableView)
  @overload(NoneType)
  def setView(self, newTableView: Optional[QQuickTableView]) -> None:
    """
    Calls Qt's 'void QQuickTableViewAttached::setView(QQuickTableView
    *newTableView)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewattached.html#setView

    Parameters
    ----------

    newTableView : Optional[QQuickTableView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTableViewAttached::setView(QQuickTableView *newTableView)
    self.uglySide.call(
        'ritual_ZN23QQuickTableViewAttached7setViewEP15QQuickTableView',
        self._addressOf(newTableView),
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setEditDelegate(
      self,
      newEditDelegate: Optional[QQmlComponent],
  ) -> None:
    """
    Calls Qt's 'void QQuickTableViewAttached::setEditDelegate(QQmlComponent
    *newEditDelegate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewattached.html#setEditDelegate

    Parameters
    ----------

    newEditDelegate : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTableViewAttached::setEditDelegate(QQmlComponent
    #      *newEditDelegate)
    self.uglySide.call(
        'ritual_ZN23QQuickTableViewAttached15setEditDelegateEP13QQmlCompone'
        'nt',
        self._addressOf(newEditDelegate),
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

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickTableViewAttached::QQuickTableViewAttached(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewattached.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickTableViewAttached::QQuickTableViewAttached(QObject *parent)
    self._noteCreation(QQuickTableViewAttached, lambda: Rituals.call(
        'ritual_ZN23QQuickTableViewAttachedC1EP7QObject',
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

  def viewChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewAttached::viewChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewattached.html#viewChanged
    """
    #  void QQuickTableViewAttached::viewChanged()
    self.uglySide.call('ritual_ZN23QQuickTableViewAttached11viewChangedEv')

  def pooled(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewAttached::pooled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewattached.html#pooled
    """
    #  void QQuickTableViewAttached::pooled()
    self.uglySide.call('ritual_ZN23QQuickTableViewAttached6pooledEv')

  def reused(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewAttached::reused()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewattached.html#reused
    """
    #  void QQuickTableViewAttached::reused()
    self.uglySide.call('ritual_ZN23QQuickTableViewAttached6reusedEv')

  def editDelegateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewAttached::editDelegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewattached.html#editDelegateChanged
    """
    #  void QQuickTableViewAttached::editDelegateChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickTableViewAttached19editDelegateChangedEv',
    )

  def commit(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewAttached::commit()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewattached.html#commit
    """
    #  void QQuickTableViewAttached::commit()
    self.uglySide.call('ritual_ZN23QQuickTableViewAttached6commitEv')
