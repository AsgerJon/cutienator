"""
QQStyleKitPropertyResolver binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitpropertyresolver_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQStyleKitPropertyResolver to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQStyleKitReader, QQStyleKitStyleAndThemeBase
  from . import QQStyleKitVariation
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQStyleKitReader = WAIT['QQStyleKitReader']
  QQStyleKitStyleAndThemeBase = WAIT['QQStyleKitStyleAndThemeBase']
  QQStyleKitVariation = WAIT['QQStyleKitVariation']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQStyleKitPropertyResolver(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQStyleKitPropertyResolver: a plain Python object
  standing in front of one C++ QQStyleKitPropertyResolver.

  C++ hands a QQStyleKitPropertyResolver around as a copy, so every C++
  QQStyleKitPropertyResolver behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQStyleKitPropertyResolver that has a ritual and
  that Python can call so far, 1 name in all: 'addVariationToReader'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QList<QQStyleKitExtendableControlType>
    QQStyleKitPropertyResolver::baseTypesForType(
    QQStyleKitExtendableControlType exactType)': gives a type Python has no
    way to take yet.
  - Qt's 'void QQStyleKitPropertyResolver::addInstanceVariationsToReader(
    QQStyleKitReader *styleReader, QQStyleKitStyleAndThemeBase *styleOrTheme,
    const AttachedVariationList &attachedVariations)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QQStyleKitPropertyResolver::~QQStyleKitPropertyResolver()': the
    destructor: Python removes its C++ QQStyleKitPropertyResolver by it, and
    has no other use for it.

  What has no ritual
  ------------------

  15 of the 19 functions Qt declares: 5 leans on 'QQStyleKitPropertyResolver;
  3 not a gap; 2 a template; 2 leans on 'QQStyleKitDebug; 2 leans on
  'QQStyleKitControl; 1 leans on 'QQStyleKitVariation.

  What to expect
  --------------

  - The C++ QQStyleKitPropertyResolver is created at the first use, not by
    'QQStyleKitPropertyResolver(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQStyleKitPropertyResolver back gives a copy the
    ritual made for Python, in a new cute QQStyleKitPropertyResolver.
  - Each name of Qt's QQStyleKitPropertyResolver that has no cute function
    yet, 'addInstanceVariationsToReader', 'addTypeVariationsToReader',
    'baseTypesForType', 'cacheReaderState', 'hasLocalStyleProperty',
    'readPropertyInControl', 'readPropertyInControlForStates',
    'readPropertyInRelevantControls', 'readPropertyInStorageForState',
    'readPropertyInStyle', 'readPropertyInVariations', 'readStyleProperty',
    'rebuildVariationsForReader', 'writeStyleProperty', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQStyleKitPropertyResolver, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class PathId(CuteNum, scoped=True):
    """
    The enum 'QQStyleKitPropertyResolver::PathId' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    ExcludeSubType = Kee[int](0)
    IncludeSubType = Kee[int](1)

  #  The classes Qt writes inside QQStyleKitPropertyResolver, each a class in
  #  here as in C++.

  class PropertyPathIds(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQStyleKitPropertyResolver::PropertyPathIds: a
    plain Python object standing in front of one C++
    QQStyleKitPropertyResolver::PropertyPathIds.

    C++ hands a QQStyleKitPropertyResolver::PropertyPathIds around as a copy,
    so every C++ QQStyleKitPropertyResolver::PropertyPathIds behind a cute
    one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QQStyleKitPropertyResolver::PropertyPathIds yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQStyleKitPropertyResolver::PropertyPathIds::~PropertyPathIds()':
      the destructor: Python removes its C++
      QQStyleKitPropertyResolver::PropertyPathIds by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QQStyleKitPropertyResolver::PropertyPathIds is created at the
      first use, not by 'QQStyleKitPropertyResolver::PropertyPathIds(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQStyleKitPropertyResolver::PropertyPathIds back
      gives a copy the ritual made for Python, in a new cute
      QQStyleKitPropertyResolver::PropertyPathIds.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQStyleKitPropertyResolver::PropertyPathIds'

    #  Qt's '~QQStyleKitPropertyResolver::PropertyPathIds()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QQStyleKitPropertyResolver::PropertyPathIds behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN26QQStyleKitPropertyResolver15PropertyPathIdsD1Ev')

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

  @staticmethod
  @overload(
      QQStyleKitReader, QQStyleKitStyleAndThemeBase, QQStyleKitVariation,
  )
  @overload(QQStyleKitReader, QQStyleKitStyleAndThemeBase, NoneType)
  @overload(QQStyleKitReader, NoneType, QQStyleKitVariation)
  @overload(QQStyleKitReader, NoneType, NoneType)
  @overload(NoneType, QQStyleKitStyleAndThemeBase, QQStyleKitVariation)
  @overload(NoneType, QQStyleKitStyleAndThemeBase, NoneType)
  @overload(NoneType, NoneType, QQStyleKitVariation)
  @overload(NoneType, NoneType, NoneType)
  def addVariationToReader(
      styleReader: Optional[QQStyleKitReader],
      styleOrTheme: Optional[QQStyleKitStyleAndThemeBase],
      variation: Optional[QQStyleKitVariation],
  ) -> None:
    """
    Calls Qt's 'void
    QQStyleKitPropertyResolver::addVariationToReader(QQStyleKitReader
    *styleReader, QQStyleKitStyleAndThemeBase *styleOrTheme,
    QQStyleKitVariation *variation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitpropertyresolver.html

    Parameters
    ----------

    styleReader : Optional[QQStyleKitReader]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    styleOrTheme : Optional[QQStyleKitStyleAndThemeBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    variation : Optional[QQStyleKitVariation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitPropertyResolver::addVariationToReader(QQStyleKitReader
    #      *styleReader, QQStyleKitStyleAndThemeBase *styleOrTheme,
    #      QQStyleKitVariation *variation)
    Rituals.call(
        'ritual_ZN26QQStyleKitPropertyResolver20addVariationToReaderEP16QQS'
        'tyleKitReaderP27QQStyleKitStyleAndThemeBaseP19QQStyleKitVariation',
        CuteMixin._addressOf(styleReader),
        CuteMixin._addressOf(styleOrTheme), CuteMixin._addressOf(variation),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQStyleKitPropertyResolver'

  #  Qt's '~QQStyleKitPropertyResolver()'. Naming it makes this a value
  #  class: Python owns every C++ QQStyleKitPropertyResolver behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QQStyleKitPropertyResolverD1Ev'

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
  def addInstanceVariationsToReader(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitPropertyResolver::addInstanceVariationsToReader(
    QQStyleKitReader *styleReader, QQStyleKitStyleAndThemeBase *styleOrTheme,
    const AttachedVariationList &attachedVariations)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQStyleKitPropertyResolver.addInstanceVariationsToReader' has no "
        "cute function yet. Qt's 'void "
        "QQStyleKitPropertyResolver::addInstanceVariationsToReader(QQStyleKi"
        "tReader *styleReader, QQStyleKitStyleAndThemeBase *styleOrTheme, "
        "const AttachedVariationList &attachedVariations)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def addTypeVariationsToReader(*__, **_) -> Never:
    """
    Qt's 'void
    QQStyleKitPropertyResolver::addTypeVariationsToReader(QQStyleKitReader
    *styleReader, QQStyleKitStyleAndThemeBase *styleOrTheme, const
    AttachedVariationList &attachedVariations)': leans on
    'QQStyleKitPropertyResolver::s_cachedState', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitPropertyResolver.addTypeVariationsToReader' has no cute "
        "function yet. Qt's 'void "
        "QQStyleKitPropertyResolver::addTypeVariationsToReader(QQStyleKitRea"
        "der *styleReader, QQStyleKitStyleAndThemeBase *styleOrTheme, const "
        "AttachedVariationList &attachedVariations)': leans on "
        "'QQStyleKitPropertyResolver::s_cachedState', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def baseTypesForType(*__, **_) -> Never:
    """
    Qt's 'const QList<QQStyleKitExtendableControlType>
    QQStyleKitPropertyResolver::baseTypesForType(
    QQStyleKitExtendableControlType exactType)': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QQStyleKitPropertyResolver.baseTypesForType' has no cute function "
        "yet. Qt's 'const QList<QQStyleKitExtendableControlType> "
        "QQStyleKitPropertyResolver::baseTypesForType(QQStyleKitExtendableCo"
        "ntrolType exactType)': gives a type Python has no way to take yet.")

  @staticmethod
  def cacheReaderState(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitPropertyResolver::cacheReaderState(QQSK::State
    state)': leans on 'QQStyleKitPropertyResolver::s_cachedState', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitPropertyResolver.cacheReaderState' has no cute function "
        "yet. Qt's 'void "
        "QQStyleKitPropertyResolver::cacheReaderState(QQSK::State state)': "
        "leans on 'QQStyleKitPropertyResolver::s_cachedState', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def hasLocalStyleProperty(*__, **_) -> Never:
    """
    Qt's 'bool QQStyleKitPropertyResolver::hasLocalStyleProperty(const
    QQStyleKitPropertyGroup *group, const QQSK::Property property)': leans on
    'QQStyleKitControl::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitPropertyResolver.hasLocalStyleProperty' has no cute "
        "function yet. Qt's 'bool "
        "QQStyleKitPropertyResolver::hasLocalStyleProperty(const "
        "QQStyleKitPropertyGroup *group, const QQSK::Property property)': "
        "leans on 'QQStyleKitControl::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def readPropertyInControl(*__, **_) -> Never:
    """
    Qt's 'QVariant QQStyleKitPropertyResolver::readPropertyInControl(const
    PropertyPathIds &ids, const QQStyleKitControl *control)': leans on
    'QQStyleKitPropertyResolver::s_cachedState', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitPropertyResolver.readPropertyInControl' has no cute "
        "function yet. Qt's 'QVariant "
        "QQStyleKitPropertyResolver::readPropertyInControl(const "
        "PropertyPathIds &ids, const QQStyleKitControl *control)': leans on "
        "'QQStyleKitPropertyResolver::s_cachedState', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def readPropertyInControlForStates(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitPropertyResolver::readPropertyInControlForStates': a
    template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QQStyleKitPropertyResolver.readPropertyInControlForStates' has no "
        "cute function yet. Qt's "
        "'QQStyleKitPropertyResolver::readPropertyInControlForStates': a "
        "template: a pattern and no single function.")

  @staticmethod
  def readPropertyInRelevantControls(*__, **_) -> Never:
    """
    Qt's 'QVariant
    QQStyleKitPropertyResolver::readPropertyInRelevantControls(const
    QQStyleKitControls *controls, const PropertyPathIds &ids, const
    QQStyleKitExtendableControlType exactType, const
    QList<QQStyleKitExtendableControlType> baseTypes)': leans on
    'QQStyleKitPropertyResolver::s_cachedState', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitPropertyResolver.readPropertyInRelevantControls' has no "
        "cute function yet. Qt's 'QVariant "
        "QQStyleKitPropertyResolver::readPropertyInRelevantControls(const "
        "QQStyleKitControls *controls, const PropertyPathIds &ids, const "
        "QQStyleKitExtendableControlType exactType, const "
        "QList<QQStyleKitExtendableControlType> baseTypes)': leans on "
        "'QQStyleKitPropertyResolver::s_cachedState', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def readPropertyInStorageForState(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitPropertyResolver::readPropertyInStorageForState': a
    template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QQStyleKitPropertyResolver.readPropertyInStorageForState' has no "
        "cute function yet. Qt's "
        "'QQStyleKitPropertyResolver::readPropertyInStorageForState': a "
        "template: a pattern and no single function.")

  @staticmethod
  def readPropertyInStyle(*__, **_) -> Never:
    """
    Qt's 'QVariant
    QQStyleKitPropertyResolver::readPropertyInStyle(QQStyleKitStyle *style,
    const PropertyPathIds &ids, QQStyleKitReader *styleReader)': leans on
    'QQStyleKitDebug::m_item', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitPropertyResolver.readPropertyInStyle' has no cute "
        "function yet. Qt's 'QVariant "
        "QQStyleKitPropertyResolver::readPropertyInStyle(QQStyleKitStyle "
        "*style, const PropertyPathIds &ids, QQStyleKitReader "
        "*styleReader)': leans on 'QQStyleKitDebug::m_item', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def readPropertyInVariations(*__, **_) -> Never:
    """
    Qt's 'QVariant QQStyleKitPropertyResolver::readPropertyInVariations(const
    QList<QPointer<QQStyleKitVariation>> &variations, const
    QQStyleKitStyleAndThemeBase *styleOrTheme, const PropertyPathIds &ids,
    const QQStyleKitExtendableControlType exactType, const
    QList<QQStyleKitExtendableControlType> baseTypes)': leans on
    'QQStyleKitPropertyResolver::s_cachedState', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitPropertyResolver.readPropertyInVariations' has no cute "
        "function yet. Qt's 'QVariant "
        "QQStyleKitPropertyResolver::readPropertyInVariations(const "
        "QList<QPointer<QQStyleKitVariation>> &variations, const "
        "QQStyleKitStyleAndThemeBase *styleOrTheme, const PropertyPathIds "
        "&ids, const QQStyleKitExtendableControlType exactType, const "
        "QList<QQStyleKitExtendableControlType> baseTypes)': leans on "
        "'QQStyleKitPropertyResolver::s_cachedState', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def readStyleProperty(*__, **_) -> Never:
    """
    Qt's 'QVariant QQStyleKitPropertyResolver::readStyleProperty(const
    QQStyleKitPropertyGroup *group, const QQSK::Property property, const
    QQSK::Property alternative)': leans on 'QQStyleKitDebug::groupBeingRead',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitPropertyResolver.readStyleProperty' has no cute "
        "function yet. Qt's 'QVariant "
        "QQStyleKitPropertyResolver::readStyleProperty(const "
        "QQStyleKitPropertyGroup *group, const QQSK::Property property, "
        "const QQSK::Property alternative)': leans on "
        "'QQStyleKitDebug::groupBeingRead', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def rebuildVariationsForReader(*__, **_) -> Never:
    """
    Qt's 'void
    QQStyleKitPropertyResolver::rebuildVariationsForReader(QQStyleKitReader
    *styleReader, QQStyleKitStyle *style)': leans on
    'QQStyleKitVariation::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitPropertyResolver.rebuildVariationsForReader' has no "
        "cute function yet. Qt's 'void "
        "QQStyleKitPropertyResolver::rebuildVariationsForReader(QQStyleKitRe"
        "ader *styleReader, QQStyleKitStyle *style)': leans on "
        "'QQStyleKitVariation::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def writeStyleProperty(*__, **_) -> Never:
    """
    Qt's 'bool QQStyleKitPropertyResolver::writeStyleProperty(const
    QQStyleKitPropertyGroup *group, const QQSK::Property property, const
    QVariant &value)': leans on 'QQStyleKitControl::staticMetaObject', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitPropertyResolver.writeStyleProperty' has no cute "
        "function yet. Qt's 'bool "
        "QQStyleKitPropertyResolver::writeStyleProperty(const "
        "QQStyleKitPropertyGroup *group, const QQSK::Property property, "
        "const QVariant &value)': leans on "
        "'QQStyleKitControl::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
