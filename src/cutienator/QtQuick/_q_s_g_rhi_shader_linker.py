"""
QSGRhiShaderLinker binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgrhishadereffectnode_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGRhiShaderLinker to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QSGShaderEffectNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtGui import QShader
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QShader = WAIT['QShader']


class QSGRhiShaderLinker(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSGRhiShaderLinker: a plain Python object standing in
  front of one C++ QSGRhiShaderLinker.

  C++ hands a QSGRhiShaderLinker around as a copy, so every C++
  QSGRhiShaderLinker behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSGRhiShaderLinker that has a ritual and that Python
  can call so far, 2 names in all: 'reset', 'linkTextureSubRects'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QSGRhiShaderLinker::feedConstants(const
    QSGShaderEffectNode::ShaderData &shader, const QSet<int> *dirtyIndices)':
    names 'QSet<int>', which has no cute class yet.
  - Qt's 'void QSGRhiShaderLinker::feedSamplers(const
    QSGShaderEffectNode::ShaderData &shader, const QSet<int> *dirtyIndices)':
    names 'QSet<int>', which has no cute class yet.
  - Qt's 'QSGRhiShaderLinker::~QSGRhiShaderLinker()': the destructor: Python
    removes its C++ QSGRhiShaderLinker by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 6 functions Qt declares: 1 leans on 'operator<<(QDebug,
  QSGRhiShaderLinker.

  What to expect
  --------------

  - The C++ QSGRhiShaderLinker is created at the first use, not by
    'QSGRhiShaderLinker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSGRhiShaderLinker back gives a copy the ritual made
    for Python, in a new cute QSGRhiShaderLinker.
  - Each name of Qt's QSGRhiShaderLinker that has no cute function yet,
    'dump', 'feedConstants', 'feedSamplers', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QSGRhiShaderLinker, each a class in here as
  #  in C++.

  class Constant(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSGRhiShaderLinker::Constant: a plain Python object
    standing in front of one C++ QSGRhiShaderLinker::Constant.

    C++ hands a QSGRhiShaderLinker::Constant around as a copy, so every C++
    QSGRhiShaderLinker::Constant behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QSGRhiShaderLinker::Constant that has a ritual and
    that Python can call so far, 1 name in all: '__eq__'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSGRhiShaderLinker::Constant::~Constant()': the destructor:
      Python removes its C++ QSGRhiShaderLinker::Constant by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QSGRhiShaderLinker::Constant is created at the first use, not
      by 'QSGRhiShaderLinker::Constant(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSGRhiShaderLinker::Constant back gives a copy the
      ritual made for Python, in a new cute QSGRhiShaderLinker::Constant.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSGRhiShaderLinker::Constant'

    #  Qt's '~QSGRhiShaderLinker::Constant()'. Naming it makes this a value
    #  class: Python owns every C++ QSGRhiShaderLinker::Constant behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN18QSGRhiShaderLinker8ConstantD1Ev'

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

    @overload(THIS)
    def __eq__(self, other: QSGRhiShaderLinker.Constant) -> bool:
      """
      Calls Qt's 'bool QSGRhiShaderLinker::Constant::operator==(const
      Constant &other) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsgrhishaderlinker-constant.html#operator==

      Parameters
      ----------

      other : QSGRhiShaderLinker.Constant
        Passed on as a value: Qt reads the C++ QSGRhiShaderLinker::Constant,
        which stays Python's own.
      """
      #  bool QSGRhiShaderLinker::Constant::operator==(const Constant &other)
      #      const
      return self.uglySide.call(
          'ritual_ZNK18QSGRhiShaderLinker8ConstanteqERKS0_',
          self._valueOf(other),
      )

    @overload.fallback
    def __eq__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGRhiShaderLinker'

  #  Qt's '~QSGRhiShaderLinker()'. Naming it makes this a value class: Python
  #  owns every C++ QSGRhiShaderLinker behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QSGRhiShaderLinkerD1Ev'

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

  @overload(QShader, QShader)
  def reset(self, vs: QShader, fs: QShader) -> None:
    """
    Calls Qt's 'void QSGRhiShaderLinker::reset(const QShader &vs, const
    QShader &fs)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrhishaderlinker.html#reset

    Parameters
    ----------

    vs : QShader
      Passed on as a value: Qt reads the C++ QShader, which stays Python's
      own.

    fs : QShader
      Passed on as a value: Qt reads the C++ QShader, which stays Python's
      own.
    """
    #  void QSGRhiShaderLinker::reset(const QShader &vs, const QShader &fs)
    self.uglySide.call(
        'ritual_ZN18QSGRhiShaderLinker5resetERK7QShaderS2_',
        self._valueOf(vs), self._valueOf(fs),
    )

  def linkTextureSubRects(self) -> None:
    """
    Calls Qt's 'void QSGRhiShaderLinker::linkTextureSubRects()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhishaderlinker.html#linkTextureSubRects
    """
    #  void QSGRhiShaderLinker::linkTextureSubRects()
    self.uglySide.call(
        'ritual_ZN18QSGRhiShaderLinker19linkTextureSubRectsEv',
    )

  @staticmethod
  def dump(*__, **_) -> Never:
    """
    Qt's 'void QSGRhiShaderLinker::dump()': leans on 'operator<<(QDebug,
    QSGRhiShaderLinker::Constant const&)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSGRhiShaderLinker.dump' has no cute function yet. Qt's 'void "
        "QSGRhiShaderLinker::dump()': leans on 'operator<<(QDebug, "
        "QSGRhiShaderLinker::Constant const&)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def feedConstants(*__, **_) -> Never:
    """
    Qt's 'void QSGRhiShaderLinker::feedConstants(const
    QSGShaderEffectNode::ShaderData &shader, const QSet<int> *dirtyIndices)':
    names 'QSet<int>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSGRhiShaderLinker.feedConstants' has no cute function yet. Qt's "
        "'void QSGRhiShaderLinker::feedConstants(const "
        "QSGShaderEffectNode::ShaderData &shader, const QSet<int> "
        "*dirtyIndices)': names 'QSet<int>', which has no cute class yet.")

  @staticmethod
  def feedSamplers(*__, **_) -> Never:
    """
    Qt's 'void QSGRhiShaderLinker::feedSamplers(const
    QSGShaderEffectNode::ShaderData &shader, const QSet<int> *dirtyIndices)':
    names 'QSet<int>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSGRhiShaderLinker.feedSamplers' has no cute function yet. Qt's "
        "'void QSGRhiShaderLinker::feedSamplers(const "
        "QSGShaderEffectNode::ShaderData &shader, const QSet<int> "
        "*dirtyIndices)': names 'QSet<int>', which has no cute class yet.")
