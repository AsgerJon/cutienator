"""
Qt3DExtras::QText2DEntity binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/qtext2dentity.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..Qt3DCore import Qt3DCore
from . import Qt3DExtras

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor, QFont
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QFont = WAIT['QFont']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QText2DEntity(Qt3DCore.QEntity):
  """
  The cute side of Qt's Qt3DExtras::QText2DEntity: a plain Python object
  standing in front of one C++ Qt3DExtras::QText2DEntity.

  It is built on the cute 'Qt3DCore::QEntity', as Qt's
  Qt3DExtras::QText2DEntity is built on Qt's Qt3DCore::QEntity, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QText2DEntity that has a ritual and that
  Python can call so far, 20 names in all: 'metaObject', 'tr', 'font',
  'setFont', 'color', 'setColor', 'text', 'setText', 'width', 'height',
  'setWidth', 'setHeight', 'alignment', 'setAlignment', 'fontChanged',
  'colorChanged', 'textChanged', 'widthChanged', 'heightChanged', 'd_func'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::QText2DEntity::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DExtras::QText2DEntity::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DExtras::QText2DEntity::~QText2DEntity()': the destructor:
    Python never removes a C++ Qt3DExtras::QText2DEntity.
  - Qt's 'const QText2DEntityPrivate *Qt3DExtras::QText2DEntity::d_func()
    const': takes in Python what 'QText2DEntityPrivate
    *Qt3DExtras::QText2DEntity::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 27 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::QText2DEntity is created at the first use, not by
    'Qt3DExtras::QText2DEntity(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QText2DEntity.
  - Qt tells when it has removed the C++ Qt3DExtras::QText2DEntity. Every
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
    Calls Qt's 'QString Qt3DExtras::QText2DEntity::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dextras-qtext2dentity.html#tr

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
    #  QString Qt3DExtras::QText2DEntity::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras13QText2DEntity2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QText2DEntity'

  #  A C++ Qt3DExtras::QText2DEntity Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QText2DEntity'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DExtras::QText2DEntity::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtext2dentity.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DExtras::QText2DEntity::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras13QText2DEntity10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont Qt3DExtras::QText2DEntity::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dextras-qtext2dentity.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont Qt3DExtras::QText2DEntity::font() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras13QText2DEntity4fontEv',
    )
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor Qt3DExtras::QText2DEntity::color() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtext2dentity.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Qt3DExtras::QText2DEntity::color() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras13QText2DEntity5colorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def text(self) -> str:
    """
    Calls Qt's 'QString Qt3DExtras::QText2DEntity::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dextras-qtext2dentity.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DExtras::QText2DEntity::text() const
    return self.uglySide.call('ritual_ZNK10Qt3DExtras13QText2DEntity4textEv')

  def width(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QText2DEntity::width() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtext2dentity.html#width
    """
    #  float Qt3DExtras::QText2DEntity::width() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras13QText2DEntity5widthEv',
    )

  def height(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QText2DEntity::height() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtext2dentity.html#height
    """
    #  float Qt3DExtras::QText2DEntity::height() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras13QText2DEntity6heightEv',
    )

  def alignment(self) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment Qt3DExtras::QText2DEntity::alignment() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtext2dentity.html#alignment

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment Qt3DExtras::QText2DEntity::alignment() const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK10Qt3DExtras13QText2DEntity9alignmentEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QText2DEntity::setFont(const QFont &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtext2dentity.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void Qt3DExtras::QText2DEntity::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QText2DEntity7setFontERK5QFont',
        self._valueOf(font),
    )

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QText2DEntity::setColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtext2dentity.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QText2DEntity::setColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QText2DEntity8setColorERK6QColor',
        self._valueOf(color),
    )

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QText2DEntity::setText(const QString
    &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtext2dentity.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DExtras::QText2DEntity::setText(const QString &text)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QText2DEntity7setTextERK7QString', text,
    )

  @overload(float)
  def setWidth(self, width: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QText2DEntity::setWidth(float width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtext2dentity.html#setWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QText2DEntity::setWidth(float width)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QText2DEntity8setWidthEf', width,
    )

  @overload(float)
  def setHeight(self, height: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QText2DEntity::setHeight(float height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtext2dentity.html#setHeight

    Parameters
    ----------

    height : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QText2DEntity::setHeight(float height)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QText2DEntity9setHeightEf', height,
    )

  @overload(Qt.Alignment)
  def setAlignment(self, alignment: Qt.Alignment) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QText2DEntity::setAlignment(Qt::Alignment
    alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtext2dentity.html#setAlignment

    Parameters
    ----------

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  void Qt3DExtras::QText2DEntity::setAlignment(Qt::Alignment alignment)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QText2DEntity12setAlignmentE6QFlagsIN2Qt13A'
        'lignmentFlagEE',
        alignment.value,
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
    'Qt3DExtras::QText2DEntity::QText2DEntity(Qt3DCore::QNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtext2dentity.html#QText2DEntity

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DExtras::QText2DEntity::QText2DEntity(Qt3DCore::QNode *parent)
    self._noteCreation(QText2DEntity, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras13QText2DEntityC1EPN8Qt3DCore5QNodeE',
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

  @overload(QFont)
  def fontChanged(self, font: QFont) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QText2DEntity::fontChanged(const QFont
    &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtext2dentity.html#fontChanged

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void Qt3DExtras::QText2DEntity::fontChanged(const QFont &font)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QText2DEntity11fontChangedERK5QFont',
        self._valueOf(font),
    )

  @overload(QColor)
  def colorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QText2DEntity::colorChanged(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtext2dentity.html#colorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QText2DEntity::colorChanged(const QColor &color)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QText2DEntity12colorChangedERK6QColor',
        self._valueOf(color),
    )

  @overload(str)
  def textChanged(self, text: str) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QText2DEntity::textChanged(const QString
    &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtext2dentity.html#textChanged

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DExtras::QText2DEntity::textChanged(const QString &text)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QText2DEntity11textChangedERK7QString', text,
    )

  @overload(float)
  def widthChanged(self, width: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QText2DEntity::widthChanged(float width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtext2dentity.html#widthChanged

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QText2DEntity::widthChanged(float width)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QText2DEntity12widthChangedEf', width,
    )

  @overload(float)
  def heightChanged(self, height: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QText2DEntity::heightChanged(float height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtext2dentity.html#heightChanged

    Parameters
    ----------

    height : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QText2DEntity::heightChanged(float height)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QText2DEntity13heightChangedEf', height,
    )

  def d_func(self) -> Optional[Qt3DExtras.QText2DEntityPrivate]:
    """
    Calls Qt's 'QText2DEntityPrivate *Qt3DExtras::QText2DEntity::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtext2dentity.html#d_func

    Returns
    -------

    Optional[Qt3DExtras.QText2DEntityPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QText2DEntityPrivate *Qt3DExtras::QText2DEntity::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras13QText2DEntity6d_funcEv',
    )
    return Qt3DExtras.QText2DEntityPrivate._cuteAt(address)
