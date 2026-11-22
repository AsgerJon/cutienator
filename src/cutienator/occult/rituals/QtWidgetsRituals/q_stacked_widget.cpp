//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstackedwidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qstackedwidget.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QStackedWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QStackedWidget10metaObjectEv(
    const QStackedWidget *self) {
  return self->metaObject();
}

//  QString QStackedWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QStackedWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QStackedWidget::tr(s, c, n));
}

//  QStackedWidget::QStackedWidget(QWidget *parent)
extern "C" Q_DECL_EXPORT
QStackedWidget *ritual_ZN14QStackedWidgetC1EP7QWidget(QWidget *parent) {
  return new QStackedWidget(parent);
}

//  QStackedWidget::~QStackedWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStackedWidgetD1Ev(QStackedWidget *self) {
  delete self;
}

//  int QStackedWidget::addWidget(QWidget *w)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QStackedWidget9addWidgetEP7QWidget(
    QStackedWidget *self,
    QWidget *w) {
  return self->addWidget(w);
}

//  int QStackedWidget::insertWidget(int index, QWidget *w)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QStackedWidget12insertWidgetEiP7QWidget(
    QStackedWidget *self,
    int index,
    QWidget *w) {
  return self->insertWidget(index, w);
}

//  void QStackedWidget::removeWidget(QWidget *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStackedWidget12removeWidgetEP7QWidget(
    QStackedWidget *self,
    QWidget *w) {
  self->removeWidget(w);
}

//  QWidget *QStackedWidget::currentWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK14QStackedWidget13currentWidgetEv(
    const QStackedWidget *self) {
  return self->currentWidget();
}

//  int QStackedWidget::currentIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QStackedWidget12currentIndexEv(const QStackedWidget *self) {
  return self->currentIndex();
}

//  int QStackedWidget::indexOf(const QWidget *a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QStackedWidget7indexOfEPK7QWidget(
    const QStackedWidget *self,
    const QWidget *a0) {
  return self->indexOf(a0);
}

//  QWidget *QStackedWidget::widget(int a0) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK14QStackedWidget6widgetEi(
    const QStackedWidget *self,
    int a0) {
  return self->widget(a0);
}

//  int QStackedWidget::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QStackedWidget5countEv(const QStackedWidget *self) {
  return self->count();
}

//  void QStackedWidget::setCurrentIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStackedWidget15setCurrentIndexEi(
    QStackedWidget *self,
    int index) {
  self->setCurrentIndex(index);
}

//  void QStackedWidget::setCurrentWidget(QWidget *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStackedWidget16setCurrentWidgetEP7QWidget(
    QStackedWidget *self,
    QWidget *w) {
  self->setCurrentWidget(w);
}
