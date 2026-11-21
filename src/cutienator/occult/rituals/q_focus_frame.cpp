//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qfocusframe.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qfocusframe.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QFocusFrame::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QFocusFrame10metaObjectEv(
    const QFocusFrame *self) {
  return self->metaObject();
}

//  QString QFocusFrame::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QFocusFrame2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QFocusFrame::tr(s, c, n));
}

//  QFocusFrame::QFocusFrame(QWidget *parent)
extern "C" Q_DECL_EXPORT
QFocusFrame *ritual_ZN11QFocusFrameC1EP7QWidget(QWidget *parent) {
  return new QFocusFrame(parent);
}

//  QFocusFrame::~QFocusFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFocusFrameD1Ev(QFocusFrame *self) {
  delete self;
}

//  void QFocusFrame::setWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFocusFrame9setWidgetEP7QWidget(
    QFocusFrame *self,
    QWidget *widget) {
  self->setWidget(widget);
}

//  QWidget *QFocusFrame::widget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK11QFocusFrame6widgetEv(const QFocusFrame *self) {
  return self->widget();
}
