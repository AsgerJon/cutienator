"""
QQmlTypeLoaderQmldirContent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmltypeloaderqmldircontent_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlTypeLoaderQmldirContent to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QUrl
  from . import QQmlError
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlError = WAIT['QQmlError']
  QUrl = WAIT['QUrl']


class QQmlTypeLoaderQmldirContent(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlTypeLoaderQmldirContent: a plain Python object
  standing in front of one C++ QQmlTypeLoaderQmldirContent.

  C++ hands a QQmlTypeLoaderQmldirContent around as a copy, so every C++
  QQmlTypeLoaderQmldirContent behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQmlTypeLoaderQmldirContent that has a ritual and
  that Python can call so far, 13 names in all: 'setContent', 'setError',
  'hasContent', 'hasError', 'errors', 'hasTypeNamespace', 'typeNamespace',
  'qmldirLocation', 'preferredPath', 'linkTarget', 'hasRedirection',
  'designerSupported', 'hasTypeInfo'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlTypeLoaderQmldirContent
    &QQmlTypeLoaderQmldirContent::operator=(const QQmlTypeLoaderQmldirContent
    &a0)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QQmlDirComponents QQmlTypeLoaderQmldirContent::components() const':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlDirScripts QQmlTypeLoaderQmldirContent::scripts() const': gives
    a type Python has no way to take yet.
  - Qt's 'QQmlDirPlugins QQmlTypeLoaderQmldirContent::plugins() const': gives
    a type Python has no way to take yet.
  - Qt's 'QQmlDirImports QQmlTypeLoaderQmldirContent::imports() const': gives
    a type Python has no way to take yet.
  - Qt's 'QQmlTypeLoaderQmldirContent::~QQmlTypeLoaderQmldirContent()': the
    destructor: Python removes its C++ QQmlTypeLoaderQmldirContent by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QQmlTypeLoaderQmldirContent is created at the first use, not by
    'QQmlTypeLoaderQmldirContent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlTypeLoaderQmldirContent back gives a copy the
    ritual made for Python, in a new cute QQmlTypeLoaderQmldirContent.
  - Each name of Qt's QQmlTypeLoaderQmldirContent that has no cute function
    yet, 'components', 'imports', 'plugins', 'scripts', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlTypeLoaderQmldirContent'

  #  Qt's '~QQmlTypeLoaderQmldirContent()'. Naming it makes this a value
  #  class: Python owns every C++ QQmlTypeLoaderQmldirContent behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN27QQmlTypeLoaderQmldirContentD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasContent(self) -> bool:
    """
    Calls Qt's 'bool QQmlTypeLoaderQmldirContent::hasContent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloaderqmldircontent.html#hasContent
    """
    #  bool QQmlTypeLoaderQmldirContent::hasContent() const
    return self.uglySide.call(
        'ritual_ZNK27QQmlTypeLoaderQmldirContent10hasContentEv',
    )

  def hasError(self) -> bool:
    """
    Calls Qt's 'bool QQmlTypeLoaderQmldirContent::hasError() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloaderqmldircontent.html#hasError
    """
    #  bool QQmlTypeLoaderQmldirContent::hasError() const
    return self.uglySide.call(
        'ritual_ZNK27QQmlTypeLoaderQmldirContent8hasErrorEv',
    )

  @overload(str, QUrl)
  def errors(self, uri: str, url: QUrl) -> QList[QQmlError]:
    """
    Calls Qt's 'QList<QQmlError> QQmlTypeLoaderQmldirContent::errors(const
    QString &uri, const QUrl &url) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloaderqmldircontent.html#errors

    Parameters
    ----------

    uri : str
      Passed on as it is: a QString is made of it for the call.

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QList[QQmlError]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQmlError> QQmlTypeLoaderQmldirContent::errors(const QString
    #      &uri, const QUrl &url) const
    address = self.uglySide.call(
        'ritual_ZNK27QQmlTypeLoaderQmldirContent6errorsERK7QStringRK4QUrl',
        uri, self._valueOf(url),
    )
    from . import QQmlError
    return QList[QQmlError]._cuteOwning(address)

  def hasTypeNamespace(self) -> bool:
    """
    Calls Qt's 'bool QQmlTypeLoaderQmldirContent::hasTypeNamespace() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloaderqmldircontent.html#hasTypeNamespace
    """
    #  bool QQmlTypeLoaderQmldirContent::hasTypeNamespace() const
    return self.uglySide.call(
        'ritual_ZNK27QQmlTypeLoaderQmldirContent16hasTypeNamespaceEv',
    )

  def typeNamespace(self) -> str:
    """
    Calls Qt's 'QString QQmlTypeLoaderQmldirContent::typeNamespace() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloaderqmldircontent.html#typeNamespace

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlTypeLoaderQmldirContent::typeNamespace() const
    return self.uglySide.call(
        'ritual_ZNK27QQmlTypeLoaderQmldirContent13typeNamespaceEv',
    )

  def qmldirLocation(self) -> str:
    """
    Calls Qt's 'QString QQmlTypeLoaderQmldirContent::qmldirLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloaderqmldircontent.html#qmldirLocation

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlTypeLoaderQmldirContent::qmldirLocation() const
    return self.uglySide.call(
        'ritual_ZNK27QQmlTypeLoaderQmldirContent14qmldirLocationEv',
    )

  def preferredPath(self) -> str:
    """
    Calls Qt's 'QString QQmlTypeLoaderQmldirContent::preferredPath() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloaderqmldircontent.html#preferredPath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlTypeLoaderQmldirContent::preferredPath() const
    return self.uglySide.call(
        'ritual_ZNK27QQmlTypeLoaderQmldirContent13preferredPathEv',
    )

  def linkTarget(self) -> str:
    """
    Calls Qt's 'QString QQmlTypeLoaderQmldirContent::linkTarget() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloaderqmldircontent.html#linkTarget

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlTypeLoaderQmldirContent::linkTarget() const
    return self.uglySide.call(
        'ritual_ZNK27QQmlTypeLoaderQmldirContent10linkTargetEv',
    )

  def hasRedirection(self) -> bool:
    """
    Calls Qt's 'bool QQmlTypeLoaderQmldirContent::hasRedirection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloaderqmldircontent.html#hasRedirection
    """
    #  bool QQmlTypeLoaderQmldirContent::hasRedirection() const
    return self.uglySide.call(
        'ritual_ZNK27QQmlTypeLoaderQmldirContent14hasRedirectionEv',
    )

  def designerSupported(self) -> bool:
    """
    Calls Qt's 'bool QQmlTypeLoaderQmldirContent::designerSupported() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloaderqmldircontent.html#designerSupported
    """
    #  bool QQmlTypeLoaderQmldirContent::designerSupported() const
    return self.uglySide.call(
        'ritual_ZNK27QQmlTypeLoaderQmldirContent17designerSupportedEv',
    )

  def hasTypeInfo(self) -> bool:
    """
    Calls Qt's 'bool QQmlTypeLoaderQmldirContent::hasTypeInfo() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloaderqmldircontent.html#hasTypeInfo
    """
    #  bool QQmlTypeLoaderQmldirContent::hasTypeInfo() const
    return self.uglySide.call(
        'ritual_ZNK27QQmlTypeLoaderQmldirContent11hasTypeInfoEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, str)
  def setContent(self, location: str, content: str) -> None:
    """
    Calls Qt's 'void QQmlTypeLoaderQmldirContent::setContent(const QString
    &location, const QString &content)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloaderqmldircontent.html#setContent

    Parameters
    ----------

    location : str
      Passed on as it is: a QString is made of it for the call.

    content : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlTypeLoaderQmldirContent::setContent(const QString &location,
    #      const QString &content)
    self.uglySide.call(
        'ritual_ZN27QQmlTypeLoaderQmldirContent10setContentERK7QStringS2_',
        location, content,
    )

  @overload(QQmlError)
  def setError(self, a0: QQmlError) -> None:
    """
    Calls Qt's 'void QQmlTypeLoaderQmldirContent::setError(const QQmlError
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloaderqmldircontent.html#setError

    Parameters
    ----------

    a0 : QQmlError
      Passed on as a value: Qt reads the C++ QQmlError, which stays Python's
      own.
    """
    #  void QQmlTypeLoaderQmldirContent::setError(const QQmlError &a0)
    self.uglySide.call(
        'ritual_ZN27QQmlTypeLoaderQmldirContent8setErrorERK9QQmlError',
        self._valueOf(a0),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQmlTypeLoaderQmldirContent::QQmlTypeLoaderQmldirContent()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloaderqmldircontent.html
    """
    #  QQmlTypeLoaderQmldirContent::QQmlTypeLoaderQmldirContent()
    self._noteCreation(QQmlTypeLoaderQmldirContent, lambda: Rituals.call(
        'ritual_ZN27QQmlTypeLoaderQmldirContentC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QQmlTypeLoaderQmldirContent) -> None:
    """
    Notes what was given, for Qt's
    'QQmlTypeLoaderQmldirContent::QQmlTypeLoaderQmldirContent(const
    QQmlTypeLoaderQmldirContent &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypeloaderqmldircontent.html

    Parameters
    ----------

    a0 : QQmlTypeLoaderQmldirContent
      Passed on as a value: Qt reads the C++ QQmlTypeLoaderQmldirContent,
      which stays Python's own.
    """
    #  QQmlTypeLoaderQmldirContent::QQmlTypeLoaderQmldirContent(const
    #      QQmlTypeLoaderQmldirContent &a0)
    self._noteCreation(QQmlTypeLoaderQmldirContent, lambda: Rituals.call(
        'ritual_ZN27QQmlTypeLoaderQmldirContentC1ERKS_', self._valueOf(a0),
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

  @staticmethod
  def components(*__, **_) -> Never:
    """
    Qt's 'QQmlDirComponents QQmlTypeLoaderQmldirContent::components() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlTypeLoaderQmldirContent.components' has no cute function yet. "
        "Qt's 'QQmlDirComponents QQmlTypeLoaderQmldirContent::components() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def imports(*__, **_) -> Never:
    """
    Qt's 'QQmlDirImports QQmlTypeLoaderQmldirContent::imports() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlTypeLoaderQmldirContent.imports' has no cute function yet. "
        "Qt's 'QQmlDirImports QQmlTypeLoaderQmldirContent::imports() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def plugins(*__, **_) -> Never:
    """
    Qt's 'QQmlDirPlugins QQmlTypeLoaderQmldirContent::plugins() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlTypeLoaderQmldirContent.plugins' has no cute function yet. "
        "Qt's 'QQmlDirPlugins QQmlTypeLoaderQmldirContent::plugins() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def scripts(*__, **_) -> Never:
    """
    Qt's 'QQmlDirScripts QQmlTypeLoaderQmldirContent::scripts() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlTypeLoaderQmldirContent.scripts' has no cute function yet. "
        "Qt's 'QQmlDirScripts QQmlTypeLoaderQmldirContent::scripts() "
        "const': gives a type Python has no way to take yet.")
