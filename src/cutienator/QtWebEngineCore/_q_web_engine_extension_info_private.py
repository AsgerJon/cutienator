"""
QWebEngineExtensionInfoPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/6.12.0/QtWebEngineCore/private/qwebengineextensioninfo_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QWebEngineExtensionInfoPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute
from ..QtCore import QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QUrl


class QWebEngineExtensionInfoPrivate(QSharedData):
  """
  The cute side of Qt's QWebEngineExtensionInfoPrivate: a plain Python object
  standing in front of one C++ QWebEngineExtensionInfoPrivate.

  It is built on the cute 'QSharedData', as Qt's
  QWebEngineExtensionInfoPrivate is built on Qt's QSharedData, and has
  everything that class has.

  C++ hands a QWebEngineExtensionInfoPrivate around as a copy, so every C++
  QWebEngineExtensionInfoPrivate behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QWebEngineExtensionInfoPrivate that has a ritual and
  that Python can call so far, 5 names in all: 'name', 'description', 'path',
  'error', 'actionPopupUrl'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QWebEngineExtensionInfoPrivate::QWebEngineExtensionInfoPrivate(const
    ExtensionData &data, QtWebEngineCore::ExtensionManager *manager)': names
    'QtWebEngineCore::ExtensionManager', which has no cute class yet.
  - Qt's 'QWebEngineExtensionInfoPrivate::~QWebEngineExtensionInfoPrivate()':
    the destructor: Python removes its C++ QWebEngineExtensionInfoPrivate by
    it, and has no other use for it.
  - Qt's 'std::string QWebEngineExtensionInfoPrivate::id() const': gives a
    type Python has no way to take yet.

  What has no ritual
  ------------------

  3 of the 11 functions Qt declares: 3 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QWebEngineExtensionInfoPrivate is created at the first use, not
    by 'QWebEngineExtensionInfoPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWebEngineExtensionInfoPrivate back gives a copy the
    ritual made for Python, in a new cute QWebEngineExtensionInfoPrivate.
  - Each name of Qt's QWebEngineExtensionInfoPrivate that has no cute
    function yet, '__init__', 'id', 'isEnabled', 'isInstalled', 'isLoaded',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The classes Qt writes inside QWebEngineExtensionInfoPrivate, each a
  #  class in here as in C++.

  class ExtensionData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QWebEngineExtensionInfoPrivate::ExtensionData: a
    plain Python object standing in front of one C++
    QWebEngineExtensionInfoPrivate::ExtensionData.

    C++ hands a QWebEngineExtensionInfoPrivate::ExtensionData around as a
    copy, so every C++ QWebEngineExtensionInfoPrivate::ExtensionData behind a
    cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QWebEngineExtensionInfoPrivate::ExtensionData yet.
    None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QWebEngineExtensionInfoPrivate::ExtensionData::~ExtensionData()':
      the destructor: Python removes its C++
      QWebEngineExtensionInfoPrivate::ExtensionData by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QWebEngineExtensionInfoPrivate::ExtensionData is created at the
      first use, not by 'QWebEngineExtensionInfoPrivate::ExtensionData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QWebEngineExtensionInfoPrivate::ExtensionData back
      gives a copy the ritual made for Python, in a new cute
      QWebEngineExtensionInfoPrivate::ExtensionData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QWebEngineExtensionInfoPrivate::ExtensionData'

    #  Qt's '~QWebEngineExtensionInfoPrivate::ExtensionData()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QWebEngineExtensionInfoPrivate::ExtensionData behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN30QWebEngineExtensionInfoPrivate13ExtensionDataD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineExtensionInfoPrivate'

  #  Qt's '~QWebEngineExtensionInfoPrivate()'. Naming it makes this a value
  #  class: Python owns every C++ QWebEngineExtensionInfoPrivate behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN30QWebEngineExtensionInfoPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString QWebEngineExtensionInfoPrivate::name() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineextensioninfoprivate.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineExtensionInfoPrivate::name() const
    return self.uglySide.call(
        'ritual_ZNK30QWebEngineExtensionInfoPrivate4nameEv',
    )

  def description(self) -> str:
    """
    Calls Qt's 'QString QWebEngineExtensionInfoPrivate::description() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineextensioninfoprivate.html#description

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineExtensionInfoPrivate::description() const
    return self.uglySide.call(
        'ritual_ZNK30QWebEngineExtensionInfoPrivate11descriptionEv',
    )

  def path(self) -> str:
    """
    Calls Qt's 'QString QWebEngineExtensionInfoPrivate::path() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineextensioninfoprivate.html#path

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineExtensionInfoPrivate::path() const
    return self.uglySide.call(
        'ritual_ZNK30QWebEngineExtensionInfoPrivate4pathEv',
    )

  def error(self) -> str:
    """
    Calls Qt's 'QString QWebEngineExtensionInfoPrivate::error() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineextensioninfoprivate.html#error

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineExtensionInfoPrivate::error() const
    return self.uglySide.call(
        'ritual_ZNK30QWebEngineExtensionInfoPrivate5errorEv',
    )

  def actionPopupUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEngineExtensionInfoPrivate::actionPopupUrl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineextensioninfoprivate.html#actionPopupUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEngineExtensionInfoPrivate::actionPopupUrl() const
    address = self.uglySide.call(
        'ritual_ZNK30QWebEngineExtensionInfoPrivate14actionPopupUrlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

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
    'QWebEngineExtensionInfoPrivate::QWebEngineExtensionInfoPrivate(const
    ExtensionData &data, QtWebEngineCore::ExtensionManager *manager)': names
    'QtWebEngineCore::ExtensionManager', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWebEngineExtensionInfoPrivate.__init__' has no cute function "
        "yet. Qt's "
        "'QWebEngineExtensionInfoPrivate::QWebEngineExtensionInfoPrivate(con"
        "st ExtensionData &data, QtWebEngineCore::ExtensionManager "
        "*manager)': names 'QtWebEngineCore::ExtensionManager', which has "
        "no cute class yet.")

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

  @staticmethod
  def id(*__, **_) -> Never:
    """
    Qt's 'std::string QWebEngineExtensionInfoPrivate::id() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QWebEngineExtensionInfoPrivate.id' has no cute function yet. Qt's "
        "'std::string QWebEngineExtensionInfoPrivate::id() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def isEnabled(*__, **_) -> Never:
    """
    Qt's 'bool QWebEngineExtensionInfoPrivate::isEnabled() const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QtWebEngineCore::ExtensionManager'.
    """
    raise NotImplementedError(
        "'QWebEngineExtensionInfoPrivate.isEnabled' has no cute function "
        "yet. Qt's 'bool QWebEngineExtensionInfoPrivate::isEnabled() "
        "const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QtWebEngineCore::ExtensionManager'.")

  @staticmethod
  def isInstalled(*__, **_) -> Never:
    """
    Qt's 'bool QWebEngineExtensionInfoPrivate::isInstalled() const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QtWebEngineCore::ExtensionManager'.
    """
    raise NotImplementedError(
        "'QWebEngineExtensionInfoPrivate.isInstalled' has no cute function "
        "yet. Qt's 'bool QWebEngineExtensionInfoPrivate::isInstalled() "
        "const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QtWebEngineCore::ExtensionManager'.")

  @staticmethod
  def isLoaded(*__, **_) -> Never:
    """
    Qt's 'bool QWebEngineExtensionInfoPrivate::isLoaded() const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QtWebEngineCore::ExtensionManager'.
    """
    raise NotImplementedError(
        "'QWebEngineExtensionInfoPrivate.isLoaded' has no cute function "
        "yet. Qt's 'bool QWebEngineExtensionInfoPrivate::isLoaded() const': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'QtWebEngineCore::ExtensionManager'.")
