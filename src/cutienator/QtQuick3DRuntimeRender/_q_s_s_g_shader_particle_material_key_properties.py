"""
QSSGShaderParticleMaterialKeyProperties binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderparticleshaderkeys_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGShaderParticleMaterialKeyProperties to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSSGShaderParticleMaterialKeyProperties(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGShaderParticleMaterialKeyProperties: a plain
  Python object standing in front of one C++
  QSSGShaderParticleMaterialKeyProperties.

  C++ hands a QSSGShaderParticleMaterialKeyProperties around as a copy, so
  every C++ QSSGShaderParticleMaterialKeyProperties behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGShaderParticleMaterialKeyProperties that has a
  ritual and that Python can call so far, 1 name in all: 'init'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGShaderParticleMaterialKeyProperties::
    ~QSSGShaderParticleMaterialKeyProperties()': the destructor: Python
    removes its C++ QSSGShaderParticleMaterialKeyProperties by it, and has no
    other use for it.

  What has no ritual
  ------------------

  1 of the 4 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QSSGShaderParticleMaterialKeyProperties is created at the first
    use, not by 'QSSGShaderParticleMaterialKeyProperties(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGShaderParticleMaterialKeyProperties back gives a
    copy the ritual made for Python, in a new cute
    QSSGShaderParticleMaterialKeyProperties.
  - Each name of Qt's QSSGShaderParticleMaterialKeyProperties that has no
    cute function yet, 'visitProperties', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QSSGShaderParticleMaterialKeyProperties,
  #  each a class in here as in C++.

  class InitVisitor(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's
    QSSGShaderParticleMaterialKeyProperties::InitVisitor: a plain Python
    object standing in front of one C++
    QSSGShaderParticleMaterialKeyProperties::InitVisitor.

    C++ hands a QSSGShaderParticleMaterialKeyProperties::InitVisitor around
    as a copy, so every C++
    QSSGShaderParticleMaterialKeyProperties::InitVisitor behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QSSGShaderParticleMaterialKeyProperties::InitVisitor
    yet. None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QSSGShaderParticleMaterialKeyProperties::InitVisitor::~InitVisitor()':
      the destructor: Python removes its C++
      QSSGShaderParticleMaterialKeyProperties::InitVisitor by it, and has no
      other use for it.

    What has no ritual
    ------------------

    1 of the 2 functions Qt declares: 1 a template.

    What to expect
    --------------

    - The C++ QSSGShaderParticleMaterialKeyProperties::InitVisitor is created
      at the first use, not by
      'QSSGShaderParticleMaterialKeyProperties::InitVisitor(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a
      QSSGShaderParticleMaterialKeyProperties::InitVisitor back gives a copy
      the ritual made for Python, in a new cute
      QSSGShaderParticleMaterialKeyProperties::InitVisitor.
    - Each name of Qt's QSSGShaderParticleMaterialKeyProperties::InitVisitor
      that has no cute function yet, 'visit', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGShaderParticleMaterialKeyProperties::InitVisitor'

    #  Qt's '~QSSGShaderParticleMaterialKeyProperties::InitVisitor()'. Naming
    #  it makes this a value class: Python owns every C++
    #  QSSGShaderParticleMaterialKeyProperties::InitVisitor behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN39QSSGShaderParticleMaterialKeyProperties11InitVisitorD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    def visit(*__, **_) -> Never:
      """
      Qt's 'QSSGShaderParticleMaterialKeyProperties::InitVisitor::visit': a
      template: a pattern and no single function.
      """
      raise NotImplementedError(
          "'QSSGShaderParticleMaterialKeyProperties.InitVisitor.visit' has "
          "no cute function yet. Qt's "
          "'QSSGShaderParticleMaterialKeyProperties::InitVisitor::visit': a "
          "template: a pattern and no single function.")

  class OffsetVisitor(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's
    QSSGShaderParticleMaterialKeyProperties::OffsetVisitor: a plain Python
    object standing in front of one C++
    QSSGShaderParticleMaterialKeyProperties::OffsetVisitor.

    C++ hands a QSSGShaderParticleMaterialKeyProperties::OffsetVisitor around
    as a copy, so every C++
    QSSGShaderParticleMaterialKeyProperties::OffsetVisitor behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's
    QSSGShaderParticleMaterialKeyProperties::OffsetVisitor yet. It can be
    made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGShaderParticleMaterialKeyProperties::OffsetVisitor::
      ~OffsetVisitor()': the destructor: Python removes its C++
      QSSGShaderParticleMaterialKeyProperties::OffsetVisitor by it, and has
      no other use for it.

    What has no ritual
    ------------------

    1 of the 3 functions Qt declares: 1 a template.

    What to expect
    --------------

    - The C++ QSSGShaderParticleMaterialKeyProperties::OffsetVisitor is
      created at the first use, not by
      'QSSGShaderParticleMaterialKeyProperties::OffsetVisitor(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a
      QSSGShaderParticleMaterialKeyProperties::OffsetVisitor back gives a
      copy the ritual made for Python, in a new cute
      QSSGShaderParticleMaterialKeyProperties::OffsetVisitor.
    - Each name of Qt's
      QSSGShaderParticleMaterialKeyProperties::OffsetVisitor that has no cute
      function yet, 'visit', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGShaderParticleMaterialKeyProperties::OffsetVisitor'

    #  Qt's '~QSSGShaderParticleMaterialKeyProperties::OffsetVisitor()'.
    #  Naming it makes this a value class: Python owns every C++
    #  QSSGShaderParticleMaterialKeyProperties::OffsetVisitor behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN39QSSGShaderParticleMaterialKeyProperties13OffsetVisitorD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QSSGShaderParticleMaterialKeyProperties::OffsetVisitor::OffsetVisitor(
      )', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgshaderparticlematerialkeyproperties-offsetvisitor.html
      """
      #  QSSGShaderParticleMaterialKeyProperties::OffsetVisitor::
      #      OffsetVisitor()
      self._noteCreation(
          QSSGShaderParticleMaterialKeyProperties.OffsetVisitor, lambda: Rituals.call(
              'ritual_ZN39QSSGShaderParticleMaterialKeyProperties13OffsetVi'
              'sitorC1Ev',
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    def visit(*__, **_) -> Never:
      """
      Qt's 'QSSGShaderParticleMaterialKeyProperties::OffsetVisitor::visit': a
      template: a pattern and no single function.
      """
      raise NotImplementedError(
          "'QSSGShaderParticleMaterialKeyProperties.OffsetVisitor.visit' "
          "has no cute function yet. Qt's "
          "'QSSGShaderParticleMaterialKeyProperties::OffsetVisitor::visit': "
          "a template: a pattern and no single function.")

  class StringSizeVisitor(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's
    QSSGShaderParticleMaterialKeyProperties::StringSizeVisitor: a plain
    Python object standing in front of one C++
    QSSGShaderParticleMaterialKeyProperties::StringSizeVisitor.

    C++ hands a QSSGShaderParticleMaterialKeyProperties::StringSizeVisitor
    around as a copy, so every C++
    QSSGShaderParticleMaterialKeyProperties::StringSizeVisitor behind a cute
    one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's
    QSSGShaderParticleMaterialKeyProperties::StringSizeVisitor yet. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGShaderParticleMaterialKeyProperties::StringSizeVisitor::
      ~StringSizeVisitor()': the destructor: Python removes its C++
      QSSGShaderParticleMaterialKeyProperties::StringSizeVisitor by it, and
      has no other use for it.

    What has no ritual
    ------------------

    1 of the 2 functions Qt declares: 1 a template.

    What to expect
    --------------

    - The C++ QSSGShaderParticleMaterialKeyProperties::StringSizeVisitor is
      created at the first use, not by
      'QSSGShaderParticleMaterialKeyProperties::StringSizeVisitor(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a
      QSSGShaderParticleMaterialKeyProperties::StringSizeVisitor back gives a
      copy the ritual made for Python, in a new cute
      QSSGShaderParticleMaterialKeyProperties::StringSizeVisitor.
    - Each name of Qt's
      QSSGShaderParticleMaterialKeyProperties::StringSizeVisitor that has no
      cute function yet, 'visit', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGShaderParticleMaterialKeyProperties::StringSizeVisitor'

    #  Qt's '~QSSGShaderParticleMaterialKeyProperties::StringSizeVisitor()'.
    #  Naming it makes this a value class: Python owns every C++
    #  QSSGShaderParticleMaterialKeyProperties::StringSizeVisitor behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN39QSSGShaderParticleMaterialKeyProperties17StringSizeVisitorD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    def visit(*__, **_) -> Never:
      """
      Qt's
      'QSSGShaderParticleMaterialKeyProperties::StringSizeVisitor::visit': a
      template: a pattern and no single function.
      """
      raise NotImplementedError(
          "'QSSGShaderParticleMaterialKeyProperties.StringSizeVisitor.visit'"
          " has no cute function yet. Qt's "
          "'QSSGShaderParticleMaterialKeyProperties::StringSizeVisitor::visi"
          "t': a template: a pattern and no single function.")

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGShaderParticleMaterialKeyProperties'

  #  Qt's '~QSSGShaderParticleMaterialKeyProperties()'. Naming it makes this
  #  a value class: Python owns every C++
  #  QSSGShaderParticleMaterialKeyProperties behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN39QSSGShaderParticleMaterialKeyPropertiesD1Ev')

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QSSGShaderParticleMaterialKeyProperties::
    QSSGShaderParticleMaterialKeyProperties()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderparticlematerialkeyproperties.html
    """
    #  QSSGShaderParticleMaterialKeyProperties::
    #      QSSGShaderParticleMaterialKeyProperties()
    self._noteCreation(
        QSSGShaderParticleMaterialKeyProperties, lambda: Rituals.call(
            'ritual_ZN39QSSGShaderParticleMaterialKeyPropertiesC1Ev',
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

  def init(self) -> None:
    """
    Calls Qt's 'void QSSGShaderParticleMaterialKeyProperties::init()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderparticlematerialkeyproperties.html#init
    """
    #  void QSSGShaderParticleMaterialKeyProperties::init()
    self.uglySide.call(
        'ritual_ZN39QSSGShaderParticleMaterialKeyProperties4initEv',
    )

  @staticmethod
  def visitProperties(*__, **_) -> Never:
    """
    Qt's 'QSSGShaderParticleMaterialKeyProperties::visitProperties': a
    template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QSSGShaderParticleMaterialKeyProperties.visitProperties' has no "
        "cute function yet. Qt's "
        "'QSSGShaderParticleMaterialKeyProperties::visitProperties': a "
        "template: a pattern and no single function.")
