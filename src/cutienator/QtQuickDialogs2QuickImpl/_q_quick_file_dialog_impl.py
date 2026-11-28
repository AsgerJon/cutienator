"""
QQuickFileDialogImpl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfiledialogimpl_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickFileDialogImpl to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QObject, QUrl
  from . import QQuickFileDialogImplAttached, QQuickFileDialogImplPrivate
  from ..QtQuickDialogs2Utils import QQuickFileNameFilter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickFileDialogImpl(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickFileDialogImpl: a plain Python object standing
  in front of one C++ QQuickFileDialogImpl.

  What exists
  -----------

  Every function of Qt's QQuickFileDialogImpl that has a ritual and that
  Python can call so far, 25 names in all: 'metaObject', 'tr',
  'qmlAttachedProperties', 'currentFolder', 'setCurrentFolder',
  'selectedFile', 'setSelectedFile',
  'setInitialCurrentFolderAndSelectedFile', 'nameFilters',
  'resetNameFilters', 'selectedNameFilter', 'setAcceptLabel',
  'setRejectLabel', 'fileName', 'setFileName', 'currentFolderName',
  'selectNameFilter', 'currentFolderChanged', 'selectedFileChanged',
  'nameFiltersChanged', 'fileSelected', 'filterSelected',
  'componentComplete', 'itemChange', 'd_func'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickFileDialogImpl::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickFileDialogImpl::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickFileDialogImpl::qt_qmlMarker_attached()': one of Qt's
    own inner workings.
  - Qt's 'QSharedPointer<QFileDialogOptions> QQuickFileDialogImpl::options()
    const': gives a type Python has no way to take yet.
  - Qt's 'void QQuickFileDialogImpl::setOptions(const
    QSharedPointer<QFileDialogOptions> &options)': takes a type Python has no
    way to hand over yet.
  - Qt's 'const QQuickFileDialogImplPrivate *QQuickFileDialogImpl::d_func()
    const': takes in Python what 'QQuickFileDialogImplPrivate
    *QQuickFileDialogImpl::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 36 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickFileDialogImpl is created at the first use, not by
    'QQuickFileDialogImpl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFileDialogImpl.
  - Qt tells when it has removed the C++ QQuickFileDialogImpl. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickFileDialogImpl that has no cute function yet,
    'options', 'setOptions', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickFileDialogImpl, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class SetReason(CuteNum, scoped=True):
    """
    The enum 'QQuickFileDialogImpl::SetReason' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    External = Kee[int](0)
    Internal = Kee[int](1)

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
    Calls Qt's 'QString QQuickFileDialogImpl::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfiledialogimpl.html#tr

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
    #  QString QQuickFileDialogImpl::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuickFileDialogImpl2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      object: Optional[QObject],
  ) -> Optional[QQuickFileDialogImplAttached]:
    """
    Calls Qt's 'QQuickFileDialogImplAttached
    *QQuickFileDialogImpl::qmlAttachedProperties(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimpl.html#qmlAttachedProperties

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickFileDialogImplAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFileDialogImplAttached
    #      *QQuickFileDialogImpl::qmlAttachedProperties(QObject *object)
    address = Rituals.call(
        'ritual_ZN20QQuickFileDialogImpl21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    from . import QQuickFileDialogImplAttached
    return QQuickFileDialogImplAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFileDialogImpl'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickFileDialogImpl::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimpl.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickFileDialogImpl::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickFileDialogImpl10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def currentFolder(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickFileDialogImpl::currentFolder() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimpl.html#currentFolder

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickFileDialogImpl::currentFolder() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickFileDialogImpl13currentFolderEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def selectedFile(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickFileDialogImpl::selectedFile() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimpl.html#selectedFile

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickFileDialogImpl::selectedFile() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickFileDialogImpl12selectedFileEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def nameFilters(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQuickFileDialogImpl::nameFilters() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimpl.html#nameFilters

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQuickFileDialogImpl::nameFilters() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickFileDialogImpl11nameFiltersEv',
    )
    return QStringList._cuteOwning(address)

  def selectedNameFilter(self) -> Optional[QQuickFileNameFilter]:
    """
    Calls Qt's 'QQuickFileNameFilter
    *QQuickFileDialogImpl::selectedNameFilter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimpl.html#selectedNameFilter

    Returns
    -------

    Optional[QQuickFileNameFilter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFileNameFilter *QQuickFileDialogImpl::selectedNameFilter() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickFileDialogImpl18selectedNameFilterEv',
    )
    from ..QtQuickDialogs2Utils import QQuickFileNameFilter
    return QQuickFileNameFilter._cuteAt(address)

  def fileName(self) -> str:
    """
    Calls Qt's 'QString QQuickFileDialogImpl::fileName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfiledialogimpl.html#fileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickFileDialogImpl::fileName() const
    return self.uglySide.call('ritual_ZNK20QQuickFileDialogImpl8fileNameEv')

  def currentFolderName(self) -> str:
    """
    Calls Qt's 'QString QQuickFileDialogImpl::currentFolderName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimpl.html#currentFolderName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickFileDialogImpl::currentFolderName() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickFileDialogImpl17currentFolderNameEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  @overload(QUrl, SetReason)
  def setCurrentFolder(
      self,
      currentFolder: QUrl,
      setReason: SetReason = SetReason.External,
  ) -> None:
    """
    Calls Qt's 'void QQuickFileDialogImpl::setCurrentFolder(const QUrl
    &currentFolder, SetReason setReason)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimpl.html#setCurrentFolder

    Parameters
    ----------

    currentFolder : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    setReason : SetReason
      Passed on as its number. May be left out, as in Qt: it is then
      SetReason.External.
    """
    #  void QQuickFileDialogImpl::setCurrentFolder(const QUrl &currentFolder,
    #      SetReason setReason)
    self.uglySide.call(
        'ritual_ZN20QQuickFileDialogImpl16setCurrentFolderERK4QUrlNS_9SetRe'
        'asonE',
        self._valueOf(currentFolder), setReason.value,
    )

  @overload(QUrl)
  def setSelectedFile(self, file: QUrl) -> None:
    """
    Calls Qt's 'void QQuickFileDialogImpl::setSelectedFile(const QUrl
    &file)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimpl.html#setSelectedFile

    Parameters
    ----------

    file : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickFileDialogImpl::setSelectedFile(const QUrl &file)
    self.uglySide.call(
        'ritual_ZN20QQuickFileDialogImpl15setSelectedFileERK4QUrl',
        self._valueOf(file),
    )

  @overload(QUrl)
  def setInitialCurrentFolderAndSelectedFile(self, file: QUrl) -> None:
    """
    Calls Qt's 'void
    QQuickFileDialogImpl::setInitialCurrentFolderAndSelectedFile(const QUrl
    &file)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimpl.html

    Parameters
    ----------

    file : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void
    #      QQuickFileDialogImpl::setInitialCurrentFolderAndSelectedFile(const
    #      QUrl &file)
    self.uglySide.call(
        'ritual_ZN20QQuickFileDialogImpl38setInitialCurrentFolderAndSelecte'
        'dFileERK4QUrl',
        self._valueOf(file),
    )

  @overload(str)
  def setAcceptLabel(self, label: str) -> None:
    """
    Calls Qt's 'void QQuickFileDialogImpl::setAcceptLabel(const QString
    &label)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimpl.html#setAcceptLabel

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickFileDialogImpl::setAcceptLabel(const QString &label)
    self.uglySide.call(
        'ritual_ZN20QQuickFileDialogImpl14setAcceptLabelERK7QString', label,
    )

  @overload(str)
  def setRejectLabel(self, label: str) -> None:
    """
    Calls Qt's 'void QQuickFileDialogImpl::setRejectLabel(const QString
    &label)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimpl.html#setRejectLabel

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickFileDialogImpl::setRejectLabel(const QString &label)
    self.uglySide.call(
        'ritual_ZN20QQuickFileDialogImpl14setRejectLabelERK7QString', label,
    )

  @overload(str)
  def setFileName(self, fileName: str) -> None:
    """
    Calls Qt's 'void QQuickFileDialogImpl::setFileName(const QString
    &fileName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimpl.html#setFileName

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickFileDialogImpl::setFileName(const QString &fileName)
    self.uglySide.call(
        'ritual_ZN20QQuickFileDialogImpl11setFileNameERK7QString', fileName,
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
    'QQuickFileDialogImpl::QQuickFileDialogImpl(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimpl.html#QQuickFileDialogImpl

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickFileDialogImpl::QQuickFileDialogImpl(QObject *parent)
    self._noteCreation(QQuickFileDialogImpl, lambda: Rituals.call(
        'ritual_ZN20QQuickFileDialogImplC1EP7QObject',
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

  def resetNameFilters(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialogImpl::resetNameFilters()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimpl.html#resetNameFilters
    """
    #  void QQuickFileDialogImpl::resetNameFilters()
    self.uglySide.call('ritual_ZN20QQuickFileDialogImpl16resetNameFiltersEv')

  @overload(str)
  def selectNameFilter(self, filter: str) -> None:
    """
    Calls Qt's 'void QQuickFileDialogImpl::selectNameFilter(const QString
    &filter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimpl.html#selectNameFilter

    Parameters
    ----------

    filter : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickFileDialogImpl::selectNameFilter(const QString &filter)
    self.uglySide.call(
        'ritual_ZN20QQuickFileDialogImpl16selectNameFilterERK7QString',
        filter,
    )

  @overload(QUrl)
  def currentFolderChanged(self, folderUrl: QUrl) -> None:
    """
    Calls Qt's 'void QQuickFileDialogImpl::currentFolderChanged(const QUrl
    &folderUrl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimpl.html#currentFolderChanged

    Parameters
    ----------

    folderUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickFileDialogImpl::currentFolderChanged(const QUrl &folderUrl)
    self.uglySide.call(
        'ritual_ZN20QQuickFileDialogImpl20currentFolderChangedERK4QUrl',
        self._valueOf(folderUrl),
    )

  @overload(QUrl)
  def selectedFileChanged(self, selectedFileUrl: QUrl) -> None:
    """
    Calls Qt's 'void QQuickFileDialogImpl::selectedFileChanged(const QUrl
    &selectedFileUrl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimpl.html#selectedFileChanged

    Parameters
    ----------

    selectedFileUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickFileDialogImpl::selectedFileChanged(const QUrl
    #      &selectedFileUrl)
    self.uglySide.call(
        'ritual_ZN20QQuickFileDialogImpl19selectedFileChangedERK4QUrl',
        self._valueOf(selectedFileUrl),
    )

  def nameFiltersChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialogImpl::nameFiltersChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimpl.html#nameFiltersChanged
    """
    #  void QQuickFileDialogImpl::nameFiltersChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickFileDialogImpl18nameFiltersChangedEv',
    )

  @overload(QUrl)
  def fileSelected(self, fileUrl: QUrl) -> None:
    """
    Calls Qt's 'void QQuickFileDialogImpl::fileSelected(const QUrl
    &fileUrl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimpl.html#fileSelected

    Parameters
    ----------

    fileUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickFileDialogImpl::fileSelected(const QUrl &fileUrl)
    self.uglySide.call(
        'ritual_ZN20QQuickFileDialogImpl12fileSelectedERK4QUrl',
        self._valueOf(fileUrl),
    )

  @overload(str)
  def filterSelected(self, filter: str) -> None:
    """
    Calls Qt's 'void QQuickFileDialogImpl::filterSelected(const QString
    &filter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimpl.html#filterSelected

    Parameters
    ----------

    filter : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickFileDialogImpl::filterSelected(const QString &filter)
    self.uglySide.call(
        'ritual_ZN20QQuickFileDialogImpl14filterSelectedERK7QString', filter,
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialogImpl::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimpl.html#componentComplete
    """
    #  void QQuickFileDialogImpl::componentComplete()
    ritual = 'ritual_ZN20QQuickFileDialogImpl17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickFileDialogImpl17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      data: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickFileDialogImpl::itemChange(QQuickItem::ItemChange
    change, const QQuickItem::ItemChangeData &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimpl.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    data : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickFileDialogImpl::itemChange(QQuickItem::ItemChange change,
    #      const QQuickItem::ItemChangeData &data)
    ritual = (
        'ritual_ZN20QQuickFileDialogImpl10itemChangeEN10QQuickItem10ItemCha'
        'ngeERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickFileDialogImpl10itemChangeEN10QQuickItem10I'
          'temChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(data))

  def d_func(self) -> Optional[QQuickFileDialogImplPrivate]:
    """
    Calls Qt's 'QQuickFileDialogImplPrivate *QQuickFileDialogImpl::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfiledialogimpl.html#d_func

    Returns
    -------

    Optional[QQuickFileDialogImplPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFileDialogImplPrivate *QQuickFileDialogImpl::d_func()
    address = self.uglySide.call('ritual_ZN20QQuickFileDialogImpl6d_funcEv')
    from . import QQuickFileDialogImplPrivate
    return QQuickFileDialogImplPrivate._cuteAt(address)

  @staticmethod
  def options(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<QFileDialogOptions> QQuickFileDialogImpl::options()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickFileDialogImpl.options' has no cute function yet. Qt's "
        "'QSharedPointer<QFileDialogOptions> "
        "QQuickFileDialogImpl::options() const': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def setOptions(*__, **_) -> Never:
    """
    Qt's 'void QQuickFileDialogImpl::setOptions(const
    QSharedPointer<QFileDialogOptions> &options)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickFileDialogImpl.setOptions' has no cute function yet. Qt's "
        "'void QQuickFileDialogImpl::setOptions(const "
        "QSharedPointer<QFileDialogOptions> &options)': takes a type Python "
        "has no way to hand over yet.")
