"""
QQuickPropertyAction binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickanimation_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickPropertyAction to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickAbstractAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from . import QQuickPropertyActionPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPropertyAction(QQuickAbstractAnimation):
  """
  The cute side of Qt's QQuickPropertyAction: a plain Python object standing
  in front of one C++ QQuickPropertyAction.

  It is built on the cute 'QQuickAbstractAnimation', as Qt's
  QQuickPropertyAction is built on Qt's QQuickAbstractAnimation, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPropertyAction that has a ritual and that
  Python can call so far, 15 names in all: 'metaObject', 'tr', 'd_func',
  'target', 'setTargetObject', 'property', 'setProperty', 'properties',
  'setProperties', 'value', 'setValue', 'valueChanged', 'propertiesChanged',
  'targetChanged', 'propertyChanged'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPropertyAction::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickPropertyAction::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickPropertyActionPrivate *QQuickPropertyAction::d_func()
    const': takes in Python what 'QQuickPropertyActionPrivate
    *QQuickPropertyAction::d_func()' takes.
  - Qt's 'QQuickPropertyAction::~QQuickPropertyAction()': the destructor:
    Python never removes a C++ QQuickPropertyAction.
  - Qt's 'QQmlListProperty<QObject> QQuickPropertyAction::targets()': gives a
    type Python has no way to take yet.
  - Qt's 'QQmlListProperty<QObject> QQuickPropertyAction::exclude()': gives a
    type Python has no way to take yet.
  - Qt's 'QAbstractAnimationJob
    *QQuickPropertyAction::transition(QQuickStateActions &actions,
    QQmlProperties &modified, TransitionDirection direction, QObject
    *defaultTarget)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 25 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickPropertyAction is created at the first use, not by
    'QQuickPropertyAction(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPropertyAction.
  - Qt tells when it has removed the C++ QQuickPropertyAction. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickPropertyAction that has no cute function yet,
    'exclude', 'targets', holds a function that raises 'NotImplementedError',
    and its docstring says why.
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
    Calls Qt's 'QString QQuickPropertyAction::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpropertyaction.html#tr

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
    #  QString QQuickPropertyAction::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuickPropertyAction2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPropertyAction'

  #  A C++ QQuickPropertyAction Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPropertyAction'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPropertyAction::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyaction.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPropertyAction::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickPropertyAction10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def target(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQuickPropertyAction::target() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpropertyaction.html#target

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQuickPropertyAction::target() const
    address = self.uglySide.call('ritual_ZNK20QQuickPropertyAction6targetEv')
    return QObject._cuteAt(address)

  def property(self) -> str:
    """
    Calls Qt's 'QString QQuickPropertyAction::property() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpropertyaction.html#property

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickPropertyAction::property() const
    return self.uglySide.call('ritual_ZNK20QQuickPropertyAction8propertyEv')

  def properties(self) -> str:
    """
    Calls Qt's 'QString QQuickPropertyAction::properties() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyaction.html#properties

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickPropertyAction::properties() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickPropertyAction10propertiesEv',
    )

  def value(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickPropertyAction::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpropertyaction.html#value

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickPropertyAction::value() const
    address = self.uglySide.call('ritual_ZNK20QQuickPropertyAction5valueEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def setTargetObject(self, a0: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickPropertyAction::setTargetObject(QObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyaction.html#setTargetObject

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPropertyAction::setTargetObject(QObject *a0)
    self.uglySide.call(
        'ritual_ZN20QQuickPropertyAction15setTargetObjectEP7QObject',
        self._addressOf(a0, 'QObject'),
    )

  @overload(str)
  def setProperty(self, a0: str) -> None:
    """
    Calls Qt's 'void QQuickPropertyAction::setProperty(const QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyaction.html#setProperty

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickPropertyAction::setProperty(const QString &a0)
    self.uglySide.call(
        'ritual_ZN20QQuickPropertyAction11setPropertyERK7QString', a0,
    )

  @overload(str)
  def setProperties(self, a0: str) -> None:
    """
    Calls Qt's 'void QQuickPropertyAction::setProperties(const QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyaction.html#setProperties

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickPropertyAction::setProperties(const QString &a0)
    self.uglySide.call(
        'ritual_ZN20QQuickPropertyAction13setPropertiesERK7QString', a0,
    )

  @overload(QVariant)
  def setValue(self, a0: QVariant) -> None:
    """
    Calls Qt's 'void QQuickPropertyAction::setValue(const QVariant &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpropertyaction.html#setValue

    Parameters
    ----------

    a0 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickPropertyAction::setValue(const QVariant &a0)
    self.uglySide.call(
        'ritual_ZN20QQuickPropertyAction8setValueERK8QVariant',
        self._valueOf(a0),
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
    'QQuickPropertyAction::QQuickPropertyAction(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyaction.html#QQuickPropertyAction

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickPropertyAction::QQuickPropertyAction(QObject *parent)
    self._noteCreation(QQuickPropertyAction, lambda: Rituals.call(
        'ritual_ZN20QQuickPropertyActionC1EP7QObject',
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

  def d_func(self) -> Optional[QQuickPropertyActionPrivate]:
    """
    Calls Qt's 'QQuickPropertyActionPrivate *QQuickPropertyAction::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpropertyaction.html#d_func

    Returns
    -------

    Optional[QQuickPropertyActionPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPropertyActionPrivate *QQuickPropertyAction::d_func()
    address = self.uglySide.call('ritual_ZN20QQuickPropertyAction6d_funcEv')
    from . import QQuickPropertyActionPrivate
    return QQuickPropertyActionPrivate._cuteAt(address)

  @overload(QVariant)
  def valueChanged(self, a0: QVariant) -> None:
    """
    Calls Qt's 'void QQuickPropertyAction::valueChanged(const QVariant &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyaction.html#valueChanged

    Parameters
    ----------

    a0 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickPropertyAction::valueChanged(const QVariant &a0)
    self.uglySide.call(
        'ritual_ZN20QQuickPropertyAction12valueChangedERK8QVariant',
        self._valueOf(a0),
    )

  @overload(str)
  def propertiesChanged(self, a0: str) -> None:
    """
    Calls Qt's 'void QQuickPropertyAction::propertiesChanged(const QString
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyaction.html#propertiesChanged

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickPropertyAction::propertiesChanged(const QString &a0)
    self.uglySide.call(
        'ritual_ZN20QQuickPropertyAction17propertiesChangedERK7QString', a0,
    )

  def targetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPropertyAction::targetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyaction.html#targetChanged
    """
    #  void QQuickPropertyAction::targetChanged()
    self.uglySide.call('ritual_ZN20QQuickPropertyAction13targetChangedEv')

  def propertyChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPropertyAction::propertyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyaction.html#propertyChanged
    """
    #  void QQuickPropertyAction::propertyChanged()
    self.uglySide.call('ritual_ZN20QQuickPropertyAction15propertyChangedEv')

  @staticmethod
  def exclude(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QQuickPropertyAction::exclude()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickPropertyAction.exclude' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QQuickPropertyAction::exclude()': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def targets(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QQuickPropertyAction::targets()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickPropertyAction.targets' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QQuickPropertyAction::targets()': gives "
        "a type Python has no way to take yet.")
