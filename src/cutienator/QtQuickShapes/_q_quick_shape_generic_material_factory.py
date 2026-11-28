"""
QQuickShapeGenericMaterialFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapegenericrenderer_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickShapeGenericMaterialFactory to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickShapeGenericStrokeFillNode
  from ..QtQuick import QQuickWindow, QSGMaterial
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickShapeGenericStrokeFillNode = WAIT['QQuickShapeGenericStrokeFillNode']
  QQuickWindow = WAIT['QQuickWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickShapeGenericMaterialFactory(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickShapeGenericMaterialFactory: a plain Python
  object standing in front of one C++ QQuickShapeGenericMaterialFactory.

  C++ hands a QQuickShapeGenericMaterialFactory around as a copy, so every
  C++ QQuickShapeGenericMaterialFactory behind a cute one is Python's own: it
  is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's QQuickShapeGenericMaterialFactory that has a ritual
  and that Python can call so far, 5 names in all: 'createVertexColor',
  'createLinearGradient', 'createRadialGradient', 'createConicalGradient',
  'createTextureFill'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QQuickShapeGenericMaterialFactory::~QQuickShapeGenericMaterialFactory(
    )': the destructor: Python removes its C++
    QQuickShapeGenericMaterialFactory by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQuickShapeGenericMaterialFactory is created at the first use,
    not by 'QQuickShapeGenericMaterialFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickShapeGenericMaterialFactory back gives a copy
    the ritual made for Python, in a new cute
    QQuickShapeGenericMaterialFactory.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickWindow)
  @overload(NoneType)
  def createVertexColor(
      window: Optional[QQuickWindow],
  ) -> Optional[QSGMaterial]:
    """
    Calls Qt's 'QSGMaterial
    *QQuickShapeGenericMaterialFactory::createVertexColor(QQuickWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapegenericmaterialfactory.html

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGMaterial]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGMaterial
    #      *QQuickShapeGenericMaterialFactory::createVertexColor(QQuickWindow
    #      *window)
    address = Rituals.call(
        'ritual_ZN33QQuickShapeGenericMaterialFactory17createVertexColorEP1'
        '2QQuickWindow',
        CuteMixin._addressOf(window),
    )
    from ..QtQuick import QSGMaterial
    return QSGMaterial._cuteAt(address)

  @staticmethod
  @overload(QQuickWindow, QQuickShapeGenericStrokeFillNode)
  @overload(QQuickWindow, NoneType)
  @overload(NoneType, QQuickShapeGenericStrokeFillNode)
  @overload(NoneType, NoneType)
  def createLinearGradient(
      window: Optional[QQuickWindow],
      node: Optional[QQuickShapeGenericStrokeFillNode],
  ) -> Optional[QSGMaterial]:
    """
    Calls Qt's 'QSGMaterial
    *QQuickShapeGenericMaterialFactory::createLinearGradient(QQuickWindow
    *window, QQuickShapeGenericStrokeFillNode *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapegenericmaterialfactory.html

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    node : Optional[QQuickShapeGenericStrokeFillNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGMaterial]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGMaterial *QQuickShapeGenericMaterialFactory::createLinearGradient(
    #      QQuickWindow *window, QQuickShapeGenericStrokeFillNode *node)
    address = Rituals.call(
        'ritual_ZN33QQuickShapeGenericMaterialFactory20createLinearGradient'
        'EP12QQuickWindowP32QQuickShapeGenericStrokeFillNode',
        CuteMixin._addressOf(window), CuteMixin._addressOf(node),
    )
    from ..QtQuick import QSGMaterial
    return QSGMaterial._cuteAt(address)

  @staticmethod
  @overload(QQuickWindow, QQuickShapeGenericStrokeFillNode)
  @overload(QQuickWindow, NoneType)
  @overload(NoneType, QQuickShapeGenericStrokeFillNode)
  @overload(NoneType, NoneType)
  def createRadialGradient(
      window: Optional[QQuickWindow],
      node: Optional[QQuickShapeGenericStrokeFillNode],
  ) -> Optional[QSGMaterial]:
    """
    Calls Qt's 'QSGMaterial
    *QQuickShapeGenericMaterialFactory::createRadialGradient(QQuickWindow
    *window, QQuickShapeGenericStrokeFillNode *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapegenericmaterialfactory.html

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    node : Optional[QQuickShapeGenericStrokeFillNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGMaterial]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGMaterial *QQuickShapeGenericMaterialFactory::createRadialGradient(
    #      QQuickWindow *window, QQuickShapeGenericStrokeFillNode *node)
    address = Rituals.call(
        'ritual_ZN33QQuickShapeGenericMaterialFactory20createRadialGradient'
        'EP12QQuickWindowP32QQuickShapeGenericStrokeFillNode',
        CuteMixin._addressOf(window), CuteMixin._addressOf(node),
    )
    from ..QtQuick import QSGMaterial
    return QSGMaterial._cuteAt(address)

  @staticmethod
  @overload(QQuickWindow, QQuickShapeGenericStrokeFillNode)
  @overload(QQuickWindow, NoneType)
  @overload(NoneType, QQuickShapeGenericStrokeFillNode)
  @overload(NoneType, NoneType)
  def createConicalGradient(
      window: Optional[QQuickWindow],
      node: Optional[QQuickShapeGenericStrokeFillNode],
  ) -> Optional[QSGMaterial]:
    """
    Calls Qt's 'QSGMaterial
    *QQuickShapeGenericMaterialFactory::createConicalGradient(QQuickWindow
    *window, QQuickShapeGenericStrokeFillNode *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapegenericmaterialfactory.html

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    node : Optional[QQuickShapeGenericStrokeFillNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGMaterial]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGMaterial *QQuickShapeGenericMaterialFactory::createConicalGradient(
    #      QQuickWindow *window, QQuickShapeGenericStrokeFillNode *node)
    address = Rituals.call(
        'ritual_ZN33QQuickShapeGenericMaterialFactory21createConicalGradien'
        'tEP12QQuickWindowP32QQuickShapeGenericStrokeFillNode',
        CuteMixin._addressOf(window), CuteMixin._addressOf(node),
    )
    from ..QtQuick import QSGMaterial
    return QSGMaterial._cuteAt(address)

  @staticmethod
  @overload(QQuickWindow, QQuickShapeGenericStrokeFillNode)
  @overload(QQuickWindow, NoneType)
  @overload(NoneType, QQuickShapeGenericStrokeFillNode)
  @overload(NoneType, NoneType)
  def createTextureFill(
      window: Optional[QQuickWindow],
      node: Optional[QQuickShapeGenericStrokeFillNode],
  ) -> Optional[QSGMaterial]:
    """
    Calls Qt's 'QSGMaterial
    *QQuickShapeGenericMaterialFactory::createTextureFill(QQuickWindow
    *window, QQuickShapeGenericStrokeFillNode *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapegenericmaterialfactory.html

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    node : Optional[QQuickShapeGenericStrokeFillNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGMaterial]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGMaterial
    #      *QQuickShapeGenericMaterialFactory::createTextureFill(QQuickWindow
    #      *window, QQuickShapeGenericStrokeFillNode *node)
    address = Rituals.call(
        'ritual_ZN33QQuickShapeGenericMaterialFactory17createTextureFillEP1'
        '2QQuickWindowP32QQuickShapeGenericStrokeFillNode',
        CuteMixin._addressOf(window), CuteMixin._addressOf(node),
    )
    from ..QtQuick import QSGMaterial
    return QSGMaterial._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickShapeGenericMaterialFactory'

  #  Qt's '~QQuickShapeGenericMaterialFactory()'. Naming it makes this a
  #  value class: Python owns every C++ QQuickShapeGenericMaterialFactory
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN33QQuickShapeGenericMaterialFactoryD1Ev'

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
