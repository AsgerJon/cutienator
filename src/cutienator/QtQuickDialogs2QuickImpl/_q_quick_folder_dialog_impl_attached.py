"""
QQuickFolderDialogImplAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfolderdialogimpl_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickFolderDialogImplAttached to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtQuick import QQuickListView
  from . import QQuickFolderBreadcrumbBar
  from . import QQuickFolderDialogImplAttachedPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickFolderBreadcrumbBar = WAIT['QQuickFolderBreadcrumbBar']
  QQuickListView = WAIT['QQuickListView']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickFolderDialogImplAttached(QObject):
  """
  The cute side of Qt's QQuickFolderDialogImplAttached: a plain Python object
  standing in front of one C++ QQuickFolderDialogImplAttached.

  It is built on the cute 'QObject', as Qt's QQuickFolderDialogImplAttached
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickFolderDialogImplAttached that has a ritual and
  that Python can call so far, 9 names in all: 'metaObject', 'tr',
  'folderDialogListView', 'setFolderDialogListView', 'breadcrumbBar',
  'setBreadcrumbBar', 'folderDialogListViewChanged', 'breadcrumbBarChanged',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickFolderDialogImplAttached::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuickFolderDialogImplAttached::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickFolderDialogImplAttachedPrivate
    *QQuickFolderDialogImplAttached::d_func() const': takes in Python what
    'QQuickFolderDialogImplAttachedPrivate
    *QQuickFolderDialogImplAttached::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 17 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickFolderDialogImplAttached is created at the first use, not
    by 'QQuickFolderDialogImplAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFolderDialogImplAttached.
  - Qt tells when it has removed the C++ QQuickFolderDialogImplAttached.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QQuickFolderDialogImplAttached::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimplattached.html#tr

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
    #  QString QQuickFolderDialogImplAttached::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN30QQuickFolderDialogImplAttached2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFolderDialogImplAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuickFolderDialogImplAttached::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimplattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickFolderDialogImplAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuickFolderDialogImplAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def folderDialogListView(self) -> Optional[QQuickListView]:
    """
    Calls Qt's 'QQuickListView
    *QQuickFolderDialogImplAttached::folderDialogListView() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimplattached.html

    Returns
    -------

    Optional[QQuickListView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickListView *QQuickFolderDialogImplAttached::folderDialogListView()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK30QQuickFolderDialogImplAttached20folderDialogListViewEv',
    )
    from ..QtQuick import QQuickListView
    return QQuickListView._cuteAt(address)

  def breadcrumbBar(self) -> Optional[QQuickFolderBreadcrumbBar]:
    """
    Calls Qt's 'QQuickFolderBreadcrumbBar
    *QQuickFolderDialogImplAttached::breadcrumbBar() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimplattached.html#breadcrumbBar

    Returns
    -------

    Optional[QQuickFolderBreadcrumbBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFolderBreadcrumbBar
    #      *QQuickFolderDialogImplAttached::breadcrumbBar() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuickFolderDialogImplAttached13breadcrumbBarEv',
    )
    from . import QQuickFolderBreadcrumbBar
    return QQuickFolderBreadcrumbBar._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickListView)
  @overload(NoneType)
  def setFolderDialogListView(
      self,
      folderDialogListView: Optional[QQuickListView],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickFolderDialogImplAttached::setFolderDialogListView(QQuickListView
    *folderDialogListView)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimplattached.html

    Parameters
    ----------

    folderDialogListView : Optional[QQuickListView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFolderDialogImplAttached::setFolderDialogListView(
    #      QQuickListView *folderDialogListView)
    self.uglySide.call(
        'ritual_ZN30QQuickFolderDialogImplAttached23setFolderDialogListView'
        'EP14QQuickListView',
        self._addressOf(folderDialogListView),
    )

  @overload(QQuickFolderBreadcrumbBar)
  @overload(NoneType)
  def setBreadcrumbBar(
      self,
      breadcrumbBar: Optional[QQuickFolderBreadcrumbBar],
  ) -> None:
    """
    Calls Qt's 'void QQuickFolderDialogImplAttached::setBreadcrumbBar(
    QQuickFolderBreadcrumbBar *breadcrumbBar)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimplattached.html

    Parameters
    ----------

    breadcrumbBar : Optional[QQuickFolderBreadcrumbBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFolderDialogImplAttached::setBreadcrumbBar(
    #      QQuickFolderBreadcrumbBar *breadcrumbBar)
    self.uglySide.call(
        'ritual_ZN30QQuickFolderDialogImplAttached16setBreadcrumbBarEP25QQu'
        'ickFolderBreadcrumbBar',
        self._addressOf(breadcrumbBar),
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
    'QQuickFolderDialogImplAttached::QQuickFolderDialogImplAttached(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimplattached.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickFolderDialogImplAttached::QQuickFolderDialogImplAttached(QObject
    #      *parent)
    self._noteCreation(QQuickFolderDialogImplAttached, lambda: Rituals.call(
        'ritual_ZN30QQuickFolderDialogImplAttachedC1EP7QObject',
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

  def folderDialogListViewChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickFolderDialogImplAttached::folderDialogListViewChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimplattached.html
    """
    #  void QQuickFolderDialogImplAttached::folderDialogListViewChanged()
    self.uglySide.call(
        'ritual_ZN30QQuickFolderDialogImplAttached27folderDialogListViewCha'
        'ngedEv',
    )

  def breadcrumbBarChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFolderDialogImplAttached::breadcrumbBarChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimplattached.html
    """
    #  void QQuickFolderDialogImplAttached::breadcrumbBarChanged()
    self.uglySide.call(
        'ritual_ZN30QQuickFolderDialogImplAttached20breadcrumbBarChangedEv',
    )

  def d_func(self) -> Optional[QQuickFolderDialogImplAttachedPrivate]:
    """
    Calls Qt's 'QQuickFolderDialogImplAttachedPrivate
    *QQuickFolderDialogImplAttached::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimplattached.html#d_func

    Returns
    -------

    Optional[QQuickFolderDialogImplAttachedPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFolderDialogImplAttachedPrivate
    #      *QQuickFolderDialogImplAttached::d_func()
    address = self.uglySide.call(
        'ritual_ZN30QQuickFolderDialogImplAttached6d_funcEv',
    )
    from . import QQuickFolderDialogImplAttachedPrivate
    return QQuickFolderDialogImplAttachedPrivate._cuteAt(address)
