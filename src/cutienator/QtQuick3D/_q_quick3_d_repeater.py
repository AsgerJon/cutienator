"""
QQuick3DRepeater binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3drepeater_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DRepeater to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuick3DNode, QQuick3DObject
from ..QtQmlModels import QQmlDelegateModel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
  from ..QtQml import QQmlComponent
  from ..QtQmlModels import QQmlChangeSet, QQmlDelegateModelPointer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlChangeSet = WAIT['QQmlChangeSet']
  QQmlComponent = WAIT['QQmlComponent']
  QQmlDelegateModelPointer = WAIT['QQmlDelegateModelPointer']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DRepeater(QQuick3DNode):
  """
  The cute side of Qt's QQuick3DRepeater: a plain Python object standing in
  front of one C++ QQuick3DRepeater.

  It is built on the cute 'QQuick3DNode', as Qt's QQuick3DRepeater is built
  on Qt's QQuick3DNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DRepeater that has a ritual and that Python
  can call so far, 29 names in all: 'metaObject', 'tr', 'model', 'setModel',
  'delegate', 'setDelegate', 'count', 'objectAt', 'delegateModelAccess',
  'setDelegateModelAccess', 'modelChanged', 'delegateChanged',
  'countChanged', 'objectAdded', 'objectRemoved',
  'delegateModelAccessChanged', 'clear', 'regenerate', 'componentComplete',
  'itemChange', 'initDelegate', 'createdObject', 'initObject',
  'modelUpdated', 'requestItems', 'applyDelegateChange',
  'createDelegateModel', 'connectModel', 'disconnectModel'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DRepeater::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuick3DRepeater::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DRepeater::~QQuick3DRepeater()': the destructor: Python
    never removes a C++ QQuick3DRepeater.

  What has no ritual
  ------------------

  4 of the 37 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuick3DRepeater is created at the first use, not by
    'QQuick3DRepeater(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DRepeater.
  - Qt tells when it has removed the C++ QQuick3DRepeater. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QQuick3DRepeater::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drepeater.html#tr

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
    #  QString QQuick3DRepeater::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQuick3DRepeater2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DRepeater'

  #  A C++ QQuick3DRepeater Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DRepeater'

  #  The functions Qt calls itself that QQuick3DRepeater is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'initDelegate': (
          ('_ZN16QQuick3DRepeater12initDelegateEiP12QQuick3DNode',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'address', 'QtQuick3D:QQuick3DNode'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DRepeater::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drepeater.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DRepeater::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DRepeater10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def model(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuick3DRepeater::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drepeater.html#model

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuick3DRepeater::model() const
    address = self.uglySide.call('ritual_ZNK16QQuick3DRepeater5modelEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def delegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuick3DRepeater::delegate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drepeater.html#delegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuick3DRepeater::delegate() const
    address = self.uglySide.call('ritual_ZNK16QQuick3DRepeater8delegateEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QQuick3DRepeater::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drepeater.html#count
    """
    #  int QQuick3DRepeater::count() const
    return self.uglySide.call('ritual_ZNK16QQuick3DRepeater5countEv')

  @overload(int)
  def objectAt(self, index: int) -> Optional[QQuick3DObject]:
    """
    Calls Qt's 'QQuick3DObject *QQuick3DRepeater::objectAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drepeater.html#objectAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QQuick3DObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DObject *QQuick3DRepeater::objectAt(int index) const
    address = self.uglySide.call(
        'ritual_ZNK16QQuick3DRepeater8objectAtEi', index,
    )
    return QQuick3DObject._cuteAt(address)

  def delegateModelAccess(self) -> QQmlDelegateModel.DelegateModelAccess:
    """
    Calls Qt's 'QQmlDelegateModel::DelegateModelAccess
    QQuick3DRepeater::delegateModelAccess() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drepeater.html#delegateModelAccess

    Returns
    -------

    QQmlDelegateModel.DelegateModelAccess
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlDelegateModel.DelegateModelAccess(number)' gives.
    """
    #  QQmlDelegateModel::DelegateModelAccess
    #      QQuick3DRepeater::delegateModelAccess() const
    return QQmlDelegateModel.DelegateModelAccess(self.uglySide.call(
        'ritual_ZNK16QQuick3DRepeater19delegateModelAccessEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setModel(self, a0: QVariant) -> None:
    """
    Calls Qt's 'void QQuick3DRepeater::setModel(const QVariant &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drepeater.html#setModel

    Parameters
    ----------

    a0 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuick3DRepeater::setModel(const QVariant &a0)
    self.uglySide.call(
        'ritual_ZN16QQuick3DRepeater8setModelERK8QVariant',
        self._valueOf(a0),
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setDelegate(self, a0: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuick3DRepeater::setDelegate(QQmlComponent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drepeater.html#setDelegate

    Parameters
    ----------

    a0 : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DRepeater::setDelegate(QQmlComponent *a0)
    self.uglySide.call(
        'ritual_ZN16QQuick3DRepeater11setDelegateEP13QQmlComponent',
        self._addressOf(a0),
    )

  @overload(QQmlDelegateModel.DelegateModelAccess)
  def setDelegateModelAccess(
      self,
      delegateModelAccess: QQmlDelegateModel.DelegateModelAccess,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DRepeater::setDelegateModelAccess(QQmlDelegateModel::
    DelegateModelAccess delegateModelAccess)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drepeater.html#setDelegateModelAccess

    Parameters
    ----------

    delegateModelAccess : QQmlDelegateModel.DelegateModelAccess
      Passed on as its number.
    """
    #  void QQuick3DRepeater::setDelegateModelAccess(QQmlDelegateModel::
    #      DelegateModelAccess delegateModelAccess)
    self.uglySide.call(
        'ritual_ZN16QQuick3DRepeater22setDelegateModelAccessEN17QQmlDelegat'
        'eModel19DelegateModelAccessE',
        delegateModelAccess.value,
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
  @overload(QQuick3DNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DRepeater::QQuick3DRepeater(QQuick3DNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drepeater.html#QQuick3DRepeater

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DRepeater::QQuick3DRepeater(QQuick3DNode *parent)
    self._noteCreation(QQuick3DRepeater, lambda: Rituals.call(
        'ritual_ZN16QQuick3DRepeaterC1EP12QQuick3DNode',
        self._addressOf(parent),
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

  def modelChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRepeater::modelChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drepeater.html#modelChanged
    """
    #  void QQuick3DRepeater::modelChanged()
    self.uglySide.call('ritual_ZN16QQuick3DRepeater12modelChangedEv')

  def delegateChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRepeater::delegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drepeater.html#delegateChanged
    """
    #  void QQuick3DRepeater::delegateChanged()
    self.uglySide.call('ritual_ZN16QQuick3DRepeater15delegateChangedEv')

  def countChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRepeater::countChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drepeater.html#countChanged
    """
    #  void QQuick3DRepeater::countChanged()
    self.uglySide.call('ritual_ZN16QQuick3DRepeater12countChangedEv')

  @overload(int, QQuick3DObject)
  @overload(int, NoneType)
  def objectAdded(
      self,
      index: int,
      object: Optional[QQuick3DObject],
  ) -> None:
    """
    Calls Qt's 'void QQuick3DRepeater::objectAdded(int index, QQuick3DObject
    *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drepeater.html#objectAdded

    Parameters
    ----------

    index : int
      Passed on as it is.

    object : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DRepeater::objectAdded(int index, QQuick3DObject *object)
    self.uglySide.call(
        'ritual_ZN16QQuick3DRepeater11objectAddedEiP14QQuick3DObject',
        index, self._addressOf(object),
    )

  @overload(int, QQuick3DObject)
  @overload(int, NoneType)
  def objectRemoved(
      self,
      index: int,
      object: Optional[QQuick3DObject],
  ) -> None:
    """
    Calls Qt's 'void QQuick3DRepeater::objectRemoved(int index,
    QQuick3DObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drepeater.html#objectRemoved

    Parameters
    ----------

    index : int
      Passed on as it is.

    object : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DRepeater::objectRemoved(int index, QQuick3DObject
    #      *object)
    self.uglySide.call(
        'ritual_ZN16QQuick3DRepeater13objectRemovedEiP14QQuick3DObject',
        index, self._addressOf(object),
    )

  def delegateModelAccessChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRepeater::delegateModelAccessChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drepeater.html#delegateModelAccessChanged
    """
    #  void QQuick3DRepeater::delegateModelAccessChanged()
    self.uglySide.call(
        'ritual_ZN16QQuick3DRepeater26delegateModelAccessChangedEv',
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QQuick3DRepeater::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drepeater.html#clear
    """
    #  void QQuick3DRepeater::clear()
    self.uglySide.call('ritual_ZN16QQuick3DRepeater5clearEv')

  def regenerate(self) -> None:
    """
    Calls Qt's 'void QQuick3DRepeater::regenerate()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drepeater.html#regenerate
    """
    #  void QQuick3DRepeater::regenerate()
    self.uglySide.call('ritual_ZN16QQuick3DRepeater10regenerateEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuick3DRepeater::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drepeater.html#componentComplete
    """
    #  void QQuick3DRepeater::componentComplete()
    ritual = 'ritual_ZN16QQuick3DRepeater17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuick3DRepeater17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QQuick3DObject.ItemChange, QQuick3DObject.ItemChangeData)
  def itemChange(
      self,
      change: QQuick3DObject.ItemChange,
      value: QQuick3DObject.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DRepeater::itemChange(ItemChange change, const
    ItemChangeData &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drepeater.html#itemChange

    Parameters
    ----------

    change : QQuick3DObject.ItemChange
      Passed on as its number.

    value : QQuick3DObject.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuick3DObject::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuick3DRepeater::itemChange(ItemChange change, const
    #      ItemChangeData &value)
    ritual = (
        'ritual_ZN16QQuick3DRepeater10itemChangeEN14QQuick3DObject10ItemCha'
        'ngeERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuick3DRepeater10itemChangeEN14QQuick3DObject10I'
          'temChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(value))

  @overload(int, QQuick3DNode)
  @overload(int, NoneType)
  def initDelegate(self, a0: int, a1: Optional[QQuick3DNode]) -> None:
    """
    Calls Qt's 'void QQuick3DRepeater::initDelegate(int a0, QQuick3DNode
    *a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drepeater.html#initDelegate

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DRepeater::initDelegate(int a0, QQuick3DNode *a1)
    ritual = 'ritual_ZN16QQuick3DRepeater12initDelegateEiP12QQuick3DNode'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuick3DRepeater12initDelegateEiP12QQuick3DNode')
    self.uglySide.call(ritual, a0, self._addressOf(a1))

  @overload(int, QObject)
  @overload(int, NoneType)
  def createdObject(self, index: int, item: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuick3DRepeater::createdObject(int index, QObject
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drepeater.html#createdObject

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DRepeater::createdObject(int index, QObject *item)
    self.uglySide.call(
        'ritual_ZN16QQuick3DRepeater13createdObjectEiP7QObject',
        index, self._addressOf(item, 'QObject'),
    )

  @overload(int, QObject)
  @overload(int, NoneType)
  def initObject(self, a0: int, item: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuick3DRepeater::initObject(int a0, QObject *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drepeater.html#initObject

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    item : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DRepeater::initObject(int a0, QObject *item)
    self.uglySide.call(
        'ritual_ZN16QQuick3DRepeater10initObjectEiP7QObject',
        a0, self._addressOf(item, 'QObject'),
    )

  @overload(QQmlChangeSet, bool)
  def modelUpdated(self, changeSet: QQmlChangeSet, reset: bool) -> None:
    """
    Calls Qt's 'void QQuick3DRepeater::modelUpdated(const QQmlChangeSet
    &changeSet, bool reset)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drepeater.html#modelUpdated

    Parameters
    ----------

    changeSet : QQmlChangeSet
      Passed on as a value: Qt reads the C++ QQmlChangeSet, which stays
      Python's own.

    reset : bool
      Passed on as it is.
    """
    #  void QQuick3DRepeater::modelUpdated(const QQmlChangeSet &changeSet,
    #      bool reset)
    self.uglySide.call(
        'ritual_ZN16QQuick3DRepeater12modelUpdatedERK13QQmlChangeSetb',
        self._valueOf(changeSet), reset,
    )

  def requestItems(self) -> None:
    """
    Calls Qt's 'void QQuick3DRepeater::requestItems()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drepeater.html#requestItems
    """
    #  void QQuick3DRepeater::requestItems()
    self.uglySide.call('ritual_ZN16QQuick3DRepeater12requestItemsEv')

  def applyDelegateChange(self) -> None:
    """
    Calls Qt's 'void QQuick3DRepeater::applyDelegateChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drepeater.html#applyDelegateChange
    """
    #  void QQuick3DRepeater::applyDelegateChange()
    self.uglySide.call('ritual_ZN16QQuick3DRepeater19applyDelegateChangeEv')

  def createDelegateModel(self) -> Optional[QQmlDelegateModel]:
    """
    Calls Qt's 'QQmlDelegateModel *QQuick3DRepeater::createDelegateModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drepeater.html#createDelegateModel

    Returns
    -------

    Optional[QQmlDelegateModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlDelegateModel *QQuick3DRepeater::createDelegateModel()
    address = self.uglySide.call(
        'ritual_ZN16QQuick3DRepeater19createDelegateModelEv',
    )
    return QQmlDelegateModel._cuteAt(address)

  @overload(QQmlDelegateModelPointer)
  @overload(NoneType)
  def connectModel(self, model: Optional[QQmlDelegateModelPointer]) -> None:
    """
    Calls Qt's 'void QQuick3DRepeater::connectModel(QQmlDelegateModelPointer
    *model)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3drepeater.html#connectModel

    Parameters
    ----------

    model : Optional[QQmlDelegateModelPointer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DRepeater::connectModel(QQmlDelegateModelPointer *model)
    self.uglySide.call(
        'ritual_ZN16QQuick3DRepeater12connectModelEP24QQmlDelegateModelPoin'
        'ter',
        self._addressOf(model),
    )

  @overload(QQmlDelegateModelPointer)
  @overload(NoneType)
  def disconnectModel(
      self,
      model: Optional[QQmlDelegateModelPointer],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DRepeater::disconnectModel(QQmlDelegateModelPointer *model)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3drepeater.html#disconnectModel

    Parameters
    ----------

    model : Optional[QQmlDelegateModelPointer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DRepeater::disconnectModel(QQmlDelegateModelPointer
    #      *model)
    self.uglySide.call(
        'ritual_ZN16QQuick3DRepeater15disconnectModelEP24QQmlDelegateModelP'
        'ointer',
        self._addressOf(model),
    )
