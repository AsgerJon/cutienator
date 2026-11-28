"""
QQuickGradient binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickrectangle_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickGradient to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickGradient(QObject):
  """
  The cute side of Qt's QQuickGradient: a plain Python object standing in
  front of one C++ QQuickGradient.

  It is built on the cute 'QObject', as Qt's QQuickGradient is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickGradient that has a ritual and that Python can
  call so far, 8 names in all: 'metaObject', 'tr', 'qmlExtendedNamespace',
  'orientation', 'setOrientation', 'updated', 'orientationChanged',
  'doUpdate'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickGradient::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickGradient::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickGradient::qt_qmlMarker_extendedNamespace()': one of Qt's
    own inner workings.
  - Qt's 'QQuickGradient::~QQuickGradient()': the destructor: Python never
    removes a C++ QQuickGradient.
  - Qt's 'QQmlListProperty<QQuickGradientStop> QQuickGradient::stops()':
    gives a type Python has no way to take yet.
  - Qt's 'QGradientStops QQuickGradient::gradientStops() const': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickGradient is created at the first use, not by
    'QQuickGradient(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickGradient.
  - Qt tells when it has removed the C++ QQuickGradient. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickGradient that has no cute function yet,
    'gradientStops', 'stops', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickGradient, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Orientation(CuteNum):
    """
    The enum 'QQuickGradient::Orientation' of Qt, with the 2 names Qt gives
    in it.
    """

    Vertical = Kee[int](2)
    Horizontal = Kee[int](1)

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
    Calls Qt's 'QString QQuickGradient::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgradient.html#tr

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
    #  QString QQuickGradient::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuickGradient2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def qmlExtendedNamespace() -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickGradient::qmlExtendedNamespace()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgradient.html#qmlExtendedNamespace

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickGradient::qmlExtendedNamespace()
    address = Rituals.call(
        'ritual_ZN14QQuickGradient20qmlExtendedNamespaceEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickGradient'

  #  A C++ QQuickGradient Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickGradient'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickGradient::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgradient.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickGradient::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuickGradient10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def orientation(self) -> Orientation:
    """
    Calls Qt's 'Orientation QQuickGradient::orientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgradient.html#orientation

    Returns
    -------

    Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Orientation(number)'
      gives.
    """
    #  Orientation QQuickGradient::orientation() const
    return QQuickGradient.Orientation(self.uglySide.call(
        'ritual_ZNK14QQuickGradient11orientationEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Orientation)
  def setOrientation(self, orientation: Orientation) -> None:
    """
    Calls Qt's 'void QQuickGradient::setOrientation(Orientation
    orientation)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgradient.html#setOrientation

    Parameters
    ----------

    orientation : Orientation
      Passed on as its number.
    """
    #  void QQuickGradient::setOrientation(Orientation orientation)
    self.uglySide.call(
        'ritual_ZN14QQuickGradient14setOrientationENS_11OrientationE',
        orientation.value,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickGradient::QQuickGradient(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickgradient.html#QQuickGradient

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickGradient::QQuickGradient(QObject *parent)
    self._noteCreation(QQuickGradient, lambda: Rituals.call(
        'ritual_ZN14QQuickGradientC1EP7QObject',
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

  def updated(self) -> None:
    """
    Calls Qt's 'void QQuickGradient::updated()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgradient.html#updated
    """
    #  void QQuickGradient::updated()
    self.uglySide.call('ritual_ZN14QQuickGradient7updatedEv')

  def orientationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGradient::orientationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgradient.html#orientationChanged
    """
    #  void QQuickGradient::orientationChanged()
    self.uglySide.call('ritual_ZN14QQuickGradient18orientationChangedEv')

  def doUpdate(self) -> None:
    """
    Calls Qt's 'void QQuickGradient::doUpdate()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgradient.html#doUpdate
    """
    #  void QQuickGradient::doUpdate()
    self.uglySide.call('ritual_ZN14QQuickGradient8doUpdateEv')

  @staticmethod
  def gradientStops(*__, **_) -> Never:
    """
    Qt's 'QGradientStops QQuickGradient::gradientStops() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickGradient.gradientStops' has no cute function yet. Qt's "
        "'QGradientStops QQuickGradient::gradientStops() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def stops(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickGradientStop> QQuickGradient::stops()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickGradient.stops' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuickGradientStop> QQuickGradient::stops()': "
        "gives a type Python has no way to take yet.")


#  Qt's 'QList<QQuickGradient *>': the list of QQuickGradient, which
#  'QList[QQuickGradient]' gives. It is made here, so that there is one as
#  soon as there can be a QQuickGradient.
QList.createKind(
    QQuickGradient, 'address',
    make='ritual_list_make_QQuickGradient_ptr',
    add='ritual_list_add_QQuickGradient_ptr',
    size='ritual_list_size_QQuickGradient_ptr',
    at='ritual_list_at_QQuickGradient_ptr',
    drop='ritual_list_drop_QQuickGradient_ptr',
)
