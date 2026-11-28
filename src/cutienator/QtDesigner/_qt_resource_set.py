"""
QtResourceSet binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qtresourcemodel_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QtResourceSet to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QtResourceModel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QtResourceModel = WAIT['QtResourceModel']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QtResourceSet(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtResourceSet: a plain Python object standing in
  front of one C++ QtResourceSet.

  What exists
  -----------

  Every function of Qt's QtResourceSet that has a ritual and that Python can
  call so far, 3 names in all: 'activeResourceFilePaths', 'isModified',
  'setModified'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QtResourceSet::activateResourceFilePaths(const QStringList
    &paths, int *errorCount, QString *errorMessages)': takes a number to
    change where it is.
  - Qt's 'QtResourceSet::~QtResourceSet()': the destructor: Python never
    removes a C++ QtResourceSet.
  - Qt's 'QtResourceSetPrivate *QtResourceSet::d_func()': gives
    'QtResourceSetPrivate', which has no cute class yet.
  - Qt's 'const QtResourceSetPrivate *QtResourceSet::d_func() const': gives
    'QtResourceSetPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 13 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QtResourceSet is created at the first use, not by
    'QtResourceSet(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtResourceSet.
  - Each name of Qt's QtResourceSet that has no cute function yet,
    'activateResourceFilePaths', 'd_func', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtResourceSet'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def activeResourceFilePaths(self) -> QStringList:
    """
    Calls Qt's 'QStringList QtResourceSet::activeResourceFilePaths() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtresourceset.html#activeResourceFilePaths

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QtResourceSet::activeResourceFilePaths() const
    address = self.uglySide.call(
        'ritual_ZNK13QtResourceSet23activeResourceFilePathsEv',
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def isModified(self, path: str) -> bool:
    """
    Calls Qt's 'bool QtResourceSet::isModified(const QString &path) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtresourceset.html#isModified

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QtResourceSet::isModified(const QString &path) const
    return self.uglySide.call(
        'ritual_ZNK13QtResourceSet10isModifiedERK7QString', path,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setModified(self, path: str) -> None:
    """
    Calls Qt's 'void QtResourceSet::setModified(const QString &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qtresourceset.html#setModified

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QtResourceSet::setModified(const QString &path)
    self.uglySide.call(
        'ritual_ZN13QtResourceSet11setModifiedERK7QString', path,
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
    Notes what was given, for Qt's 'QtResourceSet::QtResourceSet()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtresourceset.html#QtResourceSet
    """
    #  QtResourceSet::QtResourceSet()
    self._noteCreation(QtResourceSet, lambda: Rituals.call(
        'ritual_ZN13QtResourceSetC1Ev',
    ))

  @overload(QtResourceModel)
  @overload(NoneType)
  def __init__(self, model: Optional[QtResourceModel]) -> None:
    """
    Notes what was given, for Qt's
    'QtResourceSet::QtResourceSet(QtResourceModel *model)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtresourceset.html#QtResourceSet

    Parameters
    ----------

    model : Optional[QtResourceModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QtResourceSet::QtResourceSet(QtResourceModel *model)
    self._noteCreation(QtResourceSet, lambda: Rituals.call(
        'ritual_ZN13QtResourceSetC1EP15QtResourceModel',
        self._addressOf(model),
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
  def activateResourceFilePaths(*__, **_) -> Never:
    """
    Qt's 'void QtResourceSet::activateResourceFilePaths(const QStringList
    &paths, int *errorCount, QString *errorMessages)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QtResourceSet.activateResourceFilePaths' has no cute function "
        "yet. Qt's 'void QtResourceSet::activateResourceFilePaths(const "
        "QStringList &paths, int *errorCount, QString *errorMessages)': "
        "takes a number to change where it is.")

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QtResourceSetPrivate *QtResourceSet::d_func()': gives
      'QtResourceSetPrivate', which has no cute class yet.
    - Qt's 'const QtResourceSetPrivate *QtResourceSet::d_func() const': gives
      'QtResourceSetPrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QtResourceSet.d_func' has no cute function yet. Qt's "
        "'QtResourceSetPrivate *QtResourceSet::d_func()': gives "
        "'QtResourceSetPrivate', which has no cute class yet. Qt's 'const "
        "QtResourceSetPrivate *QtResourceSet::d_func() const': gives "
        "'QtResourceSetPrivate', which has no cute class yet.")


#  Qt's 'QList<QtResourceSet *>': the list of QtResourceSet, which
#  'QList[QtResourceSet]' gives. It is made here, so that there is one as
#  soon as there can be a QtResourceSet.
QList.createKind(
    QtResourceSet, 'address',
    make='ritual_list_make_QtResourceSet_ptr',
    add='ritual_list_add_QtResourceSet_ptr',
    size='ritual_list_size_QtResourceSet_ptr',
    at='ritual_list_at_QtResourceSet_ptr',
    drop='ritual_list_drop_QtResourceSet_ptr',
)
