//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstatusbar.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qstatusbar.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QStatusBar::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QStatusBar10metaObjectEv(
    const QStatusBar *self) {
  return self->metaObject();
}

//  QString QStatusBar::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QStatusBar2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QStatusBar::tr(s, c, n));
}

//  QStatusBar::QStatusBar(QWidget *parent)
extern "C" Q_DECL_EXPORT
QStatusBar *ritual_ZN10QStatusBarC1EP7QWidget(QWidget *parent) {
  return new QStatusBar(parent);
}

//  QStatusBar::~QStatusBar()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QStatusBarD1Ev(QStatusBar *self) {
  delete self;
}

//  void QStatusBar::addWidget(QWidget *widget, int stretch)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QStatusBar9addWidgetEP7QWidgeti(
    QStatusBar *self,
    QWidget *widget,
    int stretch) {
  self->addWidget(widget, stretch);
}

//  int QStatusBar::insertWidget(int index, QWidget *widget, int stretch)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QStatusBar12insertWidgetEiP7QWidgeti(
    QStatusBar *self,
    int index,
    QWidget *widget,
    int stretch) {
  return self->insertWidget(index, widget, stretch);
}

//  void QStatusBar::addPermanentWidget(QWidget *widget, int stretch)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QStatusBar18addPermanentWidgetEP7QWidgeti(
    QStatusBar *self,
    QWidget *widget,
    int stretch) {
  self->addPermanentWidget(widget, stretch);
}

//  int QStatusBar::insertPermanentWidget(int index, QWidget *widget, int
//      stretch)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QStatusBar21insertPermanentWidgetEiP7QWidgeti(
    QStatusBar *self,
    int index,
    QWidget *widget,
    int stretch) {
  return self->insertPermanentWidget(index, widget, stretch);
}

//  void QStatusBar::removeWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QStatusBar12removeWidgetEP7QWidget(
    QStatusBar *self,
    QWidget *widget) {
  self->removeWidget(widget);
}

//  void QStatusBar::setSizeGripEnabled(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QStatusBar18setSizeGripEnabledEb(QStatusBar *self, bool a0) {
  self->setSizeGripEnabled(a0);
}

//  bool QStatusBar::isSizeGripEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QStatusBar17isSizeGripEnabledEv(const QStatusBar *self) {
  return self->isSizeGripEnabled();
}

//  QString QStatusBar::currentMessage() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QStatusBar14currentMessageEv(const QStatusBar *self) {
  return new QString(self->currentMessage());
}

//  void QStatusBar::showMessage(const QString &text, int timeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QStatusBar11showMessageERK7QStringi(
    QStatusBar *self,
    const QString *text,
    int timeout) {
  self->showMessage(*text, timeout);
}

//  void QStatusBar::clearMessage()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QStatusBar12clearMessageEv(QStatusBar *self) {
  self->clearMessage();
}
