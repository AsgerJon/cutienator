"""
QSvgGradientPaint binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgpaintserver_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSvgGradientPaint to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QSvgPaintServer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QGradient, QTransform
  from . import QSvgDocument
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSvgDocument = WAIT['QSvgDocument']
  QTransform = WAIT['QTransform']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSvgGradientPaint(QSvgPaintServer):
  """
  The cute side of Qt's QSvgGradientPaint: a plain Python object standing in
  front of one C++ QSvgGradientPaint.

  It is built on the cute 'QSvgPaintServer', as Qt's QSvgGradientPaint is
  built on Qt's QSvgPaintServer, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgGradientPaint that has a ritual and that Python
  can call so far, 9 names in all: 'type', 'setStopLink', 'stopLink',
  'setTransform', 'qtransform', 'qgradient', 'gradientStopsSet',
  'setGradientStopsSet', 'resolveStops'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgGradientPaint::~QSvgGradientPaint()': the destructor: Python
    never removes a C++ QSvgGradientPaint.
  - Qt's 'QBrush QSvgGradientPaint::brush(QPainter *a0, const QSvgNode *a1,
    QSvgExtraStates &a2)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSvgGradientPaint::resolveStops_helper(QSet<QString>
    &visited)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 13 functions Qt declares: 1 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ QSvgGradientPaint is created at the first use, not by
    'QSvgGradientPaint(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgGradientPaint.
  - Each name of Qt's QSvgGradientPaint that has no cute function yet,
    '__init__', 'resolveStops_helper', holds a function that raises
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
  __qt_class__ = 'QSvgGradientPaint'

  #  A C++ QSvgGradientPaint Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgGradientPaint'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QSvgPaintServer.Type:
    """
    Calls Qt's 'Type QSvgGradientPaint::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvggradientpaint.html#type

    Returns
    -------

    QSvgPaintServer.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSvgPaintServer.Type(number)' gives.
    """
    #  Type QSvgGradientPaint::type() const
    ritual = 'ritual_ZNK17QSvgGradientPaint4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QSvgGradientPaint4typeEv'
    return QSvgPaintServer.Type(self.uglySide.call(ritual))

  def stopLink(self) -> str:
    """
    Calls Qt's 'QString QSvgGradientPaint::stopLink() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvggradientpaint.html#stopLink

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSvgGradientPaint::stopLink() const
    return self.uglySide.call('ritual_ZNK17QSvgGradientPaint8stopLinkEv')

  def qtransform(self) -> QTransform:
    """
    Calls Qt's 'QTransform QSvgGradientPaint::qtransform() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvggradientpaint.html#qtransform

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QSvgGradientPaint::qtransform() const
    address = self.uglySide.call(
        'ritual_ZNK17QSvgGradientPaint10qtransformEv',
    )
    from ..QtGui import QTransform
    return QTransform._cuteOwning(address)

  def gradientStopsSet(self) -> bool:
    """
    Calls Qt's 'bool QSvgGradientPaint::gradientStopsSet() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvggradientpaint.html#gradientStopsSet
    """
    #  bool QSvgGradientPaint::gradientStopsSet() const
    return self.uglySide.call(
        'ritual_ZNK17QSvgGradientPaint16gradientStopsSetEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, QSvgDocument)
  @overload(str, NoneType)
  def setStopLink(self, link: str, doc: Optional[QSvgDocument]) -> None:
    """
    Calls Qt's 'void QSvgGradientPaint::setStopLink(const QString &link,
    QSvgDocument *doc)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvggradientpaint.html#setStopLink

    Parameters
    ----------

    link : str
      Passed on as it is: a QString is made of it for the call.

    doc : Optional[QSvgDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgGradientPaint::setStopLink(const QString &link, QSvgDocument
    #      *doc)
    self.uglySide.call(
        'ritual_ZN17QSvgGradientPaint11setStopLinkERK7QStringP12QSvgDocumen'
        't',
        link, self._addressOf(doc),
    )

  @overload(QTransform)
  def setTransform(self, transform: QTransform) -> None:
    """
    Calls Qt's 'void QSvgGradientPaint::setTransform(const QTransform
    &transform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvggradientpaint.html#setTransform

    Parameters
    ----------

    transform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  void QSvgGradientPaint::setTransform(const QTransform &transform)
    self.uglySide.call(
        'ritual_ZN17QSvgGradientPaint12setTransformERK10QTransform',
        self._valueOf(transform),
    )

  @overload(bool)
  def setGradientStopsSet(self, set: bool) -> None:
    """
    Calls Qt's 'void QSvgGradientPaint::setGradientStopsSet(bool set)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvggradientpaint.html#setGradientStopsSet

    Parameters
    ----------

    set : bool
      Passed on as it is.
    """
    #  void QSvgGradientPaint::setGradientStopsSet(bool set)
    self.uglySide.call(
        'ritual_ZN17QSvgGradientPaint19setGradientStopsSetEb', set,
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
    Qt's 'QSvgGradientPaint::QSvgGradientPaint(std::unique_ptr<QGradient>
    grad)': the compiler refuses its ritual as it would be written here: call
    to deleted constructor of 'std::unique_ptr<QGradient>'.
    """
    raise NotImplementedError(
        "'QSvgGradientPaint.__init__' has no cute function yet. Qt's "
        "'QSvgGradientPaint::QSvgGradientPaint(std::unique_ptr<QGradient> "
        "grad)': the compiler refuses its ritual as it would be written "
        "here: call to deleted constructor of 'std::unique_ptr<QGradient>'.")

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

  def qgradient(self) -> Optional[QGradient]:
    """
    Calls Qt's 'QGradient *QSvgGradientPaint::qgradient()'.

    Qt's own words: https://doc.qt.io/qt-6/qsvggradientpaint.html#qgradient

    Returns
    -------

    Optional[QGradient]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGradient *QSvgGradientPaint::qgradient()
    address = self.uglySide.call('ritual_ZN17QSvgGradientPaint9qgradientEv')
    from ..QtGui import QGradient
    return QGradient._cuteAt(address)

  def resolveStops(self) -> None:
    """
    Calls Qt's 'void QSvgGradientPaint::resolveStops()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvggradientpaint.html#resolveStops
    """
    #  void QSvgGradientPaint::resolveStops()
    self.uglySide.call('ritual_ZN17QSvgGradientPaint12resolveStopsEv')

  @staticmethod
  def resolveStops_helper(*__, **_) -> Never:
    """
    Qt's 'void QSvgGradientPaint::resolveStops_helper(QSet<QString>
    &visited)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgGradientPaint.resolveStops_helper' has no cute function yet. "
        "Qt's 'void QSvgGradientPaint::resolveStops_helper(QSet<QString> "
        "&visited)': takes a type Python has no way to hand over yet.")
