"""
QQmlInstantiator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmlinstantiator_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlInstantiator to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQml import QQmlParserStatus
from . import QQmlDelegateModel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
  from ..QtQml import QQmlComponent
  from . import QQmlInstantiatorPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlComponent = WAIT['QQmlComponent']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlInstantiator(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QQmlInstantiator: a plain Python object standing in
  front of one C++ QQmlInstantiator.

  It is built on the cute 'QObject', as Qt's QQmlInstantiator is built on
  Qt's QObject, and has everything that class has. It is built on the cute
  'QQmlParserStatus' as well, as Qt's QQmlInstantiator is built on Qt's
  QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlInstantiator that has a ritual and that Python
  can call so far, 27 names in all: 'metaObject', 'tr', 'isActive',
  'setActive', 'isAsync', 'setAsync', 'count', 'delegate', 'setDelegate',
  'model', 'setModel', 'delegateModelAccess', 'setDelegateModelAccess',
  'object', 'objectAt', 'classBegin', 'componentComplete', 'modelChanged',
  'delegateChanged', 'countChanged', 'objectChanged', 'activeChanged',
  'asynchronousChanged', 'objectAdded', 'objectRemoved',
  'delegateModelAccessChanged', 'd_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlInstantiator::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQmlInstantiator::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlInstantiator::~QQmlInstantiator()': the destructor: Python
    never removes a C++ QQmlInstantiator.
  - Qt's 'const QQmlInstantiatorPrivate *QQmlInstantiator::d_func() const':
    takes in Python what 'QQmlInstantiatorPrivate
    *QQmlInstantiator::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 36 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQmlInstantiator is created at the first use, not by
    'QQmlInstantiator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlInstantiator.
  - Qt tells when it has removed the C++ QQmlInstantiator. Every call on the
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
    Calls Qt's 'QString QQmlInstantiator::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstantiator.html#tr

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
    #  QString QQmlInstantiator::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQmlInstantiator2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlInstantiator'

  #  Qt's QQmlInstantiator is built on more than one class. The part of a C++
  #  QQmlInstantiator that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_QQmlInstantiator_QQmlParserStatus',
  }

  #  A C++ QQmlInstantiator Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlInstantiator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlInstantiator::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstantiator.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlInstantiator::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlInstantiator10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QQmlInstantiator::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstantiator.html#isActive
    """
    #  bool QQmlInstantiator::isActive() const
    return self.uglySide.call('ritual_ZNK16QQmlInstantiator8isActiveEv')

  def isAsync(self) -> bool:
    """
    Calls Qt's 'bool QQmlInstantiator::isAsync() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstantiator.html#isAsync
    """
    #  bool QQmlInstantiator::isAsync() const
    return self.uglySide.call('ritual_ZNK16QQmlInstantiator7isAsyncEv')

  def count(self) -> int:
    """
    Calls Qt's 'int QQmlInstantiator::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstantiator.html#count
    """
    #  int QQmlInstantiator::count() const
    return self.uglySide.call('ritual_ZNK16QQmlInstantiator5countEv')

  def model(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlInstantiator::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstantiator.html#model

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlInstantiator::model() const
    address = self.uglySide.call('ritual_ZNK16QQmlInstantiator5modelEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def delegateModelAccess(self) -> QQmlDelegateModel.DelegateModelAccess:
    """
    Calls Qt's 'QQmlDelegateModel::DelegateModelAccess
    QQmlInstantiator::delegateModelAccess() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinstantiator.html#delegateModelAccess

    Returns
    -------

    QQmlDelegateModel.DelegateModelAccess
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlDelegateModel.DelegateModelAccess(number)' gives.
    """
    #  QQmlDelegateModel::DelegateModelAccess
    #      QQmlInstantiator::delegateModelAccess() const
    return QQmlDelegateModel.DelegateModelAccess(self.uglySide.call(
        'ritual_ZNK16QQmlInstantiator19delegateModelAccessEv',
    ))

  def object(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlInstantiator::object() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstantiator.html#object

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlInstantiator::object() const
    address = self.uglySide.call('ritual_ZNK16QQmlInstantiator6objectEv')
    return QObject._cuteAt(address)

  @overload(int)
  def objectAt(self, index: int) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlInstantiator::objectAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstantiator.html#objectAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlInstantiator::objectAt(int index) const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlInstantiator8objectAtEi', index,
    )
    return QObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setActive(self, newVal: bool) -> None:
    """
    Calls Qt's 'void QQmlInstantiator::setActive(bool newVal)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstantiator.html#setActive

    Parameters
    ----------

    newVal : bool
      Passed on as it is.
    """
    #  void QQmlInstantiator::setActive(bool newVal)
    self.uglySide.call('ritual_ZN16QQmlInstantiator9setActiveEb', newVal)

  @overload(bool)
  def setAsync(self, newVal: bool) -> None:
    """
    Calls Qt's 'void QQmlInstantiator::setAsync(bool newVal)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstantiator.html#setAsync

    Parameters
    ----------

    newVal : bool
      Passed on as it is.
    """
    #  void QQmlInstantiator::setAsync(bool newVal)
    self.uglySide.call('ritual_ZN16QQmlInstantiator8setAsyncEb', newVal)

  @overload(QQmlComponent)
  @overload(NoneType)
  def setDelegate(self, c: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQmlInstantiator::setDelegate(QQmlComponent *c)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstantiator.html#setDelegate

    Parameters
    ----------

    c : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlInstantiator::setDelegate(QQmlComponent *c)
    self.uglySide.call(
        'ritual_ZN16QQmlInstantiator11setDelegateEP13QQmlComponent',
        self._addressOf(c),
    )

  @overload(QVariant)
  def setModel(self, v: QVariant) -> None:
    """
    Calls Qt's 'void QQmlInstantiator::setModel(const QVariant &v)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstantiator.html#setModel

    Parameters
    ----------

    v : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlInstantiator::setModel(const QVariant &v)
    self.uglySide.call(
        'ritual_ZN16QQmlInstantiator8setModelERK8QVariant', self._valueOf(v),
    )

  @overload(QQmlDelegateModel.DelegateModelAccess)
  def setDelegateModelAccess(
      self,
      delegateModelAccess: QQmlDelegateModel.DelegateModelAccess,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlInstantiator::setDelegateModelAccess(QQmlDelegateModel::
    DelegateModelAccess delegateModelAccess)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinstantiator.html#setDelegateModelAccess

    Parameters
    ----------

    delegateModelAccess : QQmlDelegateModel.DelegateModelAccess
      Passed on as its number.
    """
    #  void QQmlInstantiator::setDelegateModelAccess(QQmlDelegateModel::
    #      DelegateModelAccess delegateModelAccess)
    self.uglySide.call(
        'ritual_ZN16QQmlInstantiator22setDelegateModelAccessEN17QQmlDelegat'
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQmlInstantiator::QQmlInstantiator(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinstantiator.html#QQmlInstantiator

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlInstantiator::QQmlInstantiator(QObject *parent)
    self._noteCreation(QQmlInstantiator, lambda: Rituals.call(
        'ritual_ZN16QQmlInstantiatorC1EP7QObject',
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

  def delegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQmlInstantiator::delegate()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstantiator.html#delegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQmlInstantiator::delegate()
    address = self.uglySide.call('ritual_ZN16QQmlInstantiator8delegateEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQmlInstantiator::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstantiator.html#classBegin
    """
    #  void QQmlInstantiator::classBegin()
    ritual = 'ritual_ZN16QQmlInstantiator10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQmlInstantiator10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQmlInstantiator::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinstantiator.html#componentComplete
    """
    #  void QQmlInstantiator::componentComplete()
    ritual = 'ritual_ZN16QQmlInstantiator17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQmlInstantiator17componentCompleteEv'
    self.uglySide.call(ritual)

  def modelChanged(self) -> None:
    """
    Calls Qt's 'void QQmlInstantiator::modelChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstantiator.html#modelChanged
    """
    #  void QQmlInstantiator::modelChanged()
    self.uglySide.call('ritual_ZN16QQmlInstantiator12modelChangedEv')

  def delegateChanged(self) -> None:
    """
    Calls Qt's 'void QQmlInstantiator::delegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinstantiator.html#delegateChanged
    """
    #  void QQmlInstantiator::delegateChanged()
    self.uglySide.call('ritual_ZN16QQmlInstantiator15delegateChangedEv')

  def countChanged(self) -> None:
    """
    Calls Qt's 'void QQmlInstantiator::countChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstantiator.html#countChanged
    """
    #  void QQmlInstantiator::countChanged()
    self.uglySide.call('ritual_ZN16QQmlInstantiator12countChangedEv')

  def objectChanged(self) -> None:
    """
    Calls Qt's 'void QQmlInstantiator::objectChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinstantiator.html#objectChanged
    """
    #  void QQmlInstantiator::objectChanged()
    self.uglySide.call('ritual_ZN16QQmlInstantiator13objectChangedEv')

  def activeChanged(self) -> None:
    """
    Calls Qt's 'void QQmlInstantiator::activeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinstantiator.html#activeChanged
    """
    #  void QQmlInstantiator::activeChanged()
    self.uglySide.call('ritual_ZN16QQmlInstantiator13activeChangedEv')

  def asynchronousChanged(self) -> None:
    """
    Calls Qt's 'void QQmlInstantiator::asynchronousChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinstantiator.html#asynchronousChanged
    """
    #  void QQmlInstantiator::asynchronousChanged()
    self.uglySide.call('ritual_ZN16QQmlInstantiator19asynchronousChangedEv')

  @overload(int, QObject)
  @overload(int, NoneType)
  def objectAdded(self, index: int, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlInstantiator::objectAdded(int index, QObject
    *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstantiator.html#objectAdded

    Parameters
    ----------

    index : int
      Passed on as it is.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlInstantiator::objectAdded(int index, QObject *object)
    self.uglySide.call(
        'ritual_ZN16QQmlInstantiator11objectAddedEiP7QObject',
        index, self._addressOf(object, 'QObject'),
    )

  @overload(int, QObject)
  @overload(int, NoneType)
  def objectRemoved(self, index: int, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlInstantiator::objectRemoved(int index, QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinstantiator.html#objectRemoved

    Parameters
    ----------

    index : int
      Passed on as it is.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlInstantiator::objectRemoved(int index, QObject *object)
    self.uglySide.call(
        'ritual_ZN16QQmlInstantiator13objectRemovedEiP7QObject',
        index, self._addressOf(object, 'QObject'),
    )

  def delegateModelAccessChanged(self) -> None:
    """
    Calls Qt's 'void QQmlInstantiator::delegateModelAccessChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlinstantiator.html#delegateModelAccessChanged
    """
    #  void QQmlInstantiator::delegateModelAccessChanged()
    self.uglySide.call(
        'ritual_ZN16QQmlInstantiator26delegateModelAccessChangedEv',
    )

  def d_func(self) -> Optional[QQmlInstantiatorPrivate]:
    """
    Calls Qt's 'QQmlInstantiatorPrivate *QQmlInstantiator::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlinstantiator.html#d_func

    Returns
    -------

    Optional[QQmlInstantiatorPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlInstantiatorPrivate *QQmlInstantiator::d_func()
    address = self.uglySide.call('ritual_ZN16QQmlInstantiator6d_funcEv')
    from . import QQmlInstantiatorPrivate
    return QQmlInstantiatorPrivate._cuteAt(address)
