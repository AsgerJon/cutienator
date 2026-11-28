"""
QtPrivate::QQuickAttachedPropertyPropagatorPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickattachedpropertypropagator_p_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QtPrivate::QQuickAttachedPropertyPropagatorPrivate to be private:
#  it declares the class in a header it calls private. cutienator does not
#  care. Qt hands objects of the class out all the same, and a class we are
#  handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate
from . import QtPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QObject
  from ..QtGui import QWindow
  from . import QQuickItem, QQuickWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaObject = WAIT['QMetaObject']
  QObject = WAIT['QObject']
  QQuickItem = WAIT['QQuickItem']
  QQuickWindow = WAIT['QQuickWindow']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickAttachedPropertyPropagatorPrivate(QObjectPrivate):
  """
  The cute side of Qt's QtPrivate::QQuickAttachedPropertyPropagatorPrivate: a
  plain Python object standing in front of one C++
  QtPrivate::QQuickAttachedPropertyPropagatorPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QtPrivate::QQuickAttachedPropertyPropagatorPrivate is built on Qt's
  QObjectPrivate, and has everything that class has. Qt's
  QtPrivate::QQuickAttachedPropertyPropagatorPrivate is built on Qt's
  QSafeQuickItemChangeListener<QQuickAttachedPropertyPropagatorPrivate> as
  well, which is not reflected.

  What exists
  -----------

  Every function of Qt's QtPrivate::QQuickAttachedPropertyPropagatorPrivate
  that has a ritual and that Python can call so far, 12 names in all:
  'q_func', 'get', 'init', 'attachTo', 'detachFrom', 'setAttachedParent',
  'itemWindowChanged', 'transientParentWindowChanged', 'itemParentChanged',
  'firstCppMetaObject', 'findAttachedParent', 'findAttachedItem'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickAttachedPropertyPropagator
    *QtPrivate::QQuickAttachedPropertyPropagatorPrivate::q_func() const':
    takes in Python what 'QQuickAttachedPropertyPropagator
    *QtPrivate::QQuickAttachedPropertyPropagatorPrivate::q_func()' takes.
  - Qt's 'QList<QQuickAttachedPropertyPropagator *>
    QtPrivate::QQuickAttachedPropertyPropagatorPrivate::findAttachedChildren(
    const QMetaObject *attachedType, QObject *object)': gives a type Python
    has no way to take yet.

  What to expect
  --------------

  - The C++ QtPrivate::QQuickAttachedPropertyPropagatorPrivate is created at
    the first use, not by
    'QtPrivate::QQuickAttachedPropertyPropagatorPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    QtPrivate::QQuickAttachedPropertyPropagatorPrivate.
  - Each name of Qt's QtPrivate::QQuickAttachedPropertyPropagatorPrivate that
    has no cute function yet, 'findAttachedChildren', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QtPrivate.QQuickAttachedPropertyPropagator'])
  @overload(NoneType)
  def get(
      attachedObject: Optional[QtPrivate.QQuickAttachedPropertyPropagator],
  ) -> Optional[QQuickAttachedPropertyPropagatorPrivate]:
    """
    Calls Qt's 'QQuickAttachedPropertyPropagatorPrivate
    *QtPrivate::QQuickAttachedPropertyPropagatorPrivate::get(
    QQuickAttachedPropertyPropagator *attachedObject)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qquickattachedpropertypropagatorprivate.html

    Parameters
    ----------

    attachedObject : Optional[QtPrivate.QQuickAttachedPropertyPropagator]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickAttachedPropertyPropagatorPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAttachedPropertyPropagatorPrivate
    #      *QtPrivate::QQuickAttachedPropertyPropagatorPrivate::get(
    #      QQuickAttachedPropertyPropagator *attachedObject)
    address = Rituals.call(
        'ritual_ZN9QtPrivate39QQuickAttachedPropertyPropagatorPrivate3getEP'
        'NS_32QQuickAttachedPropertyPropagatorE',
        CuteMixin._addressOf(attachedObject),
    )
    return QQuickAttachedPropertyPropagatorPrivate._cuteAt(address)

  @staticmethod
  @overload(WAIT['QtPrivate.QQuickAttachedPropertyPropagator'])
  @overload(NoneType)
  def firstCppMetaObject(
      propagator: Optional[QtPrivate.QQuickAttachedPropertyPropagator],
  ) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QtPrivate::QQuickAttachedPropertyPropagatorPrivate::firstCppMetaObject(
    QQuickAttachedPropertyPropagator *propagator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qquickattachedpropertypropagatorprivate.html

    Parameters
    ----------

    propagator : Optional[QtPrivate.QQuickAttachedPropertyPropagator]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QtPrivate::QQuickAttachedPropertyPropagatorPrivate::
    #      firstCppMetaObject(QQuickAttachedPropertyPropagator *propagator)
    address = Rituals.call(
        'ritual_ZN9QtPrivate39QQuickAttachedPropertyPropagatorPrivate18firs'
        'tCppMetaObjectEPNS_32QQuickAttachedPropertyPropagatorE',
        CuteMixin._addressOf(propagator),
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @staticmethod
  @overload(QMetaObject, QObject)
  @overload(QMetaObject, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def findAttachedParent(
      attachedType: Optional[QMetaObject],
      attachee: Optional[QObject],
  ) -> Optional[QtPrivate.QQuickAttachedPropertyPropagator]:
    """
    Calls Qt's 'QQuickAttachedPropertyPropagator
    *QtPrivate::QQuickAttachedPropertyPropagatorPrivate::findAttachedParent(
    const QMetaObject *attachedType, QObject *attachee)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qquickattachedpropertypropagatorprivate.html

    Parameters
    ----------

    attachedType : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    attachee : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QtPrivate.QQuickAttachedPropertyPropagator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAttachedPropertyPropagator
    #      *QtPrivate::QQuickAttachedPropertyPropagatorPrivate::
    #      findAttachedParent(const QMetaObject *attachedType, QObject
    #      *attachee)
    address = Rituals.call(
        'ritual_ZN9QtPrivate39QQuickAttachedPropertyPropagatorPrivate18find'
        'AttachedParentEPK11QMetaObjectP7QObject',
        CuteMixin._addressOf(attachedType, 'QMetaObject'),
        CuteMixin._addressOf(attachee, 'QObject'),
    )
    return QtPrivate.QQuickAttachedPropertyPropagator._cuteAt(address)

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def findAttachedItem(object: Optional[QObject]) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem
    *QtPrivate::QQuickAttachedPropertyPropagatorPrivate::findAttachedItem(
    QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qquickattachedpropertypropagatorprivate.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QtPrivate::QQuickAttachedPropertyPropagatorPrivate::
    #      findAttachedItem(QObject *object)
    address = Rituals.call(
        'ritual_ZN9QtPrivate39QQuickAttachedPropertyPropagatorPrivate16find'
        'AttachedItemEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtPrivate::QQuickAttachedPropertyPropagatorPrivate'

  #  A C++ QtPrivate::QQuickAttachedPropertyPropagatorPrivate Python makes is
  #  of a C++ class of ours, in which Python can take functions over. This
  #  ritual hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtPrivate_QQuickAttachedPropertyPropagatorPrivate'

  #  The functions Qt calls itself that
  #  QtPrivate::QQuickAttachedPropertyPropagatorPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'itemParentChanged': (
          ('_ZN9QtPrivate39QQuickAttachedPropertyPropagatorPrivate17itemPar'
           'entChangedEP10QQuickItemS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'address', 'QtQuick:QQuickItem'),
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QtPrivate.QQuickAttachedPropertyPropagator'])
  @overload(NoneType)
  def setAttachedParent(
      self,
      parent: Optional[QtPrivate.QQuickAttachedPropertyPropagator],
  ) -> None:
    """
    Calls Qt's 'void
    QtPrivate::QQuickAttachedPropertyPropagatorPrivate::setAttachedParent(
    QQuickAttachedPropertyPropagator *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qquickattachedpropertypropagatorprivate.html

    Parameters
    ----------

    parent : Optional[QtPrivate.QQuickAttachedPropertyPropagator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtPrivate::QQuickAttachedPropertyPropagatorPrivate::
    #      setAttachedParent(QQuickAttachedPropertyPropagator *parent)
    self.uglySide.call(
        'ritual_ZN9QtPrivate39QQuickAttachedPropertyPropagatorPrivate17setA'
        'ttachedParentEPNS_32QQuickAttachedPropertyPropagatorE',
        self._addressOf(parent),
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

  def q_func(self) -> Optional[QtPrivate.QQuickAttachedPropertyPropagator]:
    """
    Calls Qt's 'QQuickAttachedPropertyPropagator
    *QtPrivate::QQuickAttachedPropertyPropagatorPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qquickattachedpropertypropagatorprivate.html

    Returns
    -------

    Optional[QtPrivate.QQuickAttachedPropertyPropagator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAttachedPropertyPropagator
    #      *QtPrivate::QQuickAttachedPropertyPropagatorPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN9QtPrivate39QQuickAttachedPropertyPropagatorPrivate6q_fun'
        'cEv',
    )
    return QtPrivate.QQuickAttachedPropertyPropagator._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void
    QtPrivate::QQuickAttachedPropertyPropagatorPrivate::init()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qquickattachedpropertypropagatorprivate.html
    """
    #  void QtPrivate::QQuickAttachedPropertyPropagatorPrivate::init()
    self.uglySide.call(
        'ritual_ZN9QtPrivate39QQuickAttachedPropertyPropagatorPrivate4initE'
        'v',
    )

  @overload(QObject)
  @overload(NoneType)
  def attachTo(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void
    QtPrivate::QQuickAttachedPropertyPropagatorPrivate::attachTo(QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qquickattachedpropertypropagatorprivate.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtPrivate::QQuickAttachedPropertyPropagatorPrivate::attachTo(
    #      QObject *object)
    self.uglySide.call(
        'ritual_ZN9QtPrivate39QQuickAttachedPropertyPropagatorPrivate8attac'
        'hToEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  @overload(QObject)
  @overload(NoneType)
  def detachFrom(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void
    QtPrivate::QQuickAttachedPropertyPropagatorPrivate::detachFrom(QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qquickattachedpropertypropagatorprivate.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtPrivate::QQuickAttachedPropertyPropagatorPrivate::detachFrom(
    #      QObject *object)
    self.uglySide.call(
        'ritual_ZN9QtPrivate39QQuickAttachedPropertyPropagatorPrivate10deta'
        'chFromEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def itemWindowChanged(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void
    QtPrivate::QQuickAttachedPropertyPropagatorPrivate::itemWindowChanged(
    QQuickWindow *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qquickattachedpropertypropagatorprivate.html

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtPrivate::QQuickAttachedPropertyPropagatorPrivate::
    #      itemWindowChanged(QQuickWindow *window)
    self.uglySide.call(
        'ritual_ZN9QtPrivate39QQuickAttachedPropertyPropagatorPrivate17item'
        'WindowChangedEP12QQuickWindow',
        self._addressOf(window),
    )

  @overload(QWindow)
  @overload(NoneType)
  def transientParentWindowChanged(
      self,
      newTransientParent: Optional[QWindow],
  ) -> None:
    """
    Calls Qt's 'void QtPrivate::QQuickAttachedPropertyPropagatorPrivate::
    transientParentWindowChanged(QWindow *newTransientParent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qquickattachedpropertypropagatorprivate.html

    Parameters
    ----------

    newTransientParent : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtPrivate::QQuickAttachedPropertyPropagatorPrivate::
    #      transientParentWindowChanged(QWindow *newTransientParent)
    self.uglySide.call(
        'ritual_ZN9QtPrivate39QQuickAttachedPropertyPropagatorPrivate28tran'
        'sientParentWindowChangedEP7QWindow',
        self._addressOf(newTransientParent),
    )

  @overload(QQuickItem, QQuickItem)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  def itemParentChanged(
      self,
      item: Optional[QQuickItem],
      parent: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void
    QtPrivate::QQuickAttachedPropertyPropagatorPrivate::itemParentChanged(
    QQuickItem *item, QQuickItem *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qquickattachedpropertypropagatorprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QtPrivate::QQuickAttachedPropertyPropagatorPrivate::
    #      itemParentChanged(QQuickItem *item, QQuickItem *parent)
    ritual = (
        'ritual_ZN9QtPrivate39QQuickAttachedPropertyPropagatorPrivate17item'
        'ParentChangedEP10QQuickItemS2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QtPrivate39QQuickAttachedPropertyPropagatorPrivate'
          '17itemParentChangedEP10QQuickItemS2_')
    self.uglySide.call(
        ritual, self._addressOf(item), self._addressOf(parent),
    )

  @staticmethod
  def findAttachedChildren(*__, **_) -> Never:
    """
    Qt's 'QList<QQuickAttachedPropertyPropagator *>
    QtPrivate::QQuickAttachedPropertyPropagatorPrivate::findAttachedChildren(
    const QMetaObject *attachedType, QObject *object)': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QtPrivate.QQuickAttachedPropertyPropagatorPrivate.findAttachedChil"
        "dren' has no cute function yet. Qt's "
        "'QList<QQuickAttachedPropertyPropagator *> "
        "QtPrivate::QQuickAttachedPropertyPropagatorPrivate::findAttachedChi"
        "ldren(const QMetaObject *attachedType, QObject *object)': gives a "
        "type Python has no way to take yet.")
