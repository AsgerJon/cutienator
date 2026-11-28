"""
QQuickPathAnimationAnimator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickitemanimation_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickPathAnimationAnimator to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QQuickBulkValueAnimator

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickPathAnimationPrivate, QQuickPathAnimationUpdater
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickPathAnimationPrivate = WAIT['QQuickPathAnimationPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPathAnimationAnimator(QQuickBulkValueAnimator):
  """
  The cute side of Qt's QQuickPathAnimationAnimator: a plain Python object
  standing in front of one C++ QQuickPathAnimationAnimator.

  It is built on the cute 'QQuickBulkValueAnimator', as Qt's
  QQuickPathAnimationAnimator is built on Qt's QQuickBulkValueAnimator, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPathAnimationAnimator that has a ritual and
  that Python can call so far, 2 names in all: 'clearTemplate',
  'pathUpdater'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickPathAnimationAnimator::~QQuickPathAnimationAnimator()': the
    destructor: Python never removes a C++ QQuickPathAnimationAnimator.

  What to expect
  --------------

  - The C++ QQuickPathAnimationAnimator is created at the first use, not by
    'QQuickPathAnimationAnimator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPathAnimationAnimator.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPathAnimationAnimator'

  #  A C++ QQuickPathAnimationAnimator Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPathAnimationAnimator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def pathUpdater(self) -> Optional[QQuickPathAnimationUpdater]:
    """
    Calls Qt's 'QQuickPathAnimationUpdater
    *QQuickPathAnimationAnimator::pathUpdater() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanimationanimator.html#pathUpdater

    Returns
    -------

    Optional[QQuickPathAnimationUpdater]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPathAnimationUpdater *QQuickPathAnimationAnimator::pathUpdater()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK27QQuickPathAnimationAnimator11pathUpdaterEv',
    )
    from . import QQuickPathAnimationUpdater
    return QQuickPathAnimationUpdater._cuteAt(address)

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
  @overload(QQuickPathAnimationPrivate)
  @overload(NoneType)
  def __init__(
      self,
      a0: Optional[QQuickPathAnimationPrivate] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuickPathAnimationAnimator::QQuickPathAnimationAnimator(
    QQuickPathAnimationPrivate *a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanimationanimator.html

    Parameters
    ----------

    a0 : Optional[QQuickPathAnimationPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickPathAnimationAnimator::QQuickPathAnimationAnimator(
    #      QQuickPathAnimationPrivate *a0)
    self._noteCreation(QQuickPathAnimationAnimator, lambda: Rituals.call(
        'ritual_ZN27QQuickPathAnimationAnimatorC1EP26QQuickPathAnimationPri'
        'vate',
        self._addressOf(a0),
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

  def clearTemplate(self) -> None:
    """
    Calls Qt's 'void QQuickPathAnimationAnimator::clearTemplate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathanimationanimator.html#clearTemplate
    """
    #  void QQuickPathAnimationAnimator::clearTemplate()
    self.uglySide.call(
        'ritual_ZN27QQuickPathAnimationAnimator13clearTemplateEv',
    )
