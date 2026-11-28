"""
QDesignerMetaObjectInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/abstractintrospection_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QDesignerMetaObjectInterface to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QDesignerMetaEnumInterface, QDesignerMetaMethodInterface
  from . import QDesignerMetaPropertyInterface


class QDesignerMetaObjectInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDesignerMetaObjectInterface: a plain Python object
  standing in front of one C++ QDesignerMetaObjectInterface.

  What exists
  -----------

  Every function of Qt's QDesignerMetaObjectInterface that has a ritual and
  that Python can call so far, 17 names in all: 'className', 'enumerator',
  'enumeratorCount', 'enumeratorOffset', 'indexOfEnumerator',
  'indexOfMethod', 'indexOfProperty', 'indexOfSignal', 'indexOfSlot',
  'method', 'methodCount', 'methodOffset', 'property', 'propertyCount',
  'propertyOffset', 'superClass', 'userProperty'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDesignerMetaObjectInterface::~QDesignerMetaObjectInterface()': the
    destructor: Python never removes a C++ QDesignerMetaObjectInterface.

  What has no ritual
  ------------------

  4 of the 23 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QDesignerMetaObjectInterface is created at the first use, not by
    'QDesignerMetaObjectInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerMetaObjectInterface.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerMetaObjectInterface'

  #  A C++ QDesignerMetaObjectInterface Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerMetaObjectInterface'

  #  The functions Qt calls itself that QDesignerMetaObjectInterface is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'className': (
          ('_ZNK28QDesignerMetaObjectInterface9classNameEv',
           ('address', 'text', ''),
           ()),
      ),
      'enumerator': (
          ('_ZNK28QDesignerMetaObjectInterface10enumeratorEi',
           ('address', 'address', 'QtDesigner:QDesignerMetaEnumInterface'),
           (
               ('int', 'number', ''),
           )),
      ),
      'enumeratorCount': (
          ('_ZNK28QDesignerMetaObjectInterface15enumeratorCountEv',
           ('int', 'number', ''),
           ()),
      ),
      'enumeratorOffset': (
          ('_ZNK28QDesignerMetaObjectInterface16enumeratorOffsetEv',
           ('int', 'number', ''),
           ()),
      ),
      'indexOfEnumerator': (
          ('_ZNK28QDesignerMetaObjectInterface17indexOfEnumeratorERK7QStrin'
           'g',
           ('int', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'indexOfMethod': (
          ('_ZNK28QDesignerMetaObjectInterface13indexOfMethodERK7QString',
           ('int', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'indexOfProperty': (
          ('_ZNK28QDesignerMetaObjectInterface15indexOfPropertyERK7QString',
           ('int', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'indexOfSignal': (
          ('_ZNK28QDesignerMetaObjectInterface13indexOfSignalERK7QString',
           ('int', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'indexOfSlot': (
          ('_ZNK28QDesignerMetaObjectInterface11indexOfSlotERK7QString',
           ('int', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'method': (
          ('_ZNK28QDesignerMetaObjectInterface6methodEi',
           ('address', 'address', 'QtDesigner:QDesignerMetaMethodInterface'),
           (
               ('int', 'number', ''),
           )),
      ),
      'methodCount': (
          ('_ZNK28QDesignerMetaObjectInterface11methodCountEv',
           ('int', 'number', ''),
           ()),
      ),
      'methodOffset': (
          ('_ZNK28QDesignerMetaObjectInterface12methodOffsetEv',
           ('int', 'number', ''),
           ()),
      ),
      'property': (
          ('_ZNK28QDesignerMetaObjectInterface8propertyEi',
           ('address', 'address',
            'QtDesigner:QDesignerMetaPropertyInterface'),
           (
               ('int', 'number', ''),
           )),
      ),
      'propertyCount': (
          ('_ZNK28QDesignerMetaObjectInterface13propertyCountEv',
           ('int', 'number', ''),
           ()),
      ),
      'propertyOffset': (
          ('_ZNK28QDesignerMetaObjectInterface14propertyOffsetEv',
           ('int', 'number', ''),
           ()),
      ),
      'superClass': (
          ('_ZNK28QDesignerMetaObjectInterface10superClassEv',
           ('address', 'address', 'QtDesigner:QDesignerMetaObjectInterface'),
           ()),
      ),
      'userProperty': (
          ('_ZNK28QDesignerMetaObjectInterface12userPropertyEv',
           ('address', 'address',
            'QtDesigner:QDesignerMetaPropertyInterface'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def className(self) -> str:
    """
    Calls Qt's 'QString QDesignerMetaObjectInterface::className() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetaobjectinterface.html#className

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerMetaObjectInterface::className() const
    return self.uglySide.call(
        'ritual_ZNK28QDesignerMetaObjectInterface9classNameEv',
    )

  @overload(int)
  def enumerator(self, index: int) -> Optional[QDesignerMetaEnumInterface]:
    """
    Calls Qt's 'const QDesignerMetaEnumInterface
    *QDesignerMetaObjectInterface::enumerator(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetaobjectinterface.html#enumerator

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QDesignerMetaEnumInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QDesignerMetaEnumInterface
    #      *QDesignerMetaObjectInterface::enumerator(int index) const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerMetaObjectInterface10enumeratorEi', index,
    )
    from . import QDesignerMetaEnumInterface
    return QDesignerMetaEnumInterface._cuteAt(address)

  def enumeratorCount(self) -> int:
    """
    Calls Qt's 'int QDesignerMetaObjectInterface::enumeratorCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetaobjectinterface.html#enumeratorCount
    """
    #  int QDesignerMetaObjectInterface::enumeratorCount() const
    return self.uglySide.call(
        'ritual_ZNK28QDesignerMetaObjectInterface15enumeratorCountEv',
    )

  def enumeratorOffset(self) -> int:
    """
    Calls Qt's 'int QDesignerMetaObjectInterface::enumeratorOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetaobjectinterface.html#enumeratorOffset
    """
    #  int QDesignerMetaObjectInterface::enumeratorOffset() const
    return self.uglySide.call(
        'ritual_ZNK28QDesignerMetaObjectInterface16enumeratorOffsetEv',
    )

  @overload(str)
  def indexOfEnumerator(self, name: str) -> int:
    """
    Calls Qt's 'int QDesignerMetaObjectInterface::indexOfEnumerator(const
    QString &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetaobjectinterface.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QDesignerMetaObjectInterface::indexOfEnumerator(const QString
    #      &name) const
    return self.uglySide.call(
        'ritual_ZNK28QDesignerMetaObjectInterface17indexOfEnumeratorERK7QSt'
        'ring',
        name,
    )

  @overload(str)
  def indexOfMethod(self, method: str) -> int:
    """
    Calls Qt's 'int QDesignerMetaObjectInterface::indexOfMethod(const QString
    &method) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetaobjectinterface.html#indexOfMethod

    Parameters
    ----------

    method : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QDesignerMetaObjectInterface::indexOfMethod(const QString &method)
    #      const
    return self.uglySide.call(
        'ritual_ZNK28QDesignerMetaObjectInterface13indexOfMethodERK7QString',
        method,
    )

  @overload(str)
  def indexOfProperty(self, name: str) -> int:
    """
    Calls Qt's 'int QDesignerMetaObjectInterface::indexOfProperty(const
    QString &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetaobjectinterface.html#indexOfProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QDesignerMetaObjectInterface::indexOfProperty(const QString &name)
    #      const
    return self.uglySide.call(
        'ritual_ZNK28QDesignerMetaObjectInterface15indexOfPropertyERK7QStri'
        'ng',
        name,
    )

  @overload(str)
  def indexOfSignal(self, signal: str) -> int:
    """
    Calls Qt's 'int QDesignerMetaObjectInterface::indexOfSignal(const QString
    &signal) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetaobjectinterface.html#indexOfSignal

    Parameters
    ----------

    signal : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QDesignerMetaObjectInterface::indexOfSignal(const QString &signal)
    #      const
    return self.uglySide.call(
        'ritual_ZNK28QDesignerMetaObjectInterface13indexOfSignalERK7QString',
        signal,
    )

  @overload(str)
  def indexOfSlot(self, slot: str) -> int:
    """
    Calls Qt's 'int QDesignerMetaObjectInterface::indexOfSlot(const QString
    &slot) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetaobjectinterface.html#indexOfSlot

    Parameters
    ----------

    slot : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QDesignerMetaObjectInterface::indexOfSlot(const QString &slot)
    #      const
    return self.uglySide.call(
        'ritual_ZNK28QDesignerMetaObjectInterface11indexOfSlotERK7QString',
        slot,
    )

  @overload(int)
  def method(self, index: int) -> Optional[QDesignerMetaMethodInterface]:
    """
    Calls Qt's 'const QDesignerMetaMethodInterface
    *QDesignerMetaObjectInterface::method(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetaobjectinterface.html#method

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QDesignerMetaMethodInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QDesignerMetaMethodInterface
    #      *QDesignerMetaObjectInterface::method(int index) const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerMetaObjectInterface6methodEi', index,
    )
    from . import QDesignerMetaMethodInterface
    return QDesignerMetaMethodInterface._cuteAt(address)

  def methodCount(self) -> int:
    """
    Calls Qt's 'int QDesignerMetaObjectInterface::methodCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetaobjectinterface.html#methodCount
    """
    #  int QDesignerMetaObjectInterface::methodCount() const
    return self.uglySide.call(
        'ritual_ZNK28QDesignerMetaObjectInterface11methodCountEv',
    )

  def methodOffset(self) -> int:
    """
    Calls Qt's 'int QDesignerMetaObjectInterface::methodOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetaobjectinterface.html#methodOffset
    """
    #  int QDesignerMetaObjectInterface::methodOffset() const
    return self.uglySide.call(
        'ritual_ZNK28QDesignerMetaObjectInterface12methodOffsetEv',
    )

  @overload(int)
  def property(self, index: int) -> Optional[QDesignerMetaPropertyInterface]:
    """
    Calls Qt's 'const QDesignerMetaPropertyInterface
    *QDesignerMetaObjectInterface::property(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetaobjectinterface.html#property

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QDesignerMetaPropertyInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QDesignerMetaPropertyInterface
    #      *QDesignerMetaObjectInterface::property(int index) const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerMetaObjectInterface8propertyEi', index,
    )
    from . import QDesignerMetaPropertyInterface
    return QDesignerMetaPropertyInterface._cuteAt(address)

  def propertyCount(self) -> int:
    """
    Calls Qt's 'int QDesignerMetaObjectInterface::propertyCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetaobjectinterface.html#propertyCount
    """
    #  int QDesignerMetaObjectInterface::propertyCount() const
    return self.uglySide.call(
        'ritual_ZNK28QDesignerMetaObjectInterface13propertyCountEv',
    )

  def propertyOffset(self) -> int:
    """
    Calls Qt's 'int QDesignerMetaObjectInterface::propertyOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetaobjectinterface.html#propertyOffset
    """
    #  int QDesignerMetaObjectInterface::propertyOffset() const
    return self.uglySide.call(
        'ritual_ZNK28QDesignerMetaObjectInterface14propertyOffsetEv',
    )

  def superClass(self) -> Optional[QDesignerMetaObjectInterface]:
    """
    Calls Qt's 'const QDesignerMetaObjectInterface
    *QDesignerMetaObjectInterface::superClass() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetaobjectinterface.html#superClass

    Returns
    -------

    Optional[QDesignerMetaObjectInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QDesignerMetaObjectInterface
    #      *QDesignerMetaObjectInterface::superClass() const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerMetaObjectInterface10superClassEv',
    )
    return QDesignerMetaObjectInterface._cuteAt(address)

  def userProperty(self) -> Optional[QDesignerMetaPropertyInterface]:
    """
    Calls Qt's 'const QDesignerMetaPropertyInterface
    *QDesignerMetaObjectInterface::userProperty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetaobjectinterface.html#userProperty

    Returns
    -------

    Optional[QDesignerMetaPropertyInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QDesignerMetaPropertyInterface
    #      *QDesignerMetaObjectInterface::userProperty() const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerMetaObjectInterface12userPropertyEv',
    )
    from . import QDesignerMetaPropertyInterface
    return QDesignerMetaPropertyInterface._cuteAt(address)

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QDesignerMetaObjectInterface::QDesignerMetaObjectInterface()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetaobjectinterface.html
    """
    #  QDesignerMetaObjectInterface::QDesignerMetaObjectInterface()
    self._noteCreation(QDesignerMetaObjectInterface, lambda: Rituals.call(
        'ritual_ZN28QDesignerMetaObjectInterfaceC1Ev',
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
