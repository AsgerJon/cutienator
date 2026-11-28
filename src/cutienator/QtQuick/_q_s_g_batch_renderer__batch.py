"""
QSGBatchRenderer::Batch binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGBatchRenderer::Batch to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QSGBatchRenderer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSGGeometryNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSGGeometryNode = WAIT['QSGGeometryNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Batch(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSGBatchRenderer::Batch: a plain Python object
  standing in front of one C++ QSGBatchRenderer::Batch.

  What exists
  -----------

  Every function of Qt's QSGBatchRenderer::Batch that has a ritual and that
  Python can call so far, 7 names in all: 'geometryWasChanged',
  'isMaterialCompatible', 'invalidate', 'cleanupRemovedElements',
  'isTranslateOnlyToRoot', 'isSafeToBatch', 'init'. It can be made from
  Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QSGBatchRenderer::Batch is created at the first use, not by
    'QSGBatchRenderer::Batch(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGBatchRenderer::Batch.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGBatchRenderer::Batch'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QSGBatchRenderer.Element'])
  @overload(NoneType)
  def isMaterialCompatible(
      self,
      e: Optional[QSGBatchRenderer.Element],
  ) -> QSGBatchRenderer.BatchCompatibility:
    """
    Calls Qt's 'BatchCompatibility
    QSGBatchRenderer::Batch::isMaterialCompatible(Element *e) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-batch.html#isMaterialCompatible

    Parameters
    ----------

    e : Optional[QSGBatchRenderer.Element]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QSGBatchRenderer.BatchCompatibility
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSGBatchRenderer.BatchCompatibility(number)' gives.
    """
    #  BatchCompatibility
    #      QSGBatchRenderer::Batch::isMaterialCompatible(Element *e) const
    return QSGBatchRenderer.BatchCompatibility(self.uglySide.call(
        'ritual_ZNK16QSGBatchRenderer5Batch20isMaterialCompatibleEPNS_7Elem'
        'entE',
        self._addressOf(e),
    ))

  def isTranslateOnlyToRoot(self) -> bool:
    """
    Calls Qt's 'bool QSGBatchRenderer::Batch::isTranslateOnlyToRoot() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-batch.html#isTranslateOnlyToRoot
    """
    #  bool QSGBatchRenderer::Batch::isTranslateOnlyToRoot() const
    return self.uglySide.call(
        'ritual_ZNK16QSGBatchRenderer5Batch21isTranslateOnlyToRootEv',
    )

  def isSafeToBatch(self) -> bool:
    """
    Calls Qt's 'bool QSGBatchRenderer::Batch::isSafeToBatch() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-batch.html#isSafeToBatch
    """
    #  bool QSGBatchRenderer::Batch::isSafeToBatch() const
    return self.uglySide.call(
        'ritual_ZNK16QSGBatchRenderer5Batch13isSafeToBatchEv',
    )

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
    Notes what was given, for Qt's 'QSGBatchRenderer::Batch::Batch()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsgbatchrenderer-batch.html#Batch
    """
    #  QSGBatchRenderer::Batch::Batch()
    self._noteCreation(Batch, lambda: Rituals.call(
        'ritual_ZN16QSGBatchRenderer5BatchC1Ev',
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

  @overload(QSGGeometryNode)
  @overload(NoneType)
  def geometryWasChanged(self, gn: Optional[QSGGeometryNode]) -> bool:
    """
    Calls Qt's 'bool
    QSGBatchRenderer::Batch::geometryWasChanged(QSGGeometryNode *gn)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-batch.html#geometryWasChanged

    Parameters
    ----------

    gn : Optional[QSGGeometryNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGBatchRenderer::Batch::geometryWasChanged(QSGGeometryNode *gn)
    return self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer5Batch18geometryWasChangedEP15QSGGeomet'
        'ryNode',
        self._addressOf(gn, 'QSGGeometryNode'),
    )

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Batch::invalidate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-batch.html#invalidate
    """
    #  void QSGBatchRenderer::Batch::invalidate()
    self.uglySide.call('ritual_ZN16QSGBatchRenderer5Batch10invalidateEv')

  def cleanupRemovedElements(self) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Batch::cleanupRemovedElements()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-batch.html#cleanupRemovedElements
    """
    #  void QSGBatchRenderer::Batch::cleanupRemovedElements()
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer5Batch22cleanupRemovedElementsEv',
    )

  def init(self) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Batch::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgbatchrenderer-batch.html#init
    """
    #  void QSGBatchRenderer::Batch::init()
    self.uglySide.call('ritual_ZN16QSGBatchRenderer5Batch4initEv')
