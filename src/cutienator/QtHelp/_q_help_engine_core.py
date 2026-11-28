"""
QHelpEngineCore binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHelp/qhelpenginecore.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QUrl, QVariant
  from . import QHelpFilterEngine, QHelpLink
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHelpEngineCore(QObject):
  """
  The cute side of Qt's QHelpEngineCore: a plain Python object standing in
  front of one C++ QHelpEngineCore.

  It is built on the cute 'QObject', as Qt's QHelpEngineCore is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHelpEngineCore that has a ritual and that Python
  can call so far, 39 names in all: 'metaObject', 'tr', 'isReadOnly',
  'setReadOnly', 'filterEngine', 'setupData', 'collectionFile',
  'setCollectionFile', 'copyCollectionFile', 'namespaceName',
  'registerDocumentation', 'unregisterDocumentation',
  'documentationFileName', 'registeredDocumentations', 'fileData',
  'customFilters', 'removeCustomFilter', 'addCustomFilter',
  'filterAttributes', 'currentFilter', 'setCurrentFilter', 'files',
  'findFile', 'documentsForIdentifier', 'documentsForKeyword',
  'removeCustomValue', 'customValue', 'setCustomValue', 'metaData', 'error',
  'setAutoSaveFilter', 'autoSaveFilter', 'setUsesFilterEngine',
  'usesFilterEngine', 'setupStarted', 'setupFinished', 'warning',
  'currentFilterChanged', 'readersAboutToBeInvalidated'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHelpEngineCore::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QHelpEngineCore::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QHelpEngineCore::~QHelpEngineCore()': the destructor: Python never
    removes a C++ QHelpEngineCore.
  - Qt's 'QList<QStringList> QHelpEngineCore::filterAttributeSets(const
    QString &namespaceName) const': gives a type Python has no way to take
    yet.
  - Qt's 'QFuture<std::shared_ptr<QHelpContentItem>>
    QHelpEngineCore::requestContentForCurrentFilter() const': gives a type
    Python has no way to take yet.
  - Qt's 'QFuture<std::shared_ptr<QHelpContentItem>>
    QHelpEngineCore::requestContent(const QString &filter) const': gives a
    type Python has no way to take yet.
  - Qt's 'QFuture<QStringList>
    QHelpEngineCore::requestIndexForCurrentFilter() const': gives a type
    Python has no way to take yet.
  - Qt's 'QFuture<QStringList> QHelpEngineCore::requestIndex(const QString
    &filter) const': gives a type Python has no way to take yet.
  - Qt's 'QHelpEngineCore::QHelpEngineCore(QHelpEngineCorePrivate
    *helpEngineCorePrivate, QObject *parent)': names
    'QHelpEngineCorePrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 55 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QHelpEngineCore is created at the first use, not by
    'QHelpEngineCore(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHelpEngineCore.
  - Qt tells when it has removed the C++ QHelpEngineCore. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QHelpEngineCore that has no cute function yet,
    'filterAttributeSets', 'requestContent',
    'requestContentForCurrentFilter', 'requestIndex',
    'requestIndexForCurrentFilter', holds a function that raises
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
    Calls Qt's 'QString QHelpEngineCore::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpenginecore.html#tr

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
    #  QString QHelpEngineCore::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QHelpEngineCore2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(str)
  def namespaceName(documentationFileName: str) -> str:
    """
    Calls Qt's 'QString QHelpEngineCore::namespaceName(const QString
    &documentationFileName)'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpenginecore.html#namespaceName

    Parameters
    ----------

    documentationFileName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHelpEngineCore::namespaceName(const QString
    #      &documentationFileName)
    return Rituals.call(
        'ritual_ZN15QHelpEngineCore13namespaceNameERK7QString',
        documentationFileName,
    )

  @staticmethod
  @overload(str, str)
  def metaData(documentationFileName: str, name: str) -> QVariant:
    """
    Calls Qt's 'QVariant QHelpEngineCore::metaData(const QString
    &documentationFileName, const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpenginecore.html#metaData

    Parameters
    ----------

    documentationFileName : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QHelpEngineCore::metaData(const QString
    #      &documentationFileName, const QString &name)
    address = Rituals.call(
        'ritual_ZN15QHelpEngineCore8metaDataERK7QStringS2_',
        documentationFileName, name,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHelpEngineCore'

  #  A C++ QHelpEngineCore Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHelpEngineCore'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHelpEngineCore::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpenginecore.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHelpEngineCore::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QHelpEngineCore10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isReadOnly(self) -> bool:
    """
    Calls Qt's 'bool QHelpEngineCore::isReadOnly() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpenginecore.html#isReadOnly
    """
    #  bool QHelpEngineCore::isReadOnly() const
    return self.uglySide.call('ritual_ZNK15QHelpEngineCore10isReadOnlyEv')

  def filterEngine(self) -> Optional[QHelpFilterEngine]:
    """
    Calls Qt's 'QHelpFilterEngine *QHelpEngineCore::filterEngine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpenginecore.html#filterEngine

    Returns
    -------

    Optional[QHelpFilterEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHelpFilterEngine *QHelpEngineCore::filterEngine() const
    address = self.uglySide.call(
        'ritual_ZNK15QHelpEngineCore12filterEngineEv',
    )
    from . import QHelpFilterEngine
    return QHelpFilterEngine._cuteAt(address)

  def collectionFile(self) -> str:
    """
    Calls Qt's 'QString QHelpEngineCore::collectionFile() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpenginecore.html#collectionFile

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHelpEngineCore::collectionFile() const
    return self.uglySide.call(
        'ritual_ZNK15QHelpEngineCore14collectionFileEv',
    )

  def registeredDocumentations(self) -> QStringList:
    """
    Calls Qt's 'QStringList QHelpEngineCore::registeredDocumentations()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpenginecore.html#registeredDocumentations

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QHelpEngineCore::registeredDocumentations() const
    address = self.uglySide.call(
        'ritual_ZNK15QHelpEngineCore24registeredDocumentationsEv',
    )
    return QStringList._cuteOwning(address)

  @overload(QUrl)
  def fileData(self, url: QUrl) -> QByteArray:
    """
    Calls Qt's 'QByteArray QHelpEngineCore::fileData(const QUrl &url) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpenginecore.html#fileData

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QHelpEngineCore::fileData(const QUrl &url) const
    address = self.uglySide.call(
        'ritual_ZNK15QHelpEngineCore8fileDataERK4QUrl', self._valueOf(url),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def customFilters(self) -> QStringList:
    """
    Calls Qt's 'QStringList QHelpEngineCore::customFilters() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpenginecore.html#customFilters

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QHelpEngineCore::customFilters() const
    address = self.uglySide.call(
        'ritual_ZNK15QHelpEngineCore13customFiltersEv',
    )
    return QStringList._cuteOwning(address)

  @overload()
  def filterAttributes(self) -> QStringList:
    """
    Calls Qt's 'QStringList QHelpEngineCore::filterAttributes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpenginecore.html#filterAttributes

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QHelpEngineCore::filterAttributes() const
    address = self.uglySide.call(
        'ritual_ZNK15QHelpEngineCore16filterAttributesEv',
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def filterAttributes(self, filterName: str) -> QStringList:
    """
    Calls Qt's 'QStringList QHelpEngineCore::filterAttributes(const QString
    &filterName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpenginecore.html#filterAttributes

    Parameters
    ----------

    filterName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QHelpEngineCore::filterAttributes(const QString
    #      &filterName) const
    address = self.uglySide.call(
        'ritual_ZNK15QHelpEngineCore16filterAttributesERK7QString',
        filterName,
    )
    return QStringList._cuteOwning(address)

  def currentFilter(self) -> str:
    """
    Calls Qt's 'QString QHelpEngineCore::currentFilter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpenginecore.html#currentFilter

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHelpEngineCore::currentFilter() const
    return self.uglySide.call('ritual_ZNK15QHelpEngineCore13currentFilterEv')

  @overload(QUrl)
  def findFile(self, url: QUrl) -> QUrl:
    """
    Calls Qt's 'QUrl QHelpEngineCore::findFile(const QUrl &url) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpenginecore.html#findFile

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QHelpEngineCore::findFile(const QUrl &url) const
    address = self.uglySide.call(
        'ritual_ZNK15QHelpEngineCore8findFileERK4QUrl', self._valueOf(url),
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  @overload(str)
  def documentsForIdentifier(self, id: str) -> QList[QHelpLink]:
    """
    Calls Qt's 'QList<QHelpLink>
    QHelpEngineCore::documentsForIdentifier(const QString &id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpenginecore.html#documentsForIdentifier

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QList[QHelpLink]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QHelpLink> QHelpEngineCore::documentsForIdentifier(const QString
    #      &id) const
    address = self.uglySide.call(
        'ritual_ZNK15QHelpEngineCore22documentsForIdentifierERK7QString', id,
    )
    from . import QHelpLink
    return QList[QHelpLink]._cuteOwning(address)

  @overload(str, str)
  def documentsForIdentifier(
      self,
      id: str,
      filterName: str,
  ) -> QList[QHelpLink]:
    """
    Calls Qt's 'QList<QHelpLink>
    QHelpEngineCore::documentsForIdentifier(const QString &id, const QString
    &filterName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpenginecore.html#documentsForIdentifier

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    filterName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QList[QHelpLink]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QHelpLink> QHelpEngineCore::documentsForIdentifier(const QString
    #      &id, const QString &filterName) const
    address = self.uglySide.call(
        'ritual_ZNK15QHelpEngineCore22documentsForIdentifierERK7QStringS2_',
        id, filterName,
    )
    from . import QHelpLink
    return QList[QHelpLink]._cuteOwning(address)

  @overload(str)
  def documentsForKeyword(self, keyword: str) -> QList[QHelpLink]:
    """
    Calls Qt's 'QList<QHelpLink> QHelpEngineCore::documentsForKeyword(const
    QString &keyword) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpenginecore.html#documentsForKeyword

    Parameters
    ----------

    keyword : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QList[QHelpLink]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QHelpLink> QHelpEngineCore::documentsForKeyword(const QString
    #      &keyword) const
    address = self.uglySide.call(
        'ritual_ZNK15QHelpEngineCore19documentsForKeywordERK7QString',
        keyword,
    )
    from . import QHelpLink
    return QList[QHelpLink]._cuteOwning(address)

  @overload(str, str)
  def documentsForKeyword(
      self,
      keyword: str,
      filterName: str,
  ) -> QList[QHelpLink]:
    """
    Calls Qt's 'QList<QHelpLink> QHelpEngineCore::documentsForKeyword(const
    QString &keyword, const QString &filterName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpenginecore.html#documentsForKeyword

    Parameters
    ----------

    keyword : str
      Passed on as it is: a QString is made of it for the call.

    filterName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QList[QHelpLink]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QHelpLink> QHelpEngineCore::documentsForKeyword(const QString
    #      &keyword, const QString &filterName) const
    address = self.uglySide.call(
        'ritual_ZNK15QHelpEngineCore19documentsForKeywordERK7QStringS2_',
        keyword, filterName,
    )
    from . import QHelpLink
    return QList[QHelpLink]._cuteOwning(address)

  @overload(str)
  @overload(str, QVariant)
  def customValue(
      self,
      key: str,
      defaultValue: Optional[QVariant] = None,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QHelpEngineCore::customValue(const QString &key,
    const QVariant &defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpenginecore.html#customValue

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    defaultValue : Optional[QVariant]
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own. May be left out, as in Qt: a new 'QVariant()' is then passed on.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QHelpEngineCore::customValue(const QString &key, const
    #      QVariant &defaultValue) const
    if defaultValue is None:
      from ..QtCore import QVariant
      defaultValue = QVariant()
    address = self.uglySide.call(
        'ritual_ZNK15QHelpEngineCore11customValueERK7QStringRK8QVariant',
        key, self._valueOf(defaultValue),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def error(self) -> str:
    """
    Calls Qt's 'QString QHelpEngineCore::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpenginecore.html#error

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHelpEngineCore::error() const
    return self.uglySide.call('ritual_ZNK15QHelpEngineCore5errorEv')

  def autoSaveFilter(self) -> bool:
    """
    Calls Qt's 'bool QHelpEngineCore::autoSaveFilter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpenginecore.html#autoSaveFilter
    """
    #  bool QHelpEngineCore::autoSaveFilter() const
    return self.uglySide.call(
        'ritual_ZNK15QHelpEngineCore14autoSaveFilterEv',
    )

  def usesFilterEngine(self) -> bool:
    """
    Calls Qt's 'bool QHelpEngineCore::usesFilterEngine() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpenginecore.html#usesFilterEngine
    """
    #  bool QHelpEngineCore::usesFilterEngine() const
    return self.uglySide.call(
        'ritual_ZNK15QHelpEngineCore16usesFilterEngineEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setReadOnly(self, enable: bool) -> None:
    """
    Calls Qt's 'void QHelpEngineCore::setReadOnly(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpenginecore.html#setReadOnly

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QHelpEngineCore::setReadOnly(bool enable)
    self.uglySide.call('ritual_ZN15QHelpEngineCore11setReadOnlyEb', enable)

  @overload(str)
  def setCollectionFile(self, fileName: str) -> None:
    """
    Calls Qt's 'void QHelpEngineCore::setCollectionFile(const QString
    &fileName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpenginecore.html#setCollectionFile

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHelpEngineCore::setCollectionFile(const QString &fileName)
    self.uglySide.call(
        'ritual_ZN15QHelpEngineCore17setCollectionFileERK7QString', fileName,
    )

  @overload(str)
  def setCurrentFilter(self, filterName: str) -> None:
    """
    Calls Qt's 'void QHelpEngineCore::setCurrentFilter(const QString
    &filterName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpenginecore.html#setCurrentFilter

    Parameters
    ----------

    filterName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHelpEngineCore::setCurrentFilter(const QString &filterName)
    self.uglySide.call(
        'ritual_ZN15QHelpEngineCore16setCurrentFilterERK7QString',
        filterName,
    )

  @overload(str, QVariant)
  def setCustomValue(self, key: str, value: QVariant) -> bool:
    """
    Calls Qt's 'bool QHelpEngineCore::setCustomValue(const QString &key,
    const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpenginecore.html#setCustomValue

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QHelpEngineCore::setCustomValue(const QString &key, const
    #      QVariant &value)
    return self.uglySide.call(
        'ritual_ZN15QHelpEngineCore14setCustomValueERK7QStringRK8QVariant',
        key, self._valueOf(value),
    )

  @overload(bool)
  def setAutoSaveFilter(self, save: bool) -> None:
    """
    Calls Qt's 'void QHelpEngineCore::setAutoSaveFilter(bool save)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpenginecore.html#setAutoSaveFilter

    Parameters
    ----------

    save : bool
      Passed on as it is.
    """
    #  void QHelpEngineCore::setAutoSaveFilter(bool save)
    self.uglySide.call(
        'ritual_ZN15QHelpEngineCore17setAutoSaveFilterEb', save,
    )

  @overload(bool)
  def setUsesFilterEngine(self, uses: bool) -> None:
    """
    Calls Qt's 'void QHelpEngineCore::setUsesFilterEngine(bool uses)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpenginecore.html#setUsesFilterEngine

    Parameters
    ----------

    uses : bool
      Passed on as it is.
    """
    #  void QHelpEngineCore::setUsesFilterEngine(bool uses)
    self.uglySide.call(
        'ritual_ZN15QHelpEngineCore19setUsesFilterEngineEb', uses,
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

  @overload(str)
  @overload(str, QObject)
  @overload(str, NoneType)
  def __init__(
      self,
      collectionFile: str,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QHelpEngineCore::QHelpEngineCore(const
    QString &collectionFile, QObject *parent)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpenginecore.html#QHelpEngineCore

    Parameters
    ----------

    collectionFile : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QHelpEngineCore::QHelpEngineCore(const QString &collectionFile,
    #      QObject *parent)
    self._noteCreation(QHelpEngineCore, lambda: Rituals.call(
        'ritual_ZN15QHelpEngineCoreC1ERK7QStringP7QObject',
        collectionFile, self._addressOf(parent, 'QObject'),
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

  def setupData(self) -> bool:
    """
    Calls Qt's 'bool QHelpEngineCore::setupData()'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpenginecore.html#setupData
    """
    #  bool QHelpEngineCore::setupData()
    return self.uglySide.call('ritual_ZN15QHelpEngineCore9setupDataEv')

  @overload(str)
  def copyCollectionFile(self, fileName: str) -> bool:
    """
    Calls Qt's 'bool QHelpEngineCore::copyCollectionFile(const QString
    &fileName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpenginecore.html#copyCollectionFile

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QHelpEngineCore::copyCollectionFile(const QString &fileName)
    return self.uglySide.call(
        'ritual_ZN15QHelpEngineCore18copyCollectionFileERK7QString',
        fileName,
    )

  @overload(str)
  def registerDocumentation(self, documentationFileName: str) -> bool:
    """
    Calls Qt's 'bool QHelpEngineCore::registerDocumentation(const QString
    &documentationFileName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpenginecore.html#registerDocumentation

    Parameters
    ----------

    documentationFileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QHelpEngineCore::registerDocumentation(const QString
    #      &documentationFileName)
    return self.uglySide.call(
        'ritual_ZN15QHelpEngineCore21registerDocumentationERK7QString',
        documentationFileName,
    )

  @overload(str)
  def unregisterDocumentation(self, namespaceName: str) -> bool:
    """
    Calls Qt's 'bool QHelpEngineCore::unregisterDocumentation(const QString
    &namespaceName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpenginecore.html#unregisterDocumentation

    Parameters
    ----------

    namespaceName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QHelpEngineCore::unregisterDocumentation(const QString
    #      &namespaceName)
    return self.uglySide.call(
        'ritual_ZN15QHelpEngineCore23unregisterDocumentationERK7QString',
        namespaceName,
    )

  @overload(str)
  def documentationFileName(self, namespaceName: str) -> str:
    """
    Calls Qt's 'QString QHelpEngineCore::documentationFileName(const QString
    &namespaceName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpenginecore.html#documentationFileName

    Parameters
    ----------

    namespaceName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHelpEngineCore::documentationFileName(const QString
    #      &namespaceName)
    return self.uglySide.call(
        'ritual_ZN15QHelpEngineCore21documentationFileNameERK7QString',
        namespaceName,
    )

  @overload(str)
  def removeCustomFilter(self, filterName: str) -> bool:
    """
    Calls Qt's 'bool QHelpEngineCore::removeCustomFilter(const QString
    &filterName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpenginecore.html#removeCustomFilter

    Parameters
    ----------

    filterName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QHelpEngineCore::removeCustomFilter(const QString &filterName)
    return self.uglySide.call(
        'ritual_ZN15QHelpEngineCore18removeCustomFilterERK7QString',
        filterName,
    )

  @overload(str, QStringList)
  def addCustomFilter(
      self,
      filterName: str,
      attributes: QStringList,
  ) -> bool:
    """
    Calls Qt's 'bool QHelpEngineCore::addCustomFilter(const QString
    &filterName, const QStringList &attributes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpenginecore.html#addCustomFilter

    Parameters
    ----------

    filterName : str
      Passed on as it is: a QString is made of it for the call.

    attributes : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QHelpEngineCore::addCustomFilter(const QString &filterName, const
    #      QStringList &attributes)
    return self.uglySide.call(
        'ritual_ZN15QHelpEngineCore15addCustomFilterERK7QStringRK5QListIS0_'
        'E',
        filterName, self._valueOf(attributes),
    )

  @overload(str, QStringList)
  @overload(str, QStringList, str)
  def files(
      self,
      namespaceName: str,
      filterAttributes: QStringList,
      extensionFilter: str = '',
  ) -> QList[QUrl]:
    """
    Calls Qt's 'QList<QUrl> QHelpEngineCore::files(const QString
    namespaceName, const QStringList &filterAttributes, const QString
    &extensionFilter)'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpenginecore.html#files

    Parameters
    ----------

    namespaceName : str
      Passed on as it is: a QString is made of it for the call.

    filterAttributes : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    extensionFilter : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    QList[QUrl]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QUrl> QHelpEngineCore::files(const QString namespaceName, const
    #      QStringList &filterAttributes, const QString &extensionFilter)
    address = self.uglySide.call(
        'ritual_ZN15QHelpEngineCore5filesE7QStringRK5QListIS0_ERKS0_',
        namespaceName, self._valueOf(filterAttributes), extensionFilter,
    )
    from ..QtCore import QUrl
    return QList[QUrl]._cuteOwning(address)

  @overload(str, str)
  @overload(str, str, str)
  def files(
      self,
      namespaceName: str,
      filterName: str,
      extensionFilter: str = '',
  ) -> QList[QUrl]:
    """
    Calls Qt's 'QList<QUrl> QHelpEngineCore::files(const QString
    namespaceName, const QString &filterName, const QString
    &extensionFilter)'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpenginecore.html#files

    Parameters
    ----------

    namespaceName : str
      Passed on as it is: a QString is made of it for the call.

    filterName : str
      Passed on as it is: a QString is made of it for the call.

    extensionFilter : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    QList[QUrl]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QUrl> QHelpEngineCore::files(const QString namespaceName, const
    #      QString &filterName, const QString &extensionFilter)
    address = self.uglySide.call(
        'ritual_ZN15QHelpEngineCore5filesE7QStringRKS0_S2_',
        namespaceName, filterName, extensionFilter,
    )
    from ..QtCore import QUrl
    return QList[QUrl]._cuteOwning(address)

  @overload(str)
  def removeCustomValue(self, key: str) -> bool:
    """
    Calls Qt's 'bool QHelpEngineCore::removeCustomValue(const QString &key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpenginecore.html#removeCustomValue

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QHelpEngineCore::removeCustomValue(const QString &key)
    return self.uglySide.call(
        'ritual_ZN15QHelpEngineCore17removeCustomValueERK7QString', key,
    )

  def setupStarted(self) -> None:
    """
    Calls Qt's 'void QHelpEngineCore::setupStarted()'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpenginecore.html#setupStarted
    """
    #  void QHelpEngineCore::setupStarted()
    self.uglySide.call('ritual_ZN15QHelpEngineCore12setupStartedEv')

  def setupFinished(self) -> None:
    """
    Calls Qt's 'void QHelpEngineCore::setupFinished()'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpenginecore.html#setupFinished
    """
    #  void QHelpEngineCore::setupFinished()
    self.uglySide.call('ritual_ZN15QHelpEngineCore13setupFinishedEv')

  @overload(str)
  def warning(self, msg: str) -> None:
    """
    Calls Qt's 'void QHelpEngineCore::warning(const QString &msg)'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpenginecore.html#warning

    Parameters
    ----------

    msg : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHelpEngineCore::warning(const QString &msg)
    self.uglySide.call('ritual_ZN15QHelpEngineCore7warningERK7QString', msg)

  @overload(str)
  def currentFilterChanged(self, newFilter: str) -> None:
    """
    Calls Qt's 'void QHelpEngineCore::currentFilterChanged(const QString
    &newFilter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpenginecore.html#currentFilterChanged

    Parameters
    ----------

    newFilter : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHelpEngineCore::currentFilterChanged(const QString &newFilter)
    self.uglySide.call(
        'ritual_ZN15QHelpEngineCore20currentFilterChangedERK7QString',
        newFilter,
    )

  def readersAboutToBeInvalidated(self) -> None:
    """
    Calls Qt's 'void QHelpEngineCore::readersAboutToBeInvalidated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpenginecore.html#readersAboutToBeInvalidated
    """
    #  void QHelpEngineCore::readersAboutToBeInvalidated()
    self.uglySide.call(
        'ritual_ZN15QHelpEngineCore27readersAboutToBeInvalidatedEv',
    )

  @staticmethod
  def filterAttributeSets(*__, **_) -> Never:
    """
    Qt's 'QList<QStringList> QHelpEngineCore::filterAttributeSets(const
    QString &namespaceName) const': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QHelpEngineCore.filterAttributeSets' has no cute function yet. "
        "Qt's 'QList<QStringList> "
        "QHelpEngineCore::filterAttributeSets(const QString &namespaceName) "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def requestContent(*__, **_) -> Never:
    """
    Qt's 'QFuture<std::shared_ptr<QHelpContentItem>>
    QHelpEngineCore::requestContent(const QString &filter) const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QHelpEngineCore.requestContent' has no cute function yet. Qt's "
        "'QFuture<std::shared_ptr<QHelpContentItem>> "
        "QHelpEngineCore::requestContent(const QString &filter) const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def requestContentForCurrentFilter(*__, **_) -> Never:
    """
    Qt's 'QFuture<std::shared_ptr<QHelpContentItem>>
    QHelpEngineCore::requestContentForCurrentFilter() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QHelpEngineCore.requestContentForCurrentFilter' has no cute "
        "function yet. Qt's 'QFuture<std::shared_ptr<QHelpContentItem>> "
        "QHelpEngineCore::requestContentForCurrentFilter() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def requestIndex(*__, **_) -> Never:
    """
    Qt's 'QFuture<QStringList> QHelpEngineCore::requestIndex(const QString
    &filter) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QHelpEngineCore.requestIndex' has no cute function yet. Qt's "
        "'QFuture<QStringList> QHelpEngineCore::requestIndex(const QString "
        "&filter) const': gives a type Python has no way to take yet.")

  @staticmethod
  def requestIndexForCurrentFilter(*__, **_) -> Never:
    """
    Qt's 'QFuture<QStringList>
    QHelpEngineCore::requestIndexForCurrentFilter() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QHelpEngineCore.requestIndexForCurrentFilter' has no cute "
        "function yet. Qt's 'QFuture<QStringList> "
        "QHelpEngineCore::requestIndexForCurrentFilter() const': gives a "
        "type Python has no way to take yet.")
