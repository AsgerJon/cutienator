"""
ExtrudedTextGeometry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/extrudedtextgeometry_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means ExtrudedTextGeometry to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QFont
  from ..QtQuick3D import QQuick3DObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFont = WAIT['QFont']
  QQuick3DObject = WAIT['QQuick3DObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ExtrudedTextGeometry(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's ExtrudedTextGeometry: a plain Python object standing
  in front of one C++ ExtrudedTextGeometry.

  What exists
  -----------

  Every function of Qt's ExtrudedTextGeometry that has a ritual and that
  Python can call so far, 22 names in all: 'metaObject', 'tr', 'text',
  'setText', 'font', 'setFont', 'depth', 'setDepth', 'scale', 'setScale',
  'asynchronous', 'setAsynchronous', 'status', 'doUpdateGeometry',
  'requestFinished', 'textChanged', 'fontChanged', 'depthChanged',
  'scaleChanged', 'asynchronousChanged', 'statusChanged',
  'scheduleGeometryUpdate'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *ExtrudedTextGeometry::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int ExtrudedTextGeometry::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'ExtrudedTextGeometry::~ExtrudedTextGeometry()': the destructor:
    Python never removes a C++ ExtrudedTextGeometry.
  - Qt's 'void ExtrudedTextGeometry::updateGeometry(const GeometryData
    &geometryData)': takes a type Python has no way to hand over yet.
  - Qt's 'ExtrudedTextGeometry::GeometryData
    ExtrudedTextGeometry::generateExtrudedTextGeometry(const QString &text,
    const QFont &font, float depth, float scale)': gives a type Python has no
    way to take yet.
  - Qt's 'void ExtrudedTextGeometry::generateExtrudedTextGeometryAsync(
    QPromise<ExtrudedTextGeometry::GeometryData> &promise, const QString
    &text, const QFont &font, float depth, float scale)': takes a type Python
    has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 31 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ ExtrudedTextGeometry is created at the first use, not by
    'ExtrudedTextGeometry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ ExtrudedTextGeometry.
  - Qt tells when it has removed the C++ ExtrudedTextGeometry. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's ExtrudedTextGeometry that has no cute function yet,
    'generateExtrudedTextGeometry', 'generateExtrudedTextGeometryAsync',
    'updateGeometry', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside ExtrudedTextGeometry, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Status(CuteNum):
    """
    The enum 'ExtrudedTextGeometry::Status' of Qt, with the 4 names Qt gives
    in it.
    """

    Null = Kee[int](0)
    Ready = Kee[int](1)
    Loading = Kee[int](2)
    Error = Kee[int](3)

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
    Calls Qt's 'QString ExtrudedTextGeometry::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/extrudedtextgeometry.html#tr

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
    #  QString ExtrudedTextGeometry::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20ExtrudedTextGeometry2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'ExtrudedTextGeometry'

  #  A C++ ExtrudedTextGeometry Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_ExtrudedTextGeometry'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *ExtrudedTextGeometry::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/extrudedtextgeometry.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *ExtrudedTextGeometry::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20ExtrudedTextGeometry10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def text(self) -> str:
    """
    Calls Qt's 'QString ExtrudedTextGeometry::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/extrudedtextgeometry.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString ExtrudedTextGeometry::text() const
    return self.uglySide.call('ritual_ZNK20ExtrudedTextGeometry4textEv')

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont ExtrudedTextGeometry::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/extrudedtextgeometry.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont ExtrudedTextGeometry::font() const
    address = self.uglySide.call('ritual_ZNK20ExtrudedTextGeometry4fontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def depth(self) -> float:
    """
    Calls Qt's 'float ExtrudedTextGeometry::depth() const'.

    Qt's own words: https://doc.qt.io/qt-6/extrudedtextgeometry.html#depth
    """
    #  float ExtrudedTextGeometry::depth() const
    return self.uglySide.call('ritual_ZNK20ExtrudedTextGeometry5depthEv')

  def scale(self) -> float:
    """
    Calls Qt's 'float ExtrudedTextGeometry::scale() const'.

    Qt's own words: https://doc.qt.io/qt-6/extrudedtextgeometry.html#scale
    """
    #  float ExtrudedTextGeometry::scale() const
    return self.uglySide.call('ritual_ZNK20ExtrudedTextGeometry5scaleEv')

  def asynchronous(self) -> bool:
    """
    Calls Qt's 'bool ExtrudedTextGeometry::asynchronous() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/extrudedtextgeometry.html#asynchronous
    """
    #  bool ExtrudedTextGeometry::asynchronous() const
    return self.uglySide.call(
        'ritual_ZNK20ExtrudedTextGeometry12asynchronousEv',
    )

  def status(self) -> Status:
    """
    Calls Qt's 'Status ExtrudedTextGeometry::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/extrudedtextgeometry.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status ExtrudedTextGeometry::status() const
    return ExtrudedTextGeometry.Status(self.uglySide.call(
        'ritual_ZNK20ExtrudedTextGeometry6statusEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setText(self, newText: str) -> None:
    """
    Calls Qt's 'void ExtrudedTextGeometry::setText(const QString &newText)'.

    Qt's own words: https://doc.qt.io/qt-6/extrudedtextgeometry.html#setText

    Parameters
    ----------

    newText : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void ExtrudedTextGeometry::setText(const QString &newText)
    self.uglySide.call(
        'ritual_ZN20ExtrudedTextGeometry7setTextERK7QString', newText,
    )

  @overload(QFont)
  def setFont(self, newFont: QFont) -> None:
    """
    Calls Qt's 'void ExtrudedTextGeometry::setFont(const QFont &newFont)'.

    Qt's own words: https://doc.qt.io/qt-6/extrudedtextgeometry.html#setFont

    Parameters
    ----------

    newFont : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void ExtrudedTextGeometry::setFont(const QFont &newFont)
    self.uglySide.call(
        'ritual_ZN20ExtrudedTextGeometry7setFontERK5QFont',
        self._valueOf(newFont),
    )

  @overload(float)
  def setDepth(self, newDepth: float) -> None:
    """
    Calls Qt's 'void ExtrudedTextGeometry::setDepth(float newDepth)'.

    Qt's own words: https://doc.qt.io/qt-6/extrudedtextgeometry.html#setDepth

    Parameters
    ----------

    newDepth : float
      Passed on as it is.
    """
    #  void ExtrudedTextGeometry::setDepth(float newDepth)
    self.uglySide.call(
        'ritual_ZN20ExtrudedTextGeometry8setDepthEf', newDepth,
    )

  @overload(float)
  def setScale(self, newScale: float) -> None:
    """
    Calls Qt's 'void ExtrudedTextGeometry::setScale(float newScale)'.

    Qt's own words: https://doc.qt.io/qt-6/extrudedtextgeometry.html#setScale

    Parameters
    ----------

    newScale : float
      Passed on as it is.
    """
    #  void ExtrudedTextGeometry::setScale(float newScale)
    self.uglySide.call(
        'ritual_ZN20ExtrudedTextGeometry8setScaleEf', newScale,
    )

  @overload(bool)
  def setAsynchronous(self, newAsynchronous: bool) -> None:
    """
    Calls Qt's 'void ExtrudedTextGeometry::setAsynchronous(bool
    newAsynchronous)'.

    Qt's own words:
    https://doc.qt.io/qt-6/extrudedtextgeometry.html#setAsynchronous

    Parameters
    ----------

    newAsynchronous : bool
      Passed on as it is.
    """
    #  void ExtrudedTextGeometry::setAsynchronous(bool newAsynchronous)
    self.uglySide.call(
        'ritual_ZN20ExtrudedTextGeometry15setAsynchronousEb',
        newAsynchronous,
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
  @overload(QQuick3DObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'ExtrudedTextGeometry::ExtrudedTextGeometry(QQuick3DObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/extrudedtextgeometry.html#ExtrudedTextGeometry

    Parameters
    ----------

    parent : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  ExtrudedTextGeometry::ExtrudedTextGeometry(QQuick3DObject *parent)
    self._noteCreation(ExtrudedTextGeometry, lambda: Rituals.call(
        'ritual_ZN20ExtrudedTextGeometryC1EP14QQuick3DObject',
        self._addressOf(parent),
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

  def doUpdateGeometry(self) -> None:
    """
    Calls Qt's 'void ExtrudedTextGeometry::doUpdateGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/extrudedtextgeometry.html#doUpdateGeometry
    """
    #  void ExtrudedTextGeometry::doUpdateGeometry()
    self.uglySide.call('ritual_ZN20ExtrudedTextGeometry16doUpdateGeometryEv')

  def requestFinished(self) -> None:
    """
    Calls Qt's 'void ExtrudedTextGeometry::requestFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/extrudedtextgeometry.html#requestFinished
    """
    #  void ExtrudedTextGeometry::requestFinished()
    self.uglySide.call('ritual_ZN20ExtrudedTextGeometry15requestFinishedEv')

  def textChanged(self) -> None:
    """
    Calls Qt's 'void ExtrudedTextGeometry::textChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/extrudedtextgeometry.html#textChanged
    """
    #  void ExtrudedTextGeometry::textChanged()
    self.uglySide.call('ritual_ZN20ExtrudedTextGeometry11textChangedEv')

  def fontChanged(self) -> None:
    """
    Calls Qt's 'void ExtrudedTextGeometry::fontChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/extrudedtextgeometry.html#fontChanged
    """
    #  void ExtrudedTextGeometry::fontChanged()
    self.uglySide.call('ritual_ZN20ExtrudedTextGeometry11fontChangedEv')

  def depthChanged(self) -> None:
    """
    Calls Qt's 'void ExtrudedTextGeometry::depthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/extrudedtextgeometry.html#depthChanged
    """
    #  void ExtrudedTextGeometry::depthChanged()
    self.uglySide.call('ritual_ZN20ExtrudedTextGeometry12depthChangedEv')

  def scaleChanged(self) -> None:
    """
    Calls Qt's 'void ExtrudedTextGeometry::scaleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/extrudedtextgeometry.html#scaleChanged
    """
    #  void ExtrudedTextGeometry::scaleChanged()
    self.uglySide.call('ritual_ZN20ExtrudedTextGeometry12scaleChangedEv')

  def asynchronousChanged(self) -> None:
    """
    Calls Qt's 'void ExtrudedTextGeometry::asynchronousChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/extrudedtextgeometry.html#asynchronousChanged
    """
    #  void ExtrudedTextGeometry::asynchronousChanged()
    self.uglySide.call(
        'ritual_ZN20ExtrudedTextGeometry19asynchronousChangedEv',
    )

  def statusChanged(self) -> None:
    """
    Calls Qt's 'void ExtrudedTextGeometry::statusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/extrudedtextgeometry.html#statusChanged
    """
    #  void ExtrudedTextGeometry::statusChanged()
    self.uglySide.call('ritual_ZN20ExtrudedTextGeometry13statusChangedEv')

  def scheduleGeometryUpdate(self) -> None:
    """
    Calls Qt's 'void ExtrudedTextGeometry::scheduleGeometryUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/extrudedtextgeometry.html#scheduleGeometryUpdate
    """
    #  void ExtrudedTextGeometry::scheduleGeometryUpdate()
    self.uglySide.call(
        'ritual_ZN20ExtrudedTextGeometry22scheduleGeometryUpdateEv',
    )

  @staticmethod
  def generateExtrudedTextGeometry(*__, **_) -> Never:
    """
    Qt's 'ExtrudedTextGeometry::GeometryData
    ExtrudedTextGeometry::generateExtrudedTextGeometry(const QString &text,
    const QFont &font, float depth, float scale)': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'ExtrudedTextGeometry.generateExtrudedTextGeometry' has no cute "
        "function yet. Qt's 'ExtrudedTextGeometry::GeometryData "
        "ExtrudedTextGeometry::generateExtrudedTextGeometry(const QString "
        "&text, const QFont &font, float depth, float scale)': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def generateExtrudedTextGeometryAsync(*__, **_) -> Never:
    """
    Qt's 'void ExtrudedTextGeometry::generateExtrudedTextGeometryAsync(
    QPromise<ExtrudedTextGeometry::GeometryData> &promise, const QString
    &text, const QFont &font, float depth, float scale)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'ExtrudedTextGeometry.generateExtrudedTextGeometryAsync' has no "
        "cute function yet. Qt's 'void "
        "ExtrudedTextGeometry::generateExtrudedTextGeometryAsync(QPromise<Ex"
        "trudedTextGeometry::GeometryData> &promise, const QString &text, "
        "const QFont &font, float depth, float scale)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def updateGeometry(*__, **_) -> Never:
    """
    Qt's 'void ExtrudedTextGeometry::updateGeometry(const GeometryData
    &geometryData)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'ExtrudedTextGeometry.updateGeometry' has no cute function yet. "
        "Qt's 'void ExtrudedTextGeometry::updateGeometry(const GeometryData "
        "&geometryData)': takes a type Python has no way to hand over yet.")
