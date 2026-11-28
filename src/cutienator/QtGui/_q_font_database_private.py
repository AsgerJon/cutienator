"""
QFontDatabasePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qfontdatabase_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QFontDatabasePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from . import QtFontStyle

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
  from . import QFontDef, QFontEngine, QFontPrivate, QtFontFamily
  from . import QtFontFoundry, QtFontSize
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QFontDef = WAIT['QFontDef']
  QFontPrivate = WAIT['QFontPrivate']
  QtFontFamily = WAIT['QtFontFamily']
  QtFontFoundry = WAIT['QtFontFoundry']
  QtFontSize = WAIT['QtFontSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFontDatabasePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QFontDatabasePrivate: a plain Python object standing
  in front of one C++ QFontDatabasePrivate.

  What exists
  -----------

  Every function of Qt's QFontDatabasePrivate that has a ritual and that
  Python can call so far, 16 names in all: 'clearFamilies', 'family',
  'addAppFont', 'isApplicationFont', 'setApplicationFallbackFontFamilies',
  'applicationFallbackFontFamilies', 'removeApplicationFallbackFontFamily',
  'addApplicationFallbackFontFamily', 'instance', 'resolveFontFamilyAlias',
  'findFont', 'load', 'ensureFontDatabase', 'invalidate', 'loadSingleEngine',
  'loadEngine'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFontDatabasePrivate::~QFontDatabasePrivate()': the destructor:
    Python never removes a C++ QFontDatabasePrivate.
  - Qt's 'void QFontDatabasePrivate::parseFontName(const QString &name,
    QString &foundry, QString &family)': takes a type Python has no way to
    hand over yet.
  - Qt's 'int QFontDatabasePrivate::match(int script, const QFontDef
    &request, const QString &family_name, const QString &foundry_name,
    QtFontDesc *desc, const QList<int> &blacklistedFamilies, unsigned int
    *resultingScore)': names 'QtFontDesc', which has no cute class yet.
  - Qt's 'unsigned int QFontDatabasePrivate::bestFoundry(int script, unsigned
    int score, int styleStrategy, const QtFontFamily *family, const QString
    &foundry_name, QtFontStyle::Key styleKey, int pixelSize, char pitch,
    QtFontDesc *desc, const QString &styleName)': takes a single letter as C
    has it.

  What to expect
  --------------

  - The C++ QFontDatabasePrivate is created at the first use, not by
    'QFontDatabasePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFontDatabasePrivate.
  - Each name of Qt's QFontDatabasePrivate that has no cute function yet,
    'bestFoundry', 'match', 'parseFontName', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QFontDatabasePrivate, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class ExtendedScript(CuteNum):
    """
    The enum 'QFontDatabasePrivate::ExtendedScript' of Qt, with the 4 names
    Qt gives in it.
    """

    Script_Common = Kee[int](2)
    Script_Latin = Kee[int](3)
    Script_Emoji = Kee[int](175)
    ScriptCount = Kee[int](176)

  class FamilyRequestFlags(CuteNum):
    """
    The enum 'QFontDatabasePrivate::FamilyRequestFlags' of Qt, with the 3
    names Qt gives in it.
    """

    RequestFamily = Kee[int](0)
    EnsureCreated = Kee[int](1)
    EnsurePopulated = Kee[int](2)

  #  The classes Qt writes inside QFontDatabasePrivate, each a class in here
  #  as in C++.

  class ApplicationFont(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QFontDatabasePrivate::ApplicationFont: a plain
    Python object standing in front of one C++
    QFontDatabasePrivate::ApplicationFont.

    C++ hands a QFontDatabasePrivate::ApplicationFont around as a copy, so
    every C++ QFontDatabasePrivate::ApplicationFont behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QFontDatabasePrivate::ApplicationFont that has a
    ritual and that Python can call so far, 2 names in all: 'isNull',
    'isPopulated'. None can be made from Python: one comes out of a function
    of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QFontDatabasePrivate::ApplicationFont::~ApplicationFont()': the
      destructor: Python removes its C++
      QFontDatabasePrivate::ApplicationFont by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QFontDatabasePrivate::ApplicationFont is created at the first
      use, not by 'QFontDatabasePrivate::ApplicationFont(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QFontDatabasePrivate::ApplicationFont back gives a
      copy the ritual made for Python, in a new cute
      QFontDatabasePrivate::ApplicationFont.
    """

    #  The classes Qt writes inside QFontDatabasePrivate::ApplicationFont,
    #  each a class in here as in C++.

    class Properties(CuteMixin, metaclass=MetaCute):
      """
      The cute side of Qt's
      QFontDatabasePrivate::ApplicationFont::Properties: a plain Python
      object standing in front of one C++
      QFontDatabasePrivate::ApplicationFont::Properties.

      C++ hands a QFontDatabasePrivate::ApplicationFont::Properties around as
      a copy, so every C++ QFontDatabasePrivate::ApplicationFont::Properties
      behind a cute one is Python's own: it is removed, by the ritual named
      in '__delete_ritual__', when the cute object goes.

      What exists
      -----------

      No function of Qt's QFontDatabasePrivate::ApplicationFont::Properties
      yet. None can be made from Python: one comes out of a function of
      another class that gives one back.

      What has a ritual and is left out, and why
      ------------------------------------------

      - Qt's
        'QFontDatabasePrivate::ApplicationFont::Properties::~Properties()':
        the destructor: Python removes its C++
        QFontDatabasePrivate::ApplicationFont::Properties by it, and has no
        other use for it.

      What to expect
      --------------

      - The C++ QFontDatabasePrivate::ApplicationFont::Properties is created
        at the first use, not by
        'QFontDatabasePrivate::ApplicationFont::Properties(...)'.
      - A wrong argument is refused in Python, with 'DispatchException', and
        never reaches C++.
      - None is taken wherever Qt takes an object by its address, or text as
        C has it, and is passed on as nothing. Whether Qt can do with nothing
        there is as in C++.
      - A function giving a QFontDatabasePrivate::ApplicationFont::Properties
        back gives a copy the ritual made for Python, in a new cute
        QFontDatabasePrivate::ApplicationFont::Properties.
      """

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      #  Class Variables
      #  The class of Qt this class stands for.
      __qt_class__ = 'QFontDatabasePrivate::ApplicationFont::Properties'

      #  Qt's '~QFontDatabasePrivate::ApplicationFont::Properties()'. Naming
      #  it makes this a value class: Python owns every C++
      #  QFontDatabasePrivate::ApplicationFont::Properties behind a cute one,
      #  and removes it by this ritual.
      __delete_ritual__ = (
          'ritual_ZN20QFontDatabasePrivate15ApplicationFont10PropertiesD1Ev')

      #  Fallback Variables

      #  Private Variables

      #  Public Variables

      #  Virtual Variables

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
      #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QFontDatabasePrivate::ApplicationFont'

    #  Qt's '~QFontDatabasePrivate::ApplicationFont()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QFontDatabasePrivate::ApplicationFont behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN20QFontDatabasePrivate15ApplicationFontD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isNull(self) -> bool:
      """
      Calls Qt's 'bool QFontDatabasePrivate::ApplicationFont::isNull()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qfontdatabaseprivate-applicationfont.html#isNull
      """
      #  bool QFontDatabasePrivate::ApplicationFont::isNull() const
      return self.uglySide.call(
          'ritual_ZNK20QFontDatabasePrivate15ApplicationFont6isNullEv',
      )

    def isPopulated(self) -> bool:
      """
      Calls Qt's 'bool QFontDatabasePrivate::ApplicationFont::isPopulated()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qfontdatabaseprivate-applicationfont.html
      """
      #  bool QFontDatabasePrivate::ApplicationFont::isPopulated() const
      return self.uglySide.call(
          'ritual_ZNK20QFontDatabasePrivate15ApplicationFont11isPopulatedEv',
      )

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

  @staticmethod
  def instance() -> Optional[QFontDatabasePrivate]:
    """
    Calls Qt's 'QFontDatabasePrivate *QFontDatabasePrivate::instance()'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdatabaseprivate.html#instance

    Returns
    -------

    Optional[QFontDatabasePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFontDatabasePrivate *QFontDatabasePrivate::instance()
    address = Rituals.call('ritual_ZN20QFontDatabasePrivate8instanceEv')
    return QFontDatabasePrivate._cuteAt(address)

  @staticmethod
  @overload(str)
  def resolveFontFamilyAlias(family: str) -> str:
    """
    Calls Qt's 'QString QFontDatabasePrivate::resolveFontFamilyAlias(const
    QString &family)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdatabaseprivate.html#resolveFontFamilyAlias

    Parameters
    ----------

    family : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFontDatabasePrivate::resolveFontFamilyAlias(const QString
    #      &family)
    return Rituals.call(
        'ritual_ZN20QFontDatabasePrivate22resolveFontFamilyAliasERK7QString',
        family,
    )

  @staticmethod
  @overload(QFontDef, int)
  @overload(QFontDef, int, bool)
  def findFont(
      request: QFontDef,
      script: int,
      preferScriptOverFamily: bool = False,
  ) -> Optional[QFontEngine]:
    """
    Calls Qt's 'QFontEngine *QFontDatabasePrivate::findFont(const QFontDef
    &request, int script, bool preferScriptOverFamily)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdatabaseprivate.html#findFont

    Parameters
    ----------

    request : QFontDef
      Passed on as a value: Qt reads the C++ QFontDef, which stays Python's
      own.

    script : int
      Passed on as it is.

    preferScriptOverFamily : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    Returns
    -------

    Optional[QFontEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFontEngine *QFontDatabasePrivate::findFont(const QFontDef &request,
    #      int script, bool preferScriptOverFamily)
    address = Rituals.call(
        'ritual_ZN20QFontDatabasePrivate8findFontERK8QFontDefib',
        CuteMixin._valueOf(request), script, preferScriptOverFamily,
    )
    from . import QFontEngine
    return QFontEngine._cuteAt(address)

  @staticmethod
  @overload(QFontPrivate, int)
  @overload(NoneType, int)
  def load(d: Optional[QFontPrivate], script: int) -> None:
    """
    Calls Qt's 'void QFontDatabasePrivate::load(const QFontPrivate *d, int
    script)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdatabaseprivate.html#load

    Parameters
    ----------

    d : Optional[QFontPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    script : int
      Passed on as it is.
    """
    #  void QFontDatabasePrivate::load(const QFontPrivate *d, int script)
    Rituals.call(
        'ritual_ZN20QFontDatabasePrivate4loadEPK12QFontPrivatei',
        CuteMixin._addressOf(d), script,
    )

  @staticmethod
  def ensureFontDatabase() -> Optional[QFontDatabasePrivate]:
    """
    Calls Qt's 'QFontDatabasePrivate
    *QFontDatabasePrivate::ensureFontDatabase()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdatabaseprivate.html#ensureFontDatabase

    Returns
    -------

    Optional[QFontDatabasePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFontDatabasePrivate *QFontDatabasePrivate::ensureFontDatabase()
    address = Rituals.call(
        'ritual_ZN20QFontDatabasePrivate18ensureFontDatabaseEv',
    )
    return QFontDatabasePrivate._cuteAt(address)

  @staticmethod
  @overload(
      int, QFontDef, QtFontFamily, QtFontFoundry, QtFontStyle, QtFontSize,
  )
  @overload(
      int, QFontDef, QtFontFamily, QtFontFoundry, QtFontStyle, NoneType,
  )
  @overload(int, QFontDef, QtFontFamily, QtFontFoundry, NoneType, QtFontSize)
  @overload(int, QFontDef, QtFontFamily, QtFontFoundry, NoneType, NoneType)
  @overload(int, QFontDef, QtFontFamily, NoneType, QtFontStyle, QtFontSize)
  @overload(int, QFontDef, QtFontFamily, NoneType, QtFontStyle, NoneType)
  @overload(int, QFontDef, QtFontFamily, NoneType, NoneType, QtFontSize)
  @overload(int, QFontDef, QtFontFamily, NoneType, NoneType, NoneType)
  @overload(int, QFontDef, NoneType, QtFontFoundry, QtFontStyle, QtFontSize)
  @overload(int, QFontDef, NoneType, QtFontFoundry, QtFontStyle, NoneType)
  @overload(int, QFontDef, NoneType, QtFontFoundry, NoneType, QtFontSize)
  @overload(int, QFontDef, NoneType, QtFontFoundry, NoneType, NoneType)
  @overload(int, QFontDef, NoneType, NoneType, QtFontStyle, QtFontSize)
  @overload(int, QFontDef, NoneType, NoneType, QtFontStyle, NoneType)
  @overload(int, QFontDef, NoneType, NoneType, NoneType, QtFontSize)
  @overload(int, QFontDef, NoneType, NoneType, NoneType, NoneType)
  def loadSingleEngine(
      script: int,
      request: QFontDef,
      family: Optional[QtFontFamily],
      foundry: Optional[QtFontFoundry],
      style: Optional[QtFontStyle],
      size: Optional[QtFontSize],
  ) -> Optional[QFontEngine]:
    """
    Calls Qt's 'QFontEngine *QFontDatabasePrivate::loadSingleEngine(int
    script, const QFontDef &request, QtFontFamily *family, QtFontFoundry
    *foundry, QtFontStyle *style, QtFontSize *size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdatabaseprivate.html#loadSingleEngine

    Parameters
    ----------

    script : int
      Passed on as it is.

    request : QFontDef
      Passed on as a value: Qt reads the C++ QFontDef, which stays Python's
      own.

    family : Optional[QtFontFamily]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    foundry : Optional[QtFontFoundry]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    style : Optional[QtFontStyle]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    size : Optional[QtFontSize]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QFontEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFontEngine *QFontDatabasePrivate::loadSingleEngine(int script, const
    #      QFontDef &request, QtFontFamily *family, QtFontFoundry *foundry,
    #      QtFontStyle *style, QtFontSize *size)
    address = Rituals.call(
        'ritual_ZN20QFontDatabasePrivate16loadSingleEngineEiRK8QFontDefP12Q'
        'tFontFamilyP13QtFontFoundryP11QtFontStyleP10QtFontSize',
        script, CuteMixin._valueOf(request), CuteMixin._addressOf(family),
        CuteMixin._addressOf(foundry), CuteMixin._addressOf(style),
        CuteMixin._addressOf(size),
    )
    from . import QFontEngine
    return QFontEngine._cuteAt(address)

  @staticmethod
  @overload(
      int, QFontDef, QtFontFamily, QtFontFoundry, QtFontStyle, QtFontSize,
  )
  @overload(
      int, QFontDef, QtFontFamily, QtFontFoundry, QtFontStyle, NoneType,
  )
  @overload(int, QFontDef, QtFontFamily, QtFontFoundry, NoneType, QtFontSize)
  @overload(int, QFontDef, QtFontFamily, QtFontFoundry, NoneType, NoneType)
  @overload(int, QFontDef, QtFontFamily, NoneType, QtFontStyle, QtFontSize)
  @overload(int, QFontDef, QtFontFamily, NoneType, QtFontStyle, NoneType)
  @overload(int, QFontDef, QtFontFamily, NoneType, NoneType, QtFontSize)
  @overload(int, QFontDef, QtFontFamily, NoneType, NoneType, NoneType)
  @overload(int, QFontDef, NoneType, QtFontFoundry, QtFontStyle, QtFontSize)
  @overload(int, QFontDef, NoneType, QtFontFoundry, QtFontStyle, NoneType)
  @overload(int, QFontDef, NoneType, QtFontFoundry, NoneType, QtFontSize)
  @overload(int, QFontDef, NoneType, QtFontFoundry, NoneType, NoneType)
  @overload(int, QFontDef, NoneType, NoneType, QtFontStyle, QtFontSize)
  @overload(int, QFontDef, NoneType, NoneType, QtFontStyle, NoneType)
  @overload(int, QFontDef, NoneType, NoneType, NoneType, QtFontSize)
  @overload(int, QFontDef, NoneType, NoneType, NoneType, NoneType)
  def loadEngine(
      script: int,
      request: QFontDef,
      family: Optional[QtFontFamily],
      foundry: Optional[QtFontFoundry],
      style: Optional[QtFontStyle],
      size: Optional[QtFontSize],
  ) -> Optional[QFontEngine]:
    """
    Calls Qt's 'QFontEngine *QFontDatabasePrivate::loadEngine(int script,
    const QFontDef &request, QtFontFamily *family, QtFontFoundry *foundry,
    QtFontStyle *style, QtFontSize *size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdatabaseprivate.html#loadEngine

    Parameters
    ----------

    script : int
      Passed on as it is.

    request : QFontDef
      Passed on as a value: Qt reads the C++ QFontDef, which stays Python's
      own.

    family : Optional[QtFontFamily]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    foundry : Optional[QtFontFoundry]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    style : Optional[QtFontStyle]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    size : Optional[QtFontSize]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QFontEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFontEngine *QFontDatabasePrivate::loadEngine(int script, const
    #      QFontDef &request, QtFontFamily *family, QtFontFoundry *foundry,
    #      QtFontStyle *style, QtFontSize *size)
    address = Rituals.call(
        'ritual_ZN20QFontDatabasePrivate10loadEngineEiRK8QFontDefP12QtFontF'
        'amilyP13QtFontFoundryP11QtFontStyleP10QtFontSize',
        script, CuteMixin._valueOf(request), CuteMixin._addressOf(family),
        CuteMixin._addressOf(foundry), CuteMixin._addressOf(style),
        CuteMixin._addressOf(size),
    )
    from . import QFontEngine
    return QFontEngine._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFontDatabasePrivate'

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

  @overload(ExtendedScript, QStringList)
  def setApplicationFallbackFontFamilies(
      self,
      script: ExtendedScript,
      familyNames: QStringList,
  ) -> None:
    """
    Calls Qt's 'void
    QFontDatabasePrivate::setApplicationFallbackFontFamilies(ExtendedScript
    script, const QStringList &familyNames)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdatabaseprivate.html

    Parameters
    ----------

    script : ExtendedScript
      Passed on as its number.

    familyNames : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QFontDatabasePrivate::setApplicationFallbackFontFamilies(
    #      ExtendedScript script, const QStringList &familyNames)
    self.uglySide.call(
        'ritual_ZN20QFontDatabasePrivate34setApplicationFallbackFontFamilie'
        'sENS_14ExtendedScriptERK5QListI7QStringE',
        script.value, self._valueOf(familyNames),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QFontDatabasePrivate::QFontDatabasePrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdatabaseprivate.html#QFontDatabasePrivate
    """
    #  QFontDatabasePrivate::QFontDatabasePrivate()
    self._noteCreation(QFontDatabasePrivate, lambda: Rituals.call(
        'ritual_ZN20QFontDatabasePrivateC1Ev',
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

  def clearFamilies(self) -> None:
    """
    Calls Qt's 'void QFontDatabasePrivate::clearFamilies()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdatabaseprivate.html#clearFamilies
    """
    #  void QFontDatabasePrivate::clearFamilies()
    self.uglySide.call('ritual_ZN20QFontDatabasePrivate13clearFamiliesEv')

  @overload(str)
  @overload(str, FamilyRequestFlags)
  def family(
      self,
      f: str,
      flags: FamilyRequestFlags = FamilyRequestFlags.EnsurePopulated,
  ) -> Optional[QtFontFamily]:
    """
    Calls Qt's 'QtFontFamily *QFontDatabasePrivate::family(const QString &f,
    FamilyRequestFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdatabaseprivate.html#family

    Parameters
    ----------

    f : str
      Passed on as it is: a QString is made of it for the call.

    flags : FamilyRequestFlags
      Passed on as its number. May be left out, as in Qt: it is then
      FamilyRequestFlags.EnsurePopulated.

    Returns
    -------

    Optional[QtFontFamily]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QtFontFamily *QFontDatabasePrivate::family(const QString &f,
    #      FamilyRequestFlags flags)
    address = self.uglySide.call(
        'ritual_ZN20QFontDatabasePrivate6familyERK7QStringNS_18FamilyReques'
        'tFlagsE',
        f, flags.value,
    )
    from . import QtFontFamily
    return QtFontFamily._cuteAt(address)

  @overload(QByteArray, str)
  def addAppFont(self, fontData: QByteArray, fileName: str) -> int:
    """
    Calls Qt's 'int QFontDatabasePrivate::addAppFont(const QByteArray
    &fontData, const QString &fileName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdatabaseprivate.html#addAppFont

    Parameters
    ----------

    fontData : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QFontDatabasePrivate::addAppFont(const QByteArray &fontData, const
    #      QString &fileName)
    return self.uglySide.call(
        'ritual_ZN20QFontDatabasePrivate10addAppFontERK10QByteArrayRK7QStri'
        'ng',
        self._valueOf(fontData), fileName,
    )

  @overload(str)
  def isApplicationFont(self, fileName: str) -> bool:
    """
    Calls Qt's 'bool QFontDatabasePrivate::isApplicationFont(const QString
    &fileName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdatabaseprivate.html#isApplicationFont

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QFontDatabasePrivate::isApplicationFont(const QString &fileName)
    return self.uglySide.call(
        'ritual_ZN20QFontDatabasePrivate17isApplicationFontERK7QString',
        fileName,
    )

  @overload(ExtendedScript)
  def applicationFallbackFontFamilies(
      self,
      script: ExtendedScript,
  ) -> QStringList:
    """
    Calls Qt's 'QStringList
    QFontDatabasePrivate::applicationFallbackFontFamilies(ExtendedScript
    script)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdatabaseprivate.html

    Parameters
    ----------

    script : ExtendedScript
      Passed on as its number.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QFontDatabasePrivate::applicationFallbackFontFamilies(
    #      ExtendedScript script)
    address = self.uglySide.call(
        'ritual_ZN20QFontDatabasePrivate31applicationFallbackFontFamiliesEN'
        'S_14ExtendedScriptE',
        script.value,
    )
    return QStringList._cuteOwning(address)

  @overload(ExtendedScript, str)
  def removeApplicationFallbackFontFamily(
      self,
      script: ExtendedScript,
      familyName: str,
  ) -> bool:
    """
    Calls Qt's 'bool
    QFontDatabasePrivate::removeApplicationFallbackFontFamily(ExtendedScript
    script, const QString &familyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdatabaseprivate.html

    Parameters
    ----------

    script : ExtendedScript
      Passed on as its number.

    familyName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QFontDatabasePrivate::removeApplicationFallbackFontFamily(
    #      ExtendedScript script, const QString &familyName)
    return self.uglySide.call(
        'ritual_ZN20QFontDatabasePrivate35removeApplicationFallbackFontFami'
        'lyENS_14ExtendedScriptERK7QString',
        script.value, familyName,
    )

  @overload(ExtendedScript, str)
  def addApplicationFallbackFontFamily(
      self,
      script: ExtendedScript,
      familyName: str,
  ) -> None:
    """
    Calls Qt's 'void
    QFontDatabasePrivate::addApplicationFallbackFontFamily(ExtendedScript
    script, const QString &familyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdatabaseprivate.html

    Parameters
    ----------

    script : ExtendedScript
      Passed on as its number.

    familyName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFontDatabasePrivate::addApplicationFallbackFontFamily(
    #      ExtendedScript script, const QString &familyName)
    self.uglySide.call(
        'ritual_ZN20QFontDatabasePrivate32addApplicationFallbackFontFamilyE'
        'NS_14ExtendedScriptERK7QString',
        script.value, familyName,
    )

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QFontDatabasePrivate::invalidate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdatabaseprivate.html#invalidate
    """
    #  void QFontDatabasePrivate::invalidate()
    self.uglySide.call('ritual_ZN20QFontDatabasePrivate10invalidateEv')

  @staticmethod
  def bestFoundry(*__, **_) -> Never:
    """
    Qt's 'unsigned int QFontDatabasePrivate::bestFoundry(int script, unsigned
    int score, int styleStrategy, const QtFontFamily *family, const QString
    &foundry_name, QtFontStyle::Key styleKey, int pixelSize, char pitch,
    QtFontDesc *desc, const QString &styleName)': takes a single letter as C
    has it.
    """
    raise NotImplementedError(
        "'QFontDatabasePrivate.bestFoundry' has no cute function yet. Qt's "
        "'unsigned int QFontDatabasePrivate::bestFoundry(int script, "
        "unsigned int score, int styleStrategy, const QtFontFamily *family, "
        "const QString &foundry_name, QtFontStyle::Key styleKey, int "
        "pixelSize, char pitch, QtFontDesc *desc, const QString "
        "&styleName)': takes a single letter as C has it.")

  @staticmethod
  def match(*__, **_) -> Never:
    """
    Qt's 'int QFontDatabasePrivate::match(int script, const QFontDef
    &request, const QString &family_name, const QString &foundry_name,
    QtFontDesc *desc, const QList<int> &blacklistedFamilies, unsigned int
    *resultingScore)': names 'QtFontDesc', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QFontDatabasePrivate.match' has no cute function yet. Qt's 'int "
        "QFontDatabasePrivate::match(int script, const QFontDef &request, "
        "const QString &family_name, const QString &foundry_name, "
        "QtFontDesc *desc, const QList<int> &blacklistedFamilies, unsigned "
        "int *resultingScore)': names 'QtFontDesc', which has no cute class "
        "yet.")

  @staticmethod
  def parseFontName(*__, **_) -> Never:
    """
    Qt's 'void QFontDatabasePrivate::parseFontName(const QString &name,
    QString &foundry, QString &family)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QFontDatabasePrivate.parseFontName' has no cute function yet. "
        "Qt's 'void QFontDatabasePrivate::parseFontName(const QString "
        "&name, QString &foundry, QString &family)': takes a type Python "
        "has no way to hand over yet.")
