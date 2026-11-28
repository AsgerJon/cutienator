"""
QSvgAnimatedPropertyTransform binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvganimatedproperty_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSvgAnimatedPropertyTransform to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals
from . import QSvgAbstractAnimatedProperty

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSvgAnimatedPropertyTransform(QSvgAbstractAnimatedProperty):
  """
  The cute side of Qt's QSvgAnimatedPropertyTransform: a plain Python object
  standing in front of one C++ QSvgAnimatedPropertyTransform.

  It is built on the cute 'QSvgAbstractAnimatedProperty', as Qt's
  QSvgAnimatedPropertyTransform is built on Qt's
  QSvgAbstractAnimatedProperty, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgAnimatedPropertyTransform that has a ritual and
  that Python can call so far, 3 names in all: 'setTransformCount',
  'transformCount', 'interpolate'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgAnimatedPropertyTransform::~QSvgAnimatedPropertyTransform()':
    the destructor: Python never removes a C++ QSvgAnimatedPropertyTransform.
  - Qt's 'void QSvgAnimatedPropertyTransform::appendComponents(const
    QList<TransformComponent> &components)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QList<TransformComponent>
    QSvgAnimatedPropertyTransform::components() const': gives a type Python
    has no way to take yet.

  What to expect
  --------------

  - The C++ QSvgAnimatedPropertyTransform is created at the first use, not by
    'QSvgAnimatedPropertyTransform(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgAnimatedPropertyTransform.
  - Each name of Qt's QSvgAnimatedPropertyTransform that has no cute function
    yet, 'appendComponents', 'components', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QSvgAnimatedPropertyTransform, each a class
  #  in here as in C++.

  class TransformComponent(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSvgAnimatedPropertyTransform::TransformComponent:
    a plain Python object standing in front of one C++
    QSvgAnimatedPropertyTransform::TransformComponent.

    C++ hands a QSvgAnimatedPropertyTransform::TransformComponent around as a
    copy, so every C++ QSvgAnimatedPropertyTransform::TransformComponent
    behind a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QSvgAnimatedPropertyTransform::TransformComponent
    yet. None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSvgAnimatedPropertyTransform::TransformComponent::
      ~TransformComponent()': the destructor: Python removes its C++
      QSvgAnimatedPropertyTransform::TransformComponent by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QSvgAnimatedPropertyTransform::TransformComponent is created at
      the first use, not by
      'QSvgAnimatedPropertyTransform::TransformComponent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSvgAnimatedPropertyTransform::TransformComponent
      back gives a copy the ritual made for Python, in a new cute
      QSvgAnimatedPropertyTransform::TransformComponent.
    """

    #  The enums Qt writes inside
    #  QSvgAnimatedPropertyTransform::TransformComponent, each a class in
    #  here as in C++, and the names Qt has for the combinations of its flags
    #  enums.

    class Type(CuteNum):
      """
      The enum 'QSvgAnimatedPropertyTransform::TransformComponent::Type' of
      Qt, with the 5 names Qt gives in it.
      """

      Translate = Kee[int](0)
      Scale = Kee[int](1)
      Rotate = Kee[int](2)
      Skew = Kee[int](3)
      Matrix = Kee[int](4)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSvgAnimatedPropertyTransform::TransformComponent'

    #  Qt's '~QSvgAnimatedPropertyTransform::TransformComponent()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QSvgAnimatedPropertyTransform::TransformComponent behind a cute one,
    #  and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN29QSvgAnimatedPropertyTransform18TransformComponentD1Ev')

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgAnimatedPropertyTransform'

  #  A C++ QSvgAnimatedPropertyTransform Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgAnimatedPropertyTransform'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def transformCount(self) -> int:
    """
    Calls Qt's 'quint32 QSvgAnimatedPropertyTransform::transformCount()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvganimatedpropertytransform.html#transformCount
    """
    #  quint32 QSvgAnimatedPropertyTransform::transformCount() const
    return self.uglySide.call(
        'ritual_ZNK29QSvgAnimatedPropertyTransform14transformCountEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setTransformCount(self, count: int) -> None:
    """
    Calls Qt's 'void QSvgAnimatedPropertyTransform::setTransformCount(quint32
    count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvganimatedpropertytransform.html

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QSvgAnimatedPropertyTransform::setTransformCount(quint32 count)
    self.uglySide.call(
        'ritual_ZN29QSvgAnimatedPropertyTransform17setTransformCountEj',
        count,
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

  @overload(str)
  def __init__(self, name: str) -> None:
    """
    Notes what was given, for Qt's
    'QSvgAnimatedPropertyTransform::QSvgAnimatedPropertyTransform(const
    QString &name)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvganimatedpropertytransform.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QSvgAnimatedPropertyTransform::QSvgAnimatedPropertyTransform(const
    #      QString &name)
    self._noteCreation(QSvgAnimatedPropertyTransform, lambda: Rituals.call(
        'ritual_ZN29QSvgAnimatedPropertyTransformC1ERK7QString', name,
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

  @overload(int, float)
  def interpolate(self, index: int, t: float) -> None:
    """
    Calls Qt's 'void QSvgAnimatedPropertyTransform::interpolate(uint index,
    qreal t) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvganimatedpropertytransform.html#interpolate

    Parameters
    ----------

    index : int
      Passed on as it is.

    t : float
      Passed on as it is.
    """
    #  void QSvgAnimatedPropertyTransform::interpolate(uint index, qreal t)
    #      const
    ritual = 'ritual_ZNK29QSvgAnimatedPropertyTransform11interpolateEjd'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK29QSvgAnimatedPropertyTransform11interpolateEjd')
    self.uglySide.call(ritual, index, t)

  @staticmethod
  def appendComponents(*__, **_) -> Never:
    """
    Qt's 'void QSvgAnimatedPropertyTransform::appendComponents(const
    QList<TransformComponent> &components)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgAnimatedPropertyTransform.appendComponents' has no cute "
        "function yet. Qt's 'void "
        "QSvgAnimatedPropertyTransform::appendComponents(const "
        "QList<TransformComponent> &components)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def components(*__, **_) -> Never:
    """
    Qt's 'QList<TransformComponent>
    QSvgAnimatedPropertyTransform::components() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QSvgAnimatedPropertyTransform.components' has no cute function "
        "yet. Qt's 'QList<TransformComponent> "
        "QSvgAnimatedPropertyTransform::components() const': gives a type "
        "Python has no way to take yet.")
