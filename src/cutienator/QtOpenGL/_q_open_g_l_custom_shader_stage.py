"""
QOpenGLCustomShaderStage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/6.12.0/QtOpenGL/private/qopenglcustomshaderstage_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QOpenGLCustomShaderStage to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
  from ..QtGui import QPainter
  from . import QOpenGLShaderProgram
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QOpenGLShaderProgram = WAIT['QOpenGLShaderProgram']
  QPainter = WAIT['QPainter']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLCustomShaderStage(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpenGLCustomShaderStage: a plain Python object
  standing in front of one C++ QOpenGLCustomShaderStage.

  What exists
  -----------

  Every function of Qt's QOpenGLCustomShaderStage that has a ritual and that
  Python can call so far, 7 names in all: 'setUniforms', 'setUniformsDirty',
  'setOnPainter', 'removeFromPainter', 'source', 'setInactive', 'setSource'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLCustomShaderStagePrivate
    *QOpenGLCustomShaderStage::d_func()': gives
    'QOpenGLCustomShaderStagePrivate', which has no cute class yet.
  - Qt's 'const QOpenGLCustomShaderStagePrivate
    *QOpenGLCustomShaderStage::d_func() const': gives
    'QOpenGLCustomShaderStagePrivate', which has no cute class yet.
  - Qt's 'QOpenGLCustomShaderStage::~QOpenGLCustomShaderStage()': the
    destructor: Python never removes a C++ QOpenGLCustomShaderStage.

  What has no ritual
  ------------------

  4 of the 15 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QOpenGLCustomShaderStage is created at the first use, not by
    'QOpenGLCustomShaderStage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLCustomShaderStage.
  - Each name of Qt's QOpenGLCustomShaderStage that has no cute function yet,
    'd_func', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLCustomShaderStage'

  #  A C++ QOpenGLCustomShaderStage Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpenGLCustomShaderStage'

  #  The functions Qt calls itself that QOpenGLCustomShaderStage is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setUniforms': (
          ('_ZN24QOpenGLCustomShaderStage11setUniformsEP20QOpenGLShaderProg'
           'ram',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtOpenGL:QOpenGLShaderProgram'),
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

  def source(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QOpenGLCustomShaderStage::source() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcustomshaderstage.html#source

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QOpenGLCustomShaderStage::source() const
    address = self.uglySide.call(
        'ritual_ZNK24QOpenGLCustomShaderStage6sourceEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QOpenGLShaderProgram)
  @overload(NoneType)
  def setUniforms(self, a0: Optional[QOpenGLShaderProgram]) -> None:
    """
    Calls Qt's 'void
    QOpenGLCustomShaderStage::setUniforms(QOpenGLShaderProgram *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcustomshaderstage.html#setUniforms

    Parameters
    ----------

    a0 : Optional[QOpenGLShaderProgram]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGLCustomShaderStage::setUniforms(QOpenGLShaderProgram *a0)
    ritual = (
        'ritual_ZN24QOpenGLCustomShaderStage11setUniformsEP20QOpenGLShaderP'
        'rogram')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QOpenGLCustomShaderStage11setUniformsEP20QOpenGLS'
          'haderProgram')
    self.uglySide.call(ritual, self._addressOf(a0))

  def setUniformsDirty(self) -> None:
    """
    Calls Qt's 'void QOpenGLCustomShaderStage::setUniformsDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcustomshaderstage.html#setUniformsDirty
    """
    #  void QOpenGLCustomShaderStage::setUniformsDirty()
    self.uglySide.call(
        'ritual_ZN24QOpenGLCustomShaderStage16setUniformsDirtyEv',
    )

  @overload(QPainter)
  @overload(NoneType)
  def setOnPainter(self, a0: Optional[QPainter]) -> bool:
    """
    Calls Qt's 'bool QOpenGLCustomShaderStage::setOnPainter(QPainter *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcustomshaderstage.html#setOnPainter

    Parameters
    ----------

    a0 : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QOpenGLCustomShaderStage::setOnPainter(QPainter *a0)
    return self.uglySide.call(
        'ritual_ZN24QOpenGLCustomShaderStage12setOnPainterEP8QPainter',
        self._addressOf(a0),
    )

  def setInactive(self) -> None:
    """
    Calls Qt's 'void QOpenGLCustomShaderStage::setInactive()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcustomshaderstage.html#setInactive
    """
    #  void QOpenGLCustomShaderStage::setInactive()
    self.uglySide.call('ritual_ZN24QOpenGLCustomShaderStage11setInactiveEv')

  @overload(QByteArray)
  def setSource(self, a0: QByteArray) -> None:
    """
    Calls Qt's 'void QOpenGLCustomShaderStage::setSource(const QByteArray
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcustomshaderstage.html#setSource

    Parameters
    ----------

    a0 : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QOpenGLCustomShaderStage::setSource(const QByteArray &a0)
    self.uglySide.call(
        'ritual_ZN24QOpenGLCustomShaderStage9setSourceERK10QByteArray',
        self._valueOf(a0),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLCustomShaderStage::QOpenGLCustomShaderStage()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcustomshaderstage.html
    """
    #  QOpenGLCustomShaderStage::QOpenGLCustomShaderStage()
    self._noteCreation(QOpenGLCustomShaderStage, lambda: Rituals.call(
        'ritual_ZN24QOpenGLCustomShaderStageC1Ev',
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

  @overload(QPainter)
  @overload(NoneType)
  def removeFromPainter(self, a0: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void QOpenGLCustomShaderStage::removeFromPainter(QPainter
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcustomshaderstage.html#removeFromPainter

    Parameters
    ----------

    a0 : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGLCustomShaderStage::removeFromPainter(QPainter *a0)
    self.uglySide.call(
        'ritual_ZN24QOpenGLCustomShaderStage17removeFromPainterEP8QPainter',
        self._addressOf(a0),
    )

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QOpenGLCustomShaderStagePrivate
      *QOpenGLCustomShaderStage::d_func()': gives
      'QOpenGLCustomShaderStagePrivate', which has no cute class yet.
    - Qt's 'const QOpenGLCustomShaderStagePrivate
      *QOpenGLCustomShaderStage::d_func() const': gives
      'QOpenGLCustomShaderStagePrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLCustomShaderStage.d_func' has no cute function yet. Qt's "
        "'QOpenGLCustomShaderStagePrivate "
        "*QOpenGLCustomShaderStage::d_func()': gives "
        "'QOpenGLCustomShaderStagePrivate', which has no cute class yet. "
        "Qt's 'const QOpenGLCustomShaderStagePrivate "
        "*QOpenGLCustomShaderStage::d_func() const': gives "
        "'QOpenGLCustomShaderStagePrivate', which has no cute class yet.")
