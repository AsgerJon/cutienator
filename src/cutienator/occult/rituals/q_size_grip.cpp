//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qsizegrip.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qsizegrip.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QSizeGrip::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QSizeGrip10metaObjectEv(
    const QSizeGrip *self) {
  return self->metaObject();
}

//  QString QSizeGrip::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QSizeGrip2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSizeGrip::tr(s, c, n));
}

//  QSizeGrip::QSizeGrip(QWidget *parent)
extern "C" Q_DECL_EXPORT
QSizeGrip *ritual_ZN9QSizeGripC1EP7QWidget(QWidget *parent) {
  return new QSizeGrip(parent);
}

//  QSizeGrip::~QSizeGrip()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSizeGripD1Ev(QSizeGrip *self) {
  delete self;
}

//  QSize QSizeGrip::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK9QSizeGrip8sizeHintEv(const QSizeGrip *self) {
  return new QSize(self->sizeHint());
}

//  void QSizeGrip::setVisible(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSizeGrip10setVisibleEb(QSizeGrip *self, bool a0) {
  self->setVisible(a0);
}
