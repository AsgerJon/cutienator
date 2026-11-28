"""
QScxmlInvokedServices binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxmlQml/6.12.0/QtScxmlQml/private/invokedservices_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QScxmlInvokedServices to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QMap, QObject
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from ..QtScxml import QScxmlStateMachine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QScxmlStateMachine = WAIT['QScxmlStateMachine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScxmlInvokedServices(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QScxmlInvokedServices: a plain Python object standing
  in front of one C++ QScxmlInvokedServices.

  It is built on the cute 'QObject', as Qt's QScxmlInvokedServices is built
  on Qt's QObject, and has everything that class has. It is built on the cute
  'QQmlParserStatus' as well, as Qt's QScxmlInvokedServices is built on Qt's
  QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QScxmlInvokedServices that has a ritual and that
  Python can call so far, 12 names in all: 'metaObject', 'tr', 'children',
  'stateMachine', 'setStateMachine', 'childrenChanged',
  'stateMachineChanged', 'classBegin', 'componentComplete',
  'childrenActualCalculation', '_qt_property_m_stateMachine_offset',
  '_qt_property_m_children_offset'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QScxmlInvokedServices::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QScxmlInvokedServices::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QBindable<QVariantMap> QScxmlInvokedServices::bindableChildren()':
    gives a type Python has no way to take yet.
  - Qt's 'QBindable<QScxmlStateMachine *>
    QScxmlInvokedServices::bindableStateMachine()': gives a type Python has
    no way to take yet.
  - Qt's 'QQmlListProperty<QObject> QScxmlInvokedServices::qmlChildren()':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QScxmlInvokedServices is created at the first use, not by
    'QScxmlInvokedServices(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScxmlInvokedServices.
  - Qt tells when it has removed the C++ QScxmlInvokedServices. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QScxmlInvokedServices that has no cute function yet,
    'bindableChildren', 'bindableStateMachine', 'qmlChildren', holds a
    function that raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QScxmlInvokedServices::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlinvokedservices.html#tr

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
    #  QString QScxmlInvokedServices::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QScxmlInvokedServices2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def _qt_property_m_stateMachine_offset() -> int:
    """
    Calls Qt's 'size_t
    QScxmlInvokedServices::_qt_property_m_stateMachine_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinvokedservices.html
    """
    #  size_t QScxmlInvokedServices::_qt_property_m_stateMachine_offset()
    return Rituals.call(
        'ritual_ZN21QScxmlInvokedServices34_qt_property_m_stateMachine_offs'
        'etEv',
    )

  @staticmethod
  def _qt_property_m_children_offset() -> int:
    """
    Calls Qt's 'size_t
    QScxmlInvokedServices::_qt_property_m_children_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinvokedservices.html
    """
    #  size_t QScxmlInvokedServices::_qt_property_m_children_offset()
    return Rituals.call(
        'ritual_ZN21QScxmlInvokedServices30_qt_property_m_children_offsetEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScxmlInvokedServices'

  #  Qt's QScxmlInvokedServices is built on more than one class. The part of
  #  a C++ QScxmlInvokedServices that belongs to a class after the first
  #  begins somewhere inside the object, and the ritual named for that class
  #  gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus':
          'ritual_cast_QScxmlInvokedServices_QQmlParserStatus',
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
    Calls Qt's 'const QMetaObject *QScxmlInvokedServices::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinvokedservices.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QScxmlInvokedServices::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QScxmlInvokedServices10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def stateMachine(self) -> Optional[QScxmlStateMachine]:
    """
    Calls Qt's 'QScxmlStateMachine *QScxmlInvokedServices::stateMachine()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinvokedservices.html#stateMachine

    Returns
    -------

    Optional[QScxmlStateMachine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScxmlStateMachine *QScxmlInvokedServices::stateMachine() const
    address = self.uglySide.call(
        'ritual_ZNK21QScxmlInvokedServices12stateMachineEv',
    )
    from ..QtScxml import QScxmlStateMachine
    return QScxmlStateMachine._cuteAt(address)

  def childrenActualCalculation(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap
    QScxmlInvokedServices::childrenActualCalculation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinvokedservices.html

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap QScxmlInvokedServices::childrenActualCalculation() const
    address = self.uglySide.call(
        'ritual_ZNK21QScxmlInvokedServices25childrenActualCalculationEv',
    )
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QScxmlStateMachine)
  @overload(NoneType)
  def setStateMachine(
      self,
      stateMachine: Optional[QScxmlStateMachine],
  ) -> None:
    """
    Calls Qt's 'void
    QScxmlInvokedServices::setStateMachine(QScxmlStateMachine
    *stateMachine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinvokedservices.html#setStateMachine

    Parameters
    ----------

    stateMachine : Optional[QScxmlStateMachine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScxmlInvokedServices::setStateMachine(QScxmlStateMachine
    #      *stateMachine)
    self.uglySide.call(
        'ritual_ZN21QScxmlInvokedServices15setStateMachineEP18QScxmlStateMa'
        'chine',
        self._addressOf(stateMachine),
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
    'QScxmlInvokedServices::QScxmlInvokedServices(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinvokedservices.html#QScxmlInvokedServices

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QScxmlInvokedServices::QScxmlInvokedServices(QObject *parent)
    self._noteCreation(QScxmlInvokedServices, lambda: Rituals.call(
        'ritual_ZN21QScxmlInvokedServicesC1EP7QObject',
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

  def children(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap QScxmlInvokedServices::children()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinvokedservices.html#children

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap QScxmlInvokedServices::children()
    address = self.uglySide.call(
        'ritual_ZN21QScxmlInvokedServices8childrenEv',
    )
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  def childrenChanged(self) -> None:
    """
    Calls Qt's 'void QScxmlInvokedServices::childrenChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinvokedservices.html#childrenChanged
    """
    #  void QScxmlInvokedServices::childrenChanged()
    self.uglySide.call('ritual_ZN21QScxmlInvokedServices15childrenChangedEv')

  def stateMachineChanged(self) -> None:
    """
    Calls Qt's 'void QScxmlInvokedServices::stateMachineChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinvokedservices.html#stateMachineChanged
    """
    #  void QScxmlInvokedServices::stateMachineChanged()
    self.uglySide.call(
        'ritual_ZN21QScxmlInvokedServices19stateMachineChangedEv',
    )

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QScxmlInvokedServices::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinvokedservices.html#classBegin
    """
    #  void QScxmlInvokedServices::classBegin()
    ritual = 'ritual_ZN21QScxmlInvokedServices10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QScxmlInvokedServices10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QScxmlInvokedServices::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinvokedservices.html#componentComplete
    """
    #  void QScxmlInvokedServices::componentComplete()
    ritual = 'ritual_ZN21QScxmlInvokedServices17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QScxmlInvokedServices17componentCompleteEv'
    self.uglySide.call(ritual)

  @staticmethod
  def bindableChildren(*__, **_) -> Never:
    """
    Qt's 'QBindable<QVariantMap> QScxmlInvokedServices::bindableChildren()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QScxmlInvokedServices.bindableChildren' has no cute function yet. "
        "Qt's 'QBindable<QVariantMap> "
        "QScxmlInvokedServices::bindableChildren()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def bindableStateMachine(*__, **_) -> Never:
    """
    Qt's 'QBindable<QScxmlStateMachine *>
    QScxmlInvokedServices::bindableStateMachine()': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QScxmlInvokedServices.bindableStateMachine' has no cute function "
        "yet. Qt's 'QBindable<QScxmlStateMachine *> "
        "QScxmlInvokedServices::bindableStateMachine()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def qmlChildren(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QScxmlInvokedServices::qmlChildren()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QScxmlInvokedServices.qmlChildren' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QScxmlInvokedServices::qmlChildren()': "
        "gives a type Python has no way to take yet.")
