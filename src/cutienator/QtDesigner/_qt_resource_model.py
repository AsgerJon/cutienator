"""
QtResourceModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qtresourcemodel_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QtResourceModel to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QtResourceSet
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QtResourceSet = WAIT['QtResourceSet']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QtResourceModel(QObject):
  """
  The cute side of Qt's QtResourceModel: a plain Python object standing in
  front of one C++ QtResourceModel.

  It is built on the cute 'QObject', as Qt's QtResourceModel is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtResourceModel that has a ritual and that Python
  can call so far, 14 names in all: 'metaObject', 'tr', 'loadedQrcFiles',
  'isModified', 'setModified', 'resourceSets', 'currentResourceSet',
  'addResourceSet', 'removeResourceSet', 'qrcPath', 'setWatcherEnabled',
  'isWatcherEnabled', 'resourceSetActivated', 'qrcFileModifiedExternally'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtResourceModel::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QtResourceModel::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QtResourceModel::~QtResourceModel()': the destructor: Python never
    removes a C++ QtResourceModel.
  - Qt's 'void QtResourceModel::setCurrentResourceSet(QtResourceSet
    *resourceSet, int *errorCount, QString *errorMessages)': takes a number
    to change where it is.
  - Qt's 'void QtResourceModel::reload(const QString &path, int *errorCount,
    QString *errorMessages)': takes a number to change where it is.
  - Qt's 'void QtResourceModel::reload(int *errorCount, QString
    *errorMessages)': takes a number to change where it is.
  - Qt's 'QMap<QString, QString> QtResourceModel::contents() const': gives a
    type Python has no way to take yet.
  - Qt's 'QtResourceModelPrivate *QtResourceModel::d_func()': gives
    'QtResourceModelPrivate', which has no cute class yet.
  - Qt's 'const QtResourceModelPrivate *QtResourceModel::d_func() const':
    gives 'QtResourceModelPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  6 of the 32 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QtResourceModel is created at the first use, not by
    'QtResourceModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtResourceModel.
  - Qt tells when it has removed the C++ QtResourceModel. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QtResourceModel that has no cute function yet,
    'contents', 'reload', 'setCurrentResourceSet', holds a function that
    raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QtResourceModel::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtresourcemodel.html#tr

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
    #  QString QtResourceModel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QtResourceModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtResourceModel'

  #  A C++ QtResourceModel Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtResourceModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QtResourceModel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtresourcemodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtResourceModel::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QtResourceModel10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def loadedQrcFiles(self) -> QStringList:
    """
    Calls Qt's 'QStringList QtResourceModel::loadedQrcFiles() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtresourcemodel.html#loadedQrcFiles

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QtResourceModel::loadedQrcFiles() const
    address = self.uglySide.call(
        'ritual_ZNK15QtResourceModel14loadedQrcFilesEv',
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def isModified(self, path: str) -> bool:
    """
    Calls Qt's 'bool QtResourceModel::isModified(const QString &path) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtresourcemodel.html#isModified

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QtResourceModel::isModified(const QString &path) const
    return self.uglySide.call(
        'ritual_ZNK15QtResourceModel10isModifiedERK7QString', path,
    )

  def resourceSets(self) -> QList[QtResourceSet]:
    """
    Calls Qt's 'QList<QtResourceSet *> QtResourceModel::resourceSets()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtresourcemodel.html#resourceSets

    Returns
    -------

    QList[QtResourceSet]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QtResourceSet *> QtResourceModel::resourceSets() const
    address = self.uglySide.call(
        'ritual_ZNK15QtResourceModel12resourceSetsEv',
    )
    from . import QtResourceSet
    return QList[QtResourceSet]._cuteOwning(address)

  def currentResourceSet(self) -> Optional[QtResourceSet]:
    """
    Calls Qt's 'QtResourceSet *QtResourceModel::currentResourceSet() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtresourcemodel.html#currentResourceSet

    Returns
    -------

    Optional[QtResourceSet]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QtResourceSet *QtResourceModel::currentResourceSet() const
    address = self.uglySide.call(
        'ritual_ZNK15QtResourceModel18currentResourceSetEv',
    )
    from . import QtResourceSet
    return QtResourceSet._cuteAt(address)

  @overload(str)
  def qrcPath(self, file: str) -> str:
    """
    Calls Qt's 'QString QtResourceModel::qrcPath(const QString &file) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtresourcemodel.html#qrcPath

    Parameters
    ----------

    file : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtResourceModel::qrcPath(const QString &file) const
    return self.uglySide.call(
        'ritual_ZNK15QtResourceModel7qrcPathERK7QString', file,
    )

  @overload()
  def isWatcherEnabled(self) -> bool:
    """
    Calls Qt's 'bool QtResourceModel::isWatcherEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtresourcemodel.html#isWatcherEnabled
    """
    #  bool QtResourceModel::isWatcherEnabled() const
    return self.uglySide.call(
        'ritual_ZNK15QtResourceModel16isWatcherEnabledEv',
    )

  @overload(str)
  def isWatcherEnabled(self, path: str) -> bool:
    """
    Calls Qt's 'bool QtResourceModel::isWatcherEnabled(const QString &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtresourcemodel.html#isWatcherEnabled

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QtResourceModel::isWatcherEnabled(const QString &path)
    return self.uglySide.call(
        'ritual_ZN15QtResourceModel16isWatcherEnabledERK7QString', path,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setModified(self, path: str) -> None:
    """
    Calls Qt's 'void QtResourceModel::setModified(const QString &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qtresourcemodel.html#setModified

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QtResourceModel::setModified(const QString &path)
    self.uglySide.call(
        'ritual_ZN15QtResourceModel11setModifiedERK7QString', path,
    )

  @overload(bool)
  def setWatcherEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QtResourceModel::setWatcherEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtresourcemodel.html#setWatcherEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QtResourceModel::setWatcherEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN15QtResourceModel17setWatcherEnabledEb', enable,
    )

  @overload(str, bool)
  def setWatcherEnabled(self, path: str, enable: bool) -> None:
    """
    Calls Qt's 'void QtResourceModel::setWatcherEnabled(const QString &path,
    bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtresourcemodel.html#setWatcherEnabled

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    enable : bool
      Passed on as it is.
    """
    #  void QtResourceModel::setWatcherEnabled(const QString &path, bool
    #      enable)
    self.uglySide.call(
        'ritual_ZN15QtResourceModel17setWatcherEnabledERK7QStringb',
        path, enable,
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
    Notes what was given, for Qt's 'QtResourceModel::QtResourceModel(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtresourcemodel.html#QtResourceModel

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QtResourceModel::QtResourceModel(QObject *parent)
    self._noteCreation(QtResourceModel, lambda: Rituals.call(
        'ritual_ZN15QtResourceModelC1EP7QObject',
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

  @overload(QStringList)
  def addResourceSet(self, paths: QStringList) -> Optional[QtResourceSet]:
    """
    Calls Qt's 'QtResourceSet *QtResourceModel::addResourceSet(const
    QStringList &paths)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtresourcemodel.html#addResourceSet

    Parameters
    ----------

    paths : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    Optional[QtResourceSet]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QtResourceSet *QtResourceModel::addResourceSet(const QStringList
    #      &paths)
    address = self.uglySide.call(
        'ritual_ZN15QtResourceModel14addResourceSetERK5QListI7QStringE',
        self._valueOf(paths),
    )
    from . import QtResourceSet
    return QtResourceSet._cuteAt(address)

  @overload(QtResourceSet)
  @overload(NoneType)
  def removeResourceSet(self, resourceSet: Optional[QtResourceSet]) -> None:
    """
    Calls Qt's 'void QtResourceModel::removeResourceSet(QtResourceSet
    *resourceSet)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtresourcemodel.html#removeResourceSet

    Parameters
    ----------

    resourceSet : Optional[QtResourceSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtResourceModel::removeResourceSet(QtResourceSet *resourceSet)
    self.uglySide.call(
        'ritual_ZN15QtResourceModel17removeResourceSetEP13QtResourceSet',
        self._addressOf(resourceSet),
    )

  @overload(QtResourceSet, bool)
  @overload(NoneType, bool)
  def resourceSetActivated(
      self,
      resourceSet: Optional[QtResourceSet],
      resourceSetChanged: bool,
  ) -> None:
    """
    Calls Qt's 'void QtResourceModel::resourceSetActivated(QtResourceSet
    *resourceSet, bool resourceSetChanged)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtresourcemodel.html#resourceSetActivated

    Parameters
    ----------

    resourceSet : Optional[QtResourceSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resourceSetChanged : bool
      Passed on as it is.
    """
    #  void QtResourceModel::resourceSetActivated(QtResourceSet *resourceSet,
    #      bool resourceSetChanged)
    self.uglySide.call(
        'ritual_ZN15QtResourceModel20resourceSetActivatedEP13QtResourceSetb',
        self._addressOf(resourceSet), resourceSetChanged,
    )

  @overload(str)
  def qrcFileModifiedExternally(self, path: str) -> None:
    """
    Calls Qt's 'void QtResourceModel::qrcFileModifiedExternally(const QString
    &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtresourcemodel.html#qrcFileModifiedExternally

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QtResourceModel::qrcFileModifiedExternally(const QString &path)
    self.uglySide.call(
        'ritual_ZN15QtResourceModel25qrcFileModifiedExternallyERK7QString',
        path,
    )

  @staticmethod
  def contents(*__, **_) -> Never:
    """
    Qt's 'QMap<QString, QString> QtResourceModel::contents() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtResourceModel.contents' has no cute function yet. Qt's "
        "'QMap<QString, QString> QtResourceModel::contents() const': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def reload(*__, **_) -> Never:
    """
    - Qt's 'void QtResourceModel::reload(const QString &path, int
      *errorCount, QString *errorMessages)': takes a number to change where
      it is.
    - Qt's 'void QtResourceModel::reload(int *errorCount, QString
      *errorMessages)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QtResourceModel.reload' has no cute function yet. Qt's 'void "
        "QtResourceModel::reload(const QString &path, int *errorCount, "
        "QString *errorMessages)': takes a number to change where it is. "
        "Qt's 'void QtResourceModel::reload(int *errorCount, QString "
        "*errorMessages)': takes a number to change where it is.")

  @staticmethod
  def setCurrentResourceSet(*__, **_) -> Never:
    """
    Qt's 'void QtResourceModel::setCurrentResourceSet(QtResourceSet
    *resourceSet, int *errorCount, QString *errorMessages)': takes a number
    to change where it is.
    """
    raise NotImplementedError(
        "'QtResourceModel.setCurrentResourceSet' has no cute function yet. "
        "Qt's 'void QtResourceModel::setCurrentResourceSet(QtResourceSet "
        "*resourceSet, int *errorCount, QString *errorMessages)': takes a "
        "number to change where it is.")
