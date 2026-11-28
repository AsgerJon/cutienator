"""
QQmlVMEResolvedList binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlvmemetaobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlVMEResolvedList to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
  from . import QQmlVMEMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlVMEResolvedList(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlVMEResolvedList: a plain Python object standing
  in front of one C++ QQmlVMEResolvedList.

  What exists
  -----------

  Every function of Qt's QQmlVMEResolvedList that has a ritual and that
  Python can call so far, 11 names in all: 'metaObject', 'list', 'id',
  'isValid', 'append', 'replace', 'at', 'size', 'clear', 'removeLast',
  'activateSignal'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlVMEResolvedList::QQmlVMEResolvedList(QQmlListProperty<QObject>
    *prop)': names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'QQmlVMEResolvedList::~QQmlVMEResolvedList()': the destructor:
    Python never removes a C++ QQmlVMEResolvedList.

  What has no ritual
  ------------------

  4 of the 17 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QQmlVMEResolvedList is created at the first use, not by
    'QQmlVMEResolvedList(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlVMEResolvedList.
  - Each name of Qt's QQmlVMEResolvedList that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlVMEResolvedList'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QQmlVMEMetaObject]:
    """
    Calls Qt's 'QQmlVMEMetaObject *QQmlVMEResolvedList::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmeresolvedlist.html#metaObject

    Returns
    -------

    Optional[QQmlVMEMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlVMEMetaObject *QQmlVMEResolvedList::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQmlVMEResolvedList10metaObjectEv',
    )
    from . import QQmlVMEMetaObject
    return QQmlVMEMetaObject._cuteAt(address)

  def list(self) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'QV4::Heap::Object *QQmlVMEResolvedList::list() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvmeresolvedlist.html#list

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::Object *QQmlVMEResolvedList::list() const
    address = self.uglySide.call('ritual_ZNK19QQmlVMEResolvedList4listEv')
    return QV4.Heap.Object._cuteAt(address)

  def id(self) -> int:
    """
    Calls Qt's 'quintptr QQmlVMEResolvedList::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvmeresolvedlist.html#id
    """
    #  quintptr QQmlVMEResolvedList::id() const
    return self.uglySide.call('ritual_ZNK19QQmlVMEResolvedList2idEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQmlVMEResolvedList::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvmeresolvedlist.html#isValid
    """
    #  bool QQmlVMEResolvedList::isValid() const
    return self.uglySide.call('ritual_ZNK19QQmlVMEResolvedList7isValidEv')

  @overload(int)
  def at(self, i: int) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlVMEResolvedList::at(qsizetype i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvmeresolvedlist.html#at

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlVMEResolvedList::at(qsizetype i) const
    address = self.uglySide.call('ritual_ZNK19QQmlVMEResolvedList2atEx', i)
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def size(self) -> int:
    """
    Calls Qt's 'qsizetype QQmlVMEResolvedList::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvmeresolvedlist.html#size
    """
    #  qsizetype QQmlVMEResolvedList::size() const
    return self.uglySide.call('ritual_ZNK19QQmlVMEResolvedList4sizeEv')

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
    Qt's 'QQmlVMEResolvedList::QQmlVMEResolvedList(QQmlListProperty<QObject>
    *prop)': names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlVMEResolvedList.__init__' has no cute function yet. Qt's "
        "'QQmlVMEResolvedList::QQmlVMEResolvedList(QQmlListProperty<QObject>"
        " *prop)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")

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

  @overload(QObject)
  @overload(NoneType)
  def append(self, o: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlVMEResolvedList::append(QObject *o) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvmeresolvedlist.html#append

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlVMEResolvedList::append(QObject *o) const
    self.uglySide.call(
        'ritual_ZNK19QQmlVMEResolvedList6appendEP7QObject',
        self._addressOf(o, 'QObject'),
    )

  @overload(int, QObject)
  @overload(int, NoneType)
  def replace(self, i: int, o: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlVMEResolvedList::replace(qsizetype i, QObject *o)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvmeresolvedlist.html#replace

    Parameters
    ----------

    i : int
      Passed on as it is.

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlVMEResolvedList::replace(qsizetype i, QObject *o) const
    self.uglySide.call(
        'ritual_ZNK19QQmlVMEResolvedList7replaceExP7QObject',
        i, self._addressOf(o, 'QObject'),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QQmlVMEResolvedList::clear() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvmeresolvedlist.html#clear
    """
    #  void QQmlVMEResolvedList::clear() const
    self.uglySide.call('ritual_ZNK19QQmlVMEResolvedList5clearEv')

  def removeLast(self) -> None:
    """
    Calls Qt's 'void QQmlVMEResolvedList::removeLast() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmeresolvedlist.html#removeLast
    """
    #  void QQmlVMEResolvedList::removeLast() const
    self.uglySide.call('ritual_ZNK19QQmlVMEResolvedList10removeLastEv')

  def activateSignal(self) -> None:
    """
    Calls Qt's 'void QQmlVMEResolvedList::activateSignal() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmeresolvedlist.html#activateSignal
    """
    #  void QQmlVMEResolvedList::activateSignal() const
    self.uglySide.call('ritual_ZNK19QQmlVMEResolvedList14activateSignalEv')
