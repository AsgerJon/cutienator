//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qtabbar.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtabbar.h>
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#include <QtGui/qcolor.h>
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QTabBar::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7QTabBar10metaObjectEv(const QTabBar *self) {
  return self->metaObject();
}

//  QString QTabBar::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QTabBar2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QTabBar::tr(s, c, n));
}

//  QTabBar::QTabBar(QWidget *parent)
extern "C" Q_DECL_EXPORT
QTabBar *ritual_ZN7QTabBarC1EP7QWidget(QWidget *parent) {
  return new QTabBar(parent);
}

//  QTabBar::~QTabBar()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBarD1Ev(QTabBar *self) {
  delete self;
}

//  Shape QTabBar::shape() const
extern "C" Q_DECL_EXPORT
QTabBar::Shape ritual_ZNK7QTabBar5shapeEv(const QTabBar *self) {
  return self->shape();
}

//  void QTabBar::setShape(Shape shape)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar8setShapeENS_5ShapeE(
    QTabBar *self,
    QTabBar::Shape shape) {
  self->setShape(shape);
}

//  int QTabBar::addTab(const QString &text)
extern "C" Q_DECL_EXPORT
int ritual_ZN7QTabBar6addTabERK7QString(QTabBar *self, const QString *text) {
  return self->addTab(*text);
}

//  int QTabBar::addTab(const QIcon &icon, const QString &text)
extern "C" Q_DECL_EXPORT
int ritual_ZN7QTabBar6addTabERK5QIconRK7QString(
    QTabBar *self,
    const QIcon *icon,
    const QString *text) {
  return self->addTab(*icon, *text);
}

//  int QTabBar::insertTab(int index, const QString &text)
extern "C" Q_DECL_EXPORT
int ritual_ZN7QTabBar9insertTabEiRK7QString(
    QTabBar *self,
    int index,
    const QString *text) {
  return self->insertTab(index, *text);
}

//  int QTabBar::insertTab(int index, const QIcon &icon, const QString &text)
extern "C" Q_DECL_EXPORT
int ritual_ZN7QTabBar9insertTabEiRK5QIconRK7QString(
    QTabBar *self,
    int index,
    const QIcon *icon,
    const QString *text) {
  return self->insertTab(index, *icon, *text);
}

//  void QTabBar::removeTab(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar9removeTabEi(QTabBar *self, int index) {
  self->removeTab(index);
}

//  void QTabBar::moveTab(int from, int to)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar7moveTabEii(QTabBar *self, int from, int to) {
  self->moveTab(from, to);
}

//  bool QTabBar::isTabEnabled(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QTabBar12isTabEnabledEi(const QTabBar *self, int index) {
  return self->isTabEnabled(index);
}

//  void QTabBar::setTabEnabled(int index, bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar13setTabEnabledEib(
    QTabBar *self,
    int index,
    bool enabled) {
  self->setTabEnabled(index, enabled);
}

//  bool QTabBar::isTabVisible(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QTabBar12isTabVisibleEi(const QTabBar *self, int index) {
  return self->isTabVisible(index);
}

//  void QTabBar::setTabVisible(int index, bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar13setTabVisibleEib(
    QTabBar *self,
    int index,
    bool visible) {
  self->setTabVisible(index, visible);
}

//  QString QTabBar::tabText(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QTabBar7tabTextEi(const QTabBar *self, int index) {
  return new QString(self->tabText(index));
}

//  void QTabBar::setTabText(int index, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar10setTabTextEiRK7QString(
    QTabBar *self,
    int index,
    const QString *text) {
  self->setTabText(index, *text);
}

//  QColor QTabBar::tabTextColor(int index) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK7QTabBar12tabTextColorEi(const QTabBar *self, int index) {
  return new QColor(self->tabTextColor(index));
}

//  void QTabBar::setTabTextColor(int index, const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar15setTabTextColorEiRK6QColor(
    QTabBar *self,
    int index,
    const QColor *color) {
  self->setTabTextColor(index, *color);
}

//  QIcon QTabBar::tabIcon(int index) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK7QTabBar7tabIconEi(const QTabBar *self, int index) {
  return new QIcon(self->tabIcon(index));
}

//  void QTabBar::setTabIcon(int index, const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar10setTabIconEiRK5QIcon(
    QTabBar *self,
    int index,
    const QIcon *icon) {
  self->setTabIcon(index, *icon);
}

//  Qt::TextElideMode QTabBar::elideMode() const
extern "C" Q_DECL_EXPORT
Qt::TextElideMode ritual_ZNK7QTabBar9elideModeEv(const QTabBar *self) {
  return self->elideMode();
}

//  void QTabBar::setElideMode(Qt::TextElideMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar12setElideModeEN2Qt13TextElideModeE(
    QTabBar *self,
    Qt::TextElideMode mode) {
  self->setElideMode(mode);
}

//  void QTabBar::setTabToolTip(int index, const QString &tip)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar13setTabToolTipEiRK7QString(
    QTabBar *self,
    int index,
    const QString *tip) {
  self->setTabToolTip(index, *tip);
}

//  QString QTabBar::tabToolTip(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QTabBar10tabToolTipEi(const QTabBar *self, int index) {
  return new QString(self->tabToolTip(index));
}

//  void QTabBar::setTabWhatsThis(int index, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar15setTabWhatsThisEiRK7QString(
    QTabBar *self,
    int index,
    const QString *text) {
  self->setTabWhatsThis(index, *text);
}

//  QString QTabBar::tabWhatsThis(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QTabBar12tabWhatsThisEi(const QTabBar *self, int index) {
  return new QString(self->tabWhatsThis(index));
}

//  void QTabBar::setTabData(int index, const QVariant &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar10setTabDataEiRK8QVariant(
    QTabBar *self,
    int index,
    const QVariant *data) {
  self->setTabData(index, *data);
}

