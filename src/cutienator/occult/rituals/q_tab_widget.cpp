//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qtabwidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtabwidget.h>
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QTabWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QTabWidget10metaObjectEv(
    const QTabWidget *self) {
  return self->metaObject();
}

//  QString QTabWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QTabWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTabWidget::tr(s, c, n));
}

//  QTabWidget::QTabWidget(QWidget *parent)
extern "C" Q_DECL_EXPORT
QTabWidget *ritual_ZN10QTabWidgetC1EP7QWidget(QWidget *parent) {
  return new QTabWidget(parent);
}

//  QTabWidget::~QTabWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidgetD1Ev(QTabWidget *self) {
  delete self;
}

//  int QTabWidget::addTab(QWidget *widget, const QString &a1)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QTabWidget6addTabEP7QWidgetRK7QString(
    QTabWidget *self,
    QWidget *widget,
    const QString *a1) {
  return self->addTab(widget, *a1);
}

//  int QTabWidget::addTab(QWidget *widget, const QIcon &icon, const QString
//      &label)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QTabWidget6addTabEP7QWidgetRK5QIconRK7QString(
    QTabWidget *self,
    QWidget *widget,
    const QIcon *icon,
    const QString *label) {
  return self->addTab(widget, *icon, *label);
}

//  int QTabWidget::insertTab(int index, QWidget *widget, const QString &a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QTabWidget9insertTabEiP7QWidgetRK7QString(
    QTabWidget *self,
    int index,
    QWidget *widget,
    const QString *a2) {
  return self->insertTab(index, widget, *a2);
}

//  int QTabWidget::insertTab(int index, QWidget *widget, const QIcon &icon,
//      const QString &label)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QTabWidget9insertTabEiP7QWidgetRK5QIconRK7QString(
    QTabWidget *self,
    int index,
    QWidget *widget,
    const QIcon *icon,
    const QString *label) {
  return self->insertTab(index, widget, *icon, *label);
}

//  void QTabWidget::removeTab(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget9removeTabEi(QTabWidget *self, int index) {
  self->removeTab(index);
}

//  bool QTabWidget::isTabEnabled(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTabWidget12isTabEnabledEi(
    const QTabWidget *self,
    int index) {
  return self->isTabEnabled(index);
}

//  void QTabWidget::setTabEnabled(int index, bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget13setTabEnabledEib(
    QTabWidget *self,
    int index,
    bool enabled) {
  self->setTabEnabled(index, enabled);
}

//  bool QTabWidget::isTabVisible(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTabWidget12isTabVisibleEi(
    const QTabWidget *self,
    int index) {
  return self->isTabVisible(index);
}

//  void QTabWidget::setTabVisible(int index, bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget13setTabVisibleEib(
    QTabWidget *self,
    int index,
    bool visible) {
  self->setTabVisible(index, visible);
}

//  QString QTabWidget::tabText(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QTabWidget7tabTextEi(
    const QTabWidget *self,
    int index) {
  return new QString(self->tabText(index));
}

//  void QTabWidget::setTabText(int index, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget10setTabTextEiRK7QString(
    QTabWidget *self,
    int index,
    const QString *text) {
  self->setTabText(index, *text);
}

//  QIcon QTabWidget::tabIcon(int index) const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK10QTabWidget7tabIconEi(const QTabWidget *self, int index) {
  return new QIcon(self->tabIcon(index));
}

//  void QTabWidget::setTabIcon(int index, const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget10setTabIconEiRK5QIcon(
    QTabWidget *self,
    int index,
    const QIcon *icon) {
  self->setTabIcon(index, *icon);
}

//  void QTabWidget::setTabToolTip(int index, const QString &tip)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget13setTabToolTipEiRK7QString(
    QTabWidget *self,
    int index,
    const QString *tip) {
  self->setTabToolTip(index, *tip);
}

//  QString QTabWidget::tabToolTip(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QTabWidget10tabToolTipEi(
    const QTabWidget *self,
    int index) {
  return new QString(self->tabToolTip(index));
}

//  void QTabWidget::setTabWhatsThis(int index, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget15setTabWhatsThisEiRK7QString(
    QTabWidget *self,
    int index,
    const QString *text) {
  self->setTabWhatsThis(index, *text);
}

//  QString QTabWidget::tabWhatsThis(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QTabWidget12tabWhatsThisEi(
    const QTabWidget *self,
    int index) {
  return new QString(self->tabWhatsThis(index));
}

//  int QTabWidget::currentIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTabWidget12currentIndexEv(const QTabWidget *self) {
  return self->currentIndex();
}

//  QWidget *QTabWidget::currentWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK10QTabWidget13currentWidgetEv(const QTabWidget *self) {
  return self->currentWidget();
}

//  QWidget *QTabWidget::widget(int index) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK10QTabWidget6widgetEi(const QTabWidget *self, int index) {
  return self->widget(index);
}

//  int QTabWidget::indexOf(const QWidget *widget) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTabWidget7indexOfEPK7QWidget(
    const QTabWidget *self,
    const QWidget *widget) {
  return self->indexOf(widget);
}

//  int QTabWidget::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTabWidget5countEv(const QTabWidget *self) {
  return self->count();
}

