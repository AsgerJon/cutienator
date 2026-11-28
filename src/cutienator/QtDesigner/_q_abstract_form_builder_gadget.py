"""
QAbstractFormBuilderGadget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/properties_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAbstractFormBuilderGadget to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import Qt, QLocale
from ..QtGui import QFont, QGradient, QPalette
from ..QtWidgets import QSizePolicy, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QAbstractFormBuilderGadget(QWidget):
  """
  The cute side of Qt's QAbstractFormBuilderGadget: a plain Python object
  standing in front of one C++ QAbstractFormBuilderGadget.

  It is built on the cute 'QWidget', as Qt's QAbstractFormBuilderGadget is
  built on Qt's QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractFormBuilderGadget that has a ritual and
  that Python can call so far, 19 names in all: 'metaObject',
  'fakeOrientation', 'fakeSizeType', 'fakeColorGroup', 'fakeColorRole',
  'fakeStyleStrategy', 'fakeHintingPreference', 'fakeFontWeight',
  'fakeCursorShape', 'fakeBrushStyle', 'fakeToolBarArea', 'fakeGradientType',
  'fakeGradientSpread', 'fakeGradientCoordinate', 'fakeLanguage',
  'fakeCountry', 'fakeItemFlags', 'fakeCheckState', 'fakeAlignment'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstractFormBuilderGadget::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QAbstractFormBuilderGadget::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  4 of the 25 functions Qt declares: 2 not a gap; 2 leans on
  'QAbstractFormBuilderGadget.

  What to expect
  --------------

  - The C++ QAbstractFormBuilderGadget is created at the first use, not by
    'QAbstractFormBuilderGadget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractFormBuilderGadget.
  - Qt tells when it has removed the C++ QAbstractFormBuilderGadget. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QAbstractFormBuilderGadget that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractFormBuilderGadget'

  #  A C++ QAbstractFormBuilderGadget Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractFormBuilderGadget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAbstractFormBuilderGadget::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuildergadget.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractFormBuilderGadget::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QAbstractFormBuilderGadget10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def fakeOrientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QAbstractFormBuilderGadget::fakeOrientation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuildergadget.html#fakeOrientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QAbstractFormBuilderGadget::fakeOrientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK26QAbstractFormBuilderGadget15fakeOrientationEv',
    ))

  def fakeSizeType(self) -> QSizePolicy.Policy:
    """
    Calls Qt's 'QSizePolicy::Policy
    QAbstractFormBuilderGadget::fakeSizeType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuildergadget.html#fakeSizeType

    Returns
    -------

    QSizePolicy.Policy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSizePolicy.Policy(number)' gives.
    """
    #  QSizePolicy::Policy QAbstractFormBuilderGadget::fakeSizeType() const
    return QSizePolicy.Policy(self.uglySide.call(
        'ritual_ZNK26QAbstractFormBuilderGadget12fakeSizeTypeEv',
    ))

  def fakeColorGroup(self) -> QPalette.ColorGroup:
    """
    Calls Qt's 'QPalette::ColorGroup
    QAbstractFormBuilderGadget::fakeColorGroup() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuildergadget.html#fakeColorGroup

    Returns
    -------

    QPalette.ColorGroup
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPalette.ColorGroup(number)' gives.
    """
    #  QPalette::ColorGroup QAbstractFormBuilderGadget::fakeColorGroup()
    #      const
    return QPalette.ColorGroup(self.uglySide.call(
        'ritual_ZNK26QAbstractFormBuilderGadget14fakeColorGroupEv',
    ))

  def fakeColorRole(self) -> QPalette.ColorRole:
    """
    Calls Qt's 'QPalette::ColorRole
    QAbstractFormBuilderGadget::fakeColorRole() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuildergadget.html#fakeColorRole

    Returns
    -------

    QPalette.ColorRole
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPalette.ColorRole(number)' gives.
    """
    #  QPalette::ColorRole QAbstractFormBuilderGadget::fakeColorRole() const
    return QPalette.ColorRole(self.uglySide.call(
        'ritual_ZNK26QAbstractFormBuilderGadget13fakeColorRoleEv',
    ))

  def fakeStyleStrategy(self) -> QFont.StyleStrategy:
    """
    Calls Qt's 'QFont::StyleStrategy
    QAbstractFormBuilderGadget::fakeStyleStrategy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuildergadget.html#fakeStyleStrategy

    Returns
    -------

    QFont.StyleStrategy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QFont.StyleStrategy(number)' gives.
    """
    #  QFont::StyleStrategy QAbstractFormBuilderGadget::fakeStyleStrategy()
    #      const
    return QFont.StyleStrategy(self.uglySide.call(
        'ritual_ZNK26QAbstractFormBuilderGadget17fakeStyleStrategyEv',
    ))

  def fakeHintingPreference(self) -> QFont.HintingPreference:
    """
    Calls Qt's 'QFont::HintingPreference
    QAbstractFormBuilderGadget::fakeHintingPreference() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuildergadget.html

    Returns
    -------

    QFont.HintingPreference
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QFont.HintingPreference(number)' gives.
    """
    #  QFont::HintingPreference
    #      QAbstractFormBuilderGadget::fakeHintingPreference() const
    return QFont.HintingPreference(self.uglySide.call(
        'ritual_ZNK26QAbstractFormBuilderGadget21fakeHintingPreferenceEv',
    ))

  def fakeFontWeight(self) -> QFont.Weight:
    """
    Calls Qt's 'QFont::Weight QAbstractFormBuilderGadget::fakeFontWeight()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuildergadget.html#fakeFontWeight

    Returns
    -------

    QFont.Weight
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QFont.Weight(number)'
      gives.
    """
    #  QFont::Weight QAbstractFormBuilderGadget::fakeFontWeight() const
    return QFont.Weight(self.uglySide.call(
        'ritual_ZNK26QAbstractFormBuilderGadget14fakeFontWeightEv',
    ))

  def fakeCursorShape(self) -> Qt.CursorShape:
    """
    Calls Qt's 'Qt::CursorShape QAbstractFormBuilderGadget::fakeCursorShape()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuildergadget.html#fakeCursorShape

    Returns
    -------

    Qt.CursorShape
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.CursorShape(number)'
      gives.
    """
    #  Qt::CursorShape QAbstractFormBuilderGadget::fakeCursorShape() const
    return Qt.CursorShape(self.uglySide.call(
        'ritual_ZNK26QAbstractFormBuilderGadget15fakeCursorShapeEv',
    ))

  def fakeBrushStyle(self) -> Qt.BrushStyle:
    """
    Calls Qt's 'Qt::BrushStyle QAbstractFormBuilderGadget::fakeBrushStyle()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuildergadget.html#fakeBrushStyle

    Returns
    -------

    Qt.BrushStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.BrushStyle(number)'
      gives.
    """
    #  Qt::BrushStyle QAbstractFormBuilderGadget::fakeBrushStyle() const
    return Qt.BrushStyle(self.uglySide.call(
        'ritual_ZNK26QAbstractFormBuilderGadget14fakeBrushStyleEv',
    ))

  def fakeToolBarArea(self) -> Qt.ToolBarArea:
    """
    Calls Qt's 'Qt::ToolBarArea QAbstractFormBuilderGadget::fakeToolBarArea()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuildergadget.html#fakeToolBarArea

    Returns
    -------

    Qt.ToolBarArea
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.ToolBarArea(number)'
      gives.
    """
    #  Qt::ToolBarArea QAbstractFormBuilderGadget::fakeToolBarArea() const
    return Qt.ToolBarArea(self.uglySide.call(
        'ritual_ZNK26QAbstractFormBuilderGadget15fakeToolBarAreaEv',
    ))

  def fakeGradientType(self) -> QGradient.Type:
    """
    Calls Qt's 'QGradient::Type
    QAbstractFormBuilderGadget::fakeGradientType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuildergadget.html#fakeGradientType

    Returns
    -------

    QGradient.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QGradient.Type(number)'
      gives.
    """
    #  QGradient::Type QAbstractFormBuilderGadget::fakeGradientType() const
    return QGradient.Type(self.uglySide.call(
        'ritual_ZNK26QAbstractFormBuilderGadget16fakeGradientTypeEv',
    ))

  def fakeGradientSpread(self) -> QGradient.Spread:
    """
    Calls Qt's 'QGradient::Spread
    QAbstractFormBuilderGadget::fakeGradientSpread() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuildergadget.html#fakeGradientSpread

    Returns
    -------

    QGradient.Spread
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QGradient.Spread(number)'
      gives.
    """
    #  QGradient::Spread QAbstractFormBuilderGadget::fakeGradientSpread()
    #      const
    return QGradient.Spread(self.uglySide.call(
        'ritual_ZNK26QAbstractFormBuilderGadget18fakeGradientSpreadEv',
    ))

  def fakeGradientCoordinate(self) -> QGradient.CoordinateMode:
    """
    Calls Qt's 'QGradient::CoordinateMode
    QAbstractFormBuilderGadget::fakeGradientCoordinate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuildergadget.html

    Returns
    -------

    QGradient.CoordinateMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QGradient.CoordinateMode(number)' gives.
    """
    #  QGradient::CoordinateMode
    #      QAbstractFormBuilderGadget::fakeGradientCoordinate() const
    return QGradient.CoordinateMode(self.uglySide.call(
        'ritual_ZNK26QAbstractFormBuilderGadget22fakeGradientCoordinateEv',
    ))

  def fakeLanguage(self) -> QLocale.Language:
    """
    Calls Qt's 'QLocale::Language QAbstractFormBuilderGadget::fakeLanguage()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuildergadget.html#fakeLanguage

    Returns
    -------

    QLocale.Language
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QLocale.Language(number)'
      gives.
    """
    #  QLocale::Language QAbstractFormBuilderGadget::fakeLanguage() const
    return QLocale.Language(self.uglySide.call(
        'ritual_ZNK26QAbstractFormBuilderGadget12fakeLanguageEv',
    ))

  def fakeCountry(self) -> QLocale.Country:
    """
    Calls Qt's 'QLocale::Country QAbstractFormBuilderGadget::fakeCountry()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuildergadget.html#fakeCountry

    Returns
    -------

    QLocale.Country
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QLocale.Country(number)'
      gives.
    """
    #  QLocale::Country QAbstractFormBuilderGadget::fakeCountry() const
    return QLocale.Country(self.uglySide.call(
        'ritual_ZNK26QAbstractFormBuilderGadget11fakeCountryEv',
    ))

  def fakeItemFlags(self) -> Qt.ItemFlags:
    """
    Calls Qt's 'Qt::ItemFlags QAbstractFormBuilderGadget::fakeItemFlags()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuildergadget.html#fakeItemFlags

    Returns
    -------

    Qt.ItemFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::ItemFlags QAbstractFormBuilderGadget::fakeItemFlags() const
    return Qt.ItemFlags(self.uglySide.call(
        'ritual_ZNK26QAbstractFormBuilderGadget13fakeItemFlagsEv',
    ))

  def fakeCheckState(self) -> Qt.CheckState:
    """
    Calls Qt's 'Qt::CheckState QAbstractFormBuilderGadget::fakeCheckState()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuildergadget.html#fakeCheckState

    Returns
    -------

    Qt.CheckState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.CheckState(number)'
      gives.
    """
    #  Qt::CheckState QAbstractFormBuilderGadget::fakeCheckState() const
    return Qt.CheckState(self.uglySide.call(
        'ritual_ZNK26QAbstractFormBuilderGadget14fakeCheckStateEv',
    ))

  def fakeAlignment(self) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QAbstractFormBuilderGadget::fakeAlignment()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractformbuildergadget.html#fakeAlignment

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QAbstractFormBuilderGadget::fakeAlignment() const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK26QAbstractFormBuilderGadget13fakeAlignmentEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Qt's 'QAbstractFormBuilderGadget::QAbstractFormBuilderGadget()': leans on
    'QAbstractFormBuilderGadget::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QAbstractFormBuilderGadget.__init__' has no cute function yet. "
        "Qt's 'QAbstractFormBuilderGadget::QAbstractFormBuilderGadget()': "
        "leans on "
        "'QAbstractFormBuilderGadget::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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
