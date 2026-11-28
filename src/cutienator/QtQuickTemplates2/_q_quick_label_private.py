"""
QQuickLabelPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicklabel_p_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickLabelPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtGui import QAccessible
from ..QtQuick import QQuickTextPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMarginsF, QRectF
  from ..QtGui import QFont, QPalette
  from ..QtQuick import QQuickGeometryChange, QQuickItem
  from . import QQuickLabel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFont = WAIT['QFont']
  QQuickGeometryChange = WAIT['QQuickGeometryChange']
  QQuickItem = WAIT['QQuickItem']
  QQuickLabel = WAIT['QQuickLabel']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickLabelPrivate(QQuickTextPrivate):
  """
  The cute side of Qt's QQuickLabelPrivate: a plain Python object standing in
  front of one C++ QQuickLabelPrivate.

  It is built on the cute 'QQuickTextPrivate', as Qt's QQuickLabelPrivate is
  built on Qt's QQuickTextPrivate, and has everything that class has. Qt's
  QQuickLabelPrivate is built on Qt's
  QSafeQuickItemChangeListener<QQuickLabelPrivate> as well, which is not
  reflected. Qt's QQuickLabelPrivate is built on Qt's
  QAccessible::ActivationObserver as well, which is not reflected.

  What exists
  -----------

  Every function of Qt's QQuickLabelPrivate that has a ritual and that Python
  can call so far, 27 names in all: 'q_func', 'get', 'getInset',
  'getTopInset', 'getLeftInset', 'getRightInset', 'getBottomInset',
  'setTopInset', 'setLeftInset', 'setRightInset', 'setBottomInset',
  'resizeBackground', 'resolveFont', 'inheritFont', 'updateFont',
  'setFont_helper', 'textChanged', 'accessibilityActiveChanged',
  'accessibleRole', 'maybeSetAccessibleName', 'cancelBackground',
  'executeBackground', 'itemGeometryChanged', 'itemImplicitWidthChanged',
  'itemImplicitHeightChanged', 'itemDestroyed', 'defaultPalette'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickLabel *QQuickLabelPrivate::q_func() const': takes in
    Python what 'QQuickLabel *QQuickLabelPrivate::q_func()' takes.
  - Qt's 'QQuickLabelPrivate::~QQuickLabelPrivate()': the destructor: Python
    never removes a C++ QQuickLabelPrivate.

  What has no ritual
  ------------------

  1 of the 30 functions Qt declares: 1 leans on 'non-virtual thunk to
  QQuickLabelPrivate.

  What to expect
  --------------

  - The C++ QQuickLabelPrivate is created at the first use, not by
    'QQuickLabelPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickLabelPrivate.
  - Each name of Qt's QQuickLabelPrivate that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The classes Qt writes inside QQuickLabelPrivate, each a class in here as
  #  in C++.

  class ExtraData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickLabelPrivate::ExtraData: a plain Python
    object standing in front of one C++ QQuickLabelPrivate::ExtraData.

    What exists
    -----------

    No function of Qt's QQuickLabelPrivate::ExtraData yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What to expect
    --------------

    - The C++ QQuickLabelPrivate::ExtraData is created at the first use, not
      by 'QQuickLabelPrivate::ExtraData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QQuickLabelPrivate::ExtraData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickLabelPrivate::ExtraData'

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
  @overload(QQuickLabel)
  @overload(NoneType)
  def get(item: Optional[QQuickLabel]) -> Optional[QQuickLabelPrivate]:
    """
    Calls Qt's 'QQuickLabelPrivate *QQuickLabelPrivate::get(QQuickLabel
    *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabelprivate.html#get

    Parameters
    ----------

    item : Optional[QQuickLabel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickLabelPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickLabelPrivate *QQuickLabelPrivate::get(QQuickLabel *item)
    address = Rituals.call(
        'ritual_ZN18QQuickLabelPrivate3getEP11QQuickLabel',
        CuteMixin._addressOf(item),
    )
    return QQuickLabelPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickLabelPrivate'

  #  A C++ QQuickLabelPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickLabelPrivate'

  #  The functions Qt calls itself that QQuickLabelPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'itemGeometryChanged': (
          ('_ZN18QQuickLabelPrivate19itemGeometryChangedEP10QQuickItem20QQu'
           'ickGeometryChangeRK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'value', 'QtQuick:QQuickGeometryChange'),
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'itemImplicitWidthChanged': (
          ('_ZN18QQuickLabelPrivate24itemImplicitWidthChangedEP10QQuickItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemImplicitHeightChanged': (
          ('_ZN18QQuickLabelPrivate25itemImplicitHeightChangedEP10QQuickIte'
           'm',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemDestroyed': (
          ('_ZN18QQuickLabelPrivate13itemDestroyedEP10QQuickItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'defaultPalette': (
          ('_ZNK18QQuickLabelPrivate14defaultPaletteEv',
           ('address', 'value', 'QtGui:QPalette'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getInset(self) -> QMarginsF:
    """
    Calls Qt's 'QMarginsF QQuickLabelPrivate::getInset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabelprivate.html#getInset

    Returns
    -------

    QMarginsF
      A new cute QMarginsF around the copy Qt gave back. Python owns it.
    """
    #  QMarginsF QQuickLabelPrivate::getInset() const
    address = self.uglySide.call('ritual_ZNK18QQuickLabelPrivate8getInsetEv')
    from ..QtCore import QMarginsF
    return QMarginsF._cuteOwning(address)

  def getTopInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickLabelPrivate::getTopInset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabelprivate.html#getTopInset
    """
    #  qreal QQuickLabelPrivate::getTopInset() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickLabelPrivate11getTopInsetEv',
    )

  def getLeftInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickLabelPrivate::getLeftInset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabelprivate.html#getLeftInset
    """
    #  qreal QQuickLabelPrivate::getLeftInset() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickLabelPrivate12getLeftInsetEv',
    )

  def getRightInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickLabelPrivate::getRightInset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabelprivate.html#getRightInset
    """
    #  qreal QQuickLabelPrivate::getRightInset() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickLabelPrivate13getRightInsetEv',
    )

  def getBottomInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickLabelPrivate::getBottomInset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabelprivate.html#getBottomInset
    """
    #  qreal QQuickLabelPrivate::getBottomInset() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickLabelPrivate14getBottomInsetEv',
    )

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickLabelPrivate::accessibleRole()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabelprivate.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickLabelPrivate::accessibleRole() const
    ritual = 'ritual_ZNK18QQuickLabelPrivate14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QQuickLabelPrivate14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  def defaultPalette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QQuickLabelPrivate::defaultPalette() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabelprivate.html#defaultPalette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QQuickLabelPrivate::defaultPalette() const
    ritual = 'ritual_ZNK18QQuickLabelPrivate14defaultPaletteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QQuickLabelPrivate14defaultPaletteEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  @overload(float, bool)
  def setTopInset(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickLabelPrivate::setTopInset(qreal value, bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabelprivate.html#setTopInset

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickLabelPrivate::setTopInset(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN18QQuickLabelPrivate11setTopInsetEdb', value, reset,
    )

  @overload(float)
  @overload(float, bool)
  def setLeftInset(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickLabelPrivate::setLeftInset(qreal value, bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabelprivate.html#setLeftInset

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickLabelPrivate::setLeftInset(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN18QQuickLabelPrivate12setLeftInsetEdb', value, reset,
    )

  @overload(float)
  @overload(float, bool)
  def setRightInset(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickLabelPrivate::setRightInset(qreal value, bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabelprivate.html#setRightInset

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickLabelPrivate::setRightInset(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN18QQuickLabelPrivate13setRightInsetEdb', value, reset,
    )

  @overload(float)
  @overload(float, bool)
  def setBottomInset(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickLabelPrivate::setBottomInset(qreal value, bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabelprivate.html#setBottomInset

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickLabelPrivate::setBottomInset(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN18QQuickLabelPrivate14setBottomInsetEdb', value, reset,
    )

  @overload(QFont)
  def setFont_helper(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickLabelPrivate::setFont_helper(const QFont &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabelprivate.html#setFont_helper

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickLabelPrivate::setFont_helper(const QFont &font)
    self.uglySide.call(
        'ritual_ZN18QQuickLabelPrivate14setFont_helperERK5QFont',
        self._valueOf(font),
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
    Qt's 'QQuickLabelPrivate::QQuickLabelPrivate()': leans on 'non-virtual
    thunk to QQuickLabelPrivate::defaultPalette() const', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuickLabelPrivate.__init__' has no cute function yet. Qt's "
        "'QQuickLabelPrivate::QQuickLabelPrivate()': leans on 'non-virtual "
        "thunk to QQuickLabelPrivate::defaultPalette() const', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  def q_func(self) -> Optional[QQuickLabel]:
    """
    Calls Qt's 'QQuickLabel *QQuickLabelPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabelprivate.html#q_func

    Returns
    -------

    Optional[QQuickLabel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickLabel *QQuickLabelPrivate::q_func()
    address = self.uglySide.call('ritual_ZN18QQuickLabelPrivate6q_funcEv')
    from . import QQuickLabel
    return QQuickLabel._cuteAt(address)

  def resizeBackground(self) -> None:
    """
    Calls Qt's 'void QQuickLabelPrivate::resizeBackground()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabelprivate.html#resizeBackground
    """
    #  void QQuickLabelPrivate::resizeBackground()
    self.uglySide.call('ritual_ZN18QQuickLabelPrivate16resizeBackgroundEv')

  def resolveFont(self) -> None:
    """
    Calls Qt's 'void QQuickLabelPrivate::resolveFont()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabelprivate.html#resolveFont
    """
    #  void QQuickLabelPrivate::resolveFont()
    self.uglySide.call('ritual_ZN18QQuickLabelPrivate11resolveFontEv')

  @overload(QFont)
  def inheritFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickLabelPrivate::inheritFont(const QFont &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabelprivate.html#inheritFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickLabelPrivate::inheritFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN18QQuickLabelPrivate11inheritFontERK5QFont',
        self._valueOf(font),
    )

  @overload(QFont)
  def updateFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickLabelPrivate::updateFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklabelprivate.html#updateFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickLabelPrivate::updateFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN18QQuickLabelPrivate10updateFontERK5QFont',
        self._valueOf(font),
    )

  @overload(str)
  def textChanged(self, text: str) -> None:
    """
    Calls Qt's 'void QQuickLabelPrivate::textChanged(const QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabelprivate.html#textChanged

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickLabelPrivate::textChanged(const QString &text)
    self.uglySide.call(
        'ritual_ZN18QQuickLabelPrivate11textChangedERK7QString', text,
    )

  @overload(bool)
  def accessibilityActiveChanged(self, active: bool) -> None:
    """
    Calls Qt's 'void QQuickLabelPrivate::accessibilityActiveChanged(bool
    active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabelprivate.html#accessibilityActiveChanged

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QQuickLabelPrivate::accessibilityActiveChanged(bool active)
    ritual = 'ritual_ZN18QQuickLabelPrivate26accessibilityActiveChangedEb'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuickLabelPrivate26accessibilityActiveChangedEb')
    self.uglySide.call(ritual, active)

  @overload(str)
  def maybeSetAccessibleName(self, name: str) -> None:
    """
    Calls Qt's 'void QQuickLabelPrivate::maybeSetAccessibleName(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabelprivate.html#maybeSetAccessibleName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickLabelPrivate::maybeSetAccessibleName(const QString &name)
    self.uglySide.call(
        'ritual_ZN18QQuickLabelPrivate22maybeSetAccessibleNameERK7QString',
        name,
    )

  def cancelBackground(self) -> None:
    """
    Calls Qt's 'void QQuickLabelPrivate::cancelBackground()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabelprivate.html#cancelBackground
    """
    #  void QQuickLabelPrivate::cancelBackground()
    self.uglySide.call('ritual_ZN18QQuickLabelPrivate16cancelBackgroundEv')

  @overload()
  @overload(bool)
  def executeBackground(self, complete: bool = False) -> None:
    """
    Calls Qt's 'void QQuickLabelPrivate::executeBackground(bool complete)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabelprivate.html#executeBackground

    Parameters
    ----------

    complete : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickLabelPrivate::executeBackground(bool complete)
    self.uglySide.call(
        'ritual_ZN18QQuickLabelPrivate17executeBackgroundEb', complete,
    )

  @overload(QQuickItem, QQuickGeometryChange, QRectF)
  @overload(NoneType, QQuickGeometryChange, QRectF)
  def itemGeometryChanged(
      self,
      item: Optional[QQuickItem],
      change: QQuickGeometryChange,
      diff: QRectF,
  ) -> None:
    """
    Calls Qt's 'void QQuickLabelPrivate::itemGeometryChanged(QQuickItem
    *item, QQuickGeometryChange change, const QRectF &diff)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabelprivate.html#itemGeometryChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    change : QQuickGeometryChange
      Passed on as a value: Qt reads the C++ QQuickGeometryChange, which
      stays Python's own.

    diff : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickLabelPrivate::itemGeometryChanged(QQuickItem *item,
    #      QQuickGeometryChange change, const QRectF &diff)
    ritual = (
        'ritual_ZN18QQuickLabelPrivate19itemGeometryChangedEP10QQuickItem20'
        'QQuickGeometryChangeRK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuickLabelPrivate19itemGeometryChangedEP10QQuick'
          'Item20QQuickGeometryChangeRK6QRectF')
    self.uglySide.call(
        ritual,
        self._addressOf(item), self._valueOf(change), self._valueOf(diff),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitWidthChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickLabelPrivate::itemImplicitWidthChanged(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabelprivate.html#itemImplicitWidthChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLabelPrivate::itemImplicitWidthChanged(QQuickItem *item)
    ritual = (
        'ritual_ZN18QQuickLabelPrivate24itemImplicitWidthChangedEP10QQuickI'
        'tem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuickLabelPrivate24itemImplicitWidthChangedEP10Q'
          'QuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitHeightChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickLabelPrivate::itemImplicitHeightChanged(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabelprivate.html#itemImplicitHeightChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLabelPrivate::itemImplicitHeightChanged(QQuickItem *item)
    ritual = (
        'ritual_ZN18QQuickLabelPrivate25itemImplicitHeightChangedEP10QQuick'
        'Item')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuickLabelPrivate25itemImplicitHeightChangedEP10'
          'QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemDestroyed(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickLabelPrivate::itemDestroyed(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabelprivate.html#itemDestroyed

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLabelPrivate::itemDestroyed(QQuickItem *item)
    ritual = 'ritual_ZN18QQuickLabelPrivate13itemDestroyedEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuickLabelPrivate13itemDestroyedEP10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))
