//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qmdiarea.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qmdiarea.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtGui/qbrush.h>

//  const QMetaObject *QMdiArea::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8QMdiArea10metaObjectEv(const QMdiArea *self) {
  return self->metaObject();
}

//  QString QMdiArea::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QMdiArea2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QMdiArea::tr(s, c, n));
}

//  QMdiArea::QMdiArea(QWidget *parent)
extern "C" Q_DECL_EXPORT
QMdiArea *ritual_ZN8QMdiAreaC1EP7QWidget(QWidget *parent) {
  return new QMdiArea(parent);
}

//  QMdiArea::~QMdiArea()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiAreaD1Ev(QMdiArea *self) {
  delete self;
}

//  QSize QMdiArea::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK8QMdiArea8sizeHintEv(const QMdiArea *self) {
  return new QSize(self->sizeHint());
}

//  QSize QMdiArea::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK8QMdiArea15minimumSizeHintEv(const QMdiArea *self) {
  return new QSize(self->minimumSizeHint());
}

//  QMdiSubWindow *QMdiArea::currentSubWindow() const
extern "C" Q_DECL_EXPORT
QMdiSubWindow *ritual_ZNK8QMdiArea16currentSubWindowEv(
    const QMdiArea *self) {
  return self->currentSubWindow();
}

//  QMdiSubWindow *QMdiArea::activeSubWindow() const
extern "C" Q_DECL_EXPORT
QMdiSubWindow *ritual_ZNK8QMdiArea15activeSubWindowEv(const QMdiArea *self) {
  return self->activeSubWindow();
}

//  QMdiSubWindow *QMdiArea::addSubWindow(QWidget *widget, Qt::WindowFlags
//      flags)
extern "C" Q_DECL_EXPORT
QMdiSubWindow *ritual_ZN8QMdiArea12addSubWindowEP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QMdiArea *self,
    QWidget *widget,
    int flags) {
  return self->addSubWindow(widget, QFlags<Qt::WindowType>::fromInt(flags));
}

//  void QMdiArea::removeSubWindow(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea15removeSubWindowEP7QWidget(
    QMdiArea *self,
    QWidget *widget) {
  self->removeSubWindow(widget);
}

//  QBrush QMdiArea::background() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK8QMdiArea10backgroundEv(const QMdiArea *self) {
  return new QBrush(self->background());
}

//  void QMdiArea::setBackground(const QBrush &background)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea13setBackgroundERK6QBrush(
    QMdiArea *self,
    const QBrush *background) {
  self->setBackground(*background);
}

//  WindowOrder QMdiArea::activationOrder() const
extern "C" Q_DECL_EXPORT
QMdiArea::WindowOrder ritual_ZNK8QMdiArea15activationOrderEv(
    const QMdiArea *self) {
  return self->activationOrder();
}

//  void QMdiArea::setActivationOrder(WindowOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea18setActivationOrderENS_11WindowOrderE(
    QMdiArea *self,
    QMdiArea::WindowOrder order) {
  self->setActivationOrder(order);
}

//  void QMdiArea::setOption(AreaOption option, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea9setOptionENS_10AreaOptionEb(
    QMdiArea *self,
    QMdiArea::AreaOption option,
    bool on) {
  self->setOption(option, on);
}

//  bool QMdiArea::testOption(AreaOption opton) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QMdiArea10testOptionENS_10AreaOptionE(
    const QMdiArea *self,
    QMdiArea::AreaOption opton) {
  return self->testOption(opton);
}

//  void QMdiArea::setViewMode(ViewMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea11setViewModeENS_8ViewModeE(
    QMdiArea *self,
    QMdiArea::ViewMode mode) {
  self->setViewMode(mode);
}

//  ViewMode QMdiArea::viewMode() const
extern "C" Q_DECL_EXPORT
QMdiArea::ViewMode ritual_ZNK8QMdiArea8viewModeEv(const QMdiArea *self) {
  return self->viewMode();
}

//  bool QMdiArea::documentMode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QMdiArea12documentModeEv(const QMdiArea *self) {
  return self->documentMode();
}

//  void QMdiArea::setDocumentMode(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea15setDocumentModeEb(QMdiArea *self, bool enabled) {
  self->setDocumentMode(enabled);
}

//  void QMdiArea::setTabsClosable(bool closable)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea15setTabsClosableEb(QMdiArea *self, bool closable) {
  self->setTabsClosable(closable);
}

//  bool QMdiArea::tabsClosable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QMdiArea12tabsClosableEv(const QMdiArea *self) {
  return self->tabsClosable();
}

//  void QMdiArea::setTabsMovable(bool movable)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea14setTabsMovableEb(QMdiArea *self, bool movable) {
  self->setTabsMovable(movable);
}

//  bool QMdiArea::tabsMovable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QMdiArea11tabsMovableEv(const QMdiArea *self) {
  return self->tabsMovable();
}

//  void QMdiArea::setTabShape(QTabWidget::TabShape shape)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea11setTabShapeEN10QTabWidget8TabShapeE(
    QMdiArea *self,
    QTabWidget::TabShape shape) {
  self->setTabShape(shape);
}

//  QTabWidget::TabShape QMdiArea::tabShape() const
extern "C" Q_DECL_EXPORT
QTabWidget::TabShape ritual_ZNK8QMdiArea8tabShapeEv(const QMdiArea *self) {
  return self->tabShape();
}

//  void QMdiArea::setTabPosition(QTabWidget::TabPosition position)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea14setTabPositionEN10QTabWidget11TabPositionE(
    QMdiArea *self,
    QTabWidget::TabPosition position) {
  self->setTabPosition(position);
}

//  QTabWidget::TabPosition QMdiArea::tabPosition() const
extern "C" Q_DECL_EXPORT
QTabWidget::TabPosition ritual_ZNK8QMdiArea11tabPositionEv(
    const QMdiArea *self) {
  return self->tabPosition();
}

//  void QMdiArea::setActiveSubWindow(QMdiSubWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea18setActiveSubWindowEP13QMdiSubWindow(
    QMdiArea *self,
    QMdiSubWindow *window) {
  self->setActiveSubWindow(window);
}

//  void QMdiArea::tileSubWindows()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea14tileSubWindowsEv(QMdiArea *self) {
  self->tileSubWindows();
}

//  void QMdiArea::cascadeSubWindows()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea17cascadeSubWindowsEv(QMdiArea *self) {
  self->cascadeSubWindows();
}

//  void QMdiArea::closeActiveSubWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea20closeActiveSubWindowEv(QMdiArea *self) {
  self->closeActiveSubWindow();
}

//  void QMdiArea::closeAllSubWindows()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea18closeAllSubWindowsEv(QMdiArea *self) {
  self->closeAllSubWindows();
}

//  void QMdiArea::activateNextSubWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea21activateNextSubWindowEv(QMdiArea *self) {
  self->activateNextSubWindow();
}

//  void QMdiArea::activatePreviousSubWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMdiArea25activatePreviousSubWindowEv(QMdiArea *self) {
  self->activatePreviousSubWindow();
}
