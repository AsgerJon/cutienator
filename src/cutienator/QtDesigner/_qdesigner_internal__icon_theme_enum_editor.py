"""
qdesigner_internal::IconThemeEnumEditor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/iconselector_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means qdesigner_internal::IconThemeEnumEditor to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtWidgets import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtWidgets import QComboBox

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class IconThemeEnumEditor(QWidget):
  """
  The cute side of Qt's qdesigner_internal::IconThemeEnumEditor: a plain
  Python object standing in front of one C++
  qdesigner_internal::IconThemeEnumEditor.

  It is built on the cute 'QWidget', as Qt's
  qdesigner_internal::IconThemeEnumEditor is built on Qt's QWidget, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::IconThemeEnumEditor that has a
  ritual and that Python can call so far, 8 names in all: 'metaObject', 'tr',
  'themeEnum', 'setThemeEnum', 'iconName', 'createComboBox', 'edited',
  'reset'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::IconThemeEnumEditor::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::IconThemeEnumEditor::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'qdesigner_internal::IconThemeEnumEditor::~IconThemeEnumEditor()':
    the destructor: Python never removes a C++
    qdesigner_internal::IconThemeEnumEditor.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ qdesigner_internal::IconThemeEnumEditor is created at the first
    use, not by 'qdesigner_internal::IconThemeEnumEditor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::IconThemeEnumEditor.
  - Qt tells when it has removed the C++
    qdesigner_internal::IconThemeEnumEditor. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString qdesigner_internal::IconThemeEnumEditor::tr(const
    char *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-iconthemeenumeditor.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::IconThemeEnumEditor::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal19IconThemeEnumEditor2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(int)
  def iconName(e: int) -> str:
    """
    Calls Qt's 'QString qdesigner_internal::IconThemeEnumEditor::iconName(int
    e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-iconthemeenumeditor.html

    Parameters
    ----------

    e : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::IconThemeEnumEditor::iconName(int e)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal19IconThemeEnumEditor8iconNameEi', e,
    )

  @staticmethod
  @overload()
  @overload(QWidget)
  @overload(NoneType)
  def createComboBox(
      parent: Optional[QWidget] = None,
  ) -> Optional[QComboBox]:
    """
    Calls Qt's 'QComboBox
    *qdesigner_internal::IconThemeEnumEditor::createComboBox(QWidget
    *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-iconthemeenumeditor.html

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QComboBox]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QComboBox
    #      *qdesigner_internal::IconThemeEnumEditor::createComboBox(QWidget
    #      *parent)
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal19IconThemeEnumEditor14createComboBox'
        'EP7QWidget',
        CuteMixin._addressOf(parent),
    )
    from ..QtWidgets import QComboBox
    return QComboBox._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::IconThemeEnumEditor'

  #  A C++ qdesigner_internal::IconThemeEnumEditor Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_IconThemeEnumEditor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *qdesigner_internal::IconThemeEnumEditor::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-iconthemeenumeditor.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *qdesigner_internal::IconThemeEnumEditor::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal19IconThemeEnumEditor10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def themeEnum(self) -> int:
    """
    Calls Qt's 'int qdesigner_internal::IconThemeEnumEditor::themeEnum()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-iconthemeenumeditor.html
    """
    #  int qdesigner_internal::IconThemeEnumEditor::themeEnum() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal19IconThemeEnumEditor9themeEnumEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setThemeEnum(self, a0: int) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::IconThemeEnumEditor::setThemeEnum(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-iconthemeenumeditor.html

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void qdesigner_internal::IconThemeEnumEditor::setThemeEnum(int a0)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal19IconThemeEnumEditor12setThemeEnumEi',
        a0,
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
  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, bool)
  @overload(NoneType, bool)
  def __init__(
      self,
      parent: Optional[QWidget] = None,
      wantResetButton: bool = True,
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::IconThemeEnumEditor::IconThemeEnumEditor(QWidget
    *parent, bool wantResetButton)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-iconthemeenumeditor.html

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    wantResetButton : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  qdesigner_internal::IconThemeEnumEditor::IconThemeEnumEditor(QWidget
    #      *parent, bool wantResetButton)
    self._noteCreation(IconThemeEnumEditor, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal19IconThemeEnumEditorC1EP7QWidgetb',
        self._addressOf(parent), wantResetButton,
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

  @overload(int)
  def edited(self, a0: int) -> None:
    """
    Calls Qt's 'void qdesigner_internal::IconThemeEnumEditor::edited(int
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-iconthemeenumeditor.html#edited

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void qdesigner_internal::IconThemeEnumEditor::edited(int a0)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal19IconThemeEnumEditor6editedEi', a0,
    )

  def reset(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::IconThemeEnumEditor::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-iconthemeenumeditor.html#reset
    """
    #  void qdesigner_internal::IconThemeEnumEditor::reset()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal19IconThemeEnumEditor5resetEv',
    )
