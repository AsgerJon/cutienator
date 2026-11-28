"""
QWebViewSettings binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebView/qwebviewsettings.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QWebViewSettings(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebViewSettings: a plain Python object standing in
  front of one C++ QWebViewSettings.

  What exists
  -----------

  Every function of Qt's QWebViewSettings that has a ritual and that Python
  can call so far, 4 names in all: 'testAttribute', 'setAttribute',
  'doSetAttribute', 'doTestAttribute'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWebViewSettings::~QWebViewSettings()': the destructor: Python
    never removes a C++ QWebViewSettings.

  What has no ritual
  ------------------

  8 of the 13 functions Qt declares: 4 forbidden; 3 not a gap; 1 the class is
  abstract, so C++ cannot make one, and the C++ class of ours does not fill
  in every function it leaves open.

  What to expect
  --------------

  - The C++ QWebViewSettings is created at the first use, not by
    'QWebViewSettings(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebViewSettings.
  - Each name of Qt's QWebViewSettings that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QWebViewSettings, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class WebAttribute(CuteNum, scoped=True):
    """
    The enum 'QWebViewSettings::WebAttribute' of Qt, with the 4 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    LocalStorageEnabled = Kee[int](0)
    JavaScriptEnabled = Kee[int](1)
    AllowFileAccess = Kee[int](2)
    LocalContentCanAccessFileUrls = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebViewSettings'

  #  The functions Qt calls itself that QWebViewSettings is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'doSetAttribute': (
          ('_ZN16QWebViewSettings14doSetAttributeENS_12WebAttributeEb',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtWebView:QWebViewSettings.WebAttribute'),
               ('bool', 'number', ''),
           )),
      ),
      'doTestAttribute': (
          ('_ZNK16QWebViewSettings15doTestAttributeENS_12WebAttributeE',
           ('bool', 'number', ''),
           (
               ('int', 'enum', 'QtWebView:QWebViewSettings.WebAttribute'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WebAttribute)
  def testAttribute(self, attribute: WebAttribute) -> bool:
    """
    Calls Qt's 'bool QWebViewSettings::testAttribute(WebAttribute attribute)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebviewsettings.html#testAttribute

    Parameters
    ----------

    attribute : WebAttribute
      Passed on as its number.
    """
    #  bool QWebViewSettings::testAttribute(WebAttribute attribute) const
    return self.uglySide.call(
        'ritual_ZNK16QWebViewSettings13testAttributeENS_12WebAttributeE',
        attribute.value,
    )

  @overload(WebAttribute)
  def doTestAttribute(self, a: WebAttribute) -> bool:
    """
    Calls Qt's 'bool QWebViewSettings::doTestAttribute(WebAttribute a)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebviewsettings.html#doTestAttribute

    Parameters
    ----------

    a : WebAttribute
      Passed on as its number.
    """
    #  bool QWebViewSettings::doTestAttribute(WebAttribute a) const
    return self.uglySide.call(
        'ritual_ZNK16QWebViewSettings15doTestAttributeENS_12WebAttributeE',
        a.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WebAttribute, bool)
  def setAttribute(self, attribute: WebAttribute, value: bool) -> None:
    """
    Calls Qt's 'void QWebViewSettings::setAttribute(WebAttribute attribute,
    bool value)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebviewsettings.html#setAttribute

    Parameters
    ----------

    attribute : WebAttribute
      Passed on as its number.

    value : bool
      Passed on as it is.
    """
    #  void QWebViewSettings::setAttribute(WebAttribute attribute, bool
    #      value)
    self.uglySide.call(
        'ritual_ZN16QWebViewSettings12setAttributeENS_12WebAttributeEb',
        attribute.value, value,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QWebViewSettings::QWebViewSettings()': the class is abstract, so
    C++ cannot make one, and the C++ class of ours does not fill in every
    function it leaves open.
    """
    raise NotImplementedError(
        "'QWebViewSettings.__init__' has no cute function yet. Qt's "
        "'QWebViewSettings::QWebViewSettings()': the class is abstract, so "
        "C++ cannot make one, and the C++ class of ours does not fill in "
        "every function it leaves open.")

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

  @overload(WebAttribute, bool)
  def doSetAttribute(self, a: WebAttribute, v: bool) -> None:
    """
    Calls Qt's 'void QWebViewSettings::doSetAttribute(WebAttribute a, bool
    v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebviewsettings.html#doSetAttribute

    Parameters
    ----------

    a : WebAttribute
      Passed on as its number.

    v : bool
      Passed on as it is.
    """
    #  void QWebViewSettings::doSetAttribute(WebAttribute a, bool v)
    self.uglySide.call(
        'ritual_ZN16QWebViewSettings14doSetAttributeENS_12WebAttributeEb',
        a.value, v,
    )
