"""
Q3DObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/q3dobject.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QVector3D
  from . import Q3DScene
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Q3DObject(QObject):
  """
  The cute side of Qt's Q3DObject: a plain Python object standing in front of
  one C++ Q3DObject.

  It is built on the cute 'QObject', as Qt's Q3DObject is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Q3DObject that has a ritual and that Python can call
  so far, 8 names in all: 'metaObject', 'tr', 'parentScene', 'position',
  'setPosition', 'positionChanged', 'setDirty', 'isDirty'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Q3DObject::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int Q3DObject::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'Q3DObject::~Q3DObject()': the destructor: Python never removes a
    C++ Q3DObject.
  - Qt's 'void Q3DObject::copyValuesFrom(const Q3DObject &source)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 17 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ Q3DObject is created at the first use, not by 'Q3DObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Q3DObject.
  - Qt tells when it has removed the C++ Q3DObject. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's Q3DObject that has no cute function yet,
    'copyValuesFrom', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString Q3DObject::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dobject.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Q3DObject::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9Q3DObject2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Q3DObject'

  #  A C++ Q3DObject Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Q3DObject'

  #  The functions Qt calls itself that Q3DObject is the first to declare and
  #  that cannot be handed to Python yet, each as Qt declares it. A class of
  #  a program that writes one of them anew is refused, since Qt would never
  #  call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'copyValuesFrom': (
          'void Q3DObject::copyValuesFrom(const Q3DObject &)',
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Q3DObject::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dobject.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Q3DObject::metaObject() const
    address = self.uglySide.call('ritual_ZNK9Q3DObject10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def position(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Q3DObject::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dobject.html#position

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Q3DObject::position() const
    address = self.uglySide.call('ritual_ZNK9Q3DObject8positionEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def isDirty(self) -> bool:
    """
    Calls Qt's 'bool Q3DObject::isDirty() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dobject.html#isDirty
    """
    #  bool Q3DObject::isDirty() const
    return self.uglySide.call('ritual_ZNK9Q3DObject7isDirtyEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector3D)
  def setPosition(self, position: QVector3D) -> None:
    """
    Calls Qt's 'void Q3DObject::setPosition(const QVector3D &position)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dobject.html#setPosition

    Parameters
    ----------

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Q3DObject::setPosition(const QVector3D &position)
    self.uglySide.call(
        'ritual_ZN9Q3DObject11setPositionERK9QVector3D',
        self._valueOf(position),
    )

  @overload(bool)
  def setDirty(self, dirty: bool) -> None:
    """
    Calls Qt's 'void Q3DObject::setDirty(bool dirty)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dobject.html#setDirty

    Parameters
    ----------

    dirty : bool
      Passed on as it is.
    """
    #  void Q3DObject::setDirty(bool dirty)
    self.uglySide.call('ritual_ZN9Q3DObject8setDirtyEb', dirty)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'Q3DObject::Q3DObject(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/q3dobject.html#Q3DObject

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Q3DObject::Q3DObject(QObject *parent)
    self._noteCreation(Q3DObject, lambda: Rituals.call(
        'ritual_ZN9Q3DObjectC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def parentScene(self) -> Optional[Q3DScene]:
    """
    Calls Qt's 'Q3DScene *Q3DObject::parentScene()'.

    Qt's own words: https://doc.qt.io/qt-6/q3dobject.html#parentScene

    Returns
    -------

    Optional[Q3DScene]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Q3DScene *Q3DObject::parentScene()
    address = self.uglySide.call('ritual_ZN9Q3DObject11parentSceneEv')
    from . import Q3DScene
    return Q3DScene._cuteAt(address)

  @overload(QVector3D)
  def positionChanged(self, position: QVector3D) -> None:
    """
    Calls Qt's 'void Q3DObject::positionChanged(const QVector3D &position)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dobject.html#positionChanged

    Parameters
    ----------

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Q3DObject::positionChanged(const QVector3D &position)
    self.uglySide.call(
        'ritual_ZN9Q3DObject15positionChangedERK9QVector3D',
        self._valueOf(position),
    )

  @staticmethod
  def copyValuesFrom(*__, **_) -> Never:
    """
    Qt's 'void Q3DObject::copyValuesFrom(const Q3DObject &source)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Q3DObject.copyValuesFrom' has no cute function yet. Qt's 'void "
        "Q3DObject::copyValuesFrom(const Q3DObject &source)': takes a type "
        "Python has no way to hand over yet.")
