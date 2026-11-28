"""
QQStyleKitTextProperties binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcontrolproperties_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQStyleKitTextProperties to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QQStyleKitPropertyGroup

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QQStyleKitTextProperties(QQStyleKitPropertyGroup):
  """
  The cute side of Qt's QQStyleKitTextProperties: a plain Python object
  standing in front of one C++ QQStyleKitTextProperties.

  It is built on the cute 'QQStyleKitPropertyGroup', as Qt's
  QQStyleKitTextProperties is built on Qt's QQStyleKitPropertyGroup, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQStyleKitTextProperties that has a ritual and that
  Python can call so far, 13 names in all: 'metaObject', 'colorChanged',
  'alignmentChanged', 'boldChanged', 'italicChanged', 'pointSizeChanged',
  'paddingChanged', 'leftPaddingChanged', 'rightPaddingChanged',
  'topPaddingChanged', 'bottomPaddingChanged', 'firstChanged',
  'secondChanged'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQStyleKitTextProperties::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQStyleKitTextProperties::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQStyleKitTextProperties::qt_qmlMarker_uncreatable()': one of
    Qt's own inner workings.

  What has no ritual
  ------------------

  27 of the 43 functions Qt declares: 10 leans on 'void
  QQStyleKitPropertyGroup; 10 leans on 'QQStyleKitDebug; 2 not a gap; 2 leans
  on 'QQStyleKitTextProperties* QQStyleKitPropertyGroup; 1 a template; 1
  leans on 'QQStyleKitTextProperties; 1 leans on 'vtable for
  QQStyleKitTextProperties', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQStyleKitTextProperties is created at the first use, not by
    'QQStyleKitTextProperties(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQStyleKitTextProperties.
  - Qt tells when it has removed the C++ QQStyleKitTextProperties. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQStyleKitTextProperties that has no cute function yet,
    '__init__', 'alignment', 'bold', 'bottomPadding', 'color',
    'emitGlobally', 'first', 'italic', 'leftPadding', 'padding', 'pointSize',
    'rightPadding', 'second', 'setAlignment', 'setBold', 'setBottomPadding',
    'setColor', 'setItalic', 'setLeftPadding', 'setPadding', 'setPointSize',
    'setRightPadding', 'setTopPadding', 'topPadding', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQStyleKitTextProperties'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQStyleKitTextProperties::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekittextproperties.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQStyleKitTextProperties::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QQStyleKitTextProperties10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    Qt's
    'QQStyleKitTextProperties::QQStyleKitTextProperties(QQSK::PropertyGroup
    group, QQStyleKitControlProperties *parent)': leans on 'vtable for
    QQStyleKitTextProperties', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitTextProperties.__init__' has no cute function yet. Qt's "
        "'QQStyleKitTextProperties::QQStyleKitTextProperties(QQSK::PropertyG"
        "roup group, QQStyleKitControlProperties *parent)': leans on "
        "'vtable for QQStyleKitTextProperties', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  def colorChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitTextProperties::colorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekittextproperties.html#colorChanged
    """
    #  void QQStyleKitTextProperties::colorChanged()
    self.uglySide.call('ritual_ZN24QQStyleKitTextProperties12colorChangedEv')

  def alignmentChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitTextProperties::alignmentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekittextproperties.html#alignmentChanged
    """
    #  void QQStyleKitTextProperties::alignmentChanged()
    self.uglySide.call(
        'ritual_ZN24QQStyleKitTextProperties16alignmentChangedEv',
    )

  def boldChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitTextProperties::boldChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekittextproperties.html#boldChanged
    """
    #  void QQStyleKitTextProperties::boldChanged()
    self.uglySide.call('ritual_ZN24QQStyleKitTextProperties11boldChangedEv')

  def italicChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitTextProperties::italicChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekittextproperties.html#italicChanged
    """
    #  void QQStyleKitTextProperties::italicChanged()
    self.uglySide.call(
        'ritual_ZN24QQStyleKitTextProperties13italicChangedEv',
    )

  def pointSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitTextProperties::pointSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekittextproperties.html#pointSizeChanged
    """
    #  void QQStyleKitTextProperties::pointSizeChanged()
    self.uglySide.call(
        'ritual_ZN24QQStyleKitTextProperties16pointSizeChangedEv',
    )

  def paddingChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitTextProperties::paddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekittextproperties.html#paddingChanged
    """
    #  void QQStyleKitTextProperties::paddingChanged()
    self.uglySide.call(
        'ritual_ZN24QQStyleKitTextProperties14paddingChangedEv',
    )

  def leftPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitTextProperties::leftPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekittextproperties.html#leftPaddingChanged
    """
    #  void QQStyleKitTextProperties::leftPaddingChanged()
    self.uglySide.call(
        'ritual_ZN24QQStyleKitTextProperties18leftPaddingChangedEv',
    )

  def rightPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitTextProperties::rightPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekittextproperties.html#rightPaddingChanged
    """
    #  void QQStyleKitTextProperties::rightPaddingChanged()
    self.uglySide.call(
        'ritual_ZN24QQStyleKitTextProperties19rightPaddingChangedEv',
    )

  def topPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitTextProperties::topPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekittextproperties.html#topPaddingChanged
    """
    #  void QQStyleKitTextProperties::topPaddingChanged()
    self.uglySide.call(
        'ritual_ZN24QQStyleKitTextProperties17topPaddingChangedEv',
    )

  def bottomPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitTextProperties::bottomPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekittextproperties.html#bottomPaddingChanged
    """
    #  void QQStyleKitTextProperties::bottomPaddingChanged()
    self.uglySide.call(
        'ritual_ZN24QQStyleKitTextProperties20bottomPaddingChangedEv',
    )

  def firstChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitTextProperties::firstChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekittextproperties.html#firstChanged
    """
    #  void QQStyleKitTextProperties::firstChanged()
    self.uglySide.call('ritual_ZN24QQStyleKitTextProperties12firstChangedEv')

  def secondChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitTextProperties::secondChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekittextproperties.html#secondChanged
    """
    #  void QQStyleKitTextProperties::secondChanged()
    self.uglySide.call(
        'ritual_ZN24QQStyleKitTextProperties13secondChangedEv',
    )

  @staticmethod
  def alignment(*__, **_) -> Never:
    """
    Qt's 'Qt::Alignment QQStyleKitTextProperties::alignment() const': leans
    on 'QQStyleKitDebug::groupBeingRead', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitTextProperties.alignment' has no cute function yet. "
        "Qt's 'Qt::Alignment QQStyleKitTextProperties::alignment() const': "
        "leans on 'QQStyleKitDebug::groupBeingRead', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def bold(*__, **_) -> Never:
    """
    Qt's 'bool QQStyleKitTextProperties::bold() const': leans on
    'QQStyleKitDebug::groupBeingRead', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitTextProperties.bold' has no cute function yet. Qt's "
        "'bool QQStyleKitTextProperties::bold() const': leans on "
        "'QQStyleKitDebug::groupBeingRead', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def bottomPadding(*__, **_) -> Never:
    """
    Qt's 'qreal QQStyleKitTextProperties::bottomPadding() const': leans on
    'QQStyleKitDebug::groupBeingRead', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitTextProperties.bottomPadding' has no cute function yet. "
        "Qt's 'qreal QQStyleKitTextProperties::bottomPadding() const': "
        "leans on 'QQStyleKitDebug::groupBeingRead', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def color(*__, **_) -> Never:
    """
    Qt's 'QColor QQStyleKitTextProperties::color() const': leans on
    'QQStyleKitDebug::groupBeingRead', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitTextProperties.color' has no cute function yet. Qt's "
        "'QColor QQStyleKitTextProperties::color() const': leans on "
        "'QQStyleKitDebug::groupBeingRead', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def emitGlobally(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitTextProperties::emitGlobally': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QQStyleKitTextProperties.emitGlobally' has no cute function yet. "
        "Qt's 'QQStyleKitTextProperties::emitGlobally': a template: a "
        "pattern and no single function.")

  @staticmethod
  def first(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitTextProperties *QQStyleKitTextProperties::first() const':
    leans on 'QQStyleKitTextProperties*
    QQStyleKitPropertyGroup::lazyCreateGroup<QQStyleKitTextProperties>(
    QQStyleKitTextProperties* const&, QQSK::PropertyGroup) const', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitTextProperties.first' has no cute function yet. Qt's "
        "'QQStyleKitTextProperties *QQStyleKitTextProperties::first() "
        "const': leans on 'QQStyleKitTextProperties* "
        "QQStyleKitPropertyGroup::lazyCreateGroup<QQStyleKitTextProperties>("
        "QQStyleKitTextProperties* const&, QQSK::PropertyGroup) const', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def italic(*__, **_) -> Never:
    """
    Qt's 'bool QQStyleKitTextProperties::italic() const': leans on
    'QQStyleKitDebug::groupBeingRead', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitTextProperties.italic' has no cute function yet. Qt's "
        "'bool QQStyleKitTextProperties::italic() const': leans on "
        "'QQStyleKitDebug::groupBeingRead', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def leftPadding(*__, **_) -> Never:
    """
    Qt's 'qreal QQStyleKitTextProperties::leftPadding() const': leans on
    'QQStyleKitDebug::groupBeingRead', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitTextProperties.leftPadding' has no cute function yet. "
        "Qt's 'qreal QQStyleKitTextProperties::leftPadding() const': leans "
        "on 'QQStyleKitDebug::groupBeingRead', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def padding(*__, **_) -> Never:
    """
    Qt's 'qreal QQStyleKitTextProperties::padding() const': leans on
    'QQStyleKitDebug::groupBeingRead', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitTextProperties.padding' has no cute function yet. Qt's "
        "'qreal QQStyleKitTextProperties::padding() const': leans on "
        "'QQStyleKitDebug::groupBeingRead', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def pointSize(*__, **_) -> Never:
    """
    Qt's 'qreal QQStyleKitTextProperties::pointSize() const': leans on
    'QQStyleKitDebug::groupBeingRead', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitTextProperties.pointSize' has no cute function yet. "
        "Qt's 'qreal QQStyleKitTextProperties::pointSize() const': leans on "
        "'QQStyleKitDebug::groupBeingRead', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def rightPadding(*__, **_) -> Never:
    """
    Qt's 'qreal QQStyleKitTextProperties::rightPadding() const': leans on
    'QQStyleKitDebug::groupBeingRead', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitTextProperties.rightPadding' has no cute function yet. "
        "Qt's 'qreal QQStyleKitTextProperties::rightPadding() const': leans "
        "on 'QQStyleKitDebug::groupBeingRead', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def second(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitTextProperties *QQStyleKitTextProperties::second()
    const': leans on 'QQStyleKitTextProperties*
    QQStyleKitPropertyGroup::lazyCreateGroup<QQStyleKitTextProperties>(
    QQStyleKitTextProperties* const&, QQSK::PropertyGroup) const', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitTextProperties.second' has no cute function yet. Qt's "
        "'QQStyleKitTextProperties *QQStyleKitTextProperties::second() "
        "const': leans on 'QQStyleKitTextProperties* "
        "QQStyleKitPropertyGroup::lazyCreateGroup<QQStyleKitTextProperties>("
        "QQStyleKitTextProperties* const&, QQSK::PropertyGroup) const', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setAlignment(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitTextProperties::setAlignment(Qt::Alignment
    alignment)': leans on 'void QQStyleKitPropertyGroup::
    handleStylePropertyChanged<QQStyleKitTextProperties>(void
    (QQStyleKitTextProperties::*)())', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitTextProperties.setAlignment' has no cute function yet. "
        "Qt's 'void QQStyleKitTextProperties::setAlignment(Qt::Alignment "
        "alignment)': leans on 'void "
        "QQStyleKitPropertyGroup::handleStylePropertyChanged<QQStyleKitTextP"
        "roperties>(void (QQStyleKitTextProperties::*)())', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setBold(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitTextProperties::setBold(bool bold)': leans on 'void
    QQStyleKitPropertyGroup::
    handleStylePropertyChanged<QQStyleKitTextProperties>(void
    (QQStyleKitTextProperties::*)())', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitTextProperties.setBold' has no cute function yet. Qt's "
        "'void QQStyleKitTextProperties::setBold(bool bold)': leans on "
        "'void "
        "QQStyleKitPropertyGroup::handleStylePropertyChanged<QQStyleKitTextP"
        "roperties>(void (QQStyleKitTextProperties::*)())', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setBottomPadding(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitTextProperties::setBottomPadding(qreal
    bottomPadding)': leans on 'void QQStyleKitPropertyGroup::
    handleStylePropertyChanged<QQStyleKitTextProperties>(void
    (QQStyleKitTextProperties::*)())', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitTextProperties.setBottomPadding' has no cute function "
        "yet. Qt's 'void QQStyleKitTextProperties::setBottomPadding(qreal "
        "bottomPadding)': leans on 'void "
        "QQStyleKitPropertyGroup::handleStylePropertyChanged<QQStyleKitTextP"
        "roperties>(void (QQStyleKitTextProperties::*)())', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setColor(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitTextProperties::setColor(const QColor &color)':
    leans on 'void QQStyleKitPropertyGroup::
    handleStylePropertyChanged<QQStyleKitTextProperties>(void
    (QQStyleKitTextProperties::*)())', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitTextProperties.setColor' has no cute function yet. Qt's "
        "'void QQStyleKitTextProperties::setColor(const QColor &color)': "
        "leans on 'void "
        "QQStyleKitPropertyGroup::handleStylePropertyChanged<QQStyleKitTextP"
        "roperties>(void (QQStyleKitTextProperties::*)())', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setItalic(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitTextProperties::setItalic(bool italic)': leans on
    'void QQStyleKitPropertyGroup::
    handleStylePropertyChanged<QQStyleKitTextProperties>(void
    (QQStyleKitTextProperties::*)())', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitTextProperties.setItalic' has no cute function yet. "
        "Qt's 'void QQStyleKitTextProperties::setItalic(bool italic)': "
        "leans on 'void "
        "QQStyleKitPropertyGroup::handleStylePropertyChanged<QQStyleKitTextP"
        "roperties>(void (QQStyleKitTextProperties::*)())', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setLeftPadding(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitTextProperties::setLeftPadding(qreal leftPadding)':
    leans on 'void QQStyleKitPropertyGroup::
    handleStylePropertyChanged<QQStyleKitTextProperties>(void
    (QQStyleKitTextProperties::*)())', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitTextProperties.setLeftPadding' has no cute function "
        "yet. Qt's 'void QQStyleKitTextProperties::setLeftPadding(qreal "
        "leftPadding)': leans on 'void "
        "QQStyleKitPropertyGroup::handleStylePropertyChanged<QQStyleKitTextP"
        "roperties>(void (QQStyleKitTextProperties::*)())', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setPadding(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitTextProperties::setPadding(qreal padding)': leans on
    'void QQStyleKitPropertyGroup::
    handleStylePropertiesChanged<QQStyleKitTextProperties, void
    (QQStyleKitTextProperties::*)(), void (QQStyleKitTextProperties::*)(),
    void (QQStyleKitTextProperties::*)(), void
    (QQStyleKitTextProperties::*)(), void
    (QQStyleKitTextProperties::*)()>(void (QQStyleKitTextProperties::*)(),
    void (QQStyleKitTextProperties::*)(), void
    (QQStyleKitTextProperties::*)(), void (QQStyleKitTextProperties::*)(),
    void (QQStyleKitTextProperties::*)())', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitTextProperties.setPadding' has no cute function yet. "
        "Qt's 'void QQStyleKitTextProperties::setPadding(qreal padding)': "
        "leans on 'void "
        "QQStyleKitPropertyGroup::handleStylePropertiesChanged<QQStyleKitTex"
        "tProperties, void (QQStyleKitTextProperties::*)(), void "
        "(QQStyleKitTextProperties::*)(), void "
        "(QQStyleKitTextProperties::*)(), void "
        "(QQStyleKitTextProperties::*)(), void "
        "(QQStyleKitTextProperties::*)()>(void "
        "(QQStyleKitTextProperties::*)(), void "
        "(QQStyleKitTextProperties::*)(), void "
        "(QQStyleKitTextProperties::*)(), void "
        "(QQStyleKitTextProperties::*)(), void "
        "(QQStyleKitTextProperties::*)())', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setPointSize(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitTextProperties::setPointSize(qreal pointSize)':
    leans on 'void QQStyleKitPropertyGroup::
    handleStylePropertyChanged<QQStyleKitTextProperties>(void
    (QQStyleKitTextProperties::*)())', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitTextProperties.setPointSize' has no cute function yet. "
        "Qt's 'void QQStyleKitTextProperties::setPointSize(qreal "
        "pointSize)': leans on 'void "
        "QQStyleKitPropertyGroup::handleStylePropertyChanged<QQStyleKitTextP"
        "roperties>(void (QQStyleKitTextProperties::*)())', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setRightPadding(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitTextProperties::setRightPadding(qreal
    rightPadding)': leans on 'void QQStyleKitPropertyGroup::
    handleStylePropertyChanged<QQStyleKitTextProperties>(void
    (QQStyleKitTextProperties::*)())', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitTextProperties.setRightPadding' has no cute function "
        "yet. Qt's 'void QQStyleKitTextProperties::setRightPadding(qreal "
        "rightPadding)': leans on 'void "
        "QQStyleKitPropertyGroup::handleStylePropertyChanged<QQStyleKitTextP"
        "roperties>(void (QQStyleKitTextProperties::*)())', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setTopPadding(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitTextProperties::setTopPadding(qreal topPadding)':
    leans on 'void QQStyleKitPropertyGroup::
    handleStylePropertyChanged<QQStyleKitTextProperties>(void
    (QQStyleKitTextProperties::*)())', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitTextProperties.setTopPadding' has no cute function yet. "
        "Qt's 'void QQStyleKitTextProperties::setTopPadding(qreal "
        "topPadding)': leans on 'void "
        "QQStyleKitPropertyGroup::handleStylePropertyChanged<QQStyleKitTextP"
        "roperties>(void (QQStyleKitTextProperties::*)())', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def topPadding(*__, **_) -> Never:
    """
    Qt's 'qreal QQStyleKitTextProperties::topPadding() const': leans on
    'QQStyleKitDebug::groupBeingRead', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitTextProperties.topPadding' has no cute function yet. "
        "Qt's 'qreal QQStyleKitTextProperties::topPadding() const': leans "
        "on 'QQStyleKitDebug::groupBeingRead', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
