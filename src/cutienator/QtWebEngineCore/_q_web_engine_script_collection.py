"""
QWebEngineScriptCollection binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebenginescriptcollection.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QWebEngineScript
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWebEngineScript = WAIT['QWebEngineScript']


class QWebEngineScriptCollection(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebEngineScriptCollection: a plain Python object
  standing in front of one C++ QWebEngineScriptCollection.

  What exists
  -----------

  Every function of Qt's QWebEngineScriptCollection that has a ritual and
  that Python can call so far, 8 names in all: 'isEmpty', 'count',
  'contains', 'find', 'insert', 'remove', 'clear', 'toList'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWebEngineScriptCollection::~QWebEngineScriptCollection()': the
    destructor: Python never removes a C++ QWebEngineScriptCollection.
  - Qt's 'QWebEngineScriptCollection::QWebEngineScriptCollection(
    QWebEngineScriptCollectionPrivate *a0)': names
    'QWebEngineScriptCollectionPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QWebEngineScriptCollection is created at the first use, not by
    'QWebEngineScriptCollection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebEngineScriptCollection.
  - Each name of Qt's QWebEngineScriptCollection that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
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
  __qt_class__ = 'QWebEngineScriptCollection'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineScriptCollection::isEmpty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginescriptcollection.html#isEmpty
    """
    #  bool QWebEngineScriptCollection::isEmpty() const
    return self.uglySide.call(
        'ritual_ZNK26QWebEngineScriptCollection7isEmptyEv',
    )

  def count(self) -> int:
    """
    Calls Qt's 'int QWebEngineScriptCollection::count() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginescriptcollection.html#count
    """
    #  int QWebEngineScriptCollection::count() const
    return self.uglySide.call(
        'ritual_ZNK26QWebEngineScriptCollection5countEv',
    )

  @overload(QWebEngineScript)
  def contains(self, value: QWebEngineScript) -> bool:
    """
    Calls Qt's 'bool QWebEngineScriptCollection::contains(const
    QWebEngineScript &value) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginescriptcollection.html#contains

    Parameters
    ----------

    value : QWebEngineScript
      Passed on as a value: Qt reads the C++ QWebEngineScript, which stays
      Python's own.
    """
    #  bool QWebEngineScriptCollection::contains(const QWebEngineScript
    #      &value) const
    return self.uglySide.call(
        'ritual_ZNK26QWebEngineScriptCollection8containsERK16QWebEngineScri'
        'pt',
        self._valueOf(value),
    )

  @overload(str)
  def find(self, name: str) -> QList[QWebEngineScript]:
    """
    Calls Qt's 'QList<QWebEngineScript>
    QWebEngineScriptCollection::find(const QString &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginescriptcollection.html#find

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QList[QWebEngineScript]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QWebEngineScript> QWebEngineScriptCollection::find(const QString
    #      &name) const
    address = self.uglySide.call(
        'ritual_ZNK26QWebEngineScriptCollection4findERK7QString', name,
    )
    from . import QWebEngineScript
    return QList[QWebEngineScript]._cuteOwning(address)

  def toList(self) -> QList[QWebEngineScript]:
    """
    Calls Qt's 'QList<QWebEngineScript> QWebEngineScriptCollection::toList()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginescriptcollection.html#toList

    Returns
    -------

    QList[QWebEngineScript]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QWebEngineScript> QWebEngineScriptCollection::toList() const
    address = self.uglySide.call(
        'ritual_ZNK26QWebEngineScriptCollection6toListEv',
    )
    from . import QWebEngineScript
    return QList[QWebEngineScript]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QWebEngineScriptCollection::QWebEngineScriptCollection(
    QWebEngineScriptCollectionPrivate *a0)': names
    'QWebEngineScriptCollectionPrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWebEngineScriptCollection.__init__' has no cute function yet. "
        "Qt's "
        "'QWebEngineScriptCollection::QWebEngineScriptCollection(QWebEngineS"
        "criptCollectionPrivate *a0)': names "
        "'QWebEngineScriptCollectionPrivate', which has no cute class yet.")

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

  @overload(QWebEngineScript)
  def insert(self, a0: QWebEngineScript) -> None:
    """
    Calls Qt's 'void QWebEngineScriptCollection::insert(const
    QWebEngineScript &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginescriptcollection.html#insert

    Parameters
    ----------

    a0 : QWebEngineScript
      Passed on as a value: Qt reads the C++ QWebEngineScript, which stays
      Python's own.
    """
    #  void QWebEngineScriptCollection::insert(const QWebEngineScript &a0)
    self.uglySide.call(
        'ritual_ZN26QWebEngineScriptCollection6insertERK16QWebEngineScript',
        self._valueOf(a0),
    )

  @overload(QList[QWebEngineScript])
  def insert(self, list: QList[QWebEngineScript]) -> None:
    """
    Calls Qt's 'void QWebEngineScriptCollection::insert(const
    QList<QWebEngineScript> &list)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginescriptcollection.html#insert

    Parameters
    ----------

    list : QList[QWebEngineScript]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QWebEngineScriptCollection::insert(const QList<QWebEngineScript>
    #      &list)
    self.uglySide.call(
        'ritual_ZN26QWebEngineScriptCollection6insertERK5QListI16QWebEngine'
        'ScriptE',
        self._valueOf(list),
    )

  @overload(QWebEngineScript)
  def remove(self, a0: QWebEngineScript) -> bool:
    """
    Calls Qt's 'bool QWebEngineScriptCollection::remove(const
    QWebEngineScript &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginescriptcollection.html#remove

    Parameters
    ----------

    a0 : QWebEngineScript
      Passed on as a value: Qt reads the C++ QWebEngineScript, which stays
      Python's own.
    """
    #  bool QWebEngineScriptCollection::remove(const QWebEngineScript &a0)
    return self.uglySide.call(
        'ritual_ZN26QWebEngineScriptCollection6removeERK16QWebEngineScript',
        self._valueOf(a0),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QWebEngineScriptCollection::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginescriptcollection.html#clear
    """
    #  void QWebEngineScriptCollection::clear()
    self.uglySide.call('ritual_ZN26QWebEngineScriptCollection5clearEv')
