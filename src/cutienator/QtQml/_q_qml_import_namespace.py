"""
QQmlImportNamespace binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlimport_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlImportNamespace to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QTypeRevision
  from . import QQmlImportInstance
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTypeRevision = WAIT['QTypeRevision']


class QQmlImportNamespace(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlImportNamespace: a plain Python object standing
  in front of one C++ QQmlImportNamespace.

  C++ hands a QQmlImportNamespace around as a copy, so every C++
  QQmlImportNamespace behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlImportNamespace that has a ritual and that
  Python can call so far, 4 names in all: 'findImportByModuleUri',
  'findImportByLocation', 'needsSorting', 'setNeedsSorting'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlImportNamespace::~QQmlImportNamespace()': the destructor:
    Python removes its C++ QQmlImportNamespace by it, and has no other use
    for it.

  What has no ritual
  ------------------

  1 of the 7 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQmlImportNamespace is created at the first use, not by
    'QQmlImportNamespace(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlImportNamespace back gives a copy the ritual made
    for Python, in a new cute QQmlImportNamespace.
  - Each name of Qt's QQmlImportNamespace that has no cute function yet,
    'resolveType', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlImportNamespace'

  #  Qt's '~QQmlImportNamespace()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlImportNamespace behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QQmlImportNamespaceD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, QTypeRevision)
  def findImportByModuleUri(
      self,
      moduleUri: str,
      version: QTypeRevision,
  ) -> Optional[QQmlImportInstance]:
    """
    Calls Qt's 'QQmlImportInstance
    *QQmlImportNamespace::findImportByModuleUri(const QString &moduleUri,
    QTypeRevision version) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlimportnamespace.html#findImportByModuleUri

    Parameters
    ----------

    moduleUri : str
      Passed on as it is: a QString is made of it for the call.

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.

    Returns
    -------

    Optional[QQmlImportInstance]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlImportInstance *QQmlImportNamespace::findImportByModuleUri(const
    #      QString &moduleUri, QTypeRevision version) const
    address = self.uglySide.call(
        'ritual_ZNK19QQmlImportNamespace21findImportByModuleUriERK7QString1'
        '3QTypeRevision',
        moduleUri, self._valueOf(version),
    )
    from . import QQmlImportInstance
    return QQmlImportInstance._cuteAt(address)

  @overload(str, QTypeRevision)
  def findImportByLocation(
      self,
      location: str,
      version: QTypeRevision,
  ) -> Optional[QQmlImportInstance]:
    """
    Calls Qt's 'QQmlImportInstance
    *QQmlImportNamespace::findImportByLocation(const QString &location,
    QTypeRevision version) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlimportnamespace.html#findImportByLocation

    Parameters
    ----------

    location : str
      Passed on as it is: a QString is made of it for the call.

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.

    Returns
    -------

    Optional[QQmlImportInstance]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlImportInstance *QQmlImportNamespace::findImportByLocation(const
    #      QString &location, QTypeRevision version) const
    address = self.uglySide.call(
        'ritual_ZNK19QQmlImportNamespace20findImportByLocationERK7QString13'
        'QTypeRevision',
        location, self._valueOf(version),
    )
    from . import QQmlImportInstance
    return QQmlImportInstance._cuteAt(address)

  def needsSorting(self) -> bool:
    """
    Calls Qt's 'bool QQmlImportNamespace::needsSorting() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlimportnamespace.html#needsSorting
    """
    #  bool QQmlImportNamespace::needsSorting() const
    return self.uglySide.call(
        'ritual_ZNK19QQmlImportNamespace12needsSortingEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setNeedsSorting(self, needsSorting: bool) -> None:
    """
    Calls Qt's 'void QQmlImportNamespace::setNeedsSorting(bool
    needsSorting)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlimportnamespace.html#setNeedsSorting

    Parameters
    ----------

    needsSorting : bool
      Passed on as it is.
    """
    #  void QQmlImportNamespace::setNeedsSorting(bool needsSorting)
    self.uglySide.call(
        'ritual_ZN19QQmlImportNamespace15setNeedsSortingEb', needsSorting,
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
    'QQmlImportNamespace::QQmlImportNamespace()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlimportnamespace.html#QQmlImportNamespace
    """
    #  QQmlImportNamespace::QQmlImportNamespace()
    self._noteCreation(QQmlImportNamespace, lambda: Rituals.call(
        'ritual_ZN19QQmlImportNamespaceC1Ev',
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
  def resolveType(*__, **_) -> Never:
    """
    Qt's 'bool QQmlImportNamespace::resolveType(QQmlTypeLoader *typeLoader,
    const QHashedStringRef &type, QTypeRevision *version_return, QQmlType
    *type_return, const QString *base, QList<QQmlError> *errors,
    QQmlType::RegistrationType registrationType, bool
    *typeRecursionDeteced)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'qmlCheckTypes'.
    """
    raise NotImplementedError(
        "'QQmlImportNamespace.resolveType' has no cute function yet. Qt's "
        "'bool QQmlImportNamespace::resolveType(QQmlTypeLoader *typeLoader, "
        "const QHashedStringRef &type, QTypeRevision *version_return, "
        "QQmlType *type_return, const QString *base, QList<QQmlError> "
        "*errors, QQmlType::RegistrationType registrationType, bool "
        "*typeRecursionDeteced)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'qmlCheckTypes'.")
