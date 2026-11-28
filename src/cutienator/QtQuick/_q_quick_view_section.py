"""
QQuickViewSection binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicklistview_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickViewSection to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtQml import QQmlComponent
  from . import QQuickListView
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlComponent = WAIT['QQmlComponent']
  QQuickListView = WAIT['QQuickListView']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickViewSection(QObject):
  """
  The cute side of Qt's QQuickViewSection: a plain Python object standing in
  front of one C++ QQuickViewSection.

  It is built on the cute 'QObject', as Qt's QQuickViewSection is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickViewSection that has a ritual and that Python
  can call so far, 16 names in all: 'metaObject', 'tr', 'property',
  'setProperty', 'criteria', 'setCriteria', 'delegate', 'setDelegate',
  'sectionString', 'labelPositioning', 'setLabelPositioning',
  'sectionsChanged', 'propertyChanged', 'criteriaChanged', 'delegateChanged',
  'labelPositioningChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickViewSection::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickViewSection::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickViewSection is created at the first use, not by
    'QQuickViewSection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickViewSection.
  - Qt tells when it has removed the C++ QQuickViewSection. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickViewSection, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class LabelPositioning(CuteNum):
    """
    The enum 'QQuickViewSection::LabelPositioning' of Qt, with the 3 names Qt
    gives in it.
    """

    InlineLabels = Kee[int](1)
    CurrentLabelAtStart = Kee[int](2)
    NextLabelAtEnd = Kee[int](4)

  class SectionCriteria(CuteNum):
    """
    The enum 'QQuickViewSection::SectionCriteria' of Qt, with the 2 names Qt
    gives in it.
    """

    FullString = Kee[int](0)
    FirstCharacter = Kee[int](1)

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
    Calls Qt's 'QString QQuickViewSection::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickviewsection.html#tr

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
    #  QString QQuickViewSection::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QQuickViewSection2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickViewSection'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickViewSection::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickviewsection.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickViewSection::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickViewSection10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def property(self) -> str:
    """
    Calls Qt's 'QString QQuickViewSection::property() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickviewsection.html#property

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickViewSection::property() const
    return self.uglySide.call('ritual_ZNK17QQuickViewSection8propertyEv')

  def criteria(self) -> SectionCriteria:
    """
    Calls Qt's 'SectionCriteria QQuickViewSection::criteria() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickviewsection.html#criteria

    Returns
    -------

    SectionCriteria
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SectionCriteria(number)'
      gives.
    """
    #  SectionCriteria QQuickViewSection::criteria() const
    return QQuickViewSection.SectionCriteria(self.uglySide.call(
        'ritual_ZNK17QQuickViewSection8criteriaEv',
    ))

  def delegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickViewSection::delegate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickviewsection.html#delegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickViewSection::delegate() const
    address = self.uglySide.call('ritual_ZNK17QQuickViewSection8delegateEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def labelPositioning(self) -> int:
    """
    Calls Qt's 'int QQuickViewSection::labelPositioning() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickviewsection.html#labelPositioning
    """
    #  int QQuickViewSection::labelPositioning() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickViewSection16labelPositioningEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setProperty(self, a0: str) -> None:
    """
    Calls Qt's 'void QQuickViewSection::setProperty(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickviewsection.html#setProperty

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickViewSection::setProperty(const QString &a0)
    self.uglySide.call(
        'ritual_ZN17QQuickViewSection11setPropertyERK7QString', a0,
    )

  @overload(SectionCriteria)
  def setCriteria(self, a0: SectionCriteria) -> None:
    """
    Calls Qt's 'void QQuickViewSection::setCriteria(SectionCriteria a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickviewsection.html#setCriteria

    Parameters
    ----------

    a0 : SectionCriteria
      Passed on as its number.
    """
    #  void QQuickViewSection::setCriteria(SectionCriteria a0)
    self.uglySide.call(
        'ritual_ZN17QQuickViewSection11setCriteriaENS_15SectionCriteriaE',
        a0.value,
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setDelegate(self, delegate: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickViewSection::setDelegate(QQmlComponent
    *delegate)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickviewsection.html#setDelegate

    Parameters
    ----------

    delegate : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickViewSection::setDelegate(QQmlComponent *delegate)
    self.uglySide.call(
        'ritual_ZN17QQuickViewSection11setDelegateEP13QQmlComponent',
        self._addressOf(delegate),
    )

  @overload(int)
  def setLabelPositioning(self, pos: int) -> None:
    """
    Calls Qt's 'void QQuickViewSection::setLabelPositioning(int pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickviewsection.html#setLabelPositioning

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  void QQuickViewSection::setLabelPositioning(int pos)
    self.uglySide.call(
        'ritual_ZN17QQuickViewSection19setLabelPositioningEi', pos,
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
  @overload(QQuickListView)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickListView] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickViewSection::QQuickViewSection(QQuickListView *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickviewsection.html#QQuickViewSection

    Parameters
    ----------

    parent : Optional[QQuickListView]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickViewSection::QQuickViewSection(QQuickListView *parent)
    self._noteCreation(QQuickViewSection, lambda: Rituals.call(
        'ritual_ZN17QQuickViewSectionC1EP14QQuickListView',
        self._addressOf(parent),
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
  def sectionString(self, value: str) -> str:
    """
    Calls Qt's 'QString QQuickViewSection::sectionString(const QString
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickviewsection.html#sectionString

    Parameters
    ----------

    value : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickViewSection::sectionString(const QString &value)
    return self.uglySide.call(
        'ritual_ZN17QQuickViewSection13sectionStringERK7QString', value,
    )

  def sectionsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickViewSection::sectionsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickviewsection.html#sectionsChanged
    """
    #  void QQuickViewSection::sectionsChanged()
    self.uglySide.call('ritual_ZN17QQuickViewSection15sectionsChangedEv')

  def propertyChanged(self) -> None:
    """
    Calls Qt's 'void QQuickViewSection::propertyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickviewsection.html#propertyChanged
    """
    #  void QQuickViewSection::propertyChanged()
    self.uglySide.call('ritual_ZN17QQuickViewSection15propertyChangedEv')

  def criteriaChanged(self) -> None:
    """
    Calls Qt's 'void QQuickViewSection::criteriaChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickviewsection.html#criteriaChanged
    """
    #  void QQuickViewSection::criteriaChanged()
    self.uglySide.call('ritual_ZN17QQuickViewSection15criteriaChangedEv')

  def delegateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickViewSection::delegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickviewsection.html#delegateChanged
    """
    #  void QQuickViewSection::delegateChanged()
    self.uglySide.call('ritual_ZN17QQuickViewSection15delegateChangedEv')

  def labelPositioningChanged(self) -> None:
    """
    Calls Qt's 'void QQuickViewSection::labelPositioningChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickviewsection.html#labelPositioningChanged
    """
    #  void QQuickViewSection::labelPositioningChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickViewSection23labelPositioningChangedEv',
    )
