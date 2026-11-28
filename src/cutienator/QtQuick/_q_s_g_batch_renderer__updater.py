"""
QSGBatchRenderer::Updater binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGBatchRenderer::Updater to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSGBatchRenderer, QSGNodeUpdater

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QMatrix4x4
  from . import QSGNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']
  QSGNode = WAIT['QSGNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Updater(QSGNodeUpdater):
  """
  The cute side of Qt's QSGBatchRenderer::Updater: a plain Python object
  standing in front of one C++ QSGBatchRenderer::Updater.

  It is built on the cute 'QSGNodeUpdater', as Qt's QSGBatchRenderer::Updater
  is built on Qt's QSGNodeUpdater, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGBatchRenderer::Updater that has a ritual and that
  Python can call so far, 2 names in all: 'updateRootTransforms',
  'updateStates'. It can be made from Python, in 1 way; see '__init__'.

  What has no ritual
  ------------------

  7 of the 10 functions Qt declares: 5 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 cannot be
  called and cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QSGBatchRenderer::Updater is created at the first use, not by
    'QSGBatchRenderer::Updater(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGBatchRenderer::Updater.
  - Each name of Qt's QSGBatchRenderer::Updater that has no cute function
    yet, 'registerWithParentRoot', 'visitClipNode', 'visitGeometryNode',
    'visitOpacityNode', 'visitTransformNode', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGBatchRenderer::Updater'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload(WAIT['QSGBatchRenderer.Renderer'])
  @overload(NoneType)
  def __init__(self, r: Optional[QSGBatchRenderer.Renderer]) -> None:
    """
    Notes what was given, for Qt's
    'QSGBatchRenderer::Updater::Updater(Renderer *r)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-updater.html#Updater

    Parameters
    ----------

    r : Optional[QSGBatchRenderer.Renderer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSGBatchRenderer::Updater::Updater(Renderer *r)
    self._noteCreation(Updater, lambda: Rituals.call(
        'ritual_ZN16QSGBatchRenderer7UpdaterC1EPNS_8RendererE',
        self._addressOf(r),
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

  @overload(
      WAIT['QSGBatchRenderer.Node'], WAIT['QSGBatchRenderer.Node'],
      QMatrix4x4,
  )
  @overload(WAIT['QSGBatchRenderer.Node'], NoneType, QMatrix4x4)
  @overload(NoneType, WAIT['QSGBatchRenderer.Node'], QMatrix4x4)
  @overload(NoneType, NoneType, QMatrix4x4)
  def updateRootTransforms(
      self,
      n: Optional[QSGBatchRenderer.Node],
      root: Optional[QSGBatchRenderer.Node],
      combined: QMatrix4x4,
  ) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Updater::updateRootTransforms(Node *n,
    Node *root, const QMatrix4x4 &combined)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-updater.html#updateRootTransforms

    Parameters
    ----------

    n : Optional[QSGBatchRenderer.Node]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    root : Optional[QSGBatchRenderer.Node]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    combined : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  void QSGBatchRenderer::Updater::updateRootTransforms(Node *n, Node
    #      *root, const QMatrix4x4 &combined)
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer7Updater20updateRootTransformsEPNS_4Nod'
        'eES2_RK10QMatrix4x4',
        self._addressOf(n), self._addressOf(root), self._valueOf(combined),
    )

  @overload(QSGNode)
  @overload(NoneType)
  def updateStates(self, n: Optional[QSGNode]) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Updater::updateStates(QSGNode *n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-updater.html#updateStates

    Parameters
    ----------

    n : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGBatchRenderer::Updater::updateStates(QSGNode *n)
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer7Updater12updateStatesEP7QSGNode',
        self._addressOf(n, 'QSGNode'),
    )

  @staticmethod
  def registerWithParentRoot(*__, **_) -> Never:
    """
    Qt's 'void QSGBatchRenderer::Updater::registerWithParentRoot(QSGNode
    *subRoot, QSGNode *parentRoot)': cannot be called and cannot be called
    through the meta-object and cannot be copied: no header file has its
    code, Qt's source does not mark it or its class for use from outside Qt
    or writes it 'inline' or nowhere, and it is no signal, slot or invokable
    function giving back nothing, of a class built on QObject, and Qt's
    source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QSGBatchRenderer.Updater.registerWithParentRoot' has no cute "
        "function yet. Qt's 'void "
        "QSGBatchRenderer::Updater::registerWithParentRoot(QSGNode "
        "*subRoot, QSGNode *parentRoot)': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def visitClipNode(*__, **_) -> Never:
    """
    Qt's 'void QSGBatchRenderer::Updater::visitClipNode(Node *n)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'SHADOWNODE_TRAVERSE'.
    """
    raise NotImplementedError(
        "'QSGBatchRenderer.Updater.visitClipNode' has no cute function yet. "
        "Qt's 'void QSGBatchRenderer::Updater::visitClipNode(Node *n)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'SHADOWNODE_TRAVERSE'.")

  @staticmethod
  def visitGeometryNode(*__, **_) -> Never:
    """
    Qt's 'void QSGBatchRenderer::Updater::visitGeometryNode(Node *n)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'isTranslate'.
    """
    raise NotImplementedError(
        "'QSGBatchRenderer.Updater.visitGeometryNode' has no cute function "
        "yet. Qt's 'void QSGBatchRenderer::Updater::visitGeometryNode(Node "
        "*n)': Qt's library has no name for it, and its code in Qt's source "
        "does not compile apart from its file: use of undeclared identifier "
        "'isTranslate'.")

  @staticmethod
  def visitOpacityNode(*__, **_) -> Never:
    """
    Qt's 'void QSGBatchRenderer::Updater::visitOpacityNode(Node *n)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'OPAQUE_LIMIT'.
    """
    raise NotImplementedError(
        "'QSGBatchRenderer.Updater.visitOpacityNode' has no cute function "
        "yet. Qt's 'void QSGBatchRenderer::Updater::visitOpacityNode(Node "
        "*n)': Qt's library has no name for it, and its code in Qt's source "
        "does not compile apart from its file: use of undeclared identifier "
        "'OPAQUE_LIMIT'.")

  @staticmethod
  def visitTransformNode(*__, **_) -> Never:
    """
    Qt's 'void QSGBatchRenderer::Updater::visitTransformNode(Node *n)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'SHADOWNODE_TRAVERSE'.
    """
    raise NotImplementedError(
        "'QSGBatchRenderer.Updater.visitTransformNode' has no cute function "
        "yet. Qt's 'void QSGBatchRenderer::Updater::visitTransformNode(Node "
        "*n)': Qt's library has no name for it, and its code in Qt's source "
        "does not compile apart from its file: use of undeclared identifier "
        "'SHADOWNODE_TRAVERSE'.")