//  TabPosition QTabWidget::tabPosition() const
extern "C" Q_DECL_EXPORT
QTabWidget::TabPosition ritual_ZNK10QTabWidget11tabPositionEv(
    const QTabWidget *self) {
  return self->tabPosition();
}

//  void QTabWidget::setTabPosition(TabPosition position)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget14setTabPositionENS_11TabPositionE(
    QTabWidget *self,
    QTabWidget::TabPosition position) {
  self->setTabPosition(position);
}

//  bool QTabWidget::tabsClosable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTabWidget12tabsClosableEv(const QTabWidget *self) {
  return self->tabsClosable();
}

//  void QTabWidget::setTabsClosable(bool closeable)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget15setTabsClosableEb(
    QTabWidget *self,
    bool closeable) {
  self->setTabsClosable(closeable);
}

//  bool QTabWidget::isMovable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTabWidget9isMovableEv(const QTabWidget *self) {
  return self->isMovable();
}

//  void QTabWidget::setMovable(bool movable)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget10setMovableEb(QTabWidget *self, bool movable) {
  self->setMovable(movable);
}

//  TabShape QTabWidget::tabShape() const
extern "C" Q_DECL_EXPORT
QTabWidget::TabShape ritual_ZNK10QTabWidget8tabShapeEv(
    const QTabWidget *self) {
  return self->tabShape();
}

//  void QTabWidget::setTabShape(TabShape s)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget11setTabShapeENS_8TabShapeE(
    QTabWidget *self,
    QTabWidget::TabShape s) {
  self->setTabShape(s);
}

//  QSize QTabWidget::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10QTabWidget8sizeHintEv(const QTabWidget *self) {
  return new QSize(self->sizeHint());
}

//  QSize QTabWidget::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10QTabWidget15minimumSizeHintEv(const QTabWidget *self) {
  return new QSize(self->minimumSizeHint());
}

//  int QTabWidget::heightForWidth(int width) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTabWidget14heightForWidthEi(
    const QTabWidget *self,
    int width) {
  return self->heightForWidth(width);
}

//  bool QTabWidget::hasHeightForWidth() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTabWidget17hasHeightForWidthEv(const QTabWidget *self) {
  return self->hasHeightForWidth();
}

//  void QTabWidget::setCornerWidget(QWidget *w, Qt::Corner corner)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget15setCornerWidgetEP7QWidgetN2Qt6CornerE(
    QTabWidget *self,
    QWidget *w,
    Qt::Corner corner) {
  self->setCornerWidget(w, corner);
}

//  QWidget *QTabWidget::cornerWidget(Qt::Corner corner) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK10QTabWidget12cornerWidgetEN2Qt6CornerE(
    const QTabWidget *self,
    Qt::Corner corner) {
  return self->cornerWidget(corner);
}

//  Qt::TextElideMode QTabWidget::elideMode() const
extern "C" Q_DECL_EXPORT
Qt::TextElideMode ritual_ZNK10QTabWidget9elideModeEv(
    const QTabWidget *self) {
  return self->elideMode();
}

//  void QTabWidget::setElideMode(Qt::TextElideMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget12setElideModeEN2Qt13TextElideModeE(
    QTabWidget *self,
    Qt::TextElideMode mode) {
  self->setElideMode(mode);
}

//  QSize QTabWidget::iconSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10QTabWidget8iconSizeEv(const QTabWidget *self) {
  return new QSize(self->iconSize());
}

//  void QTabWidget::setIconSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget11setIconSizeERK5QSize(
    QTabWidget *self,
    const QSize *size) {
  self->setIconSize(*size);
}

//  bool QTabWidget::usesScrollButtons() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTabWidget17usesScrollButtonsEv(const QTabWidget *self) {
  return self->usesScrollButtons();
}

//  void QTabWidget::setUsesScrollButtons(bool useButtons)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget20setUsesScrollButtonsEb(
    QTabWidget *self,
    bool useButtons) {
  self->setUsesScrollButtons(useButtons);
}

//  bool QTabWidget::documentMode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTabWidget12documentModeEv(const QTabWidget *self) {
  return self->documentMode();
}

//  void QTabWidget::setDocumentMode(bool set)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget15setDocumentModeEb(QTabWidget *self, bool set) {
  self->setDocumentMode(set);
}

//  bool QTabWidget::tabBarAutoHide() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTabWidget14tabBarAutoHideEv(const QTabWidget *self) {
  return self->tabBarAutoHide();
}

//  void QTabWidget::setTabBarAutoHide(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget17setTabBarAutoHideEb(
    QTabWidget *self,
    bool enabled) {
  self->setTabBarAutoHide(enabled);
}

//  void QTabWidget::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget5clearEv(QTabWidget *self) {
  self->clear();
}

//  QTabBar *QTabWidget::tabBar() const
extern "C" Q_DECL_EXPORT
QTabBar *ritual_ZNK10QTabWidget6tabBarEv(const QTabWidget *self) {
  return self->tabBar();
}

//  void QTabWidget::setCurrentIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget15setCurrentIndexEi(QTabWidget *self, int index) {
  self->setCurrentIndex(index);
}

//  void QTabWidget::setCurrentWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTabWidget16setCurrentWidgetEP7QWidget(
    QTabWidget *self,
    QWidget *widget) {
  self->setCurrentWidget(widget);
}
