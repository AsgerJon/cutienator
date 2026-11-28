"""
QDesignerCustomWidgetData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/pluginmanager_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QDesignerCustomWidgetData to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QString
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QString = WAIT['QString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerCustomWidgetData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDesignerCustomWidgetData: a plain Python object
  standing in front of one C++ QDesignerCustomWidgetData.

  C++ hands a QDesignerCustomWidgetData around as a copy, so every C++
  QDesignerCustomWidgetData behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDesignerCustomWidgetData that has a ritual and that
  Python can call so far, 9 names in all: 'parseXml', 'isNull', 'pluginPath',
  'xmlClassName', 'xmlLanguage', 'xmlAddPageMethod', 'xmlExtends',
  'xmlDisplayName', 'propertyToolTip'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDesignerCustomWidgetData
    &QDesignerCustomWidgetData::operator=(const QDesignerCustomWidgetData
    &a0)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QDesignerCustomWidgetData::~QDesignerCustomWidgetData()': the
    destructor: Python removes its C++ QDesignerCustomWidgetData by it, and
    has no other use for it.
  - Qt's 'bool QDesignerCustomWidgetData::xmlStringPropertyType(const QString
    &name, StringPropertyType *type) const': names
    'QDesignerCustomWidgetData::StringPropertyType', which has no cute class
    yet.

  What to expect
  --------------

  - The C++ QDesignerCustomWidgetData is created at the first use, not by
    'QDesignerCustomWidgetData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDesignerCustomWidgetData back gives a copy the
    ritual made for Python, in a new cute QDesignerCustomWidgetData.
  - Each name of Qt's QDesignerCustomWidgetData that has no cute function
    yet, 'xmlStringPropertyType', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QDesignerCustomWidgetData, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class ParseResult(CuteNum):
    """
    The enum 'QDesignerCustomWidgetData::ParseResult' of Qt, with the 3 names
    Qt gives in it.
    """

    ParseOk = Kee[int](0)
    ParseWarning = Kee[int](1)
    ParseError = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerCustomWidgetData'

  #  Qt's '~QDesignerCustomWidgetData()'. Naming it makes this a value class:
  #  Python owns every C++ QDesignerCustomWidgetData behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QDesignerCustomWidgetDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QDesignerCustomWidgetData::isNull() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignercustomwidgetdata.html#isNull
    """
    #  bool QDesignerCustomWidgetData::isNull() const
    return self.uglySide.call(
        'ritual_ZNK25QDesignerCustomWidgetData6isNullEv',
    )

  def pluginPath(self) -> str:
    """
    Calls Qt's 'QString QDesignerCustomWidgetData::pluginPath() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignercustomwidgetdata.html#pluginPath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerCustomWidgetData::pluginPath() const
    return self.uglySide.call(
        'ritual_ZNK25QDesignerCustomWidgetData10pluginPathEv',
    )

  def xmlClassName(self) -> str:
    """
    Calls Qt's 'QString QDesignerCustomWidgetData::xmlClassName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignercustomwidgetdata.html#xmlClassName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerCustomWidgetData::xmlClassName() const
    return self.uglySide.call(
        'ritual_ZNK25QDesignerCustomWidgetData12xmlClassNameEv',
    )

  def xmlLanguage(self) -> str:
    """
    Calls Qt's 'QString QDesignerCustomWidgetData::xmlLanguage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignercustomwidgetdata.html#xmlLanguage

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerCustomWidgetData::xmlLanguage() const
    return self.uglySide.call(
        'ritual_ZNK25QDesignerCustomWidgetData11xmlLanguageEv',
    )

  def xmlAddPageMethod(self) -> str:
    """
    Calls Qt's 'QString QDesignerCustomWidgetData::xmlAddPageMethod() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignercustomwidgetdata.html#xmlAddPageMethod

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerCustomWidgetData::xmlAddPageMethod() const
    return self.uglySide.call(
        'ritual_ZNK25QDesignerCustomWidgetData16xmlAddPageMethodEv',
    )

  def xmlExtends(self) -> str:
    """
    Calls Qt's 'QString QDesignerCustomWidgetData::xmlExtends() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignercustomwidgetdata.html#xmlExtends

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerCustomWidgetData::xmlExtends() const
    return self.uglySide.call(
        'ritual_ZNK25QDesignerCustomWidgetData10xmlExtendsEv',
    )

  def xmlDisplayName(self) -> str:
    """
    Calls Qt's 'QString QDesignerCustomWidgetData::xmlDisplayName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignercustomwidgetdata.html#xmlDisplayName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerCustomWidgetData::xmlDisplayName() const
    return self.uglySide.call(
        'ritual_ZNK25QDesignerCustomWidgetData14xmlDisplayNameEv',
    )

  @overload(str)
  def propertyToolTip(self, name: str) -> str:
    """
    Calls Qt's 'QString QDesignerCustomWidgetData::propertyToolTip(const
    QString &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignercustomwidgetdata.html#propertyToolTip

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerCustomWidgetData::propertyToolTip(const QString
    #      &name) const
    return self.uglySide.call(
        'ritual_ZNK25QDesignerCustomWidgetData15propertyToolTipERK7QString',
        name,
    )

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
  @overload(str)
  def __init__(self, pluginPath: str = '') -> None:
    """
    Notes what was given, for Qt's
    'QDesignerCustomWidgetData::QDesignerCustomWidgetData(const QString
    &pluginPath)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignercustomwidgetdata.html

    Parameters
    ----------

    pluginPath : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  QDesignerCustomWidgetData::QDesignerCustomWidgetData(const QString
    #      &pluginPath)
    self._noteCreation(QDesignerCustomWidgetData, lambda: Rituals.call(
        'ritual_ZN25QDesignerCustomWidgetDataC1ERK7QString', pluginPath,
    ))

  @overload(THIS)
  def __init__(self, a0: QDesignerCustomWidgetData) -> None:
    """
    Notes what was given, for Qt's
    'QDesignerCustomWidgetData::QDesignerCustomWidgetData(const
    QDesignerCustomWidgetData &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignercustomwidgetdata.html

    Parameters
    ----------

    a0 : QDesignerCustomWidgetData
      Passed on as a value: Qt reads the C++ QDesignerCustomWidgetData, which
      stays Python's own.
    """
    #  QDesignerCustomWidgetData::QDesignerCustomWidgetData(const
    #      QDesignerCustomWidgetData &a0)
    self._noteCreation(QDesignerCustomWidgetData, lambda: Rituals.call(
        'ritual_ZN25QDesignerCustomWidgetDataC1ERKS_', self._valueOf(a0),
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

  @overload(str, str, QString)
  @overload(str, str, NoneType)
  def parseXml(
      self,
      xml: str,
      name: str,
      errorMessage: Optional[QString],
  ) -> ParseResult:
    """
    Calls Qt's 'ParseResult QDesignerCustomWidgetData::parseXml(const QString
    &xml, const QString &name, QString *errorMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignercustomwidgetdata.html#parseXml

    Parameters
    ----------

    xml : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    ParseResult
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ParseResult(number)'
      gives.
    """
    #  ParseResult QDesignerCustomWidgetData::parseXml(const QString &xml,
    #      const QString &name, QString *errorMessage)
    return QDesignerCustomWidgetData.ParseResult(self.uglySide.call(
        'ritual_ZN25QDesignerCustomWidgetData8parseXmlERK7QStringS2_PS0_',
        xml, name, self._addressOf(errorMessage),
    ))

  @staticmethod
  def xmlStringPropertyType(*__, **_) -> Never:
    """
    Qt's 'bool QDesignerCustomWidgetData::xmlStringPropertyType(const QString
    &name, StringPropertyType *type) const': names
    'QDesignerCustomWidgetData::StringPropertyType', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QDesignerCustomWidgetData.xmlStringPropertyType' has no cute "
        "function yet. Qt's 'bool "
        "QDesignerCustomWidgetData::xmlStringPropertyType(const QString "
        "&name, StringPropertyType *type) const': names "
        "'QDesignerCustomWidgetData::StringPropertyType', which has no cute "
        "class yet.")
