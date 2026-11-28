"""
QQuick3DSimpleQuadRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/qquick3dsimplequadrenderpass_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DSimpleQuadRenderer to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtQuick3D import QQuick3DObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtQuick3D import QQuick3DSceneManager, QQuick3DTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DSceneManager = WAIT['QQuick3DSceneManager']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DSimpleQuadRenderer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuick3DSimpleQuadRenderer: a plain Python object
  standing in front of one C++ QQuick3DSimpleQuadRenderer.

  What exists
  -----------

  Every function of Qt's QQuick3DSimpleQuadRenderer that has a ritual and
  that Python can call so far, 5 names in all: 'metaObject', 'texture',
  'textureChanged', 'itemChange', 'updateSceneManager'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DSimpleQuadRenderer::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuick3DSimpleQuadRenderer::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  6 of the 13 functions Qt declares: 3 leans on 'QQuick3DSimpleQuadRenderer;
  2 not a gap; 1 leans on 'vtable for QQuick3DSimpleQuadRenderer', which Qt's
  source does not mark for use from outside Qt and has no code for that could
  be taken.

  What to expect
  --------------

  - The C++ QQuick3DSimpleQuadRenderer is created at the first use, not by
    'QQuick3DSimpleQuadRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DSimpleQuadRenderer.
  - Qt tells when it has removed the C++ QQuick3DSimpleQuadRenderer. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DSimpleQuadRenderer that has no cute function
    yet, '__init__', 'setTexture', holds a function that raises
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
  __qt_class__ = 'QQuick3DSimpleQuadRenderer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DSimpleQuadRenderer::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsimplequadrenderer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DSimpleQuadRenderer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuick3DSimpleQuadRenderer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def texture(self) -> Optional[QQuick3DTexture]:
    """
    Calls Qt's 'QQuick3DTexture *QQuick3DSimpleQuadRenderer::texture()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsimplequadrenderer.html#texture

    Returns
    -------

    Optional[QQuick3DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DTexture *QQuick3DSimpleQuadRenderer::texture() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuick3DSimpleQuadRenderer7textureEv',
    )
    from ..QtQuick3D import QQuick3DTexture
    return QQuick3DTexture._cuteAt(address)

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
    Qt's 'QQuick3DSimpleQuadRenderer::QQuick3DSimpleQuadRenderer()': leans on
    'vtable for QQuick3DSimpleQuadRenderer', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DSimpleQuadRenderer.__init__' has no cute function yet. "
        "Qt's 'QQuick3DSimpleQuadRenderer::QQuick3DSimpleQuadRenderer()': "
        "leans on 'vtable for QQuick3DSimpleQuadRenderer', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  def textureChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSimpleQuadRenderer::textureChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsimplequadrenderer.html#textureChanged
    """
    #  void QQuick3DSimpleQuadRenderer::textureChanged()
    self.uglySide.call(
        'ritual_ZN26QQuick3DSimpleQuadRenderer14textureChangedEv',
    )

  @overload(QQuick3DObject.ItemChange, QQuick3DObject.ItemChangeData)
  def itemChange(
      self,
      a0: QQuick3DObject.ItemChange,
      a1: QQuick3DObject.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DSimpleQuadRenderer::itemChange(ItemChange a0,
    const ItemChangeData &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsimplequadrenderer.html#itemChange

    Parameters
    ----------

    a0 : QQuick3DObject.ItemChange
      Passed on as its number.

    a1 : QQuick3DObject.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuick3DObject::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuick3DSimpleQuadRenderer::itemChange(ItemChange a0, const
    #      ItemChangeData &a1)
    self.uglySide.call(
        'ritual_ZN26QQuick3DSimpleQuadRenderer10itemChangeEN14QQuick3DObjec'
        't10ItemChangeERKNS0_14ItemChangeDataE',
        a0.value, self._valueOf(a1),
    )

  @overload(QQuick3DSceneManager)
  @overload(NoneType)
  def updateSceneManager(
      self,
      sceneManager: Optional[QQuick3DSceneManager],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSimpleQuadRenderer::updateSceneManager(QQuick3DSceneManager
    *sceneManager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dsimplequadrenderer.html#updateSceneManager

    Parameters
    ----------

    sceneManager : Optional[QQuick3DSceneManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DSimpleQuadRenderer::updateSceneManager(
    #      QQuick3DSceneManager *sceneManager)
    self.uglySide.call(
        'ritual_ZN26QQuick3DSimpleQuadRenderer18updateSceneManagerEP20QQuic'
        'k3DSceneManager',
        self._addressOf(sceneManager),
    )

  @staticmethod
  def setTexture(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DSimpleQuadRenderer::setTexture(QQuick3DTexture
    *newSource)': leans on 'QQuick3DSimpleQuadRenderer::textureChanged()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DSimpleQuadRenderer.setTexture' has no cute function yet. "
        "Qt's 'void QQuick3DSimpleQuadRenderer::setTexture(QQuick3DTexture "
        "*newSource)': leans on "
        "'QQuick3DSimpleQuadRenderer::textureChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")
