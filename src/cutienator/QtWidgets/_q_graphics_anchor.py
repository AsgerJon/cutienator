"""
QGraphicsAnchor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgraphicsanchorlayout.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import QSizePolicy

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsAnchor(QObject):
  """
  The cute side of Qt's QGraphicsAnchor: a plain Python object standing in
  front of one C++ QGraphicsAnchor.

  It is built on the cute 'QObject', as Qt's QGraphicsAnchor is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsAnchor that has a ritual and that Python
  can call so far, 7 names in all: 'metaObject', 'tr', 'setSpacing',
  'unsetSpacing', 'spacing', 'setSizePolicy', 'sizePolicy'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsAnchor::~QGraphicsAnchor()': the destructor: Python never
    removes a C++ QGraphicsAnchor.

  What has no ritual
  ------------------

  7 of the 15 functions Qt declares: 4 private; 2 takes or gives a type that
  cannot be passed yet; 1 a template.

  What to expect
  --------------

  - The C++ QGraphicsAnchor is created at the first use, not by
    'QGraphicsAnchor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsAnchor.
  - Qt tells when it has removed the C++ QGraphicsAnchor. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QGraphicsAnchor::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsanchor.html#tr

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
    #  QString QGraphicsAnchor::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QGraphicsAnchor2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsAnchor'

  #  A C++ QGraphicsAnchor Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsAnchor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGraphicsAnchor::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsanchor.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGraphicsAnchor::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QGraphicsAnchor10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def spacing(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsAnchor::spacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsanchor.html#spacing
    """
    #  qreal QGraphicsAnchor::spacing() const
    return self.uglySide.call('ritual_ZNK15QGraphicsAnchor7spacingEv')

  def sizePolicy(self) -> QSizePolicy.Policy:
    """
    Calls Qt's 'QSizePolicy::Policy QGraphicsAnchor::sizePolicy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsanchor.html#sizePolicy

    Returns
    -------

    QSizePolicy.Policy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSizePolicy.Policy(number)' gives.
    """
    #  QSizePolicy::Policy QGraphicsAnchor::sizePolicy() const
    return QSizePolicy.Policy(self.uglySide.call(
        'ritual_ZNK15QGraphicsAnchor10sizePolicyEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setSpacing(self, spacing: float) -> None:
    """
    Calls Qt's 'void QGraphicsAnchor::setSpacing(qreal spacing)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsanchor.html#setSpacing

    Parameters
    ----------

    spacing : float
      Passed on as it is.
    """
    #  void QGraphicsAnchor::setSpacing(qreal spacing)
    self.uglySide.call('ritual_ZN15QGraphicsAnchor10setSpacingEd', spacing)

  @overload(QSizePolicy.Policy)
  def setSizePolicy(self, policy: QSizePolicy.Policy) -> None:
    """
    Calls Qt's 'void QGraphicsAnchor::setSizePolicy(QSizePolicy::Policy
    policy)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsanchor.html#setSizePolicy

    Parameters
    ----------

    policy : QSizePolicy.Policy
      Passed on as its number.
    """
    #  void QGraphicsAnchor::setSizePolicy(QSizePolicy::Policy policy)
    self.uglySide.call(
        'ritual_ZN15QGraphicsAnchor13setSizePolicyEN11QSizePolicy6PolicyE',
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

  def unsetSpacing(self) -> None:
    """
    Calls Qt's 'void QGraphicsAnchor::unsetSpacing()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsanchor.html#unsetSpacing
    """
    #  void QGraphicsAnchor::unsetSpacing()
    self.uglySide.call('ritual_ZN15QGraphicsAnchor12unsetSpacingEv')
