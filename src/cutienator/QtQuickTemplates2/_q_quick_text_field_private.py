"""
QQuickTextFieldPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktextfield_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickTextFieldPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtQuick import QQuickItemChangeListener, QQuickTextInputPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMarginsF, QRectF
  from ..QtGui import QFont, QPalette
  from ..QtQuick import QQuickGeometryChange, QQuickItem
  from . import QQuickTextField
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFont = WAIT['QFont']
  QQuickGeometryChange = WAIT['QQuickGeometryChange']
  QQuickItem = WAIT['QQuickItem']
  QQuickTextField = WAIT['QQuickTextField']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTextFieldPrivate(QQuickTextInputPrivate, QQuickItemChangeListener):
  """
  The cute side of Qt's QQuickTextFieldPrivate: a plain Python object
  standing in front of one C++ QQuickTextFieldPrivate.

  It is built on the cute 'QQuickTextInputPrivate', as Qt's
  QQuickTextFieldPrivate is built on Qt's QQuickTextInputPrivate, and has
  everything that class has. It is built on the cute
  'QQuickItemChangeListener' as well, as Qt's QQuickTextFieldPrivate is built
  on Qt's QQuickItemChangeListener too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTextFieldPrivate that has a ritual and that
  Python can call so far, 31 names in all: 'q_func', 'get', 'getInset',
  'getTopInset', 'getLeftInset', 'getRightInset', 'getBottomInset',
  'setTopInset', 'setLeftInset', 'setRightInset', 'setBottomInset',
  'resizeBackground', 'resolveFont', 'inheritFont', 'updateFont',
  'setFont_helper', 'updateHoverEnabled', 'getImplicitWidth',
  'getImplicitHeight', 'implicitWidthChanged', 'implicitHeightChanged',
  'readOnlyChanged', 'accessibilityActiveChanged', 'cancelBackground',
  'executeBackground', 'itemGeometryChanged', 'itemImplicitWidthChanged',
  'itemImplicitHeightChanged', 'itemDestroyed', 'defaultPalette',
  'setLastFocusChangeReason'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickTextField *QQuickTextFieldPrivate::q_func() const':
    takes in Python what 'QQuickTextField *QQuickTextFieldPrivate::q_func()'
    takes.
  - Qt's 'QQuickTextFieldPrivate::~QQuickTextFieldPrivate()': the destructor:
    Python never removes a C++ QQuickTextFieldPrivate.

  What has no ritual
  ------------------

  1 of the 34 functions Qt declares: 1 leans on 'non-virtual thunk to
  QQuickTextFieldPrivate.

  What to expect
  --------------

  - The C++ QQuickTextFieldPrivate is created at the first use, not by
    'QQuickTextFieldPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTextFieldPrivate.
  - Each name of Qt's QQuickTextFieldPrivate that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The classes Qt writes inside QQuickTextFieldPrivate, each a class in
  #  here as in C++.

  class ExtraData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickTextFieldPrivate::ExtraData: a plain Python
    object standing in front of one C++ QQuickTextFieldPrivate::ExtraData.

    C++ hands a QQuickTextFieldPrivate::ExtraData around as a copy, so every
    C++ QQuickTextFieldPrivate::ExtraData behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QQuickTextFieldPrivate::ExtraData yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickTextFieldPrivate::ExtraData::~ExtraData()': the destructor:
      Python removes its C++ QQuickTextFieldPrivate::ExtraData by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QQuickTextFieldPrivate::ExtraData is created at the first use,
      not by 'QQuickTextFieldPrivate::ExtraData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickTextFieldPrivate::ExtraData back gives a copy
      the ritual made for Python, in a new cute
      QQuickTextFieldPrivate::ExtraData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickTextFieldPrivate::ExtraData'

    #  Qt's '~QQuickTextFieldPrivate::ExtraData()'. Naming it makes this a
    #  value class: Python owns every C++ QQuickTextFieldPrivate::ExtraData
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN22QQuickTextFieldPrivate9ExtraDataD1Ev'

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
  @overload(QQuickTextField)
  @overload(NoneType)
  def get(
      item: Optional[QQuickTextField],
  ) -> Optional[QQuickTextFieldPrivate]:
    """
    Calls Qt's 'QQuickTextFieldPrivate
    *QQuickTextFieldPrivate::get(QQuickTextField *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextfieldprivate.html#get

    Parameters
    ----------

    item : Optional[QQuickTextField]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickTextFieldPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextFieldPrivate *QQuickTextFieldPrivate::get(QQuickTextField
    #      *item)
    address = Rituals.call(
        'ritual_ZN22QQuickTextFieldPrivate3getEP15QQuickTextField',
        CuteMixin._addressOf(item),
    )
    return QQuickTextFieldPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTextFieldPrivate'

  #  Qt's QQuickTextFieldPrivate is built on more than one class. The part of
  #  a C++ QQuickTextFieldPrivate that belongs to a class after the first
  #  begins somewhere inside the object, and the ritual named for that class
  #  gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQuickItemChangeListener':
          'ritual_cast_QQuickTextFieldPrivate_QQuickItemChangeListener',
  }

  #  A C++ QQuickTextFieldPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickTextFieldPrivate'

  #  The functions Qt calls itself that QQuickTextFieldPrivate is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'defaultPalette': (
          ('_ZNK22QQuickTextFieldPrivate14defaultPaletteEv',
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
    Calls Qt's 'QMarginsF QQuickTextFieldPrivate::getInset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfieldprivate.html#getInset

    Returns
    -------

    QMarginsF
      A new cute QMarginsF around the copy Qt gave back. Python owns it.
    """
    #  QMarginsF QQuickTextFieldPrivate::getInset() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickTextFieldPrivate8getInsetEv',
    )
    from ..QtCore import QMarginsF
    return QMarginsF._cuteOwning(address)

  def getTopInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextFieldPrivate::getTopInset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfieldprivate.html#getTopInset
    """
    #  qreal QQuickTextFieldPrivate::getTopInset() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTextFieldPrivate11getTopInsetEv',
    )

  def getLeftInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextFieldPrivate::getLeftInset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfieldprivate.html#getLeftInset
    """
    #  qreal QQuickTextFieldPrivate::getLeftInset() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTextFieldPrivate12getLeftInsetEv',
    )

  def getRightInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextFieldPrivate::getRightInset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfieldprivate.html#getRightInset
    """
    #  qreal QQuickTextFieldPrivate::getRightInset() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTextFieldPrivate13getRightInsetEv',
    )

  def getBottomInset(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextFieldPrivate::getBottomInset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfieldprivate.html#getBottomInset
    """
    #  qreal QQuickTextFieldPrivate::getBottomInset() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTextFieldPrivate14getBottomInsetEv',
    )

  def getImplicitWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextFieldPrivate::getImplicitWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfieldprivate.html#getImplicitWidth
    """
    #  qreal QQuickTextFieldPrivate::getImplicitWidth() const
    ritual = 'ritual_ZNK22QQuickTextFieldPrivate16getImplicitWidthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QQuickTextFieldPrivate16getImplicitWidthEv'
    return self.uglySide.call(ritual)

  def getImplicitHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickTextFieldPrivate::getImplicitHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfieldprivate.html#getImplicitHeight
    """
    #  qreal QQuickTextFieldPrivate::getImplicitHeight() const
    ritual = 'ritual_ZNK22QQuickTextFieldPrivate17getImplicitHeightEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QQuickTextFieldPrivate17getImplicitHeightEv'
    return self.uglySide.call(ritual)

  def defaultPalette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QQuickTextFieldPrivate::defaultPalette() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfieldprivate.html#defaultPalette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QQuickTextFieldPrivate::defaultPalette() const
    ritual = 'ritual_ZNK22QQuickTextFieldPrivate14defaultPaletteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QQuickTextFieldPrivate14defaultPaletteEv'
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
    Calls Qt's 'void QQuickTextFieldPrivate::setTopInset(qreal value, bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfieldprivate.html#setTopInset

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickTextFieldPrivate::setTopInset(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN22QQuickTextFieldPrivate11setTopInsetEdb', value, reset,
    )

  @overload(float)
  @overload(float, bool)
  def setLeftInset(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickTextFieldPrivate::setLeftInset(qreal value, bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfieldprivate.html#setLeftInset

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickTextFieldPrivate::setLeftInset(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN22QQuickTextFieldPrivate12setLeftInsetEdb', value, reset,
    )

  @overload(float)
  @overload(float, bool)
  def setRightInset(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickTextFieldPrivate::setRightInset(qreal value, bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfieldprivate.html#setRightInset

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickTextFieldPrivate::setRightInset(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN22QQuickTextFieldPrivate13setRightInsetEdb', value, reset,
    )

  @overload(float)
  @overload(float, bool)
  def setBottomInset(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickTextFieldPrivate::setBottomInset(qreal value, bool
    reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfieldprivate.html#setBottomInset

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickTextFieldPrivate::setBottomInset(qreal value, bool reset)
    self.uglySide.call(
        'ritual_ZN22QQuickTextFieldPrivate14setBottomInsetEdb', value, reset,
    )

  @overload(QFont)
  def setFont_helper(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickTextFieldPrivate::setFont_helper(const QFont
    &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfieldprivate.html#setFont_helper

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickTextFieldPrivate::setFont_helper(const QFont &font)
    self.uglySide.call(
        'ritual_ZN22QQuickTextFieldPrivate14setFont_helperERK5QFont',
        self._valueOf(font),
    )

  @overload(Qt.FocusReason)
  def setLastFocusChangeReason(self, reason: Qt.FocusReason) -> bool:
    """
    Calls Qt's 'bool
    QQuickTextFieldPrivate::setLastFocusChangeReason(Qt::FocusReason
    reason)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfieldprivate.html

    Parameters
    ----------

    reason : Qt.FocusReason
      Passed on as its number.
    """
    #  bool QQuickTextFieldPrivate::setLastFocusChangeReason(Qt::FocusReason
    #      reason)
    ritual = (
        'ritual_ZN22QQuickTextFieldPrivate24setLastFocusChangeReasonEN2Qt11'
        'FocusReasonE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickTextFieldPrivate24setLastFocusChangeReasonE'
          'N2Qt11FocusReasonE')
    return self.uglySide.call(ritual, reason.value)

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
    Qt's 'QQuickTextFieldPrivate::QQuickTextFieldPrivate()': leans on
    'non-virtual thunk to QQuickTextFieldPrivate::defaultPalette() const',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickTextFieldPrivate.__init__' has no cute function yet. Qt's "
        "'QQuickTextFieldPrivate::QQuickTextFieldPrivate()': leans on "
        "'non-virtual thunk to QQuickTextFieldPrivate::defaultPalette() "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  def q_func(self) -> Optional[QQuickTextField]:
    """
    Calls Qt's 'QQuickTextField *QQuickTextFieldPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextfieldprivate.html#q_func

    Returns
    -------

    Optional[QQuickTextField]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextField *QQuickTextFieldPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QQuickTextFieldPrivate6q_funcEv',
    )
    from . import QQuickTextField
    return QQuickTextField._cuteAt(address)

  def resizeBackground(self) -> None:
    """
    Calls Qt's 'void QQuickTextFieldPrivate::resizeBackground()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfieldprivate.html#resizeBackground
    """
    #  void QQuickTextFieldPrivate::resizeBackground()
    self.uglySide.call(
        'ritual_ZN22QQuickTextFieldPrivate16resizeBackgroundEv',
    )

  def resolveFont(self) -> None:
    """
    Calls Qt's 'void QQuickTextFieldPrivate::resolveFont()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfieldprivate.html#resolveFont
    """
    #  void QQuickTextFieldPrivate::resolveFont()
    self.uglySide.call('ritual_ZN22QQuickTextFieldPrivate11resolveFontEv')

  @overload(QFont)
  def inheritFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickTextFieldPrivate::inheritFont(const QFont &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfieldprivate.html#inheritFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickTextFieldPrivate::inheritFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN22QQuickTextFieldPrivate11inheritFontERK5QFont',
        self._valueOf(font),
    )

  @overload(QFont)
  def updateFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickTextFieldPrivate::updateFont(const QFont &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfieldprivate.html#updateFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickTextFieldPrivate::updateFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN22QQuickTextFieldPrivate10updateFontERK5QFont',
        self._valueOf(font),
    )

  @overload(bool, bool)
  def updateHoverEnabled(self, h: bool, e: bool) -> None:
    """
    Calls Qt's 'void QQuickTextFieldPrivate::updateHoverEnabled(bool h, bool
    e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfieldprivate.html#updateHoverEnabled

    Parameters
    ----------

    h : bool
      Passed on as it is.

    e : bool
      Passed on as it is.
    """
    #  void QQuickTextFieldPrivate::updateHoverEnabled(bool h, bool e)
    self.uglySide.call(
        'ritual_ZN22QQuickTextFieldPrivate18updateHoverEnabledEbb', h, e,
    )

  def implicitWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextFieldPrivate::implicitWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfieldprivate.html#implicitWidthChanged
    """
    #  void QQuickTextFieldPrivate::implicitWidthChanged()
    ritual = 'ritual_ZN22QQuickTextFieldPrivate20implicitWidthChangedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickTextFieldPrivate20implicitWidthChangedEv')
    self.uglySide.call(ritual)

  def implicitHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextFieldPrivate::implicitHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfieldprivate.html#implicitHeightChanged
    """
    #  void QQuickTextFieldPrivate::implicitHeightChanged()
    ritual = 'ritual_ZN22QQuickTextFieldPrivate21implicitHeightChangedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickTextFieldPrivate21implicitHeightChangedEv')
    self.uglySide.call(ritual)

  @overload(bool)
  def readOnlyChanged(self, isReadOnly: bool) -> None:
    """
    Calls Qt's 'void QQuickTextFieldPrivate::readOnlyChanged(bool
    isReadOnly)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfieldprivate.html#readOnlyChanged

    Parameters
    ----------

    isReadOnly : bool
      Passed on as it is.
    """
    #  void QQuickTextFieldPrivate::readOnlyChanged(bool isReadOnly)
    ritual = 'ritual_ZN22QQuickTextFieldPrivate15readOnlyChangedEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickTextFieldPrivate15readOnlyChangedEb'
    self.uglySide.call(ritual, isReadOnly)

  @overload(bool)
  def accessibilityActiveChanged(self, active: bool) -> None:
    """
    Calls Qt's 'void QQuickTextFieldPrivate::accessibilityActiveChanged(bool
    active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfieldprivate.html

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QQuickTextFieldPrivate::accessibilityActiveChanged(bool active)
    ritual = (
        'ritual_ZN22QQuickTextFieldPrivate26accessibilityActiveChangedEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickTextFieldPrivate26accessibilityActiveChange'
          'dEb')
    self.uglySide.call(ritual, active)

  def cancelBackground(self) -> None:
    """
    Calls Qt's 'void QQuickTextFieldPrivate::cancelBackground()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfieldprivate.html#cancelBackground
    """
    #  void QQuickTextFieldPrivate::cancelBackground()
    self.uglySide.call(
        'ritual_ZN22QQuickTextFieldPrivate16cancelBackgroundEv',
    )

  @overload()
  @overload(bool)
  def executeBackground(self, complete: bool = False) -> None:
    """
    Calls Qt's 'void QQuickTextFieldPrivate::executeBackground(bool
    complete)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfieldprivate.html#executeBackground

    Parameters
    ----------

    complete : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickTextFieldPrivate::executeBackground(bool complete)
    self.uglySide.call(
        'ritual_ZN22QQuickTextFieldPrivate17executeBackgroundEb', complete,
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
    Calls Qt's 'void QQuickTextFieldPrivate::itemGeometryChanged(QQuickItem
    *item, QQuickGeometryChange change, const QRectF &diff)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfieldprivate.html#itemGeometryChanged

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
    #  void QQuickTextFieldPrivate::itemGeometryChanged(QQuickItem *item,
    #      QQuickGeometryChange change, const QRectF &diff)
    ritual = (
        'ritual_ZN22QQuickTextFieldPrivate19itemGeometryChangedEP10QQuickIt'
        'em20QQuickGeometryChangeRK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickTextFieldPrivate19itemGeometryChangedEP10QQ'
          'uickItem20QQuickGeometryChangeRK6QRectF')
    self.uglySide.call(
        ritual,
        self._addressOf(item), self._valueOf(change), self._valueOf(diff),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitWidthChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickTextFieldPrivate::itemImplicitWidthChanged(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfieldprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextFieldPrivate::itemImplicitWidthChanged(QQuickItem
    #      *item)
    ritual = (
        'ritual_ZN22QQuickTextFieldPrivate24itemImplicitWidthChangedEP10QQu'
        'ickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickTextFieldPrivate24itemImplicitWidthChangedE'
          'P10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitHeightChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickTextFieldPrivate::itemImplicitHeightChanged(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfieldprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextFieldPrivate::itemImplicitHeightChanged(QQuickItem
    #      *item)
    ritual = (
        'ritual_ZN22QQuickTextFieldPrivate25itemImplicitHeightChangedEP10QQ'
        'uickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickTextFieldPrivate25itemImplicitHeightChanged'
          'EP10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemDestroyed(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickTextFieldPrivate::itemDestroyed(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextfieldprivate.html#itemDestroyed

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextFieldPrivate::itemDestroyed(QQuickItem *item)
    ritual = 'ritual_ZN22QQuickTextFieldPrivate13itemDestroyedEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickTextFieldPrivate13itemDestroyedEP10QQuickIt'
          'em')
    self.uglySide.call(ritual, self._addressOf(item))
