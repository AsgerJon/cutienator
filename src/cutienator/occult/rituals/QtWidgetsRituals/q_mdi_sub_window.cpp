//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qmdisubwindow.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qmdisubwindow.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QMdiSubWindow::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QMdiSubWindow10metaObjectEv(
    const QMdiSubWindow *self) {
  return self->metaObject();
}

//  QString QMdiSubWindow::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QMdiSubWindow2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QMdiSubWindow::tr(s, c, n));
}

//  QMdiSubWindow::QMdiSubWindow(QWidget *parent, Qt::WindowFlags flags)
extern "C" Q_DECL_EXPORT
QMdiSubWindow *ritual_ZN13QMdiSubWindowC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWidget *parent,
    int flags) {
  return new QMdiSubWindow(parent, QFlags<Qt::WindowType>::fromInt(flags));
}

//  QMdiSubWindow::~QMdiSubWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindowD1Ev(QMdiSubWindow *self) {
  delete self;
}

//  QSize QMdiSubWindow::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK13QMdiSubWindow8sizeHintEv(const QMdiSubWindow *self) {
  return new QSize(self->sizeHint());
}

//  QSize QMdiSubWindow::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK13QMdiSubWindow15minimumSizeHintEv(
    const QMdiSubWindow *self) {
  return new QSize(self->minimumSizeHint());
}

//  void QMdiSubWindow::setWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindow9setWidgetEP7QWidget(
    QMdiSubWindow *self,
    QWidget *widget) {
  self->setWidget(widget);
}

//  QWidget *QMdiSubWindow::widget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK13QMdiSubWindow6widgetEv(const QMdiSubWindow *self) {
  return self->widget();
}

//  QWidget *QMdiSubWindow::maximizedButtonsWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK13QMdiSubWindow22maximizedButtonsWidgetEv(
    const QMdiSubWindow *self) {
  return self->maximizedButtonsWidget();
}

//  QWidget *QMdiSubWindow::maximizedSystemMenuIconWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK13QMdiSubWindow29maximizedSystemMenuIconWidgetEv(
    const QMdiSubWindow *self) {
  return self->maximizedSystemMenuIconWidget();
}

//  bool QMdiSubWindow::isShaded() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMdiSubWindow8isShadedEv(const QMdiSubWindow *self) {
  return self->isShaded();
}

//  void QMdiSubWindow::setOption(SubWindowOption option, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindow9setOptionENS_15SubWindowOptionEb(
    QMdiSubWindow *self,
    QMdiSubWindow::SubWindowOption option,
    bool on) {
  self->setOption(option, on);
}

//  bool QMdiSubWindow::testOption(SubWindowOption a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMdiSubWindow10testOptionENS_15SubWindowOptionE(
    const QMdiSubWindow *self,
    QMdiSubWindow::SubWindowOption a0) {
  return self->testOption(a0);
}

//  void QMdiSubWindow::setKeyboardSingleStep(int step)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindow21setKeyboardSingleStepEi(
    QMdiSubWindow *self,
    int step) {
  self->setKeyboardSingleStep(step);
}

//  int QMdiSubWindow::keyboardSingleStep() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QMdiSubWindow18keyboardSingleStepEv(
    const QMdiSubWindow *self) {
  return self->keyboardSingleStep();
}

//  void QMdiSubWindow::setKeyboardPageStep(int step)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindow19setKeyboardPageStepEi(
    QMdiSubWindow *self,
    int step) {
  self->setKeyboardPageStep(step);
}

//  int QMdiSubWindow::keyboardPageStep() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QMdiSubWindow16keyboardPageStepEv(
    const QMdiSubWindow *self) {
  return self->keyboardPageStep();
}

//  void QMdiSubWindow::setSystemMenu(QMenu *systemMenu)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindow13setSystemMenuEP5QMenu(
    QMdiSubWindow *self,
    QMenu *systemMenu) {
  self->setSystemMenu(systemMenu);
}

//  QMenu *QMdiSubWindow::systemMenu() const
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZNK13QMdiSubWindow10systemMenuEv(const QMdiSubWindow *self) {
  return self->systemMenu();
}

//  QMdiArea *QMdiSubWindow::mdiArea() const
extern "C" Q_DECL_EXPORT
QMdiArea *ritual_ZNK13QMdiSubWindow7mdiAreaEv(const QMdiSubWindow *self) {
  return self->mdiArea();
}

//  void QMdiSubWindow::showSystemMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindow14showSystemMenuEv(QMdiSubWindow *self) {
  self->showSystemMenu();
}

//  void QMdiSubWindow::showShaded()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMdiSubWindow10showShadedEv(QMdiSubWindow *self) {
  self->showShaded();
}
