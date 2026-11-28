"""
Qt3DRender::QuickRenderNodeFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DQuickRender/6.12.0/Qt3DQuickRender/private/qt3dquickrendernodefactory_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means Qt3DRender::QuickRenderNodeFactory to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
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


class QuickRenderNodeFactory(Qt3DCore.QAbstractNodeFactory):
  """
  The cute side of Qt's Qt3DRender::QuickRenderNodeFactory: a plain Python
  object standing in front of one C++ Qt3DRender::QuickRenderNodeFactory.

  It is built on the cute 'Qt3DCore::QAbstractNodeFactory', as Qt's
  Qt3DRender::QuickRenderNodeFactory is built on Qt's
  Qt3DCore::QAbstractNodeFactory, and has everything that class has.

  C++ hands a Qt3DRender::QuickRenderNodeFactory around as a copy, so every
  C++ Qt3DRender::QuickRenderNodeFactory behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QuickRenderNodeFactory that has a ritual
  and that Python can call so far, 2 names in all: 'createNode',
  'registerType'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::QuickRenderNodeFactory::~QuickRenderNodeFactory()': the
    destructor: Python removes its C++ Qt3DRender::QuickRenderNodeFactory by
    it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 4 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ Qt3DRender::QuickRenderNodeFactory is created at the first use,
    not by 'Qt3DRender::QuickRenderNodeFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::QuickRenderNodeFactory back gives a copy
    the ritual made for Python, in a new cute
    Qt3DRender::QuickRenderNodeFactory.
  - Each name of Qt's Qt3DRender::QuickRenderNodeFactory that has no cute
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
  __qt_class__ = 'Qt3DRender::QuickRenderNodeFactory'

  #  Qt's '~Qt3DRender::QuickRenderNodeFactory()'. Naming it makes this a
  #  value class: Python owns every C++ Qt3DRender::QuickRenderNodeFactory
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender22QuickRenderNodeFactoryD1Ev'

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
    *Qt3DRender::QuickRenderNodeFactory::createNode(const char *type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quickrendernodefactory.html#createNode

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
    #  Qt3DCore::QNode *Qt3DRender::QuickRenderNodeFactory::createNode(const
    #      char *type)
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender22QuickRenderNodeFactory10createNodeEPKc',
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
    Calls Qt's 'void Qt3DRender::QuickRenderNodeFactory::registerType(const
    char *className, const char *quickName, int major, int minor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quickrendernodefactory.html

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
    #  void Qt3DRender::QuickRenderNodeFactory::registerType(const char
    #      *className, const char *quickName, int major, int minor)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender22QuickRenderNodeFactory12registerTypeEPKcS2_'
        'ii',
        self._bytesOf(className), self._bytesOf(quickName), major, minor,
    )

  @staticmethod
  def instance(*__, **_) -> Never:
    """
    Qt's 'QuickRenderNodeFactory
    *Qt3DRender::QuickRenderNodeFactory::instance()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'quick_render_node_factory'; did you
    mean 'QuickRenderNodeFactory'?.
    """
    raise NotImplementedError(
        "'Qt3DRender.QuickRenderNodeFactory.instance' has no cute function "
        "yet. Qt's 'QuickRenderNodeFactory "
        "*Qt3DRender::QuickRenderNodeFactory::instance()': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier "
        "'quick_render_node_factory'; did you mean "
        "'QuickRenderNodeFactory'?.")
