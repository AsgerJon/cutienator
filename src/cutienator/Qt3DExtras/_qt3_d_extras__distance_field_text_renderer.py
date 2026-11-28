"""
Qt3DExtras::DistanceFieldTextRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/6.12.0/Qt3DExtras/private/distancefieldtextrenderer_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DExtras::DistanceFieldTextRenderer to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..Qt3DCore import Qt3DCore
from . import Qt3DExtras

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']


class DistanceFieldTextRenderer(Qt3DCore.QEntity):
  """
  The cute side of Qt's Qt3DExtras::DistanceFieldTextRenderer: a plain Python
  object standing in front of one C++ Qt3DExtras::DistanceFieldTextRenderer.

  It is built on the cute 'Qt3DCore::QEntity', as Qt's
  Qt3DExtras::DistanceFieldTextRenderer is built on Qt's Qt3DCore::QEntity,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::DistanceFieldTextRenderer that has a
  ritual and that Python can call so far, 3 names in all: 'metaObject',
  'setColor', 'd_func'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::DistanceFieldTextRenderer::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DExtras::DistanceFieldTextRenderer::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'Qt3DExtras::DistanceFieldTextRenderer::~DistanceFieldTextRenderer()':
    the destructor: Python never removes a C++
    Qt3DExtras::DistanceFieldTextRenderer.
  - Qt's 'void
    Qt3DExtras::DistanceFieldTextRenderer::setGlyphData(Qt3DRender::
    QAbstractTexture *glyphTexture, const std::vector<float> &vertexData,
    const std::vector<quint16> &indexData)': takes a type Python has no way
    to hand over yet.
  - Qt's 'const DistanceFieldTextRendererPrivate
    *Qt3DExtras::DistanceFieldTextRenderer::d_func() const': takes in Python
    what 'DistanceFieldTextRendererPrivate
    *Qt3DExtras::DistanceFieldTextRenderer::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 12 functions Qt declares: 2 not a gap; 2 leans on 'Qt3DExtras.

  What to expect
  --------------

  - The C++ Qt3DExtras::DistanceFieldTextRenderer is created at the first
    use, not by 'Qt3DExtras::DistanceFieldTextRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::DistanceFieldTextRenderer.
  - Qt tells when it has removed the C++
    Qt3DExtras::DistanceFieldTextRenderer. Every call on the cute object, and
    every use of it as an argument, then raises 'RuntimeError', and nothing
    reaches C++.
  - Each name of Qt's Qt3DExtras::DistanceFieldTextRenderer that has no cute
    function yet, '__init__', 'setGlyphData', holds a function that raises
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
  __qt_class__ = 'Qt3DExtras::DistanceFieldTextRenderer'

  #  A C++ Qt3DExtras::DistanceFieldTextRenderer Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_DistanceFieldTextRenderer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *Qt3DExtras::DistanceFieldTextRenderer::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-distancefieldtextrenderer.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DExtras::DistanceFieldTextRenderer::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras25DistanceFieldTextRenderer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void Qt3DExtras::DistanceFieldTextRenderer::setColor(const
    QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-distancefieldtextrenderer.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::DistanceFieldTextRenderer::setColor(const QColor
    #      &color)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras25DistanceFieldTextRenderer8setColorERK6QColo'
        'r',
        self._valueOf(color),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'Qt3DExtras::DistanceFieldTextRenderer::DistanceFieldTextRenderer(
    Qt3DCore::QNode *parent)': leans on
    'Qt3DExtras::DistanceFieldTextRenderer::qt_metacall(QMetaObject::Call,
    int, void**)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DExtras.DistanceFieldTextRenderer.__init__' has no cute "
        "function yet. Qt's "
        "'Qt3DExtras::DistanceFieldTextRenderer::DistanceFieldTextRenderer(Q"
        "t3DCore::QNode *parent)': leans on "
        "'Qt3DExtras::DistanceFieldTextRenderer::qt_metacall(QMetaObject::Ca"
        "ll, int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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

  def d_func(self) -> Optional[Qt3DExtras.DistanceFieldTextRendererPrivate]:
    """
    Calls Qt's 'DistanceFieldTextRendererPrivate
    *Qt3DExtras::DistanceFieldTextRenderer::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-distancefieldtextrenderer.html#d_func

    Returns
    -------

    Optional[Qt3DExtras.DistanceFieldTextRendererPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DistanceFieldTextRendererPrivate
    #      *Qt3DExtras::DistanceFieldTextRenderer::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras25DistanceFieldTextRenderer6d_funcEv',
    )
    return Qt3DExtras.DistanceFieldTextRendererPrivate._cuteAt(address)

  @staticmethod
  def setGlyphData(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DExtras::DistanceFieldTextRenderer::setGlyphData(Qt3DRender::
    QAbstractTexture *glyphTexture, const std::vector<float> &vertexData,
    const std::vector<quint16> &indexData)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DExtras.DistanceFieldTextRenderer.setGlyphData' has no cute "
        "function yet. Qt's 'void "
        "Qt3DExtras::DistanceFieldTextRenderer::setGlyphData(Qt3DRender::QAb"
        "stractTexture *glyphTexture, const std::vector<float> &vertexData, "
        "const std::vector<quint16> &indexData)': takes a type Python has "
        "no way to hand over yet.")
