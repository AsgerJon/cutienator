"""
QGraphicsAnchorPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qgraphicsanchorlayout_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGraphicsAnchorPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate
from . import QSizePolicy

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QGraphicsAnchor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGraphicsAnchor = WAIT['QGraphicsAnchor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsAnchorPrivate(QObjectPrivate):
  """
  The cute side of Qt's QGraphicsAnchorPrivate: a plain Python object
  standing in front of one C++ QGraphicsAnchorPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QGraphicsAnchorPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsAnchorPrivate that has a ritual and that
  Python can call so far, 6 names in all: 'q_func', 'setSpacing',
  'unsetSpacing', 'spacing', 'setSizePolicy', 'get'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QGraphicsAnchor *QGraphicsAnchorPrivate::q_func() const':
    takes in Python what 'QGraphicsAnchor *QGraphicsAnchorPrivate::q_func()'
    takes.
  - Qt's 'QGraphicsAnchorPrivate::~QGraphicsAnchorPrivate()': the destructor:
    Python never removes a C++ QGraphicsAnchorPrivate.

  What has no ritual
  ------------------

  1 of the 9 functions Qt declares: 1 leans on 'QtGraphicsAnchorLayout.

  What to expect
  --------------

  - The C++ QGraphicsAnchorPrivate is created at the first use, not by
    'QGraphicsAnchorPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsAnchorPrivate.
  - Each name of Qt's QGraphicsAnchorPrivate that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QGraphicsAnchor)
  @overload(NoneType)
  def get(q: Optional[QGraphicsAnchor]) -> Optional[QGraphicsAnchorPrivate]:
    """
    Calls Qt's 'QGraphicsAnchorPrivate
    *QGraphicsAnchorPrivate::get(QGraphicsAnchor *q)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsanchorprivate.html#get

    Parameters
    ----------

    q : Optional[QGraphicsAnchor]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QGraphicsAnchorPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsAnchorPrivate *QGraphicsAnchorPrivate::get(QGraphicsAnchor
    #      *q)
    address = Rituals.call(
        'ritual_ZN22QGraphicsAnchorPrivate3getEP15QGraphicsAnchor',
        CuteMixin._addressOf(q),
    )
    return QGraphicsAnchorPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsAnchorPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def spacing(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsAnchorPrivate::spacing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsanchorprivate.html#spacing
    """
    #  qreal QGraphicsAnchorPrivate::spacing() const
    return self.uglySide.call('ritual_ZNK22QGraphicsAnchorPrivate7spacingEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setSpacing(self, value: float) -> None:
    """
    Calls Qt's 'void QGraphicsAnchorPrivate::setSpacing(qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsanchorprivate.html#setSpacing

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QGraphicsAnchorPrivate::setSpacing(qreal value)
    self.uglySide.call(
        'ritual_ZN22QGraphicsAnchorPrivate10setSpacingEd', value,
    )

  @overload(QSizePolicy.Policy)
  def setSizePolicy(self, policy: QSizePolicy.Policy) -> None:
    """
    Calls Qt's 'void
    QGraphicsAnchorPrivate::setSizePolicy(QSizePolicy::Policy policy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsanchorprivate.html#setSizePolicy

    Parameters
    ----------

    policy : QSizePolicy.Policy
      Passed on as its number.
    """
    #  void QGraphicsAnchorPrivate::setSizePolicy(QSizePolicy::Policy policy)
    self.uglySide.call(
        'ritual_ZN22QGraphicsAnchorPrivate13setSizePolicyEN11QSizePolicy6Po'
        'licyE',
        policy.value,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QGraphicsAnchorPrivate::QGraphicsAnchorPrivate(decltype(
    QObjectPrivateVersion) a0)': leans on
    'QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(QLayoutStyleInfo
    const*)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsAnchorPrivate.__init__' has no cute function yet. Qt's "
        "'QGraphicsAnchorPrivate::QGraphicsAnchorPrivate(decltype(QObjectPri"
        "vateVersion) a0)': leans on "
        "'QtGraphicsAnchorLayout::AnchorData::refreshSizeHints(QLayoutStyleI"
        "nfo const*)', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

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

  def q_func(self) -> Optional[QGraphicsAnchor]:
    """
    Calls Qt's 'QGraphicsAnchor *QGraphicsAnchorPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsanchorprivate.html#q_func

    Returns
    -------

    Optional[QGraphicsAnchor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsAnchor *QGraphicsAnchorPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QGraphicsAnchorPrivate6q_funcEv',
    )
    from . import QGraphicsAnchor
    return QGraphicsAnchor._cuteAt(address)

  def unsetSpacing(self) -> None:
    """
    Calls Qt's 'void QGraphicsAnchorPrivate::unsetSpacing()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsanchorprivate.html#unsetSpacing
    """
    #  void QGraphicsAnchorPrivate::unsetSpacing()
    self.uglySide.call('ritual_ZN22QGraphicsAnchorPrivate12unsetSpacingEv')
