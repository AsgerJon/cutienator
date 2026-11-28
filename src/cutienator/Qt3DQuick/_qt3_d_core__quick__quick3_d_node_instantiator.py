"""
Qt3DCore::Quick::Quick3DNodeInstantiator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DQuick/6.12.0/Qt3DQuick/private/quick3dnodeinstantiator_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DCore::Quick::Quick3DNodeInstantiator to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQml import QQmlParserStatus
from ..Qt3DCore import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
  from ..QtQml import QQmlComponent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlComponent = WAIT['QQmlComponent']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Quick3DNodeInstantiator(Qt3DCore.QNode, QQmlParserStatus):
  """
  The cute side of Qt's Qt3DCore::Quick::Quick3DNodeInstantiator: a plain
  Python object standing in front of one C++
  Qt3DCore::Quick::Quick3DNodeInstantiator.

  It is built on the cute 'Qt3DCore::QNode', as Qt's
  Qt3DCore::Quick::Quick3DNodeInstantiator is built on Qt's Qt3DCore::QNode,
  and has everything that class has. It is built on the cute
  'QQmlParserStatus' as well, as Qt's
  Qt3DCore::Quick::Quick3DNodeInstantiator is built on Qt's QQmlParserStatus
  too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::Quick::Quick3DNodeInstantiator that has a
  ritual and that Python can call so far, 24 names in all: 'metaObject',
  'tr', 'isActive', 'setActive', 'isAsync', 'setAsync', 'count', 'delegate',
  'setDelegate', 'model', 'setModel', 'object', 'objectAt', 'classBegin',
  'componentComplete', 'modelChanged', 'delegateChanged', 'countChanged',
  'objectChanged', 'activeChanged', 'asynchronousChanged', 'objectAdded',
  'objectRemoved', 'onParentChanged'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::Quick::Quick3DNodeInstantiator::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DCore::Quick::Quick3DNodeInstantiator::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  6 of the 33 functions Qt declares: 2 not a gap; 2 forbidden; 2 the compiler
  refuses its ritual as it would be written here.

  What to expect
  --------------

  - The C++ Qt3DCore::Quick::Quick3DNodeInstantiator is created at the first
    use, not by 'Qt3DCore::Quick::Quick3DNodeInstantiator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::Quick::Quick3DNodeInstantiator.
  - Qt tells when it has removed the C++
    Qt3DCore::Quick::Quick3DNodeInstantiator. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
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
    Calls Qt's 'QString Qt3DCore::Quick::Quick3DNodeInstantiator::tr(const
    char *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dnodeinstantiator.html#tr

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
    #  QString Qt3DCore::Quick::Quick3DNodeInstantiator::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator2trEPKcS3_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::Quick::Quick3DNodeInstantiator'

  #  Qt's Qt3DCore::Quick::Quick3DNodeInstantiator is built on more than one
  #  class. The part of a C++ Qt3DCore::Quick::Quick3DNodeInstantiator that
  #  belongs to a class after the first begins somewhere inside the object,
  #  and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus':
          'ritual_cast_Qt3DCore_Quick_Quick3DNodeInstantiator_QQmlParserStatus',
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
    Calls Qt's 'const QMetaObject
    *Qt3DCore::Quick::Quick3DNodeInstantiator::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dnodeinstantiator.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *Qt3DCore::Quick::Quick3DNodeInstantiator::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick23Quick3DNodeInstantiator10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::Quick::Quick3DNodeInstantiator::isActive()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dnodeinstantiator.html
    """
    #  bool Qt3DCore::Quick::Quick3DNodeInstantiator::isActive() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick23Quick3DNodeInstantiator8isActiveEv',
    )

  def isAsync(self) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::Quick::Quick3DNodeInstantiator::isAsync()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dnodeinstantiator.html
    """
    #  bool Qt3DCore::Quick::Quick3DNodeInstantiator::isAsync() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick23Quick3DNodeInstantiator7isAsyncEv',
    )

  def count(self) -> int:
    """
    Calls Qt's 'int Qt3DCore::Quick::Quick3DNodeInstantiator::count() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dnodeinstantiator.html#count
    """
    #  int Qt3DCore::Quick::Quick3DNodeInstantiator::count() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick23Quick3DNodeInstantiator5countEv',
    )

  def model(self) -> QVariant:
    """
    Calls Qt's 'QVariant Qt3DCore::Quick::Quick3DNodeInstantiator::model()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dnodeinstantiator.html#model

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant Qt3DCore::Quick::Quick3DNodeInstantiator::model() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick23Quick3DNodeInstantiator5modelEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def object(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *Qt3DCore::Quick::Quick3DNodeInstantiator::object()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dnodeinstantiator.html#object

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *Qt3DCore::Quick::Quick3DNodeInstantiator::object() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick23Quick3DNodeInstantiator6objectEv',
    )
    return QObject._cuteAt(address)

  @overload(int)
  def objectAt(self, index: int) -> Optional[QObject]:
    """
    Calls Qt's 'QObject
    *Qt3DCore::Quick::Quick3DNodeInstantiator::objectAt(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dnodeinstantiator.html

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
    #  QObject *Qt3DCore::Quick::Quick3DNodeInstantiator::objectAt(int index)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick23Quick3DNodeInstantiator8objectAtEi',
        index,
    )
    return QObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setActive(self, newVal: bool) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::Quick3DNodeInstantiator::setActive(bool
    newVal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dnodeinstantiator.html

    Parameters
    ----------

    newVal : bool
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::Quick3DNodeInstantiator::setActive(bool newVal)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator9setActiveEb',
        newVal,
    )

  @overload(bool)
  def setAsync(self, newVal: bool) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::Quick3DNodeInstantiator::setAsync(bool
    newVal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dnodeinstantiator.html

    Parameters
    ----------

    newVal : bool
      Passed on as it is.
    """
    #  void Qt3DCore::Quick::Quick3DNodeInstantiator::setAsync(bool newVal)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator8setAsyncEb',
        newVal,
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setDelegate(self, c: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::Quick3DNodeInstantiator::setDelegate(QQmlComponent *c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dnodeinstantiator.html

    Parameters
    ----------

    c : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::Quick::Quick3DNodeInstantiator::setDelegate(
    #      QQmlComponent *c)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator11setDelegateEP13'
        'QQmlComponent',
        self._addressOf(c),
    )

  @overload(QVariant)
  def setModel(self, v: QVariant) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::Quick3DNodeInstantiator::setModel(const
    QVariant &v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dnodeinstantiator.html

    Parameters
    ----------

    v : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DCore::Quick::Quick3DNodeInstantiator::setModel(const QVariant
    #      &v)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator8setModelERK8QVar'
        'iant',
        self._valueOf(v),
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DCore::Quick::Quick3DNodeInstantiator::Quick3DNodeInstantiator(QNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dnodeinstantiator.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DCore::Quick::Quick3DNodeInstantiator::Quick3DNodeInstantiator(
    #      QNode *parent)
    self._noteCreation(Quick3DNodeInstantiator, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiatorC1EPNS_5QNodeE',
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

  def delegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent
    *Qt3DCore::Quick::Quick3DNodeInstantiator::delegate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dnodeinstantiator.html

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *Qt3DCore::Quick::Quick3DNodeInstantiator::delegate()
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator8delegateEv',
    )
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def classBegin(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::Quick3DNodeInstantiator::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dnodeinstantiator.html
    """
    #  void Qt3DCore::Quick::Quick3DNodeInstantiator::classBegin()
    ritual = (
        'ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator10classBeginEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator10classBegi'
          'nEv')
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::Quick3DNodeInstantiator::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dnodeinstantiator.html
    """
    #  void Qt3DCore::Quick::Quick3DNodeInstantiator::componentComplete()
    ritual = (
        'ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator17componentComple'
        'teEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator17component'
          'CompleteEv')
    self.uglySide.call(ritual)

  def modelChanged(self) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::Quick3DNodeInstantiator::modelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dnodeinstantiator.html
    """
    #  void Qt3DCore::Quick::Quick3DNodeInstantiator::modelChanged()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator12modelChangedEv',
    )

  def delegateChanged(self) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::Quick3DNodeInstantiator::delegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dnodeinstantiator.html
    """
    #  void Qt3DCore::Quick::Quick3DNodeInstantiator::delegateChanged()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator15delegateChanged'
        'Ev',
    )

  def countChanged(self) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::Quick3DNodeInstantiator::countChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dnodeinstantiator.html
    """
    #  void Qt3DCore::Quick::Quick3DNodeInstantiator::countChanged()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator12countChangedEv',
    )

  def objectChanged(self) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::Quick3DNodeInstantiator::objectChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dnodeinstantiator.html
    """
    #  void Qt3DCore::Quick::Quick3DNodeInstantiator::objectChanged()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator13objectChangedEv',
    )

  def activeChanged(self) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::Quick3DNodeInstantiator::activeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dnodeinstantiator.html
    """
    #  void Qt3DCore::Quick::Quick3DNodeInstantiator::activeChanged()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator13activeChangedEv',
    )

  def asynchronousChanged(self) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::Quick3DNodeInstantiator::asynchronousChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dnodeinstantiator.html
    """
    #  void Qt3DCore::Quick::Quick3DNodeInstantiator::asynchronousChanged()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator19asynchronousCha'
        'ngedEv',
    )

  @overload(int, QObject)
  @overload(int, NoneType)
  def objectAdded(self, index: int, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::Quick3DNodeInstantiator::objectAdded(int index, QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dnodeinstantiator.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::Quick::Quick3DNodeInstantiator::objectAdded(int index,
    #      QObject *object)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator11objectAddedEiP7'
        'QObject',
        index, self._addressOf(object, 'QObject'),
    )

  @overload(int, QObject)
  @overload(int, NoneType)
  def objectRemoved(self, index: int, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::Quick3DNodeInstantiator::objectRemoved(int index,
    QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dnodeinstantiator.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::Quick::Quick3DNodeInstantiator::objectRemoved(int
    #      index, QObject *object)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator13objectRemovedEi'
        'P7QObject',
        index, self._addressOf(object, 'QObject'),
    )

  @overload(QObject)
  @overload(NoneType)
  def onParentChanged(self, parent: Optional[QObject]) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::Quick3DNodeInstantiator::onParentChanged(QObject
    *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dnodeinstantiator.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::Quick::Quick3DNodeInstantiator::onParentChanged(QObject
    #      *parent)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator15onParentChanged'
        'EP7QObject',
        self._addressOf(parent, 'QObject'),
    )
