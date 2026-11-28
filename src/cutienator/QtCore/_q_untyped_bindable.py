"""
QUntypedBindable binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qproperty.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QtPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QMetaProperty, QMetaType, QObject
  from . import QPropertyBindingSourceLocation, QPropertyObserver
  from . import QUntypedPropertyBinding, QUntypedPropertyData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaProperty = WAIT['QMetaProperty']
  QObject = WAIT['QObject']
  QPropertyBindingSourceLocation = WAIT['QPropertyBindingSourceLocation']
  QPropertyObserver = WAIT['QPropertyObserver']
  QUntypedPropertyBinding = WAIT['QUntypedPropertyBinding']
  QUntypedPropertyData = WAIT['QUntypedPropertyData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QUntypedBindable(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QUntypedBindable: a plain Python object standing in
  front of one C++ QUntypedBindable.

  C++ hands a QUntypedBindable around as a copy, so every C++
  QUntypedBindable behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QUntypedBindable that has a ritual and that Python
  can call so far, 10 names in all: 'isValid', 'isBindable', 'isReadOnly',
  'makeBinding', 'takeBinding', 'observe', 'binding', 'setBinding',
  'hasBinding', 'metaType'. It can be made from Python, in 4 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QUntypedBindable::~QUntypedBindable()': the destructor: Python
    removes its C++ QUntypedBindable by it, and has no other use for it.

  What has no ritual
  ------------------

  4 of the 19 functions Qt declares: 4 a template.

  What to expect
  --------------

  - The C++ QUntypedBindable is created at the first use, not by
    'QUntypedBindable(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QUntypedBindable back gives a copy the ritual made
    for Python, in a new cute QUntypedBindable.
  - Each name of Qt's QUntypedBindable that has no cute function yet,
    'addNotifier', 'onValueChanged', 'subscribe', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QUntypedBindable'

  #  Qt's '~QUntypedBindable()'. Naming it makes this a value class: Python
  #  owns every C++ QUntypedBindable behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QUntypedBindableD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QUntypedBindable::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/quntypedbindable.html#isValid
    """
    #  bool QUntypedBindable::isValid() const
    return self.uglySide.call('ritual_ZNK16QUntypedBindable7isValidEv')

  def isBindable(self) -> bool:
    """
    Calls Qt's 'bool QUntypedBindable::isBindable() const'.

    Qt's own words: https://doc.qt.io/qt-6/quntypedbindable.html#isBindable
    """
    #  bool QUntypedBindable::isBindable() const
    return self.uglySide.call('ritual_ZNK16QUntypedBindable10isBindableEv')

  def isReadOnly(self) -> bool:
    """
    Calls Qt's 'bool QUntypedBindable::isReadOnly() const'.

    Qt's own words: https://doc.qt.io/qt-6/quntypedbindable.html#isReadOnly
    """
    #  bool QUntypedBindable::isReadOnly() const
    return self.uglySide.call('ritual_ZNK16QUntypedBindable10isReadOnlyEv')

  @overload(QPropertyBindingSourceLocation)
  def makeBinding(
      self,
      location: QPropertyBindingSourceLocation,
  ) -> QUntypedPropertyBinding:
    """
    Calls Qt's 'QUntypedPropertyBinding QUntypedBindable::makeBinding(const
    QPropertyBindingSourceLocation &location) const'.

    Qt's own words: https://doc.qt.io/qt-6/quntypedbindable.html#makeBinding

    Parameters
    ----------

    location : QPropertyBindingSourceLocation
      Passed on as a value: Qt reads the C++ QPropertyBindingSourceLocation,
      which stays Python's own.

    Returns
    -------

    QUntypedPropertyBinding
      A new cute QUntypedPropertyBinding around the copy Qt gave back. Python
      owns it.
    """
    #  QUntypedPropertyBinding QUntypedBindable::makeBinding(const
    #      QPropertyBindingSourceLocation &location) const
    address = self.uglySide.call(
        'ritual_ZNK16QUntypedBindable11makeBindingERK30QPropertyBindingSour'
        'ceLocation',
        self._valueOf(location),
    )
    from . import QUntypedPropertyBinding
    return QUntypedPropertyBinding._cuteOwning(address)

  def binding(self) -> QUntypedPropertyBinding:
    """
    Calls Qt's 'QUntypedPropertyBinding QUntypedBindable::binding() const'.

    Qt's own words: https://doc.qt.io/qt-6/quntypedbindable.html#binding

    Returns
    -------

    QUntypedPropertyBinding
      A new cute QUntypedPropertyBinding around the copy Qt gave back. Python
      owns it.
    """
    #  QUntypedPropertyBinding QUntypedBindable::binding() const
    address = self.uglySide.call('ritual_ZNK16QUntypedBindable7bindingEv')
    from . import QUntypedPropertyBinding
    return QUntypedPropertyBinding._cuteOwning(address)

  def hasBinding(self) -> bool:
    """
    Calls Qt's 'bool QUntypedBindable::hasBinding() const'.

    Qt's own words: https://doc.qt.io/qt-6/quntypedbindable.html#hasBinding
    """
    #  bool QUntypedBindable::hasBinding() const
    return self.uglySide.call('ritual_ZNK16QUntypedBindable10hasBindingEv')

  def metaType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QUntypedBindable::metaType() const'.

    Qt's own words: https://doc.qt.io/qt-6/quntypedbindable.html#metaType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QUntypedBindable::metaType() const
    address = self.uglySide.call('ritual_ZNK16QUntypedBindable8metaTypeEv')
    from . import QMetaType
    return QMetaType._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUntypedPropertyBinding)
  def setBinding(self, binding: QUntypedPropertyBinding) -> bool:
    """
    Calls Qt's 'bool QUntypedBindable::setBinding(const
    QUntypedPropertyBinding &binding)'.

    Qt's own words: https://doc.qt.io/qt-6/quntypedbindable.html#setBinding

    Parameters
    ----------

    binding : QUntypedPropertyBinding
      Passed on as a value: Qt reads the C++ QUntypedPropertyBinding, which
      stays Python's own.
    """
    #  bool QUntypedBindable::setBinding(const QUntypedPropertyBinding
    #      &binding)
    return self.uglySide.call(
        'ritual_ZN16QUntypedBindable10setBindingERK23QUntypedPropertyBindin'
        'g',
        self._valueOf(binding),
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

  @overload(QUntypedPropertyData, WAIT['QtPrivate.QBindableInterface'])
  @overload(QUntypedPropertyData, NoneType)
  @overload(NoneType, WAIT['QtPrivate.QBindableInterface'])
  @overload(NoneType, NoneType)
  def __init__(
      self,
      d: Optional[QUntypedPropertyData],
      i: Optional[QtPrivate.QBindableInterface],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QUntypedBindable::QUntypedBindable(QUntypedPropertyData *d, const
    QtPrivate::QBindableInterface *i)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/quntypedbindable.html#QUntypedBindable

    Parameters
    ----------

    d : Optional[QUntypedPropertyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    i : Optional[QtPrivate.QBindableInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QUntypedBindable::QUntypedBindable(QUntypedPropertyData *d, const
    #      QtPrivate::QBindableInterface *i)
    self._noteCreation(QUntypedBindable, lambda: Rituals.call(
        'ritual_ZN16QUntypedBindableC1EP20QUntypedPropertyDataPKN9QtPrivate'
        '18QBindableInterfaceE',
        self._addressOf(d), self._addressOf(i),
    ))

  @overload(QObject, QMetaProperty, WAIT['QtPrivate.QBindableInterface'])
  @overload(QObject, QMetaProperty, NoneType)
  @overload(NoneType, QMetaProperty, WAIT['QtPrivate.QBindableInterface'])
  @overload(NoneType, QMetaProperty, NoneType)
  def __init__(
      self,
      obj: Optional[QObject],
      property: QMetaProperty,
      i: Optional[QtPrivate.QBindableInterface],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QUntypedBindable::QUntypedBindable(QObject *obj, const QMetaProperty
    &property, const QtPrivate::QBindableInterface *i)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/quntypedbindable.html#QUntypedBindable

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    property : QMetaProperty
      Passed on as a value: Qt reads the C++ QMetaProperty, which stays
      Python's own.

    i : Optional[QtPrivate.QBindableInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QUntypedBindable::QUntypedBindable(QObject *obj, const QMetaProperty
    #      &property, const QtPrivate::QBindableInterface *i)
    self._noteCreation(QUntypedBindable, lambda: Rituals.call(
        'ritual_ZN16QUntypedBindableC1EP7QObjectRK13QMetaPropertyPKN9QtPriv'
        'ate18QBindableInterfaceE',
        self._addressOf(obj, 'QObject'), self._valueOf(property),
        self._addressOf(i),
    ))

  @overload(QObject, str, WAIT['QtPrivate.QBindableInterface'])
  @overload(QObject, str, NoneType)
  @overload(QObject, NoneType, WAIT['QtPrivate.QBindableInterface'])
  @overload(QObject, NoneType, NoneType)
  @overload(NoneType, str, WAIT['QtPrivate.QBindableInterface'])
  @overload(NoneType, str, NoneType)
  @overload(NoneType, NoneType, WAIT['QtPrivate.QBindableInterface'])
  @overload(NoneType, NoneType, NoneType)
  def __init__(
      self,
      obj: Optional[QObject],
      property: Optional[str],
      i: Optional[QtPrivate.QBindableInterface],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QUntypedBindable::QUntypedBindable(QObject *obj, const char *property,
    const QtPrivate::QBindableInterface *i)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/quntypedbindable.html#QUntypedBindable

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    property : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    i : Optional[QtPrivate.QBindableInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QUntypedBindable::QUntypedBindable(QObject *obj, const char *property,
    #      const QtPrivate::QBindableInterface *i)
    self._noteCreation(QUntypedBindable, lambda: Rituals.call(
        'ritual_ZN16QUntypedBindableC1EP7QObjectPKcPKN9QtPrivate18QBindable'
        'InterfaceE',
        self._addressOf(obj, 'QObject'), self._bytesOf(property),
        self._addressOf(i),
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QUntypedBindable::QUntypedBindable()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/quntypedbindable.html#QUntypedBindable
    """
    #  QUntypedBindable::QUntypedBindable()
    self._noteCreation(QUntypedBindable, lambda: Rituals.call(
        'ritual_ZN16QUntypedBindableC1Ev',
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

  def takeBinding(self) -> QUntypedPropertyBinding:
    """
    Calls Qt's 'QUntypedPropertyBinding QUntypedBindable::takeBinding()'.

    Qt's own words: https://doc.qt.io/qt-6/quntypedbindable.html#takeBinding

    Returns
    -------

    QUntypedPropertyBinding
      A new cute QUntypedPropertyBinding around the copy Qt gave back. Python
      owns it.
    """
    #  QUntypedPropertyBinding QUntypedBindable::takeBinding()
    address = self.uglySide.call(
        'ritual_ZN16QUntypedBindable11takeBindingEv',
    )
    from . import QUntypedPropertyBinding
    return QUntypedPropertyBinding._cuteOwning(address)

  @overload(QPropertyObserver)
  @overload(NoneType)
  def observe(self, observer: Optional[QPropertyObserver]) -> None:
    """
    Calls Qt's 'void QUntypedBindable::observe(QPropertyObserver *observer)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/quntypedbindable.html#observe

    Parameters
    ----------

    observer : Optional[QPropertyObserver]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QUntypedBindable::observe(QPropertyObserver *observer) const
    self.uglySide.call(
        'ritual_ZNK16QUntypedBindable7observeEP17QPropertyObserver',
        self._addressOf(observer),
    )

  @staticmethod
  def addNotifier(*__, **_) -> Never:
    """
    Qt's 'QUntypedBindable::addNotifier': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QUntypedBindable.addNotifier' has no cute function yet. Qt's "
        "'QUntypedBindable::addNotifier': a template: a pattern and no "
        "single function.")

  @staticmethod
  def onValueChanged(*__, **_) -> Never:
    """
    Qt's 'QUntypedBindable::onValueChanged': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QUntypedBindable.onValueChanged' has no cute function yet. Qt's "
        "'QUntypedBindable::onValueChanged': a template: a pattern and no "
        "single function.")

  @staticmethod
  def subscribe(*__, **_) -> Never:
    """
    Qt's 'QUntypedBindable::subscribe': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QUntypedBindable.subscribe' has no cute function yet. Qt's "
        "'QUntypedBindable::subscribe': a template: a pattern and no single "
        "function.")