//  QVariant QTabBar::tabData(int index) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK7QTabBar7tabDataEi(const QTabBar *self, int index) {
  return new QVariant(self->tabData(index));
}

//  QRect QTabBar::tabRect(int index) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK7QTabBar7tabRectEi(const QTabBar *self, int index) {
  return new QRect(self->tabRect(index));
}

//  int QTabBar::tabAt(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QTabBar5tabAtERK6QPoint(
    const QTabBar *self,
    const QPoint *pos) {
  return self->tabAt(*pos);
}

//  int QTabBar::currentIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QTabBar12currentIndexEv(const QTabBar *self) {
  return self->currentIndex();
}

//  int QTabBar::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QTabBar5countEv(const QTabBar *self) {
  return self->count();
}

//  QSize QTabBar::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QTabBar8sizeHintEv(const QTabBar *self) {
  return new QSize(self->sizeHint());
}

//  QSize QTabBar::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QTabBar15minimumSizeHintEv(const QTabBar *self) {
  return new QSize(self->minimumSizeHint());
}

//  void QTabBar::setDrawBase(bool drawTheBase)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar11setDrawBaseEb(QTabBar *self, bool drawTheBase) {
  self->setDrawBase(drawTheBase);
}

//  bool QTabBar::drawBase() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QTabBar8drawBaseEv(const QTabBar *self) {
  return self->drawBase();
}

//  QSize QTabBar::iconSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QTabBar8iconSizeEv(const QTabBar *self) {
  return new QSize(self->iconSize());
}

//  void QTabBar::setIconSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar11setIconSizeERK5QSize(
    QTabBar *self,
    const QSize *size) {
  self->setIconSize(*size);
}

//  bool QTabBar::usesScrollButtons() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QTabBar17usesScrollButtonsEv(const QTabBar *self) {
  return self->usesScrollButtons();
}

//  void QTabBar::setUsesScrollButtons(bool useButtons)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar20setUsesScrollButtonsEb(
    QTabBar *self,
    bool useButtons) {
  self->setUsesScrollButtons(useButtons);
}

//  bool QTabBar::tabsClosable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QTabBar12tabsClosableEv(const QTabBar *self) {
  return self->tabsClosable();
}

//  void QTabBar::setTabsClosable(bool closable)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar15setTabsClosableEb(QTabBar *self, bool closable) {
  self->setTabsClosable(closable);
}

//  void QTabBar::setTabButton(int index, ButtonPosition position, QWidget
//      *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar12setTabButtonEiNS_14ButtonPositionEP7QWidget(
    QTabBar *self,
    int index,
    QTabBar::ButtonPosition position,
    QWidget *widget) {
  self->setTabButton(index, position, widget);
}

//  QWidget *QTabBar::tabButton(int index, ButtonPosition position) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK7QTabBar9tabButtonEiNS_14ButtonPositionE(
    const QTabBar *self,
    int index,
    QTabBar::ButtonPosition position) {
  return self->tabButton(index, position);
}

//  SelectionBehavior QTabBar::selectionBehaviorOnRemove() const
extern "C" Q_DECL_EXPORT
QTabBar::SelectionBehavior ritual_ZNK7QTabBar25selectionBehaviorOnRemoveEv(
    const QTabBar *self) {
  return self->selectionBehaviorOnRemove();
}

//  void QTabBar::setSelectionBehaviorOnRemove(SelectionBehavior behavior)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar28setSelectionBehaviorOnRemoveENS_17SelectionBehaviorE(
    QTabBar *self,
    QTabBar::SelectionBehavior behavior) {
  self->setSelectionBehaviorOnRemove(behavior);
}

//  bool QTabBar::expanding() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QTabBar9expandingEv(const QTabBar *self) {
  return self->expanding();
}

//  void QTabBar::setExpanding(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar12setExpandingEb(QTabBar *self, bool enabled) {
  self->setExpanding(enabled);
}

//  bool QTabBar::isMovable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QTabBar9isMovableEv(const QTabBar *self) {
  return self->isMovable();
}

//  void QTabBar::setMovable(bool movable)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar10setMovableEb(QTabBar *self, bool movable) {
  self->setMovable(movable);
}

//  bool QTabBar::documentMode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QTabBar12documentModeEv(const QTabBar *self) {
  return self->documentMode();
}

//  void QTabBar::setDocumentMode(bool set)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar15setDocumentModeEb(QTabBar *self, bool set) {
  self->setDocumentMode(set);
}

//  bool QTabBar::autoHide() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QTabBar8autoHideEv(const QTabBar *self) {
  return self->autoHide();
}

//  void QTabBar::setAutoHide(bool hide)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar11setAutoHideEb(QTabBar *self, bool hide) {
  self->setAutoHide(hide);
}

//  bool QTabBar::changeCurrentOnDrag() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QTabBar19changeCurrentOnDragEv(const QTabBar *self) {
  return self->changeCurrentOnDrag();
}

//  void QTabBar::setChangeCurrentOnDrag(bool change)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar22setChangeCurrentOnDragEb(
    QTabBar *self,
    bool change) {
  self->setChangeCurrentOnDrag(change);
}

//  QString QTabBar::accessibleTabName(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QTabBar17accessibleTabNameEi(
    const QTabBar *self,
    int index) {
  return new QString(self->accessibleTabName(index));
}

//  void QTabBar::setAccessibleTabName(int index, const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar20setAccessibleTabNameEiRK7QString(
    QTabBar *self,
    int index,
    const QString *name) {
  self->setAccessibleTabName(index, *name);
}

//  void QTabBar::setCurrentIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QTabBar15setCurrentIndexEi(QTabBar *self, int index) {
  self->setCurrentIndex(index);
}
