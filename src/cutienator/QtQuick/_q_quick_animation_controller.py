"""
QQuickAnimationController binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickanimationcontroller_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickAnimationController to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQml import QQmlFinalizerHook

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickAbstractAnimation
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickAbstractAnimation = WAIT['QQuickAbstractAnimation']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickAnimationController(QObject, QQmlFinalizerHook):
  """
  The cute side of Qt's QQuickAnimationController: a plain Python object
  standing in front of one C++ QQuickAnimationController.

  It is built on the cute 'QObject', as Qt's QQuickAnimationController is
  built on Qt's QObject, and has everything that class has. It is built on
  the cute 'QQmlFinalizerHook' as well, as Qt's QQuickAnimationController is
  built on Qt's QQmlFinalizerHook too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickAnimationController that has a ritual and that
  Python can call so far, 13 names in all: 'metaObject', 'tr', 'progress',
  'setProgress', 'animation', 'setAnimation', 'componentFinalized',
  'progressChanged', 'animationChanged', 'reload', 'completeToBeginning',
  'completeToEnd', 'updateProgress'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickAnimationController::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickAnimationController::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickAnimationControllerPrivate
    *QQuickAnimationController::d_func()': gives
    'QQuickAnimationControllerPrivate', which has no cute class yet.
  - Qt's 'const QQuickAnimationControllerPrivate
    *QQuickAnimationController::d_func() const': gives
    'QQuickAnimationControllerPrivate', which has no cute class yet.
  - Qt's 'QQuickAnimationController::~QQuickAnimationController()': the
    destructor: Python never removes a C++ QQuickAnimationController.

  What has no ritual
  ------------------

  6 of the 25 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickAnimationController is created at the first use, not by
    'QQuickAnimationController(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickAnimationController.
  - Qt tells when it has removed the C++ QQuickAnimationController. Every
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
    Calls Qt's 'QString QQuickAnimationController::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimationcontroller.html#tr

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
    #  QString QQuickAnimationController::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QQuickAnimationController2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickAnimationController'

  #  Qt's QQuickAnimationController is built on more than one class. The part
  #  of a C++ QQuickAnimationController that belongs to a class after the
  #  first begins somewhere inside the object, and the ritual named for that
  #  class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlFinalizerHook':
          'ritual_cast_QQuickAnimationController_QQmlFinalizerHook',
  }

  #  A C++ QQuickAnimationController Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickAnimationController'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickAnimationController::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimationcontroller.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickAnimationController::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickAnimationController10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def progress(self) -> float:
    """
    Calls Qt's 'qreal QQuickAnimationController::progress() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimationcontroller.html#progress
    """
    #  qreal QQuickAnimationController::progress() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickAnimationController8progressEv',
    )

  def animation(self) -> Optional[QQuickAbstractAnimation]:
    """
    Calls Qt's 'QQuickAbstractAnimation
    *QQuickAnimationController::animation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimationcontroller.html#animation

    Returns
    -------

    Optional[QQuickAbstractAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAbstractAnimation *QQuickAnimationController::animation() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickAnimationController9animationEv',
    )
    from . import QQuickAbstractAnimation
    return QQuickAbstractAnimation._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setProgress(self, progress: float) -> None:
    """
    Calls Qt's 'void QQuickAnimationController::setProgress(qreal progress)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimationcontroller.html#setProgress

    Parameters
    ----------

    progress : float
      Passed on as it is.
    """
    #  void QQuickAnimationController::setProgress(qreal progress)
    self.uglySide.call(
        'ritual_ZN25QQuickAnimationController11setProgressEd', progress,
    )

  @overload(QQuickAbstractAnimation)
  @overload(NoneType)
  def setAnimation(
      self,
      animation: Optional[QQuickAbstractAnimation],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickAnimationController::setAnimation(QQuickAbstractAnimation
    *animation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimationcontroller.html#setAnimation

    Parameters
    ----------

    animation : Optional[QQuickAbstractAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAnimationController::setAnimation(QQuickAbstractAnimation
    #      *animation)
    self.uglySide.call(
        'ritual_ZN25QQuickAnimationController12setAnimationEP23QQuickAbstra'
        'ctAnimation',
        self._addressOf(animation),
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
    'QQuickAnimationController::QQuickAnimationController(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimationcontroller.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickAnimationController::QQuickAnimationController(QObject *parent)
    self._noteCreation(QQuickAnimationController, lambda: Rituals.call(
        'ritual_ZN25QQuickAnimationControllerC1EP7QObject',
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

  def componentFinalized(self) -> None:
    """
    Calls Qt's 'void QQuickAnimationController::componentFinalized()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimationcontroller.html#componentFinalized
    """
    #  void QQuickAnimationController::componentFinalized()
    ritual = 'ritual_ZN25QQuickAnimationController18componentFinalizedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QQuickAnimationController18componentFinalizedEv')
    self.uglySide.call(ritual)

  def progressChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAnimationController::progressChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimationcontroller.html#progressChanged
    """
    #  void QQuickAnimationController::progressChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickAnimationController15progressChangedEv',
    )

  def animationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAnimationController::animationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimationcontroller.html#animationChanged
    """
    #  void QQuickAnimationController::animationChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickAnimationController16animationChangedEv',
    )

  def reload(self) -> None:
    """
    Calls Qt's 'void QQuickAnimationController::reload()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimationcontroller.html#reload
    """
    #  void QQuickAnimationController::reload()
    self.uglySide.call('ritual_ZN25QQuickAnimationController6reloadEv')

  def completeToBeginning(self) -> None:
    """
    Calls Qt's 'void QQuickAnimationController::completeToBeginning()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimationcontroller.html#completeToBeginning
    """
    #  void QQuickAnimationController::completeToBeginning()
    self.uglySide.call(
        'ritual_ZN25QQuickAnimationController19completeToBeginningEv',
    )

  def completeToEnd(self) -> None:
    """
    Calls Qt's 'void QQuickAnimationController::completeToEnd()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimationcontroller.html#completeToEnd
    """
    #  void QQuickAnimationController::completeToEnd()
    self.uglySide.call(
        'ritual_ZN25QQuickAnimationController13completeToEndEv',
    )

  def updateProgress(self) -> None:
    """
    Calls Qt's 'void QQuickAnimationController::updateProgress()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimationcontroller.html#updateProgress
    """
    #  void QQuickAnimationController::updateProgress()
    self.uglySide.call(
        'ritual_ZN25QQuickAnimationController14updateProgressEv',
    )
