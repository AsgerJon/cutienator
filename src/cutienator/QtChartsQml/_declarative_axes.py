"""
DeclarativeAxes binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtChartsQml/6.12.0/QtChartsQml/private/declarativeaxes_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means DeclarativeAxes to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtCharts import QAbstractAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractAxis = WAIT['QtCharts:QAbstractAxis']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DeclarativeAxes(QObject):
  """
  The cute side of Qt's DeclarativeAxes: a plain Python object standing in
  front of one C++ DeclarativeAxes.

  It is built on the cute 'QObject', as Qt's DeclarativeAxes is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's DeclarativeAxes that has a ritual and that Python
  can call so far, 18 names in all: 'metaObject', 'tr', 'axisX', 'setAxisX',
  'axisY', 'setAxisY', 'axisXTop', 'setAxisXTop', 'axisYRight',
  'setAxisYRight', 'emitAxisXChanged', 'emitAxisYChanged',
  'emitAxisXTopChanged', 'emitAxisYRightChanged', 'axisXChanged',
  'axisYChanged', 'axisXTopChanged', 'axisYRightChanged'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *DeclarativeAxes::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int DeclarativeAxes::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void DeclarativeAxes::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.

  What has no ritual
  ------------------

  2 of the 24 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ DeclarativeAxes is created at the first use, not by
    'DeclarativeAxes(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DeclarativeAxes.
  - Qt tells when it has removed the C++ DeclarativeAxes. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString DeclarativeAxes::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativeaxes.html#tr

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
    #  QString DeclarativeAxes::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15DeclarativeAxes2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DeclarativeAxes'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *DeclarativeAxes::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/declarativeaxes.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *DeclarativeAxes::metaObject() const
    address = self.uglySide.call('ritual_ZNK15DeclarativeAxes10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisX(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeAxes::setAxisX(QAbstractAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativeaxes.html#setAxisX

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeAxes::setAxisX(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN15DeclarativeAxes8setAxisXEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisY(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeAxes::setAxisY(QAbstractAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativeaxes.html#setAxisY

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeAxes::setAxisY(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN15DeclarativeAxes8setAxisYEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisXTop(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeAxes::setAxisXTop(QAbstractAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativeaxes.html#setAxisXTop

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeAxes::setAxisXTop(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN15DeclarativeAxes11setAxisXTopEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def setAxisYRight(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeAxes::setAxisYRight(QAbstractAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativeaxes.html#setAxisYRight

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeAxes::setAxisYRight(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN15DeclarativeAxes13setAxisYRightEP13QAbstractAxis',
        self._addressOf(axis),
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
    Notes what was given, for Qt's 'DeclarativeAxes::DeclarativeAxes(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeaxes.html#DeclarativeAxes

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  DeclarativeAxes::DeclarativeAxes(QObject *parent)
    self._noteCreation(DeclarativeAxes, lambda: Rituals.call(
        'ritual_ZN15DeclarativeAxesC1EP7QObject',
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

  def axisX(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeAxes::axisX()'.

    Qt's own words: https://doc.qt.io/qt-6/declarativeaxes.html#axisX

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeAxes::axisX()
    address = self.uglySide.call('ritual_ZN15DeclarativeAxes5axisXEv')
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisY(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeAxes::axisY()'.

    Qt's own words: https://doc.qt.io/qt-6/declarativeaxes.html#axisY

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeAxes::axisY()
    address = self.uglySide.call('ritual_ZN15DeclarativeAxes5axisYEv')
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisXTop(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeAxes::axisXTop()'.

    Qt's own words: https://doc.qt.io/qt-6/declarativeaxes.html#axisXTop

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeAxes::axisXTop()
    address = self.uglySide.call('ritual_ZN15DeclarativeAxes8axisXTopEv')
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def axisYRight(self) -> Optional[QAbstractAxis]:
    """
    Calls Qt's 'QAbstractAxis *DeclarativeAxes::axisYRight()'.

    Qt's own words: https://doc.qt.io/qt-6/declarativeaxes.html#axisYRight

    Returns
    -------

    Optional[QAbstractAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAxis *DeclarativeAxes::axisYRight()
    address = self.uglySide.call('ritual_ZN15DeclarativeAxes10axisYRightEv')
    from ..QtCharts import QAbstractAxis
    return QAbstractAxis._cuteAt(address)

  def emitAxisXChanged(self) -> None:
    """
    Calls Qt's 'void DeclarativeAxes::emitAxisXChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeaxes.html#emitAxisXChanged
    """
    #  void DeclarativeAxes::emitAxisXChanged()
    self.uglySide.call('ritual_ZN15DeclarativeAxes16emitAxisXChangedEv')

  def emitAxisYChanged(self) -> None:
    """
    Calls Qt's 'void DeclarativeAxes::emitAxisYChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeaxes.html#emitAxisYChanged
    """
    #  void DeclarativeAxes::emitAxisYChanged()
    self.uglySide.call('ritual_ZN15DeclarativeAxes16emitAxisYChangedEv')

  def emitAxisXTopChanged(self) -> None:
    """
    Calls Qt's 'void DeclarativeAxes::emitAxisXTopChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeaxes.html#emitAxisXTopChanged
    """
    #  void DeclarativeAxes::emitAxisXTopChanged()
    self.uglySide.call('ritual_ZN15DeclarativeAxes19emitAxisXTopChangedEv')

  def emitAxisYRightChanged(self) -> None:
    """
    Calls Qt's 'void DeclarativeAxes::emitAxisYRightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeaxes.html#emitAxisYRightChanged
    """
    #  void DeclarativeAxes::emitAxisYRightChanged()
    self.uglySide.call('ritual_ZN15DeclarativeAxes21emitAxisYRightChangedEv')

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisXChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeAxes::axisXChanged(QAbstractAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativeaxes.html#axisXChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeAxes::axisXChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN15DeclarativeAxes12axisXChangedEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisYChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeAxes::axisYChanged(QAbstractAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativeaxes.html#axisYChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeAxes::axisYChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN15DeclarativeAxes12axisYChangedEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisXTopChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeAxes::axisXTopChanged(QAbstractAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeaxes.html#axisXTopChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeAxes::axisXTopChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN15DeclarativeAxes15axisXTopChangedEP13QAbstractAxis',
        self._addressOf(axis),
    )

  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisYRightChanged(self, axis: Optional[QAbstractAxis]) -> None:
    """
    Calls Qt's 'void DeclarativeAxes::axisYRightChanged(QAbstractAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeaxes.html#axisYRightChanged

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeAxes::axisYRightChanged(QAbstractAxis *axis)
    self.uglySide.call(
        'ritual_ZN15DeclarativeAxes17axisYRightChangedEP13QAbstractAxis',
        self._addressOf(axis),
    )
