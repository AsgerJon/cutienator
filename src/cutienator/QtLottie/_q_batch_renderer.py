"""
QBatchRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qbatchrenderer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QBatchRenderer to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QLottieAnimation, QLottieRoot
  from ..QtCore import QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLottieAnimation = WAIT['QLottieAnimation']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBatchRenderer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QBatchRenderer: a plain Python object standing in
  front of one C++ QBatchRenderer.

  What exists
  -----------

  Every function of Qt's QBatchRenderer that has a ritual and that Python can
  call so far, 7 names in all: 'metaObject', 'getFrame', 'frameReady',
  'registerAnimator', 'deregisterAnimator', 'frameRendered', 'run'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBatchRenderer::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QBatchRenderer::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QBatchRenderer::~QBatchRenderer()': the destructor: Python never
    removes a C++ QBatchRenderer.

  What has no ritual
  ------------------

  11 of the 21 functions Qt declares: 5 leans on
  'lcLottieQtLottieRenderThread()', which Qt's source does not mark for use
  from outside Qt and has no code for that could be taken; 2 not a gap; 2
  forbidden; 2 leans on 'QBatchRenderer.

  What to expect
  --------------

  - The C++ QBatchRenderer is created at the first use, not by
    'QBatchRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBatchRenderer.
  - Qt tells when it has removed the C++ QBatchRenderer. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QBatchRenderer that has no cute function yet,
    '__init__', 'deleteInstance', 'gotoFrame', 'instance', 'prerender',
    'pruneFrameCache', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBatchRenderer'

  #  A C++ QBatchRenderer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBatchRenderer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QBatchRenderer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbatchrenderer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBatchRenderer::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QBatchRenderer10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QBatchRenderer::QBatchRenderer()': leans on
    'lcLottieQtLottieRenderThread()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QBatchRenderer.__init__' has no cute function yet. Qt's "
        "'QBatchRenderer::QBatchRenderer()': leans on "
        "'lcLottieQtLottieRenderThread()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

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

  @overload(QLottieAnimation, int)
  @overload(NoneType, int)
  def getFrame(
      self,
      animator: Optional[QLottieAnimation],
      frameNumber: int,
  ) -> Optional[QLottieRoot]:
    """
    Calls Qt's 'QLottieRoot *QBatchRenderer::getFrame(QLottieAnimation
    *animator, int frameNumber)'.

    Qt's own words: https://doc.qt.io/qt-6/qbatchrenderer.html#getFrame

    Parameters
    ----------

    animator : Optional[QLottieAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    frameNumber : int
      Passed on as it is.

    Returns
    -------

    Optional[QLottieRoot]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieRoot *QBatchRenderer::getFrame(QLottieAnimation *animator, int
    #      frameNumber)
    address = self.uglySide.call(
        'ritual_ZN14QBatchRenderer8getFrameEP16QLottieAnimationi',
        self._addressOf(animator), frameNumber,
    )
    from . import QLottieRoot
    return QLottieRoot._cuteAt(address)

  @overload(QLottieAnimation, int)
  @overload(NoneType, int)
  def frameReady(
      self,
      animator: Optional[QLottieAnimation],
      frameNumber: int,
  ) -> None:
    """
    Calls Qt's 'void QBatchRenderer::frameReady(QLottieAnimation *animator,
    int frameNumber)'.

    Qt's own words: https://doc.qt.io/qt-6/qbatchrenderer.html#frameReady

    Parameters
    ----------

    animator : Optional[QLottieAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    frameNumber : int
      Passed on as it is.
    """
    #  void QBatchRenderer::frameReady(QLottieAnimation *animator, int
    #      frameNumber)
    self.uglySide.call(
        'ritual_ZN14QBatchRenderer10frameReadyEP16QLottieAnimationi',
        self._addressOf(animator), frameNumber,
    )

  @overload(QLottieAnimation)
  @overload(NoneType)
  def registerAnimator(self, animator: Optional[QLottieAnimation]) -> None:
    """
    Calls Qt's 'void QBatchRenderer::registerAnimator(QLottieAnimation
    *animator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbatchrenderer.html#registerAnimator

    Parameters
    ----------

    animator : Optional[QLottieAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBatchRenderer::registerAnimator(QLottieAnimation *animator)
    self.uglySide.call(
        'ritual_ZN14QBatchRenderer16registerAnimatorEP16QLottieAnimation',
        self._addressOf(animator),
    )

  @overload(QLottieAnimation)
  @overload(NoneType)
  def deregisterAnimator(self, animator: Optional[QLottieAnimation]) -> None:
    """
    Calls Qt's 'void QBatchRenderer::deregisterAnimator(QLottieAnimation
    *animator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbatchrenderer.html#deregisterAnimator

    Parameters
    ----------

    animator : Optional[QLottieAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBatchRenderer::deregisterAnimator(QLottieAnimation *animator)
    self.uglySide.call(
        'ritual_ZN14QBatchRenderer18deregisterAnimatorEP16QLottieAnimation',
        self._addressOf(animator),
    )

  @overload(QLottieAnimation, int)
  @overload(NoneType, int)
  def frameRendered(
      self,
      animator: Optional[QLottieAnimation],
      frameNumber: int,
  ) -> None:
    """
    Calls Qt's 'void QBatchRenderer::frameRendered(QLottieAnimation
    *animator, int frameNumber)'.

    Qt's own words: https://doc.qt.io/qt-6/qbatchrenderer.html#frameRendered

    Parameters
    ----------

    animator : Optional[QLottieAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    frameNumber : int
      Passed on as it is.
    """
    #  void QBatchRenderer::frameRendered(QLottieAnimation *animator, int
    #      frameNumber)
    self.uglySide.call(
        'ritual_ZN14QBatchRenderer13frameRenderedEP16QLottieAnimationi',
        self._addressOf(animator), frameNumber,
    )

  def run(self) -> None:
    """
    Calls Qt's 'void QBatchRenderer::run()'.

    Qt's own words: https://doc.qt.io/qt-6/qbatchrenderer.html#run
    """
    #  void QBatchRenderer::run()
    self.uglySide.call('ritual_ZN14QBatchRenderer3runEv')

  @staticmethod
  def deleteInstance(*__, **_) -> Never:
    """
    Qt's 'void QBatchRenderer::deleteInstance()': leans on
    'QBatchRenderer::m_rendererInstance', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QBatchRenderer.deleteInstance' has no cute function yet. Qt's "
        "'void QBatchRenderer::deleteInstance()': leans on "
        "'QBatchRenderer::m_rendererInstance', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def gotoFrame(*__, **_) -> Never:
    """
    Qt's 'bool QBatchRenderer::gotoFrame(QLottieAnimation *animator, int
    frame)': leans on 'lcLottieQtLottieRenderThread()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QBatchRenderer.gotoFrame' has no cute function yet. Qt's 'bool "
        "QBatchRenderer::gotoFrame(QLottieAnimation *animator, int frame)': "
        "leans on 'lcLottieQtLottieRenderThread()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def instance(*__, **_) -> Never:
    """
    Qt's 'QBatchRenderer *QBatchRenderer::instance()': leans on
    'lcLottieQtLottieRenderThread()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QBatchRenderer.instance' has no cute function yet. Qt's "
        "'QBatchRenderer *QBatchRenderer::instance()': leans on "
        "'lcLottieQtLottieRenderThread()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def prerender(*__, **_) -> Never:
    """
    Qt's 'void QBatchRenderer::prerender(Entry *animEntry)': leans on
    'lcLottieQtLottieRenderThread()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QBatchRenderer.prerender' has no cute function yet. Qt's 'void "
        "QBatchRenderer::prerender(Entry *animEntry)': leans on "
        "'lcLottieQtLottieRenderThread()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def pruneFrameCache(*__, **_) -> Never:
    """
    Qt's 'void QBatchRenderer::pruneFrameCache(Entry *e)': leans on
    'lcLottieQtLottieRenderThread()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QBatchRenderer.pruneFrameCache' has no cute function yet. Qt's "
        "'void QBatchRenderer::pruneFrameCache(Entry *e)': leans on "
        "'lcLottieQtLottieRenderThread()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")
