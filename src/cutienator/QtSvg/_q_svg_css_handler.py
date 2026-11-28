"""
QSvgCssHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgcsshandler_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSvgCssHandler to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtGui import QCss
from . import QSvgCssValues

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QSvgCssAnimation


class QSvgCssHandler(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSvgCssHandler: a plain Python object standing in
  front of one C++ QSvgCssHandler.

  C++ hands a QSvgCssHandler around as a copy, so every C++ QSvgCssHandler
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSvgCssHandler that has a ritual and that Python can
  call so far, 4 names in all: 'createAnimation', 'collectAnimations',
  'parseStyleSheet', 'parseDecltoString'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgCssHandler::~QSvgCssHandler()': the destructor: Python removes
    its C++ QSvgCssHandler by it, and has no other use for it.
  - Qt's 'QSvgCssEasingPtr
    QSvgCssHandler::createEasing(QSvgCssValues::EasingFunction
    easingFunction, const QSvgCssValues::EasingValues &values)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QSvgCssHandler::parseCSStoXMLAttrs(const
    QList<QCss::Declaration> &declarations, QXmlStreamAttributes &attributes)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'void QSvgCssHandler::parseCSStoXMLAttrs(const QString &css,
    QXmlStreamAttributes &attributes) const': takes a type Python has no way
    to hand over yet.
  - Qt's 'void QSvgCssHandler::styleLookup(QSvgNode *node,
    QXmlStreamAttributes &attributes) const': takes a type Python has no way
    to hand over yet.
  - Qt's 'QSvgCssEasingPtr
    QSvgCssHandler::createEasingFromKeyword(QSvgCssValues::EasingFunction
    easingFunction)': gives a type Python has no way to take yet.
  - Qt's 'QSvgCssEasingPtr QSvgCssHandler::createStepsEasing(const
    QSvgCssValues::StepValues &values)': gives a type Python has no way to
    take yet.

  What to expect
  --------------

  - The C++ QSvgCssHandler is created at the first use, not by
    'QSvgCssHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSvgCssHandler back gives a copy the ritual made for
    Python, in a new cute QSvgCssHandler.
  - Each name of Qt's QSvgCssHandler that has no cute function yet,
    'createEasing', 'createEasingFromKeyword', 'createStepsEasing',
    'parseCSStoXMLAttrs', 'styleLookup', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QCss.Declaration'])
  def parseDecltoString(decl: QCss.Declaration) -> str:
    """
    Calls Qt's 'QString QSvgCssHandler::parseDecltoString(const
    QCss::Declaration &decl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgcsshandler.html#parseDecltoString

    Parameters
    ----------

    decl : QCss.Declaration
      Passed on as a value: Qt reads the C++ QCss::Declaration, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSvgCssHandler::parseDecltoString(const QCss::Declaration
    #      &decl)
    return Rituals.call(
        'ritual_ZN14QSvgCssHandler17parseDecltoStringERKN4QCss11Declaration'
        'E',
        CuteMixin._valueOf(decl),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgCssHandler'

  #  Qt's '~QSvgCssHandler()'. Naming it makes this a value class: Python
  #  owns every C++ QSvgCssHandler behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QSvgCssHandlerD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QSvgCssHandler::QSvgCssHandler()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvgcsshandler.html#QSvgCssHandler
    """
    #  QSvgCssHandler::QSvgCssHandler()
    self._noteCreation(QSvgCssHandler, lambda: Rituals.call(
        'ritual_ZN14QSvgCssHandlerC1Ev',
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
  def createAnimation(self, name: str) -> Optional[QSvgCssAnimation]:
    """
    Calls Qt's 'QSvgCssAnimation *QSvgCssHandler::createAnimation(QStringView
    name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgcsshandler.html#createAnimation

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QSvgCssAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSvgCssAnimation *QSvgCssHandler::createAnimation(QStringView name)
    address = self.uglySide.call(
        'ritual_ZN14QSvgCssHandler15createAnimationE11QStringView', name,
    )
    from . import QSvgCssAnimation
    return QSvgCssAnimation._cuteAt(address)

  @overload(WAIT['QCss.StyleSheet'])
  def collectAnimations(self, sheet: QCss.StyleSheet) -> None:
    """
    Calls Qt's 'void QSvgCssHandler::collectAnimations(const QCss::StyleSheet
    &sheet)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgcsshandler.html#collectAnimations

    Parameters
    ----------

    sheet : QCss.StyleSheet
      Passed on as a value: Qt reads the C++ QCss::StyleSheet, which stays
      Python's own.
    """
    #  void QSvgCssHandler::collectAnimations(const QCss::StyleSheet &sheet)
    self.uglySide.call(
        'ritual_ZN14QSvgCssHandler17collectAnimationsERKN4QCss10StyleSheetE',
        self._valueOf(sheet),
    )

  @overload(str)
  def parseStyleSheet(self, str: str) -> None:
    """
    Calls Qt's 'void QSvgCssHandler::parseStyleSheet(const QStringView str)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgcsshandler.html#parseStyleSheet

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSvgCssHandler::parseStyleSheet(const QStringView str)
    self.uglySide.call(
        'ritual_ZN14QSvgCssHandler15parseStyleSheetE11QStringView', str,
    )

  @staticmethod
  def createEasing(*__, **_) -> Never:
    """
    Qt's 'QSvgCssEasingPtr
    QSvgCssHandler::createEasing(QSvgCssValues::EasingFunction
    easingFunction, const QSvgCssValues::EasingValues &values)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgCssHandler.createEasing' has no cute function yet. Qt's "
        "'QSvgCssEasingPtr "
        "QSvgCssHandler::createEasing(QSvgCssValues::EasingFunction "
        "easingFunction, const QSvgCssValues::EasingValues &values)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def createEasingFromKeyword(*__, **_) -> Never:
    """
    Qt's 'QSvgCssEasingPtr
    QSvgCssHandler::createEasingFromKeyword(QSvgCssValues::EasingFunction
    easingFunction)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSvgCssHandler.createEasingFromKeyword' has no cute function yet. "
        "Qt's 'QSvgCssEasingPtr "
        "QSvgCssHandler::createEasingFromKeyword(QSvgCssValues::EasingFuncti"
        "on easingFunction)': gives a type Python has no way to take yet.")

  @staticmethod
  def createStepsEasing(*__, **_) -> Never:
    """
    Qt's 'QSvgCssEasingPtr QSvgCssHandler::createStepsEasing(const
    QSvgCssValues::StepValues &values)': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QSvgCssHandler.createStepsEasing' has no cute function yet. Qt's "
        "'QSvgCssEasingPtr QSvgCssHandler::createStepsEasing(const "
        "QSvgCssValues::StepValues &values)': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def parseCSStoXMLAttrs(*__, **_) -> Never:
    """
    - Qt's 'void QSvgCssHandler::parseCSStoXMLAttrs(const
      QList<QCss::Declaration> &declarations, QXmlStreamAttributes
      &attributes) const': takes a type Python has no way to hand over yet.
    - Qt's 'void QSvgCssHandler::parseCSStoXMLAttrs(const QString &css,
      QXmlStreamAttributes &attributes) const': takes a type Python has no
      way to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgCssHandler.parseCSStoXMLAttrs' has no cute function yet. Qt's "
        "'void QSvgCssHandler::parseCSStoXMLAttrs(const "
        "QList<QCss::Declaration> &declarations, QXmlStreamAttributes "
        "&attributes) const': takes a type Python has no way to hand over "
        "yet. Qt's 'void QSvgCssHandler::parseCSStoXMLAttrs(const QString "
        "&css, QXmlStreamAttributes &attributes) const': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def styleLookup(*__, **_) -> Never:
    """
    Qt's 'void QSvgCssHandler::styleLookup(QSvgNode *node,
    QXmlStreamAttributes &attributes) const': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgCssHandler.styleLookup' has no cute function yet. Qt's 'void "
        "QSvgCssHandler::styleLookup(QSvgNode *node, QXmlStreamAttributes "
        "&attributes) const': takes a type Python has no way to hand over "
        "yet.")
