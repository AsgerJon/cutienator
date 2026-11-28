"""
QSvgAbstractAnimatedProperty binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvganimatedproperty_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSvgAbstractAnimatedProperty to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QVariant
  from . import QSvgEasingInterface


class QSvgAbstractAnimatedProperty(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSvgAbstractAnimatedProperty: a plain Python object
  standing in front of one C++ QSvgAbstractAnimatedProperty.

  What exists
  -----------

  Every function of Qt's QSvgAbstractAnimatedProperty that has a ritual and
  that Python can call so far, 8 names in all: 'appendKeyFrame', 'easingAt',
  'setPropertyName', 'propertyName', 'type', 'interpolatedValue',
  'interpolate', 'createAnimatedProperty'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgAbstractAnimatedProperty::~QSvgAbstractAnimatedProperty()': the
    destructor: Python never removes a C++ QSvgAbstractAnimatedProperty.
  - Qt's 'void QSvgAbstractAnimatedProperty::setKeyFrames(const QList<qreal>
    &keyFrames)': takes a type Python has no way to hand over yet.
  - Qt's 'QList<qreal> QSvgAbstractAnimatedProperty::keyFrames() const':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  5 of the 17 functions Qt declares: 4 forbidden; 1 the compiler refuses its
  ritual as it would be written here.

  What to expect
  --------------

  - The C++ QSvgAbstractAnimatedProperty is created at the first use, not by
    'QSvgAbstractAnimatedProperty(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgAbstractAnimatedProperty.
  - Each name of Qt's QSvgAbstractAnimatedProperty that has no cute function
    yet, 'appendEasing', 'keyFrames', 'setKeyFrames', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSvgAbstractAnimatedProperty, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Type(CuteNum):
    """
    The enum 'QSvgAbstractAnimatedProperty::Type' of Qt, with the 4 names Qt
    gives in it.
    """

    Int = Kee[int](0)
    Float = Kee[int](1)
    Color = Kee[int](2)
    Transform = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def createAnimatedProperty(
      name: str,
  ) -> Optional[QSvgAbstractAnimatedProperty]:
    """
    Calls Qt's 'QSvgAbstractAnimatedProperty
    *QSvgAbstractAnimatedProperty::createAnimatedProperty(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgabstractanimatedproperty.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QSvgAbstractAnimatedProperty]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSvgAbstractAnimatedProperty
    #      *QSvgAbstractAnimatedProperty::createAnimatedProperty(const
    #      QString &name)
    address = Rituals.call(
        'ritual_ZN28QSvgAbstractAnimatedProperty22createAnimatedPropertyERK'
        '7QString',
        name,
    )
    return QSvgAbstractAnimatedProperty._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgAbstractAnimatedProperty'

  #  A C++ QSvgAbstractAnimatedProperty Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgAbstractAnimatedProperty'

  #  The functions Qt calls itself that QSvgAbstractAnimatedProperty is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'interpolate': (
          ('_ZNK28QSvgAbstractAnimatedProperty11interpolateEjd',
           ('nothing', 'nothing', ''),
           (
               ('unsigned int', 'number', ''),
               ('double', 'number', ''),
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

  @overload(int)
  def easingAt(self, i: int) -> Optional[QSvgEasingInterface]:
    """
    Calls Qt's 'const QSvgEasingInterface
    *QSvgAbstractAnimatedProperty::easingAt(unsigned int i) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgabstractanimatedproperty.html#easingAt

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    Optional[QSvgEasingInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QSvgEasingInterface
    #      *QSvgAbstractAnimatedProperty::easingAt(unsigned int i) const
    address = self.uglySide.call(
        'ritual_ZNK28QSvgAbstractAnimatedProperty8easingAtEj', i,
    )
    from . import QSvgEasingInterface
    return QSvgEasingInterface._cuteAt(address)

  def propertyName(self) -> str:
    """
    Calls Qt's 'QStringView QSvgAbstractAnimatedProperty::propertyName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgabstractanimatedproperty.html#propertyName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QSvgAbstractAnimatedProperty::propertyName() const
    return self.uglySide.call(
        'ritual_ZNK28QSvgAbstractAnimatedProperty12propertyNameEv',
    )

  def type(self) -> Type:
    """
    Calls Qt's 'Type QSvgAbstractAnimatedProperty::type() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgabstractanimatedproperty.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QSvgAbstractAnimatedProperty::type() const
    return QSvgAbstractAnimatedProperty.Type(self.uglySide.call(
        'ritual_ZNK28QSvgAbstractAnimatedProperty4typeEv',
    ))

  def interpolatedValue(self) -> QVariant:
    """
    Calls Qt's 'QVariant QSvgAbstractAnimatedProperty::interpolatedValue()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgabstractanimatedproperty.html

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QSvgAbstractAnimatedProperty::interpolatedValue() const
    address = self.uglySide.call(
        'ritual_ZNK28QSvgAbstractAnimatedProperty17interpolatedValueEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setPropertyName(self, name: str) -> None:
    """
    Calls Qt's 'void QSvgAbstractAnimatedProperty::setPropertyName(const
    QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgabstractanimatedproperty.html#setPropertyName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSvgAbstractAnimatedProperty::setPropertyName(const QString
    #      &name)
    self.uglySide.call(
        'ritual_ZN28QSvgAbstractAnimatedProperty15setPropertyNameERK7QStrin'
        'g',
        name,
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

  @overload(str, Type)
  def __init__(self, name: str, type: Type) -> None:
    """
    Notes what was given, for Qt's
    'QSvgAbstractAnimatedProperty::QSvgAbstractAnimatedProperty(const QString
    &name, Type type)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgabstractanimatedproperty.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    type : Type
      Passed on as its number.
    """
    #  QSvgAbstractAnimatedProperty::QSvgAbstractAnimatedProperty(const
    #      QString &name, Type type)
    self._noteCreation(QSvgAbstractAnimatedProperty, lambda: Rituals.call(
        'ritual_ZN28QSvgAbstractAnimatedPropertyC1ERK7QStringNS_4TypeE',
        name, type.value,
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

  @overload(float)
  def appendKeyFrame(self, keyFrame: float) -> None:
    """
    Calls Qt's 'void QSvgAbstractAnimatedProperty::appendKeyFrame(qreal
    keyFrame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgabstractanimatedproperty.html#appendKeyFrame

    Parameters
    ----------

    keyFrame : float
      Passed on as it is.
    """
    #  void QSvgAbstractAnimatedProperty::appendKeyFrame(qreal keyFrame)
    self.uglySide.call(
        'ritual_ZN28QSvgAbstractAnimatedProperty14appendKeyFrameEd',
        keyFrame,
    )

  @overload(int, float)
  def interpolate(self, index: int, t: float) -> None:
    """
    Calls Qt's 'void QSvgAbstractAnimatedProperty::interpolate(uint index,
    qreal t) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgabstractanimatedproperty.html#interpolate

    Parameters
    ----------

    index : int
      Passed on as it is.

    t : float
      Passed on as it is.
    """
    #  void QSvgAbstractAnimatedProperty::interpolate(uint index, qreal t)
    #      const
    self.uglySide.call(
        'ritual_ZNK28QSvgAbstractAnimatedProperty11interpolateEjd', index, t,
    )

  @staticmethod
  def appendEasing(*__, **_) -> Never:
    """
    Qt's 'void
    QSvgAbstractAnimatedProperty::appendEasing(QSvgEasingInterfacePtr
    easing)': the compiler refuses its ritual as it would be written here:
    call to deleted constructor of 'QSvgEasingInterfacePtr' (aka
    'std::unique_ptr<QSvgEasingInterface>').
    """
    raise NotImplementedError(
        "'QSvgAbstractAnimatedProperty.appendEasing' has no cute function "
        "yet. Qt's 'void "
        "QSvgAbstractAnimatedProperty::appendEasing(QSvgEasingInterfacePtr "
        "easing)': the compiler refuses its ritual as it would be written "
        "here: call to deleted constructor of 'QSvgEasingInterfacePtr' (aka "
        "'std::unique_ptr<QSvgEasingInterface>').")

  @staticmethod
  def keyFrames(*__, **_) -> Never:
    """
    Qt's 'QList<qreal> QSvgAbstractAnimatedProperty::keyFrames() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSvgAbstractAnimatedProperty.keyFrames' has no cute function yet. "
        "Qt's 'QList<qreal> QSvgAbstractAnimatedProperty::keyFrames() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def setKeyFrames(*__, **_) -> Never:
    """
    Qt's 'void QSvgAbstractAnimatedProperty::setKeyFrames(const QList<qreal>
    &keyFrames)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgAbstractAnimatedProperty.setKeyFrames' has no cute function "
        "yet. Qt's 'void QSvgAbstractAnimatedProperty::setKeyFrames(const "
        "QList<qreal> &keyFrames)': takes a type Python has no way to hand "
        "over yet.")


#  Qt's 'QList<QSvgAbstractAnimatedProperty *>': the list of
#  QSvgAbstractAnimatedProperty, which 'QList[QSvgAbstractAnimatedProperty]'
#  gives. It is made here, so that there is one as soon as there can be a
#  QSvgAbstractAnimatedProperty.
QList.createKind(
    QSvgAbstractAnimatedProperty, 'address',
    make='ritual_list_make_QSvgAbstractAnimatedProperty_ptr',
    add='ritual_list_add_QSvgAbstractAnimatedProperty_ptr',
    size='ritual_list_size_QSvgAbstractAnimatedProperty_ptr',
    at='ritual_list_at_QSvgAbstractAnimatedProperty_ptr',
    drop='ritual_list_drop_QSvgAbstractAnimatedProperty_ptr',
)
