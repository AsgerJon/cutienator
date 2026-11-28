"""
qdesigner_internal::PropertySheetPixmapValue binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::PropertySheetPixmapValue to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QDesignerFormEditorInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PropertySheetPixmapValue(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's qdesigner_internal::PropertySheetPixmapValue: a plain
  Python object standing in front of one C++
  qdesigner_internal::PropertySheetPixmapValue.

  C++ hands a qdesigner_internal::PropertySheetPixmapValue around as a copy,
  so every C++ qdesigner_internal::PropertySheetPixmapValue behind a cute one
  is Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::PropertySheetPixmapValue that
  has a ritual and that Python can call so far, 6 names in all:
  'getPixmapSource', 'pixmapSource', 'path', 'setPath', '__eq__', '__ne__'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'qdesigner_internal::PropertySheetPixmapValue::~PropertySheetPixmapValue(
    )': the destructor: Python removes its C++
    qdesigner_internal::PropertySheetPixmapValue by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ qdesigner_internal::PropertySheetPixmapValue is created at the
    first use, not by 'qdesigner_internal::PropertySheetPixmapValue(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a qdesigner_internal::PropertySheetPixmapValue back
    gives a copy the ritual made for Python, in a new cute
    qdesigner_internal::PropertySheetPixmapValue.
  """

  #  The enums Qt writes inside qdesigner_internal::PropertySheetPixmapValue,
  #  each a class in here as in C++, and the names Qt has for the
  #  combinations of its flags enums.

  class PixmapSource(CuteNum):
    """
    The enum 'qdesigner_internal::PropertySheetPixmapValue::PixmapSource' of
    Qt, with the 3 names Qt gives in it.
    """

    LanguageResourcePixmap = Kee[int](0)
    ResourcePixmap = Kee[int](1)
    FilePixmap = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QDesignerFormEditorInterface, str)
  @overload(NoneType, str)
  def getPixmapSource(
      core: Optional[QDesignerFormEditorInterface],
      path: str,
  ) -> PixmapSource:
    """
    Calls Qt's 'PixmapSource
    qdesigner_internal::PropertySheetPixmapValue::getPixmapSource(
    QDesignerFormEditorInterface *core, const QString &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheetpixmapvalue.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    path : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    PixmapSource
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PixmapSource(number)'
      gives.
    """
    #  PixmapSource
    #      qdesigner_internal::PropertySheetPixmapValue::getPixmapSource(
    #      QDesignerFormEditorInterface *core, const QString &path)
    return PropertySheetPixmapValue.PixmapSource(Rituals.call(
        'ritual_ZN18qdesigner_internal24PropertySheetPixmapValue15getPixmap'
        'SourceEP28QDesignerFormEditorInterfaceRK7QString',
        CuteMixin._addressOf(core), path,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::PropertySheetPixmapValue'

  #  Qt's '~qdesigner_internal::PropertySheetPixmapValue()'. Naming it makes
  #  this a value class: Python owns every C++
  #  qdesigner_internal::PropertySheetPixmapValue behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN18qdesigner_internal24PropertySheetPixmapValueD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDesignerFormEditorInterface)
  @overload(NoneType)
  def pixmapSource(
      self,
      core: Optional[QDesignerFormEditorInterface],
  ) -> PixmapSource:
    """
    Calls Qt's 'PixmapSource
    qdesigner_internal::PropertySheetPixmapValue::pixmapSource(
    QDesignerFormEditorInterface *core) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheetpixmapvalue.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    PixmapSource
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PixmapSource(number)'
      gives.
    """
    #  PixmapSource
    #      qdesigner_internal::PropertySheetPixmapValue::pixmapSource(
    #      QDesignerFormEditorInterface *core) const
    return PropertySheetPixmapValue.PixmapSource(self.uglySide.call(
        'ritual_ZNK18qdesigner_internal24PropertySheetPixmapValue12pixmapSo'
        'urceEP28QDesignerFormEditorInterface',
        self._addressOf(core),
    ))

  def path(self) -> str:
    """
    Calls Qt's 'QString qdesigner_internal::PropertySheetPixmapValue::path()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheetpixmapvalue.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::PropertySheetPixmapValue::path() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal24PropertySheetPixmapValue4pathEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setPath(self, path: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PropertySheetPixmapValue::setPath(const QString
    &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheetpixmapvalue.html

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::PropertySheetPixmapValue::setPath(const
    #      QString &path)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal24PropertySheetPixmapValue7setPathERK'
        '7QString',
        path,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: PropertySheetPixmapValue) -> bool:
    """
    Calls Qt's 'bool operator==(const PropertySheetPixmapValue &lhs, const
    PropertySheetPixmapValue &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheetpixmapvalue.html

    Parameters
    ----------

    rhs : PropertySheetPixmapValue
      Passed on as a value: Qt reads the C++
      qdesigner_internal::PropertySheetPixmapValue, which stays Python's own.
    """
    #  bool operator==(const PropertySheetPixmapValue &lhs, const
    #      PropertySheetPixmapValue &rhs)
    return Rituals.call(
        'ritual_ZN18qdesigner_internaleqERKNS_24PropertySheetPixmapValueES2'
        '_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: PropertySheetPixmapValue) -> bool:
    """
    Calls Qt's 'bool operator!=(const PropertySheetPixmapValue &lhs, const
    PropertySheetPixmapValue &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheetpixmapvalue.html

    Parameters
    ----------

    rhs : PropertySheetPixmapValue
      Passed on as a value: Qt reads the C++
      qdesigner_internal::PropertySheetPixmapValue, which stays Python's own.
    """
    #  bool operator!=(const PropertySheetPixmapValue &lhs, const
    #      PropertySheetPixmapValue &rhs)
    return Rituals.call(
        'ritual_ZN18qdesigner_internalneERKNS_24PropertySheetPixmapValueES2'
        '_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def __init__(self, path: str) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::PropertySheetPixmapValue::PropertySheetPixmapValue(
    const QString &path)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheetpixmapvalue.html

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  qdesigner_internal::PropertySheetPixmapValue::
    #      PropertySheetPixmapValue(const QString &path)
    self._noteCreation(PropertySheetPixmapValue, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal24PropertySheetPixmapValueC1ERK7QStri'
        'ng',
        path,
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::PropertySheetPixmapValue::PropertySheetPixmapValue(
    )', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheetpixmapvalue.html
    """
    #  qdesigner_internal::PropertySheetPixmapValue::
    #      PropertySheetPixmapValue()
    self._noteCreation(PropertySheetPixmapValue, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal24PropertySheetPixmapValueC1Ev',
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
