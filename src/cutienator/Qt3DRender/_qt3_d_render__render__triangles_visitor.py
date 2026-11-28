"""
Qt3DRender::Render::TrianglesVisitor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/trianglesvisitor_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::Render::TrianglesVisitor to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class TrianglesVisitor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::Render::TrianglesVisitor: a plain Python
  object standing in front of one C++ Qt3DRender::Render::TrianglesVisitor.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::TrianglesVisitor that has a
  ritual and that Python can call so far, 1 name in all: 'visit'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::TrianglesVisitor::~TrianglesVisitor()': the
    destructor: Python never removes a C++
    Qt3DRender::Render::TrianglesVisitor.

  What has no ritual
  ------------------

  3 of the 6 functions Qt declares: 2 leans on 'Qt3DRender; 1 cannot be
  called and cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::TrianglesVisitor is created at the first use,
    not by 'Qt3DRender::Render::TrianglesVisitor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::TrianglesVisitor.
  - Each name of Qt's Qt3DRender::Render::TrianglesVisitor that has no cute
    function yet, 'apply', holds a function that raises
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
  __qt_class__ = 'Qt3DRender::Render::TrianglesVisitor'

  #  A C++ Qt3DRender::Render::TrianglesVisitor Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_TrianglesVisitor'

  #  The functions Qt calls itself that Qt3DRender::Render::TrianglesVisitor
  #  is the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'visit': (
          ('_ZN10Qt3DRender6Render16TrianglesVisitor5visitEjRK9QVector3DjS4'
           '_jS4_',
           ('nothing', 'nothing', ''),
           (
               ('unsigned int', 'number', ''),
               ('address', 'value', 'QtGui:QVector3D'),
               ('unsigned int', 'number', ''),
               ('address', 'value', 'QtGui:QVector3D'),
               ('unsigned int', 'number', ''),
               ('address', 'value', 'QtGui:QVector3D'),
           )),
      ),
  }

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

  @overload(WAIT['Qt3DRender.Render.NodeManagers'])
  @overload(NoneType)
  def __init__(
      self,
      manager: Optional[Qt3DRender.Render.NodeManagers],
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::TrianglesVisitor::TrianglesVisitor(NodeManagers
    *manager)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-trianglesvisitor.html

    Parameters
    ----------

    manager : Optional[Qt3DRender.Render.NodeManagers]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  Qt3DRender::Render::TrianglesVisitor::TrianglesVisitor(NodeManagers
    #      *manager)
    self._noteCreation(TrianglesVisitor, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render16TrianglesVisitorC1EPNS0_12NodeManage'
        'rsE',
        self._addressOf(manager),
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

  @overload(int, QVector3D, int, QVector3D, int, QVector3D)
  def visit(
      self,
      andx: int,
      a: QVector3D,
      bndx: int,
      b: QVector3D,
      cndx: int,
      c: QVector3D,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::TrianglesVisitor::visit(uint andx,
    const Vector3D &a, uint bndx, const Vector3D &b, uint cndx, const
    Vector3D &c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-trianglesvisitor.html#visit

    Parameters
    ----------

    andx : int
      Passed on as it is.

    a : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    bndx : int
      Passed on as it is.

    b : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    cndx : int
      Passed on as it is.

    c : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DRender::Render::TrianglesVisitor::visit(uint andx, const
    #      Vector3D &a, uint bndx, const Vector3D &b, uint cndx, const
    #      Vector3D &c)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render16TrianglesVisitor5visitEjRK9QVector3D'
        'jS4_jS4_',
        andx, self._valueOf(a), bndx, self._valueOf(b), cndx,
        self._valueOf(c),
    )

  @staticmethod
  def apply(*__, **_) -> Never:
    """
    - Qt's 'void Qt3DRender::Render::TrianglesVisitor::apply(const
      PickingProxy *proxy, const Qt3DCore::QNodeId id)': cannot be called and
      cannot be called through the meta-object and cannot be copied: no
      header file has its code, Qt's source does not mark it or its class for
      use from outside Qt or writes it 'inline' or nowhere, and it is no
      signal, slot or invokable function giving back nothing, of a class
      built on QObject, and Qt's source has no code for it that could be told
      from the rest.
    - Qt's 'void Qt3DRender::Render::TrianglesVisitor::apply(const
      Qt3DCore::QEntity *entity)': leans on
      'Qt3DRender::Render::BufferManager*
      Qt3DRender::Render::NodeManagers::manager<Qt3DRender::Render::Buffer,
      Qt3DRender::Render::BufferManager>() const', which Qt's source does not
      mark for use from outside Qt and has no code for that could be taken.
    - Qt's 'void Qt3DRender::Render::TrianglesVisitor::apply(const
      GeometryRenderer *renderer, const Qt3DCore::QNodeId id)': leans on
      'Qt3DRender::Render::BufferManager*
      Qt3DRender::Render::NodeManagers::manager<Qt3DRender::Render::Buffer,
      Qt3DRender::Render::BufferManager>() const', which Qt's source does not
      mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.TrianglesVisitor.apply' has no cute function "
        "yet. Qt's 'void Qt3DRender::Render::TrianglesVisitor::apply(const "
        "PickingProxy *proxy, const Qt3DCore::QNodeId id)': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest. Qt's 'void "
        "Qt3DRender::Render::TrianglesVisitor::apply(const "
        "Qt3DCore::QEntity *entity)': leans on "
        "'Qt3DRender::Render::BufferManager* "
        "Qt3DRender::Render::NodeManagers::manager<Qt3DRender::Render::Buffe"
        "r, Qt3DRender::Render::BufferManager>() const', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken. Qt's 'void "
        "Qt3DRender::Render::TrianglesVisitor::apply(const GeometryRenderer "
        "*renderer, const Qt3DCore::QNodeId id)': leans on "
        "'Qt3DRender::Render::BufferManager* "
        "Qt3DRender::Render::NodeManagers::manager<Qt3DRender::Render::Buffe"
        "r, Qt3DRender::Render::BufferManager>() const', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")
