"""
QQmlAbstractDelegateComponent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmlabstractdelegatecomponent_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQmlAbstractDelegateComponent to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQml import QQmlComponent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
  from . import QQmlAdaptorModel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlAdaptorModel = WAIT['QQmlAdaptorModel']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlAbstractDelegateComponent(QQmlComponent):
  """
  The cute side of Qt's QQmlAbstractDelegateComponent: a plain Python object
  standing in front of one C++ QQmlAbstractDelegateComponent.

  It is built on the cute 'QQmlComponent', as Qt's
  QQmlAbstractDelegateComponent is built on Qt's QQmlComponent, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlAbstractDelegateComponent that has a ritual and
  that Python can call so far, 6 names in all: 'metaObject', 'tr',
  'delegate', 'role', 'delegateChanged', 'value'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlAbstractDelegateComponent::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQmlAbstractDelegateComponent::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQmlAbstractDelegateComponent::qt_qmlMarker_uncreatable()':
    one of Qt's own inner workings.
  - Qt's 'QQmlAbstractDelegateComponent::~QQmlAbstractDelegateComponent()':
    the destructor: Python never removes a C++ QQmlAbstractDelegateComponent.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlAbstractDelegateComponent is created at the first use, not by
    'QQmlAbstractDelegateComponent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlAbstractDelegateComponent.
  - Qt tells when it has removed the C++ QQmlAbstractDelegateComponent. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQmlAbstractDelegateComponent::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractdelegatecomponent.html#tr

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
    #  QString QQmlAbstractDelegateComponent::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN29QQmlAbstractDelegateComponent2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlAbstractDelegateComponent'

  #  A C++ QQmlAbstractDelegateComponent Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlAbstractDelegateComponent'

  #  The functions Qt calls itself that QQmlAbstractDelegateComponent is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'delegate': (
          ('_ZNK29QQmlAbstractDelegateComponent8delegateEP16QQmlAdaptorMode'
           'lii',
           ('address', 'address', 'QtQml:QQmlComponent'),
           (
               ('address', 'address', 'QtQmlModels:QQmlAdaptorModel'),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'role': (
          ('_ZNK29QQmlAbstractDelegateComponent4roleEv',
           ('address', 'text', ''),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQmlAbstractDelegateComponent::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractdelegatecomponent.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlAbstractDelegateComponent::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK29QQmlAbstractDelegateComponent10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QQmlAdaptorModel, int)
  @overload(NoneType, int)
  @overload(QQmlAdaptorModel, int, int)
  @overload(NoneType, int, int)
  def delegate(
      self,
      adaptorModel: Optional[QQmlAdaptorModel],
      row: int,
      column: int = 0,
  ) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent
    *QQmlAbstractDelegateComponent::delegate(QQmlAdaptorModel *adaptorModel,
    int row, int column) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractdelegatecomponent.html#delegate

    Parameters
    ----------

    adaptorModel : Optional[QQmlAdaptorModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    row : int
      Passed on as it is.

    column : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent
    #      *QQmlAbstractDelegateComponent::delegate(QQmlAdaptorModel
    #      *adaptorModel, int row, int column) const
    address = self.uglySide.call(
        'ritual_ZNK29QQmlAbstractDelegateComponent8delegateEP16QQmlAdaptorM'
        'odelii',
        self._addressOf(adaptorModel), row, column,
    )
    return QQmlComponent._cuteAt(address)

  def role(self) -> str:
    """
    Calls Qt's 'QString QQmlAbstractDelegateComponent::role() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractdelegatecomponent.html#role

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlAbstractDelegateComponent::role() const
    return self.uglySide.call(
        'ritual_ZNK29QQmlAbstractDelegateComponent4roleEv',
    )

  @overload(QQmlAdaptorModel, int, int, str)
  @overload(NoneType, int, int, str)
  def value(
      self,
      adaptorModel: Optional[QQmlAdaptorModel],
      row: int,
      column: int,
      role: str,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant
    QQmlAbstractDelegateComponent::value(QQmlAdaptorModel *adaptorModel, int
    row, int column, const QString &role) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractdelegatecomponent.html#value

    Parameters
    ----------

    adaptorModel : Optional[QQmlAdaptorModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    role : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlAbstractDelegateComponent::value(QQmlAdaptorModel
    #      *adaptorModel, int row, int column, const QString &role) const
    address = self.uglySide.call(
        'ritual_ZNK29QQmlAbstractDelegateComponent5valueEP16QQmlAdaptorMode'
        'liiRK7QString',
        self._addressOf(adaptorModel), row, column, role,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQmlAbstractDelegateComponent::QQmlAbstractDelegateComponent(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractdelegatecomponent.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlAbstractDelegateComponent::QQmlAbstractDelegateComponent(QObject
    #      *parent)
    self._noteCreation(QQmlAbstractDelegateComponent, lambda: Rituals.call(
        'ritual_ZN29QQmlAbstractDelegateComponentC1EP7QObject',
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

  def delegateChanged(self) -> None:
    """
    Calls Qt's 'void QQmlAbstractDelegateComponent::delegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractdelegatecomponent.html#delegateChanged
    """
    #  void QQmlAbstractDelegateComponent::delegateChanged()
    self.uglySide.call(
        'ritual_ZN29QQmlAbstractDelegateComponent15delegateChangedEv',
    )
