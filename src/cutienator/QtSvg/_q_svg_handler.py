"""
QSvgHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvghandler_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSvgHandler to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtGui import QGuiSvg
from . import QtSvg

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QIODevice, QXmlStreamAttributes
  from ..QtGui import QColor, QPen
  from . import QSvgDocument, QSvgStyleProperty
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QColor = WAIT['QColor']
  QIODevice = WAIT['QIODevice']
  QSvgStyleProperty = WAIT['QSvgStyleProperty']
  QXmlStreamAttributes = WAIT['QXmlStreamAttributes']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSvgHandler(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSvgHandler: a plain Python object standing in front
  of one C++ QSvgHandler.

  What exists
  -----------

  Every function of Qt's QSvgHandler that has a ritual and that Python can
  call so far, 29 names in all: 'device', 'document', 'ok', 'errorString',
  'lineNumber', 'setDefaultCoordinateSystem', 'defaultCoordinateSystem',
  'pushColor', 'pushColorCopy', 'popColor', 'currentColor',
  'pushUnresolvedStyle', 'setCurrentSvgFontFamily', 'setInStyle', 'inStyle',
  'setAnimPeriod', 'animationDuration', 'defaultPen', 'options',
  'animatorType', 'trustedSourceMode', 'startElement', 'endElement',
  'characters', 'processingInstruction', 'init', 'parse',
  'resolvePaintServers', 'resolveNodes'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgHandler::QSvgHandler(QXmlStreamReader *const data,
    QtSvg::Options options, QtSvg::AnimatorType type)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QSvgHandler::~QSvgHandler()': the destructor: Python never removes
    a C++ QSvgHandler.
  - Qt's 'QSvgCssHandler &QSvgHandler::cssHandler()': gives a type Python has
    no way to take yet.

  What has no ritual
  ------------------

  1 of the 35 functions Qt declares: 1 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ QSvgHandler is created at the first use, not by
    'QSvgHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgHandler.
  - Each name of Qt's QSvgHandler that has no cute function yet,
    'cssHandler', 'takeDocument', holds a function that raises
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
  __qt_class__ = 'QSvgHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def device(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QSvgHandler::device() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvghandler.html#device

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QSvgHandler::device() const
    address = self.uglySide.call('ritual_ZNK11QSvgHandler6deviceEv')
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  def document(self) -> Optional[QSvgDocument]:
    """
    Calls Qt's 'QSvgDocument *QSvgHandler::document() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvghandler.html#document

    Returns
    -------

    Optional[QSvgDocument]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSvgDocument *QSvgHandler::document() const
    address = self.uglySide.call('ritual_ZNK11QSvgHandler8documentEv')
    from . import QSvgDocument
    return QSvgDocument._cuteAt(address)

  def ok(self) -> bool:
    """
    Calls Qt's 'bool QSvgHandler::ok() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvghandler.html#ok
    """
    #  bool QSvgHandler::ok() const
    return self.uglySide.call('ritual_ZNK11QSvgHandler2okEv')

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QSvgHandler::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvghandler.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSvgHandler::errorString() const
    return self.uglySide.call('ritual_ZNK11QSvgHandler11errorStringEv')

  def lineNumber(self) -> int:
    """
    Calls Qt's 'int QSvgHandler::lineNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvghandler.html#lineNumber
    """
    #  int QSvgHandler::lineNumber() const
    return self.uglySide.call('ritual_ZNK11QSvgHandler10lineNumberEv')

  def defaultCoordinateSystem(self) -> QGuiSvg.LengthType:
    """
    Calls Qt's 'QGuiSvg::LengthType QSvgHandler::defaultCoordinateSystem()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvghandler.html#defaultCoordinateSystem

    Returns
    -------

    QGuiSvg.LengthType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QGuiSvg.LengthType(number)' gives.
    """
    #  QGuiSvg::LengthType QSvgHandler::defaultCoordinateSystem() const
    return QGuiSvg.LengthType(self.uglySide.call(
        'ritual_ZNK11QSvgHandler23defaultCoordinateSystemEv',
    ))

  def currentColor(self) -> QColor:
    """
    Calls Qt's 'QColor QSvgHandler::currentColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvghandler.html#currentColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QSvgHandler::currentColor() const
    address = self.uglySide.call('ritual_ZNK11QSvgHandler12currentColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def inStyle(self) -> bool:
    """
    Calls Qt's 'bool QSvgHandler::inStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvghandler.html#inStyle
    """
    #  bool QSvgHandler::inStyle() const
    return self.uglySide.call('ritual_ZNK11QSvgHandler7inStyleEv')

  def animationDuration(self) -> int:
    """
    Calls Qt's 'int QSvgHandler::animationDuration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvghandler.html#animationDuration
    """
    #  int QSvgHandler::animationDuration() const
    return self.uglySide.call('ritual_ZNK11QSvgHandler17animationDurationEv')

  def defaultPen(self) -> QPen:
    """
    Calls Qt's 'QPen QSvgHandler::defaultPen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvghandler.html#defaultPen

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen QSvgHandler::defaultPen() const
    address = self.uglySide.call('ritual_ZNK11QSvgHandler10defaultPenEv')
    from ..QtGui import QPen
    return QPen._cuteOwning(address)

  def options(self) -> QtSvg.Options:
    """
    Calls Qt's 'QtSvg::Options QSvgHandler::options() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvghandler.html#options

    Returns
    -------

    QtSvg.Options
      The value standing for the combination Qt gave back.
    """
    #  QtSvg::Options QSvgHandler::options() const
    return QtSvg.Options(self.uglySide.call(
        'ritual_ZNK11QSvgHandler7optionsEv',
    ))

  def animatorType(self) -> QtSvg.AnimatorType:
    """
    Calls Qt's 'QtSvg::AnimatorType QSvgHandler::animatorType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvghandler.html#animatorType

    Returns
    -------

    QtSvg.AnimatorType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtSvg.AnimatorType(number)' gives.
    """
    #  QtSvg::AnimatorType QSvgHandler::animatorType() const
    return QtSvg.AnimatorType(self.uglySide.call(
        'ritual_ZNK11QSvgHandler12animatorTypeEv',
    ))

  def trustedSourceMode(self) -> bool:
    """
    Calls Qt's 'bool QSvgHandler::trustedSourceMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvghandler.html#trustedSourceMode
    """
    #  bool QSvgHandler::trustedSourceMode() const
    return self.uglySide.call('ritual_ZNK11QSvgHandler17trustedSourceModeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGuiSvg.LengthType)
  def setDefaultCoordinateSystem(self, type: QGuiSvg.LengthType) -> None:
    """
    Calls Qt's 'void
    QSvgHandler::setDefaultCoordinateSystem(QGuiSvg::LengthType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvghandler.html#setDefaultCoordinateSystem

    Parameters
    ----------

    type : QGuiSvg.LengthType
      Passed on as its number.
    """
    #  void QSvgHandler::setDefaultCoordinateSystem(QGuiSvg::LengthType type)
    self.uglySide.call(
        'ritual_ZN11QSvgHandler26setDefaultCoordinateSystemEN7QGuiSvg10Leng'
        'thTypeE',
        type.value,
    )

  @overload(str)
  def setCurrentSvgFontFamily(self, family: str) -> None:
    """
    Calls Qt's 'void QSvgHandler::setCurrentSvgFontFamily(QStringView
    family)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvghandler.html#setCurrentSvgFontFamily

    Parameters
    ----------

    family : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSvgHandler::setCurrentSvgFontFamily(QStringView family)
    self.uglySide.call(
        'ritual_ZN11QSvgHandler23setCurrentSvgFontFamilyE11QStringView',
        family,
    )

  @overload(bool)
  def setInStyle(self, b: bool) -> None:
    """
    Calls Qt's 'void QSvgHandler::setInStyle(bool b)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvghandler.html#setInStyle

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QSvgHandler::setInStyle(bool b)
    self.uglySide.call('ritual_ZN11QSvgHandler10setInStyleEb', b)

  @overload(int, int)
  def setAnimPeriod(self, start: int, end: int) -> None:
    """
    Calls Qt's 'void QSvgHandler::setAnimPeriod(int start, int end)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvghandler.html#setAnimPeriod

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QSvgHandler::setAnimPeriod(int start, int end)
    self.uglySide.call(
        'ritual_ZN11QSvgHandler13setAnimPeriodEii', start, end,
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

  @overload(QIODevice)
  @overload(NoneType)
  @overload(QIODevice, QtSvg.Options)
  @overload(NoneType, QtSvg.Options)
  @overload(QIODevice, QtSvg.Options, QtSvg.AnimatorType)
  @overload(NoneType, QtSvg.Options, QtSvg.AnimatorType)
  def __init__(
      self,
      device: Optional[QIODevice],
      options: QtSvg.Options = QtSvg.Options(),
      type: QtSvg.AnimatorType = QtSvg.AnimatorType.Automatic,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSvgHandler::QSvgHandler(QIODevice
    *device, QtSvg::Options options, QtSvg::AnimatorType type)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvghandler.html#QSvgHandler

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    options : QtSvg.Options
      Passed on as its number. May be left out, as in Qt: it is then
      QtSvg.Options().

    type : QtSvg.AnimatorType
      Passed on as its number. May be left out, as in Qt: it is then
      QtSvg.AnimatorType.Automatic.
    """
    #  QSvgHandler::QSvgHandler(QIODevice *device, QtSvg::Options options,
    #      QtSvg::AnimatorType type)
    self._noteCreation(QSvgHandler, lambda: Rituals.call(
        'ritual_ZN11QSvgHandlerC1EP9QIODevice6QFlagsIN5QtSvg6OptionEENS3_12'
        'AnimatorTypeE',
        self._addressOf(device), options.value, type.value,
    ))

  @overload(QByteArray)
  @overload(QByteArray, QtSvg.Options)
  @overload(QByteArray, QtSvg.Options, QtSvg.AnimatorType)
  def __init__(
      self,
      data: QByteArray,
      options: QtSvg.Options = QtSvg.Options(),
      type: QtSvg.AnimatorType = QtSvg.AnimatorType.Automatic,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSvgHandler::QSvgHandler(const QByteArray
    &data, QtSvg::Options options, QtSvg::AnimatorType type)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvghandler.html#QSvgHandler

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    options : QtSvg.Options
      Passed on as its number. May be left out, as in Qt: it is then
      QtSvg.Options().

    type : QtSvg.AnimatorType
      Passed on as its number. May be left out, as in Qt: it is then
      QtSvg.AnimatorType.Automatic.
    """
    #  QSvgHandler::QSvgHandler(const QByteArray &data, QtSvg::Options
    #      options, QtSvg::AnimatorType type)
    self._noteCreation(QSvgHandler, lambda: Rituals.call(
        'ritual_ZN11QSvgHandlerC1ERK10QByteArray6QFlagsIN5QtSvg6OptionEENS4'
        '_12AnimatorTypeE',
        self._valueOf(data), options.value, type.value,
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

  @overload(QColor)
  def pushColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSvgHandler::pushColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvghandler.html#pushColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSvgHandler::pushColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN11QSvgHandler9pushColorERK6QColor', self._valueOf(color),
    )

  def pushColorCopy(self) -> None:
    """
    Calls Qt's 'void QSvgHandler::pushColorCopy()'.

    Qt's own words: https://doc.qt.io/qt-6/qsvghandler.html#pushColorCopy
    """
    #  void QSvgHandler::pushColorCopy()
    self.uglySide.call('ritual_ZN11QSvgHandler13pushColorCopyEv')

  def popColor(self) -> None:
    """
    Calls Qt's 'void QSvgHandler::popColor()'.

    Qt's own words: https://doc.qt.io/qt-6/qsvghandler.html#popColor
    """
    #  void QSvgHandler::popColor()
    self.uglySide.call('ritual_ZN11QSvgHandler8popColorEv')

  @overload(QSvgStyleProperty)
  @overload(NoneType)
  def pushUnresolvedStyle(self, prop: Optional[QSvgStyleProperty]) -> None:
    """
    Calls Qt's 'void QSvgHandler::pushUnresolvedStyle(QSvgStyleProperty
    *prop)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvghandler.html#pushUnresolvedStyle

    Parameters
    ----------

    prop : Optional[QSvgStyleProperty]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgHandler::pushUnresolvedStyle(QSvgStyleProperty *prop)
    self.uglySide.call(
        'ritual_ZN11QSvgHandler19pushUnresolvedStyleEP17QSvgStyleProperty',
        self._addressOf(prop),
    )

  @overload(str, QXmlStreamAttributes)
  def startElement(
      self,
      localName: str,
      attributes: QXmlStreamAttributes,
  ) -> bool:
    """
    Calls Qt's 'bool QSvgHandler::startElement(const QStringView localName,
    const QXmlStreamAttributes &attributes)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvghandler.html#startElement

    Parameters
    ----------

    localName : str
      Passed on as it is: a QString is made of it for the call.

    attributes : QXmlStreamAttributes
      Passed on as a value: Qt reads the C++ QXmlStreamAttributes, which
      stays Python's own.
    """
    #  bool QSvgHandler::startElement(const QStringView localName, const
    #      QXmlStreamAttributes &attributes)
    return self.uglySide.call(
        'ritual_ZN11QSvgHandler12startElementE11QStringViewRK20QXmlStreamAt'
        'tributes',
        localName, self._valueOf(attributes),
    )

  @overload(str)
  def endElement(self, localName: str) -> bool:
    """
    Calls Qt's 'bool QSvgHandler::endElement(const QStringView localName)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvghandler.html#endElement

    Parameters
    ----------

    localName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QSvgHandler::endElement(const QStringView localName)
    return self.uglySide.call(
        'ritual_ZN11QSvgHandler10endElementE11QStringView', localName,
    )

  @overload(str)
  def characters(self, str: str) -> bool:
    """
    Calls Qt's 'bool QSvgHandler::characters(const QStringView str)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvghandler.html#characters

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QSvgHandler::characters(const QStringView str)
    return self.uglySide.call(
        'ritual_ZN11QSvgHandler10charactersE11QStringView', str,
    )

  @overload(str, str)
  def processingInstruction(self, target: str, data: str) -> bool:
    """
    Calls Qt's 'bool QSvgHandler::processingInstruction(const QStringView
    target, const QStringView data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvghandler.html#processingInstruction

    Parameters
    ----------

    target : str
      Passed on as it is: a QString is made of it for the call.

    data : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QSvgHandler::processingInstruction(const QStringView target,
    #      const QStringView data)
    return self.uglySide.call(
        'ritual_ZN11QSvgHandler21processingInstructionE11QStringViewS0_',
        target, data,
    )

  def init(self) -> None:
    """
    Calls Qt's 'void QSvgHandler::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qsvghandler.html#init
    """
    #  void QSvgHandler::init()
    self.uglySide.call('ritual_ZN11QSvgHandler4initEv')

  def parse(self) -> None:
    """
    Calls Qt's 'void QSvgHandler::parse()'.

    Qt's own words: https://doc.qt.io/qt-6/qsvghandler.html#parse
    """
    #  void QSvgHandler::parse()
    self.uglySide.call('ritual_ZN11QSvgHandler5parseEv')

  def resolvePaintServers(self) -> None:
    """
    Calls Qt's 'void QSvgHandler::resolvePaintServers()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvghandler.html#resolvePaintServers
    """
    #  void QSvgHandler::resolvePaintServers()
    self.uglySide.call('ritual_ZN11QSvgHandler19resolvePaintServersEv')

  def resolveNodes(self) -> None:
    """
    Calls Qt's 'void QSvgHandler::resolveNodes()'.

    Qt's own words: https://doc.qt.io/qt-6/qsvghandler.html#resolveNodes
    """
    #  void QSvgHandler::resolveNodes()
    self.uglySide.call('ritual_ZN11QSvgHandler12resolveNodesEv')

  @staticmethod
  def cssHandler(*__, **_) -> Never:
    """
    Qt's 'QSvgCssHandler &QSvgHandler::cssHandler()': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QSvgHandler.cssHandler' has no cute function yet. Qt's "
        "'QSvgCssHandler &QSvgHandler::cssHandler()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def takeDocument(*__, **_) -> Never:
    """
    Qt's 'std::unique_ptr<QSvgDocument> QSvgHandler::takeDocument()': the
    compiler refuses its ritual as it would be written here: invalid
    application of 'sizeof' to an incomplete type 'QSvgDocument'.
    """
    raise NotImplementedError(
        "'QSvgHandler.takeDocument' has no cute function yet. Qt's "
        "'std::unique_ptr<QSvgDocument> QSvgHandler::takeDocument()': the "
        "compiler refuses its ritual as it would be written here: invalid "
        "application of 'sizeof' to an incomplete type 'QSvgDocument'.")
