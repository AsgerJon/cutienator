"""
Qt3DExtras::QExtrudedTextGeometry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/qextrudedtextgeometry.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DExtras

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QFont
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFont = WAIT['QFont']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QExtrudedTextGeometry(Qt3DCore.QGeometry):
  """
  The cute side of Qt's Qt3DExtras::QExtrudedTextGeometry: a plain Python
  object standing in front of one C++ Qt3DExtras::QExtrudedTextGeometry.

  It is built on the cute 'Qt3DCore::QGeometry', as Qt's
  Qt3DExtras::QExtrudedTextGeometry is built on Qt's Qt3DCore::QGeometry, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QExtrudedTextGeometry that has a ritual
  and that Python can call so far, 15 names in all: 'metaObject', 'tr',
  'positionAttribute', 'normalAttribute', 'indexAttribute', 'text', 'font',
  'extrusionLength', 'setText', 'setFont', 'setDepth', 'textChanged',
  'fontChanged', 'depthChanged', 'd_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::QExtrudedTextGeometry::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DExtras::QExtrudedTextGeometry::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DExtras::QExtrudedTextGeometry::~QExtrudedTextGeometry()': the
    destructor: Python never removes a C++ Qt3DExtras::QExtrudedTextGeometry.
  - Qt's 'Qt3DExtras::QExtrudedTextGeometry::QExtrudedTextGeometry(
    QExtrudedTextGeometryPrivate &dd, QNode *parent)': takes a type Python
    has no way to hand over yet.
  - Qt's 'const QExtrudedTextGeometryPrivate
    *Qt3DExtras::QExtrudedTextGeometry::d_func() const': takes in Python what
    'QExtrudedTextGeometryPrivate
    *Qt3DExtras::QExtrudedTextGeometry::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::QExtrudedTextGeometry is created at the first use,
    not by 'Qt3DExtras::QExtrudedTextGeometry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QExtrudedTextGeometry.
  - Qt tells when it has removed the C++ Qt3DExtras::QExtrudedTextGeometry.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString Qt3DExtras::QExtrudedTextGeometry::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qextrudedtextgeometry.html#tr

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
    #  QString Qt3DExtras::QExtrudedTextGeometry::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras21QExtrudedTextGeometry2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QExtrudedTextGeometry'

  #  A C++ Qt3DExtras::QExtrudedTextGeometry Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QExtrudedTextGeometry'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *Qt3DExtras::QExtrudedTextGeometry::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qextrudedtextgeometry.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DExtras::QExtrudedTextGeometry::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras21QExtrudedTextGeometry10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def positionAttribute(self) -> Optional[Qt3DCore.QAttribute]:
    """
    Calls Qt's 'Qt3DCore::QAttribute
    *Qt3DExtras::QExtrudedTextGeometry::positionAttribute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qextrudedtextgeometry.html

    Returns
    -------

    Optional[Qt3DCore.QAttribute]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QAttribute
    #      *Qt3DExtras::QExtrudedTextGeometry::positionAttribute() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras21QExtrudedTextGeometry17positionAttributeEv',
    )
    return Qt3DCore.QAttribute._cuteAt(address)

  def normalAttribute(self) -> Optional[Qt3DCore.QAttribute]:
    """
    Calls Qt's 'Qt3DCore::QAttribute
    *Qt3DExtras::QExtrudedTextGeometry::normalAttribute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qextrudedtextgeometry.html

    Returns
    -------

    Optional[Qt3DCore.QAttribute]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QAttribute
    #      *Qt3DExtras::QExtrudedTextGeometry::normalAttribute() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras21QExtrudedTextGeometry15normalAttributeEv',
    )
    return Qt3DCore.QAttribute._cuteAt(address)

  def indexAttribute(self) -> Optional[Qt3DCore.QAttribute]:
    """
    Calls Qt's 'Qt3DCore::QAttribute
    *Qt3DExtras::QExtrudedTextGeometry::indexAttribute() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qextrudedtextgeometry.html

    Returns
    -------

    Optional[Qt3DCore.QAttribute]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QAttribute
    #      *Qt3DExtras::QExtrudedTextGeometry::indexAttribute() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras21QExtrudedTextGeometry14indexAttributeEv',
    )
    return Qt3DCore.QAttribute._cuteAt(address)

  def text(self) -> str:
    """
    Calls Qt's 'QString Qt3DExtras::QExtrudedTextGeometry::text() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qextrudedtextgeometry.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DExtras::QExtrudedTextGeometry::text() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras21QExtrudedTextGeometry4textEv',
    )

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont Qt3DExtras::QExtrudedTextGeometry::font() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qextrudedtextgeometry.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont Qt3DExtras::QExtrudedTextGeometry::font() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras21QExtrudedTextGeometry4fontEv',
    )
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def extrusionLength(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QExtrudedTextGeometry::extrusionLength()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qextrudedtextgeometry.html
    """
    #  float Qt3DExtras::QExtrudedTextGeometry::extrusionLength() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras21QExtrudedTextGeometry15extrusionLengthEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QExtrudedTextGeometry::setText(const QString
    &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qextrudedtextgeometry.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DExtras::QExtrudedTextGeometry::setText(const QString &text)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras21QExtrudedTextGeometry7setTextERK7QString',
        text,
    )

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QExtrudedTextGeometry::setFont(const QFont
    &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qextrudedtextgeometry.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void Qt3DExtras::QExtrudedTextGeometry::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras21QExtrudedTextGeometry7setFontERK5QFont',
        self._valueOf(font),
    )

  @overload(float)
  def setDepth(self, extrusionLength: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QExtrudedTextGeometry::setDepth(float
    extrusionLength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qextrudedtextgeometry.html#setDepth

    Parameters
    ----------

    extrusionLength : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QExtrudedTextGeometry::setDepth(float
    #      extrusionLength)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras21QExtrudedTextGeometry8setDepthEf',
        extrusionLength,
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DExtras::QExtrudedTextGeometry::QExtrudedTextGeometry(Qt3DCore::QNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qextrudedtextgeometry.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DExtras::QExtrudedTextGeometry::QExtrudedTextGeometry(
    #      Qt3DCore::QNode *parent)
    self._noteCreation(QExtrudedTextGeometry, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras21QExtrudedTextGeometryC1EPN8Qt3DCore5QNodeE',
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

  @overload(str)
  def textChanged(self, text: str) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QExtrudedTextGeometry::textChanged(const
    QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qextrudedtextgeometry.html#textChanged

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DExtras::QExtrudedTextGeometry::textChanged(const QString
    #      &text)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras21QExtrudedTextGeometry11textChangedERK7QStri'
        'ng',
        text,
    )

  @overload(QFont)
  def fontChanged(self, font: QFont) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QExtrudedTextGeometry::fontChanged(const
    QFont &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qextrudedtextgeometry.html#fontChanged

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void Qt3DExtras::QExtrudedTextGeometry::fontChanged(const QFont &font)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras21QExtrudedTextGeometry11fontChangedERK5QFont',
        self._valueOf(font),
    )

  @overload(float)
  def depthChanged(self, extrusionLength: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QExtrudedTextGeometry::depthChanged(float
    extrusionLength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qextrudedtextgeometry.html#depthChanged

    Parameters
    ----------

    extrusionLength : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QExtrudedTextGeometry::depthChanged(float
    #      extrusionLength)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras21QExtrudedTextGeometry12depthChangedEf',
        extrusionLength,
    )

  def d_func(self) -> Optional[Qt3DExtras.QExtrudedTextGeometryPrivate]:
    """
    Calls Qt's 'QExtrudedTextGeometryPrivate
    *Qt3DExtras::QExtrudedTextGeometry::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qextrudedtextgeometry.html#d_func

    Returns
    -------

    Optional[Qt3DExtras.QExtrudedTextGeometryPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QExtrudedTextGeometryPrivate
    #      *Qt3DExtras::QExtrudedTextGeometry::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras21QExtrudedTextGeometry6d_funcEv',
    )
    return Qt3DExtras.QExtrudedTextGeometryPrivate._cuteAt(address)
