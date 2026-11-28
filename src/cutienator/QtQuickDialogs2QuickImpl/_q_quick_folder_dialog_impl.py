"""
QQuickFolderDialogImpl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfolderdialogimpl_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickFolderDialogImpl to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QObject, QUrl
  from . import QQuickFolderDialogImplAttached, QQuickFolderDialogImplPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickFolderDialogImpl(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickFolderDialogImpl: a plain Python object
  standing in front of one C++ QQuickFolderDialogImpl.

  What exists
  -----------

  Every function of Qt's QQuickFolderDialogImpl that has a ritual and that
  Python can call so far, 15 names in all: 'metaObject', 'tr',
  'qmlAttachedProperties', 'currentFolder', 'setCurrentFolder',
  'selectedFolder', 'setSelectedFolder', 'setAcceptLabel', 'setRejectLabel',
  'currentFolderChanged', 'selectedFolderChanged', 'nameFiltersChanged',
  'componentComplete', 'itemChange', 'd_func'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickFolderDialogImpl::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickFolderDialogImpl::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickFolderDialogImpl::qt_qmlMarker_attached()': one of Qt's
    own inner workings.
  - Qt's 'QSharedPointer<QFileDialogOptions>
    QQuickFolderDialogImpl::options() const': gives a type Python has no way
    to take yet.
  - Qt's 'void QQuickFolderDialogImpl::setOptions(const
    QSharedPointer<QFileDialogOptions> &options)': takes a type Python has no
    way to hand over yet.
  - Qt's 'const QQuickFolderDialogImplPrivate
    *QQuickFolderDialogImpl::d_func() const': takes in Python what
    'QQuickFolderDialogImplPrivate *QQuickFolderDialogImpl::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 26 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickFolderDialogImpl is created at the first use, not by
    'QQuickFolderDialogImpl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFolderDialogImpl.
  - Qt tells when it has removed the C++ QQuickFolderDialogImpl. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickFolderDialogImpl that has no cute function yet,
    'options', 'setOptions', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QQuickFolderDialogImpl::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfolderdialogimpl.html#tr

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
    #  QString QQuickFolderDialogImpl::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QQuickFolderDialogImpl2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      object: Optional[QObject],
  ) -> Optional[QQuickFolderDialogImplAttached]:
    """
    Calls Qt's 'QQuickFolderDialogImplAttached
    *QQuickFolderDialogImpl::qmlAttachedProperties(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimpl.html#qmlAttachedProperties

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickFolderDialogImplAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFolderDialogImplAttached
    #      *QQuickFolderDialogImpl::qmlAttachedProperties(QObject *object)
    address = Rituals.call(
        'ritual_ZN22QQuickFolderDialogImpl21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    from . import QQuickFolderDialogImplAttached
    return QQuickFolderDialogImplAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFolderDialogImpl'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickFolderDialogImpl::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimpl.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickFolderDialogImpl::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickFolderDialogImpl10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def currentFolder(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickFolderDialogImpl::currentFolder() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimpl.html#currentFolder

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickFolderDialogImpl::currentFolder() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickFolderDialogImpl13currentFolderEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def selectedFolder(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickFolderDialogImpl::selectedFolder() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimpl.html#selectedFolder

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickFolderDialogImpl::selectedFolder() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickFolderDialogImpl14selectedFolderEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setCurrentFolder(self, folder: QUrl) -> None:
    """
    Calls Qt's 'void QQuickFolderDialogImpl::setCurrentFolder(const QUrl
    &folder)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimpl.html#setCurrentFolder

    Parameters
    ----------

    folder : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickFolderDialogImpl::setCurrentFolder(const QUrl &folder)
    self.uglySide.call(
        'ritual_ZN22QQuickFolderDialogImpl16setCurrentFolderERK4QUrl',
        self._valueOf(folder),
    )

  @overload(QUrl)
  def setSelectedFolder(self, selectedFolder: QUrl) -> None:
    """
    Calls Qt's 'void QQuickFolderDialogImpl::setSelectedFolder(const QUrl
    &selectedFolder)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimpl.html#setSelectedFolder

    Parameters
    ----------

    selectedFolder : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickFolderDialogImpl::setSelectedFolder(const QUrl
    #      &selectedFolder)
    self.uglySide.call(
        'ritual_ZN22QQuickFolderDialogImpl17setSelectedFolderERK4QUrl',
        self._valueOf(selectedFolder),
    )

  @overload(str)
  def setAcceptLabel(self, label: str) -> None:
    """
    Calls Qt's 'void QQuickFolderDialogImpl::setAcceptLabel(const QString
    &label)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimpl.html#setAcceptLabel

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickFolderDialogImpl::setAcceptLabel(const QString &label)
    self.uglySide.call(
        'ritual_ZN22QQuickFolderDialogImpl14setAcceptLabelERK7QString',
        label,
    )

  @overload(str)
  def setRejectLabel(self, label: str) -> None:
    """
    Calls Qt's 'void QQuickFolderDialogImpl::setRejectLabel(const QString
    &label)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimpl.html#setRejectLabel

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickFolderDialogImpl::setRejectLabel(const QString &label)
    self.uglySide.call(
        'ritual_ZN22QQuickFolderDialogImpl14setRejectLabelERK7QString',
        label,
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
    'QQuickFolderDialogImpl::QQuickFolderDialogImpl(QObject *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimpl.html#QQuickFolderDialogImpl

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickFolderDialogImpl::QQuickFolderDialogImpl(QObject *parent)
    self._noteCreation(QQuickFolderDialogImpl, lambda: Rituals.call(
        'ritual_ZN22QQuickFolderDialogImplC1EP7QObject',
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

  @overload(QUrl)
  def currentFolderChanged(self, folderUrl: QUrl) -> None:
    """
    Calls Qt's 'void QQuickFolderDialogImpl::currentFolderChanged(const QUrl
    &folderUrl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimpl.html#currentFolderChanged

    Parameters
    ----------

    folderUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickFolderDialogImpl::currentFolderChanged(const QUrl
    #      &folderUrl)
    self.uglySide.call(
        'ritual_ZN22QQuickFolderDialogImpl20currentFolderChangedERK4QUrl',
        self._valueOf(folderUrl),
    )

  @overload(QUrl)
  def selectedFolderChanged(self, folderUrl: QUrl) -> None:
    """
    Calls Qt's 'void QQuickFolderDialogImpl::selectedFolderChanged(const QUrl
    &folderUrl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimpl.html#selectedFolderChanged

    Parameters
    ----------

    folderUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickFolderDialogImpl::selectedFolderChanged(const QUrl
    #      &folderUrl)
    self.uglySide.call(
        'ritual_ZN22QQuickFolderDialogImpl21selectedFolderChangedERK4QUrl',
        self._valueOf(folderUrl),
    )

  def nameFiltersChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFolderDialogImpl::nameFiltersChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimpl.html#nameFiltersChanged
    """
    #  void QQuickFolderDialogImpl::nameFiltersChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickFolderDialogImpl18nameFiltersChangedEv',
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickFolderDialogImpl::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimpl.html#componentComplete
    """
    #  void QQuickFolderDialogImpl::componentComplete()
    ritual = 'ritual_ZN22QQuickFolderDialogImpl17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickFolderDialogImpl17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      data: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickFolderDialogImpl::itemChange(QQuickItem::ItemChange change, const
    QQuickItem::ItemChangeData &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimpl.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    data : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickFolderDialogImpl::itemChange(QQuickItem::ItemChange change,
    #      const QQuickItem::ItemChangeData &data)
    ritual = (
        'ritual_ZN22QQuickFolderDialogImpl10itemChangeEN10QQuickItem10ItemC'
        'hangeERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickFolderDialogImpl10itemChangeEN10QQuickItem1'
          '0ItemChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(data))

  def d_func(self) -> Optional[QQuickFolderDialogImplPrivate]:
    """
    Calls Qt's 'QQuickFolderDialogImplPrivate
    *QQuickFolderDialogImpl::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfolderdialogimpl.html#d_func

    Returns
    -------

    Optional[QQuickFolderDialogImplPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFolderDialogImplPrivate *QQuickFolderDialogImpl::d_func()
    address = self.uglySide.call(
        'ritual_ZN22QQuickFolderDialogImpl6d_funcEv',
    )
    from . import QQuickFolderDialogImplPrivate
    return QQuickFolderDialogImplPrivate._cuteAt(address)

  @staticmethod
  def options(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<QFileDialogOptions>
    QQuickFolderDialogImpl::options() const': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QQuickFolderDialogImpl.options' has no cute function yet. Qt's "
        "'QSharedPointer<QFileDialogOptions> "
        "QQuickFolderDialogImpl::options() const': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def setOptions(*__, **_) -> Never:
    """
    Qt's 'void QQuickFolderDialogImpl::setOptions(const
    QSharedPointer<QFileDialogOptions> &options)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickFolderDialogImpl.setOptions' has no cute function yet. Qt's "
        "'void QQuickFolderDialogImpl::setOptions(const "
        "QSharedPointer<QFileDialogOptions> &options)': takes a type Python "
        "has no way to hand over yet.")
