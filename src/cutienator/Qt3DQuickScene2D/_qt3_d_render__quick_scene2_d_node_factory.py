"""
Qt3DRender::QuickScene2DNodeFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DQuickScene2D/6.12.0/Qt3DQuickScene2D/private/qt3dquickscene2dnodefactory_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means Qt3DRender::QuickScene2DNodeFactory to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..Qt3DCore import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QuickScene2DNodeFactory(Qt3DCore.QAbstractNodeFactory):
  """
  The cute side of Qt's Qt3DRender::QuickScene2DNodeFactory: a plain Python
  object standing in front of one C++ Qt3DRender::QuickScene2DNodeFactory.

  It is built on the cute 'Qt3DCore::QAbstractNodeFactory', as Qt's
  Qt3DRender::QuickScene2DNodeFactory is built on Qt's
  Qt3DCore::QAbstractNodeFactory, and has everything that class has.

  C++ hands a Qt3DRender::QuickScene2DNodeFactory around as a copy, so every
  C++ Qt3DRender::QuickScene2DNodeFactory behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QuickScene2DNodeFactory that has a
  ritual and that Python can call so far, 2 names in all: 'createNode',
  'registerType'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::QuickScene2DNodeFactory::~QuickScene2DNodeFactory()':
    the destructor: Python removes its C++
    Qt3DRender::QuickScene2DNodeFactory by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 4 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ Qt3DRender::QuickScene2DNodeFactory is created at the first use,
    not by 'Qt3DRender::QuickScene2DNodeFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::QuickScene2DNodeFactory back gives a copy
    the ritual made for Python, in a new cute
    Qt3DRender::QuickScene2DNodeFactory.
  - Each name of Qt's Qt3DRender::QuickScene2DNodeFactory that has no cute
    function yet, 'instance', holds a function that raises
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
  __qt_class__ = 'Qt3DRender::QuickScene2DNodeFactory'

  #  Qt's '~Qt3DRender::QuickScene2DNodeFactory()'. Naming it makes this a
  #  value class: Python owns every C++ Qt3DRender::QuickScene2DNodeFactory
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender23QuickScene2DNodeFactoryD1Ev'

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

  @overload(str)
  @overload(NoneType)
  def createNode(self, type: Optional[str]) -> Optional[Qt3DCore.QNode]:
    """
    Calls Qt's 'Qt3DCore::QNode
    *Qt3DRender::QuickScene2DNodeFactory::createNode(const char *type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quickscene2dnodefactory.html#createNode

    Parameters
    ----------

    type : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    Returns
    -------

    Optional[Qt3DCore.QNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QNode *Qt3DRender::QuickScene2DNodeFactory::createNode(const
    #      char *type)
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender23QuickScene2DNodeFactory10createNodeEPKc',
        self._bytesOf(type),
    )
    return Qt3DCore.QNode._cuteAt(address)

  @overload(str, str, int, int)
  @overload(str, NoneType, int, int)
  @overload(NoneType, str, int, int)
  @overload(NoneType, NoneType, int, int)
  def registerType(
      self,
      className: Optional[str],
      quickName: Optional[str],
      major: int,
      minor: int,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::QuickScene2DNodeFactory::registerType(const
    char *className, const char *quickName, int major, int minor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quickscene2dnodefactory.html

    Parameters
    ----------

    className : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    quickName : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    major : int
      Passed on as it is.

    minor : int
      Passed on as it is.
    """
    #  void Qt3DRender::QuickScene2DNodeFactory::registerType(const char
    #      *className, const char *quickName, int major, int minor)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender23QuickScene2DNodeFactory12registerTypeEPKcS2'
        '_ii',
        self._bytesOf(className), self._bytesOf(quickName), major, minor,
    )

  @staticmethod
  def instance(*__, **_) -> Never:
    """
    Qt's 'QuickScene2DNodeFactory
    *Qt3DRender::QuickScene2DNodeFactory::instance()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'quick_scene2d_node_factory'; did you
    mean 'QuickScene2DNodeFactory'?.
    """
    raise NotImplementedError(
        "'Qt3DRender.QuickScene2DNodeFactory.instance' has no cute function "
        "yet. Qt's 'QuickScene2DNodeFactory "
        "*Qt3DRender::QuickScene2DNodeFactory::instance()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'quick_scene2d_node_factory'; did you mean "
        "'QuickScene2DNodeFactory'?.")
