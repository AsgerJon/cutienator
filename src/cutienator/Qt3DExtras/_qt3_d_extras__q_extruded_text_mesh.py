"""
Qt3DExtras::QExtrudedTextMesh binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/qextrudedtextmesh.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from ..Qt3DRender import Qt3DRender

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


class QExtrudedTextMesh(Qt3DRender.QGeometryRenderer):
  """
  The cute side of Qt's Qt3DExtras::QExtrudedTextMesh: a plain Python object
  standing in front of one C++ Qt3DExtras::QExtrudedTextMesh.

  It is built on the cute 'Qt3DRender::QGeometryRenderer', as Qt's
  Qt3DExtras::QExtrudedTextMesh is built on Qt's
  Qt3DRender::QGeometryRenderer, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QExtrudedTextMesh that has a ritual and
  that Python can call so far, 11 names in all: 'metaObject', 'tr', 'text',
  'font', 'depth', 'setText', 'setFont', 'setDepth', 'textChanged',
  'fontChanged', 'depthChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::QExtrudedTextMesh::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DExtras::QExtrudedTextMesh::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DExtras::QExtrudedTextMesh::~QExtrudedTextMesh()': the
    destructor: Python never removes a C++ Qt3DExtras::QExtrudedTextMesh.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::QExtrudedTextMesh is created at the first use, not by
    'Qt3DExtras::QExtrudedTextMesh(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QExtrudedTextMesh.
  - Qt tells when it has removed the C++ Qt3DExtras::QExtrudedTextMesh. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString Qt3DExtras::QExtrudedTextMesh::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qextrudedtextmesh.html#tr

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
    #  QString Qt3DExtras::QExtrudedTextMesh::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras17QExtrudedTextMesh2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QExtrudedTextMesh'

  #  A C++ Qt3DExtras::QExtrudedTextMesh Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QExtrudedTextMesh'

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
    *Qt3DExtras::QExtrudedTextMesh::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qextrudedtextmesh.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DExtras::QExtrudedTextMesh::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras17QExtrudedTextMesh10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def text(self) -> str:
    """
    Calls Qt's 'QString Qt3DExtras::QExtrudedTextMesh::text() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qextrudedtextmesh.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DExtras::QExtrudedTextMesh::text() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras17QExtrudedTextMesh4textEv',
    )

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont Qt3DExtras::QExtrudedTextMesh::font() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qextrudedtextmesh.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont Qt3DExtras::QExtrudedTextMesh::font() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras17QExtrudedTextMesh4fontEv',
    )
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def depth(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QExtrudedTextMesh::depth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qextrudedtextmesh.html#depth
    """
    #  float Qt3DExtras::QExtrudedTextMesh::depth() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras17QExtrudedTextMesh5depthEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QExtrudedTextMesh::setText(const QString
    &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qextrudedtextmesh.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DExtras::QExtrudedTextMesh::setText(const QString &text)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras17QExtrudedTextMesh7setTextERK7QString', text,
    )

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QExtrudedTextMesh::setFont(const QFont
    &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qextrudedtextmesh.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void Qt3DExtras::QExtrudedTextMesh::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras17QExtrudedTextMesh7setFontERK5QFont',
        self._valueOf(font),
    )

  @overload(float)
  def setDepth(self, depth: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QExtrudedTextMesh::setDepth(float depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qextrudedtextmesh.html#setDepth

    Parameters
    ----------

    depth : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QExtrudedTextMesh::setDepth(float depth)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras17QExtrudedTextMesh8setDepthEf', depth,
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
    'Qt3DExtras::QExtrudedTextMesh::QExtrudedTextMesh(Qt3DCore::QNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qextrudedtextmesh.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DExtras::QExtrudedTextMesh::QExtrudedTextMesh(Qt3DCore::QNode
    #      *parent)
    self._noteCreation(QExtrudedTextMesh, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras17QExtrudedTextMeshC1EPN8Qt3DCore5QNodeE',
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
    Calls Qt's 'void Qt3DExtras::QExtrudedTextMesh::textChanged(const QString
    &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qextrudedtextmesh.html#textChanged

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DExtras::QExtrudedTextMesh::textChanged(const QString &text)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras17QExtrudedTextMesh11textChangedERK7QString',
        text,
    )

  @overload(QFont)
  def fontChanged(self, font: QFont) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QExtrudedTextMesh::fontChanged(const QFont
    &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qextrudedtextmesh.html#fontChanged

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void Qt3DExtras::QExtrudedTextMesh::fontChanged(const QFont &font)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras17QExtrudedTextMesh11fontChangedERK5QFont',
        self._valueOf(font),
    )

  @overload(float)
  def depthChanged(self, depth: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QExtrudedTextMesh::depthChanged(float
    depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qextrudedtextmesh.html#depthChanged

    Parameters
    ----------

    depth : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QExtrudedTextMesh::depthChanged(float depth)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras17QExtrudedTextMesh12depthChangedEf', depth,
    )
