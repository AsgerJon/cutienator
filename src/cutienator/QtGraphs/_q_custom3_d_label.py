"""
QCustom3DLabel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qcustom3dlabel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QCustom3DItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor, QFont, QQuaternion, QVector3D
  from . import QCustom3DLabelPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QFont = WAIT['QFont']
  QQuaternion = WAIT['QQuaternion']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCustom3DLabel(QCustom3DItem):
  """
  The cute side of Qt's QCustom3DLabel: a plain Python object standing in
  front of one C++ QCustom3DLabel.

  It is built on the cute 'QCustom3DItem', as Qt's QCustom3DLabel is built on
  Qt's QCustom3DItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCustom3DLabel that has a ritual and that Python can
  call so far, 24 names in all: 'metaObject', 'tr', 'd_func', 'setText',
  'text', 'setFont', 'font', 'setTextColor', 'textColor',
  'setBackgroundColor', 'backgroundColor', 'setBorderVisible',
  'isBorderVisible', 'setBackgroundVisible', 'isBackgroundVisible',
  'setFacingCamera', 'isFacingCamera', 'textChanged', 'fontChanged',
  'textColorChanged', 'backgroundColorChanged', 'borderVisibleChanged',
  'backgroundVisibleChanged', 'facingCameraChanged'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCustom3DLabel::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QCustom3DLabel::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QCustom3DLabelPrivate *QCustom3DLabel::d_func() const': takes
    in Python what 'QCustom3DLabelPrivate *QCustom3DLabel::d_func()' takes.
  - Qt's 'QCustom3DLabel::~QCustom3DLabel()': the destructor: Python never
    removes a C++ QCustom3DLabel.

  What has no ritual
  ------------------

  4 of the 34 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QCustom3DLabel is created at the first use, not by
    'QCustom3DLabel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCustom3DLabel.
  - Qt tells when it has removed the C++ QCustom3DLabel. Every call on the
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
    Calls Qt's 'QString QCustom3DLabel::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3dlabel.html#tr

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
    #  QString QCustom3DLabel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QCustom3DLabel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCustom3DLabel'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QCustom3DLabel Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCustom3DLabel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCustom3DLabel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3dlabel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCustom3DLabel::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QCustom3DLabel10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def text(self) -> str:
    """
    Calls Qt's 'QString QCustom3DLabel::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3dlabel.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCustom3DLabel::text() const
    return self.uglySide.call('ritual_ZNK14QCustom3DLabel4textEv')

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QCustom3DLabel::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3dlabel.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QCustom3DLabel::font() const
    address = self.uglySide.call('ritual_ZNK14QCustom3DLabel4fontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def textColor(self) -> QColor:
    """
    Calls Qt's 'QColor QCustom3DLabel::textColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3dlabel.html#textColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QCustom3DLabel::textColor() const
    address = self.uglySide.call('ritual_ZNK14QCustom3DLabel9textColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def backgroundColor(self) -> QColor:
    """
    Calls Qt's 'QColor QCustom3DLabel::backgroundColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dlabel.html#backgroundColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QCustom3DLabel::backgroundColor() const
    address = self.uglySide.call(
        'ritual_ZNK14QCustom3DLabel15backgroundColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def isBorderVisible(self) -> bool:
    """
    Calls Qt's 'bool QCustom3DLabel::isBorderVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dlabel.html#isBorderVisible
    """
    #  bool QCustom3DLabel::isBorderVisible() const
    return self.uglySide.call(
        'ritual_ZNK14QCustom3DLabel15isBorderVisibleEv',
    )

  def isBackgroundVisible(self) -> bool:
    """
    Calls Qt's 'bool QCustom3DLabel::isBackgroundVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dlabel.html#isBackgroundVisible
    """
    #  bool QCustom3DLabel::isBackgroundVisible() const
    return self.uglySide.call(
        'ritual_ZNK14QCustom3DLabel19isBackgroundVisibleEv',
    )

  def isFacingCamera(self) -> bool:
    """
    Calls Qt's 'bool QCustom3DLabel::isFacingCamera() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3dlabel.html#isFacingCamera
    """
    #  bool QCustom3DLabel::isFacingCamera() const
    return self.uglySide.call('ritual_ZNK14QCustom3DLabel14isFacingCameraEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void QCustom3DLabel::setText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3dlabel.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCustom3DLabel::setText(const QString &text)
    self.uglySide.call('ritual_ZN14QCustom3DLabel7setTextERK7QString', text)

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QCustom3DLabel::setFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3dlabel.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QCustom3DLabel::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN14QCustom3DLabel7setFontERK5QFont', self._valueOf(font),
    )

  @overload(QColor)
  def setTextColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QCustom3DLabel::setTextColor(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3dlabel.html#setTextColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QCustom3DLabel::setTextColor(QColor color)
    self.uglySide.call(
        'ritual_ZN14QCustom3DLabel12setTextColorE6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setBackgroundColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QCustom3DLabel::setBackgroundColor(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dlabel.html#setBackgroundColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QCustom3DLabel::setBackgroundColor(QColor color)
    self.uglySide.call(
        'ritual_ZN14QCustom3DLabel18setBackgroundColorE6QColor',
        self._valueOf(color),
    )

  @overload(bool)
  def setBorderVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QCustom3DLabel::setBorderVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dlabel.html#setBorderVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QCustom3DLabel::setBorderVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN14QCustom3DLabel16setBorderVisibleEb', visible,
    )

  @overload(bool)
  def setBackgroundVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QCustom3DLabel::setBackgroundVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dlabel.html#setBackgroundVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QCustom3DLabel::setBackgroundVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN14QCustom3DLabel20setBackgroundVisibleEb', visible,
    )

  @overload(bool)
  def setFacingCamera(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QCustom3DLabel::setFacingCamera(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dlabel.html#setFacingCamera

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QCustom3DLabel::setFacingCamera(bool enabled)
    self.uglySide.call(
        'ritual_ZN14QCustom3DLabel15setFacingCameraEb', enabled,
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
    Notes what was given, for Qt's 'QCustom3DLabel::QCustom3DLabel(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3dlabel.html#QCustom3DLabel

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QCustom3DLabel::QCustom3DLabel(QObject *parent)
    self._noteCreation(QCustom3DLabel, lambda: Rituals.call(
        'ritual_ZN14QCustom3DLabelC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(str, QFont, QVector3D, QVector3D, QQuaternion)
  @overload(str, QFont, QVector3D, QVector3D, QQuaternion, QObject)
  @overload(str, QFont, QVector3D, QVector3D, QQuaternion, NoneType)
  def __init__(
      self,
      text: str,
      font: QFont,
      position: QVector3D,
      scaling: QVector3D,
      rotation: QQuaternion,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QCustom3DLabel::QCustom3DLabel(const
    QString &text, const QFont &font, QVector3D position, QVector3D scaling,
    const QQuaternion &rotation, QObject *parent)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3dlabel.html#QCustom3DLabel

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    scaling : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    rotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QCustom3DLabel::QCustom3DLabel(const QString &text, const QFont &font,
    #      QVector3D position, QVector3D scaling, const QQuaternion
    #      &rotation, QObject *parent)
    self._noteCreation(QCustom3DLabel, lambda: Rituals.call(
        'ritual_ZN14QCustom3DLabelC1ERK7QStringRK5QFont9QVector3DS6_RK11QQu'
        'aternionP7QObject',
        text, self._valueOf(font), self._valueOf(position),
        self._valueOf(scaling), self._valueOf(rotation),
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

  def d_func(self) -> Optional[QCustom3DLabelPrivate]:
    """
    Calls Qt's 'QCustom3DLabelPrivate *QCustom3DLabel::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3dlabel.html#d_func

    Returns
    -------

    Optional[QCustom3DLabelPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCustom3DLabelPrivate *QCustom3DLabel::d_func()
    address = self.uglySide.call('ritual_ZN14QCustom3DLabel6d_funcEv')
    from . import QCustom3DLabelPrivate
    return QCustom3DLabelPrivate._cuteAt(address)

  @overload(str)
  def textChanged(self, text: str) -> None:
    """
    Calls Qt's 'void QCustom3DLabel::textChanged(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3dlabel.html#textChanged

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCustom3DLabel::textChanged(const QString &text)
    self.uglySide.call(
        'ritual_ZN14QCustom3DLabel11textChangedERK7QString', text,
    )

  @overload(QFont)
  def fontChanged(self, font: QFont) -> None:
    """
    Calls Qt's 'void QCustom3DLabel::fontChanged(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3dlabel.html#fontChanged

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QCustom3DLabel::fontChanged(const QFont &font)
    self.uglySide.call(
        'ritual_ZN14QCustom3DLabel11fontChangedERK5QFont',
        self._valueOf(font),
    )

  @overload(QColor)
  def textColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QCustom3DLabel::textColorChanged(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dlabel.html#textColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QCustom3DLabel::textColorChanged(QColor color)
    self.uglySide.call(
        'ritual_ZN14QCustom3DLabel16textColorChangedE6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def backgroundColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QCustom3DLabel::backgroundColorChanged(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dlabel.html#backgroundColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QCustom3DLabel::backgroundColorChanged(QColor color)
    self.uglySide.call(
        'ritual_ZN14QCustom3DLabel22backgroundColorChangedE6QColor',
        self._valueOf(color),
    )

  @overload(bool)
  def borderVisibleChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void QCustom3DLabel::borderVisibleChanged(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dlabel.html#borderVisibleChanged

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QCustom3DLabel::borderVisibleChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN14QCustom3DLabel20borderVisibleChangedEb', visible,
    )

  @overload(bool)
  def backgroundVisibleChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void QCustom3DLabel::backgroundVisibleChanged(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dlabel.html#backgroundVisibleChanged

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QCustom3DLabel::backgroundVisibleChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN14QCustom3DLabel24backgroundVisibleChangedEb', visible,
    )

  @overload(bool)
  def facingCameraChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QCustom3DLabel::facingCameraChanged(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dlabel.html#facingCameraChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QCustom3DLabel::facingCameraChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN14QCustom3DLabel19facingCameraChangedEb', enabled,
    )
