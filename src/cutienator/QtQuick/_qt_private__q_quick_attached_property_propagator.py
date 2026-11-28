"""
QtPrivate::QQuickAttachedPropertyPropagator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickattachedpropertypropagator_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QtPrivate::QQuickAttachedPropertyPropagator to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QtPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaObject = WAIT['QMetaObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickAttachedPropertyPropagator(QObject):
  """
  The cute side of Qt's QtPrivate::QQuickAttachedPropertyPropagator: a plain
  Python object standing in front of one C++
  QtPrivate::QQuickAttachedPropertyPropagator.

  It is built on the cute 'QObject', as Qt's
  QtPrivate::QQuickAttachedPropertyPropagator is built on Qt's QObject, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QtPrivate::QQuickAttachedPropertyPropagator that has
  a ritual and that Python can call so far, 8 names in all: 'metaObject',
  'tr', 'attachedParent', 'attachedObject', 'fallbackAttachedObject',
  'initialize', 'attachedParentChange', 'd_func'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *QtPrivate::QQuickAttachedPropertyPropagator::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QtPrivate::QQuickAttachedPropertyPropagator::qt_metacall(QMetaObject::
    Call a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QtPrivate::QQuickAttachedPropertyPropagator::
    ~QQuickAttachedPropertyPropagator()': the destructor: Python never
    removes a C++ QtPrivate::QQuickAttachedPropertyPropagator.
  - Qt's 'QList<QQuickAttachedPropertyPropagator *>
    QtPrivate::QQuickAttachedPropertyPropagator::attachedChildren() const':
    gives a type Python has no way to take yet.
  - Qt's 'QtPrivate::QQuickAttachedPropertyPropagator::
    QQuickAttachedPropertyPropagator(QQuickAttachedPropertyPropagatorPrivate
    &dd, QObject *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'QDebug operator<<(QDebug debug, const
    QQuickAttachedPropertyPropagator *propagator)': an operator between other
    classes, written inside this one.
  - Qt's 'const QQuickAttachedPropertyPropagatorPrivate
    *QtPrivate::QQuickAttachedPropertyPropagator::d_func() const': takes in
    Python what 'QQuickAttachedPropertyPropagatorPrivate
    *QtPrivate::QQuickAttachedPropertyPropagator::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 18 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QtPrivate::QQuickAttachedPropertyPropagator is created at the
    first use, not by 'QtPrivate::QQuickAttachedPropertyPropagator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtPrivate::QQuickAttachedPropertyPropagator.
  - Qt tells when it has removed the C++
    QtPrivate::QQuickAttachedPropertyPropagator. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QtPrivate::QQuickAttachedPropertyPropagator that has no
    cute function yet, 'attachedChildren', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QtPrivate::QQuickAttachedPropertyPropagator::tr(const
    char *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qquickattachedpropertypropagator.html#tr

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
    #  QString QtPrivate::QQuickAttachedPropertyPropagator::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN9QtPrivate32QQuickAttachedPropertyPropagator2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QMetaObject, QObject)
  @overload(QMetaObject, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  @overload(QMetaObject, QObject, bool)
  @overload(QMetaObject, NoneType, bool)
  @overload(NoneType, QObject, bool)
  @overload(NoneType, NoneType, bool)
  def attachedObject(
      attachedType: Optional[QMetaObject],
      attachee: Optional[QObject],
      create: bool = False,
  ) -> Optional[QQuickAttachedPropertyPropagator]:
    """
    Calls Qt's 'QQuickAttachedPropertyPropagator
    *QtPrivate::QQuickAttachedPropertyPropagator::attachedObject(const
    QMetaObject *attachedType, QObject *attachee, bool create)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qquickattachedpropertypropagator.html

    Parameters
    ----------

    attachedType : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    attachee : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    create : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    Returns
    -------

    Optional[QQuickAttachedPropertyPropagator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAttachedPropertyPropagator
    #      *QtPrivate::QQuickAttachedPropertyPropagator::attachedObject(const
    #      QMetaObject *attachedType, QObject *attachee, bool create)
    address = Rituals.call(
        'ritual_ZN9QtPrivate32QQuickAttachedPropertyPropagator14attachedObj'
        'ectEPK11QMetaObjectP7QObjectb',
        CuteMixin._addressOf(attachedType, 'QMetaObject'),
        CuteMixin._addressOf(attachee, 'QObject'), create,
    )
    return QQuickAttachedPropertyPropagator._cuteAt(address)

  @staticmethod
  @overload(QMetaObject, QObject)
  @overload(QMetaObject, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def fallbackAttachedObject(
      attachedType: Optional[QMetaObject],
      attachee: Optional[QObject],
  ) -> Optional[QQuickAttachedPropertyPropagator]:
    """
    Calls Qt's 'QQuickAttachedPropertyPropagator
    *QtPrivate::QQuickAttachedPropertyPropagator::fallbackAttachedObject(
    const QMetaObject *attachedType, QObject *attachee)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qquickattachedpropertypropagator.html

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

    Optional[QQuickAttachedPropertyPropagator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAttachedPropertyPropagator
    #      *QtPrivate::QQuickAttachedPropertyPropagator::
    #      fallbackAttachedObject(const QMetaObject *attachedType, QObject
    #      *attachee)
    address = Rituals.call(
        'ritual_ZN9QtPrivate32QQuickAttachedPropertyPropagator22fallbackAtt'
        'achedObjectEPK11QMetaObjectP7QObject',
        CuteMixin._addressOf(attachedType, 'QMetaObject'),
        CuteMixin._addressOf(attachee, 'QObject'),
    )
    return QQuickAttachedPropertyPropagator._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtPrivate::QQuickAttachedPropertyPropagator'

  #  A C++ QtPrivate::QQuickAttachedPropertyPropagator Python makes is of a
  #  C++ class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtPrivate_QQuickAttachedPropertyPropagator'

  #  The functions Qt calls itself that
  #  QtPrivate::QQuickAttachedPropertyPropagator is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'attachedParentChange': (
          ('_ZN9QtPrivate32QQuickAttachedPropertyPropagator20attachedParent'
           'ChangeEPS0_S1_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtQuick:QtPrivate.QQuickAttachedPropertyPropagator'),
               ('address', 'address',
                'QtQuick:QtPrivate.QQuickAttachedPropertyPropagator'),
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
    Calls Qt's 'const QMetaObject
    *QtPrivate::QQuickAttachedPropertyPropagator::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qquickattachedpropertypropagator.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QtPrivate::QQuickAttachedPropertyPropagator::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK9QtPrivate32QQuickAttachedPropertyPropagator10metaObject'
        'Ev',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def attachedParent(self) -> Optional[QQuickAttachedPropertyPropagator]:
    """
    Calls Qt's 'QQuickAttachedPropertyPropagator
    *QtPrivate::QQuickAttachedPropertyPropagator::attachedParent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qquickattachedpropertypropagator.html

    Returns
    -------

    Optional[QQuickAttachedPropertyPropagator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAttachedPropertyPropagator
    #      *QtPrivate::QQuickAttachedPropertyPropagator::attachedParent()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK9QtPrivate32QQuickAttachedPropertyPropagator14attachedPa'
        'rentEv',
    )
    return QQuickAttachedPropertyPropagator._cuteAt(address)

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
    'QtPrivate::QQuickAttachedPropertyPropagator::
    QQuickAttachedPropertyPropagator(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qquickattachedpropertypropagator.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QtPrivate::QQuickAttachedPropertyPropagator::
    #      QQuickAttachedPropertyPropagator(QObject *parent)
    self._noteCreation(
        QQuickAttachedPropertyPropagator, lambda: Rituals.call(
            'ritual_ZN9QtPrivate32QQuickAttachedPropertyPropagatorC1EP7QObj'
            'ect',
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

  def initialize(self) -> None:
    """
    Calls Qt's 'void
    QtPrivate::QQuickAttachedPropertyPropagator::initialize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qquickattachedpropertypropagator.html
    """
    #  void QtPrivate::QQuickAttachedPropertyPropagator::initialize()
    self.uglySide.call(
        'ritual_ZN9QtPrivate32QQuickAttachedPropertyPropagator10initializeE'
        'v',
    )

  @overload(THIS, THIS)
  @overload(THIS, NoneType)
  @overload(NoneType, THIS)
  @overload(NoneType, NoneType)
  def attachedParentChange(
      self,
      newParent: Optional[QQuickAttachedPropertyPropagator],
      oldParent: Optional[QQuickAttachedPropertyPropagator],
  ) -> None:
    """
    Calls Qt's 'void
    QtPrivate::QQuickAttachedPropertyPropagator::attachedParentChange(
    QQuickAttachedPropertyPropagator *newParent,
    QQuickAttachedPropertyPropagator *oldParent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qquickattachedpropertypropagator.html

    Parameters
    ----------

    newParent : Optional[QQuickAttachedPropertyPropagator]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldParent : Optional[QQuickAttachedPropertyPropagator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QtPrivate::QQuickAttachedPropertyPropagator::attachedParentChange(
    #      QQuickAttachedPropertyPropagator *newParent,
    #      QQuickAttachedPropertyPropagator *oldParent)
    ritual = (
        'ritual_ZN9QtPrivate32QQuickAttachedPropertyPropagator20attachedPar'
        'entChangeEPS0_S1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QtPrivate32QQuickAttachedPropertyPropagator20attac'
          'hedParentChangeEPS0_S1_')
    self.uglySide.call(
        ritual, self._addressOf(newParent), self._addressOf(oldParent),
    )

  def d_func(
      self,
  ) -> Optional[QtPrivate.QQuickAttachedPropertyPropagatorPrivate]:
    """
    Calls Qt's 'QQuickAttachedPropertyPropagatorPrivate
    *QtPrivate::QQuickAttachedPropertyPropagator::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qquickattachedpropertypropagator.html

    Returns
    -------

    Optional[QtPrivate.QQuickAttachedPropertyPropagatorPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAttachedPropertyPropagatorPrivate
    #      *QtPrivate::QQuickAttachedPropertyPropagator::d_func()
    address = self.uglySide.call(
        'ritual_ZN9QtPrivate32QQuickAttachedPropertyPropagator6d_funcEv',
    )
    return QtPrivate.QQuickAttachedPropertyPropagatorPrivate._cuteAt(address)

  @staticmethod
  def attachedChildren(*__, **_) -> Never:
    """
    Qt's 'QList<QQuickAttachedPropertyPropagator *>
    QtPrivate::QQuickAttachedPropertyPropagator::attachedChildren() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtPrivate.QQuickAttachedPropertyPropagator.attachedChildren' has "
        "no cute function yet. Qt's 'QList<QQuickAttachedPropertyPropagator "
        "*> QtPrivate::QQuickAttachedPropertyPropagator::attachedChildren() "
        "const': gives a type Python has no way to take yet.")
