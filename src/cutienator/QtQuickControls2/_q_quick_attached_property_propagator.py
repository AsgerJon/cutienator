"""
QQuickAttachedPropertyPropagator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2/qquickattachedpropertypropagator.h, Qt 6.12.0. Changes
#  made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickAttachedPropertyPropagator(QObject):
  """
  The cute side of Qt's QQuickAttachedPropertyPropagator: a plain Python
  object standing in front of one C++ QQuickAttachedPropertyPropagator.

  It is built on the cute 'QObject', as Qt's QQuickAttachedPropertyPropagator
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickAttachedPropertyPropagator that has a ritual
  and that Python can call so far, 6 names in all: 'metaObject', 'tr',
  'attachedChildren', 'attachedParent', 'initialize', 'attachedParentChange'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickAttachedPropertyPropagator::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QQuickAttachedPropertyPropagator::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'QQuickAttachedPropertyPropagator::~QQuickAttachedPropertyPropagator()':
    the destructor: Python never removes a C++
    QQuickAttachedPropertyPropagator.
  - Qt's 'QDebug operator<<(QDebug debug, const
    QQuickAttachedPropertyPropagator *propagator)': an operator between other
    classes, written inside this one.
  - Qt's 'QQuickAttachedPropertyPropagatorPrivate
    *QQuickAttachedPropertyPropagator::d_func()': gives
    'QQuickAttachedPropertyPropagatorPrivate', which has no cute class yet.
  - Qt's 'const QQuickAttachedPropertyPropagatorPrivate
    *QQuickAttachedPropertyPropagator::d_func() const': gives
    'QQuickAttachedPropertyPropagatorPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickAttachedPropertyPropagator is created at the first use, not
    by 'QQuickAttachedPropertyPropagator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickAttachedPropertyPropagator.
  - Qt tells when it has removed the C++ QQuickAttachedPropertyPropagator.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QQuickAttachedPropertyPropagator::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickattachedpropertypropagator.html#tr

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
    #  QString QQuickAttachedPropertyPropagator::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN32QQuickAttachedPropertyPropagator2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickAttachedPropertyPropagator'

  #  A C++ QQuickAttachedPropertyPropagator Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickAttachedPropertyPropagator'

  #  The functions Qt calls itself that QQuickAttachedPropertyPropagator is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'attachedParentChange': (
          ('_ZN32QQuickAttachedPropertyPropagator20attachedParentChangeEPS_'
           'S0_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtQuickControls2:QQuickAttachedPropertyPropagator'),
               ('address', 'address',
                'QtQuickControls2:QQuickAttachedPropertyPropagator'),
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
    *QQuickAttachedPropertyPropagator::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickattachedpropertypropagator.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickAttachedPropertyPropagator::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK32QQuickAttachedPropertyPropagator10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def attachedChildren(self) -> QList[QQuickAttachedPropertyPropagator]:
    """
    Calls Qt's 'QList<QQuickAttachedPropertyPropagator *>
    QQuickAttachedPropertyPropagator::attachedChildren() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickattachedpropertypropagator.html

    Returns
    -------

    QList[QQuickAttachedPropertyPropagator]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQuickAttachedPropertyPropagator *>
    #      QQuickAttachedPropertyPropagator::attachedChildren() const
    address = self.uglySide.call(
        'ritual_ZNK32QQuickAttachedPropertyPropagator16attachedChildrenEv',
    )
    return QList[QQuickAttachedPropertyPropagator]._cuteOwning(address)

  def attachedParent(self) -> Optional[QQuickAttachedPropertyPropagator]:
    """
    Calls Qt's 'QQuickAttachedPropertyPropagator
    *QQuickAttachedPropertyPropagator::attachedParent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickattachedpropertypropagator.html

    Returns
    -------

    Optional[QQuickAttachedPropertyPropagator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAttachedPropertyPropagator
    #      *QQuickAttachedPropertyPropagator::attachedParent() const
    address = self.uglySide.call(
        'ritual_ZNK32QQuickAttachedPropertyPropagator14attachedParentEv',
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
    'QQuickAttachedPropertyPropagator::QQuickAttachedPropertyPropagator(
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickattachedpropertypropagator.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickAttachedPropertyPropagator::
    #      QQuickAttachedPropertyPropagator(QObject *parent)
    self._noteCreation(
        QQuickAttachedPropertyPropagator, lambda: Rituals.call(
            'ritual_ZN32QQuickAttachedPropertyPropagatorC1EP7QObject',
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
    Calls Qt's 'void QQuickAttachedPropertyPropagator::initialize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickattachedpropertypropagator.html#initialize
    """
    #  void QQuickAttachedPropertyPropagator::initialize()
    self.uglySide.call(
        'ritual_ZN32QQuickAttachedPropertyPropagator10initializeEv',
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
    Calls Qt's 'void QQuickAttachedPropertyPropagator::attachedParentChange(
    QQuickAttachedPropertyPropagator *newParent,
    QQuickAttachedPropertyPropagator *oldParent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickattachedpropertypropagator.html

    Parameters
    ----------

    newParent : Optional[QQuickAttachedPropertyPropagator]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldParent : Optional[QQuickAttachedPropertyPropagator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAttachedPropertyPropagator::attachedParentChange(
    #      QQuickAttachedPropertyPropagator *newParent,
    #      QQuickAttachedPropertyPropagator *oldParent)
    ritual = (
        'ritual_ZN32QQuickAttachedPropertyPropagator20attachedParentChangeE'
        'PS_S0_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QQuickAttachedPropertyPropagator20attachedParentC'
          'hangeEPS_S0_')
    self.uglySide.call(
        ritual, self._addressOf(newParent), self._addressOf(oldParent),
    )


#  Qt's 'QList<QQuickAttachedPropertyPropagator *>': the list of
#  QQuickAttachedPropertyPropagator, which
#  'QList[QQuickAttachedPropertyPropagator]' gives. It is made here, so that
#  there is one as soon as there can be a QQuickAttachedPropertyPropagator.
QList.createKind(
    QQuickAttachedPropertyPropagator, 'address',
    make='ritual_list_make_QQuickAttachedPropertyPropagator_ptr',
    add='ritual_list_add_QQuickAttachedPropertyPropagator_ptr',
    size='ritual_list_size_QQuickAttachedPropertyPropagator_ptr',
    at='ritual_list_at_QQuickAttachedPropertyPropagator_ptr',
    drop='ritual_list_drop_QQuickAttachedPropertyPropagator_ptr',
)
