//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qdial.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qdial.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QDial::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK5QDial10metaObjectEv(const QDial *self) {
  return self->metaObject();
}

//  QString QDial::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5QDial2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QDial::tr(s, c, n));
}

//  QDial::QDial(QWidget *parent)
extern "C" Q_DECL_EXPORT
QDial *ritual_ZN5QDialC1EP7QWidget(QWidget *parent) {
  return new QDial(parent);
}

//  QDial::~QDial()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QDialD1Ev(QDial *self) {
  delete self;
}

//  bool QDial::wrapping() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QDial8wrappingEv(const QDial *self) {
  return self->wrapping();
}

//  int QDial::notchSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QDial9notchSizeEv(const QDial *self) {
  return self->notchSize();
}

//  void QDial::setNotchTarget(double target)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QDial14setNotchTargetEd(QDial *self, double target) {
  self->setNotchTarget(target);
}

//  qreal QDial::notchTarget() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK5QDial11notchTargetEv(const QDial *self) {
  return self->notchTarget();
}

//  bool QDial::notchesVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QDial14notchesVisibleEv(const QDial *self) {
  return self->notchesVisible();
}

//  QSize QDial::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK5QDial8sizeHintEv(const QDial *self) {
  return new QSize(self->sizeHint());
}

//  QSize QDial::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK5QDial15minimumSizeHintEv(const QDial *self) {
  return new QSize(self->minimumSizeHint());
}

//  void QDial::setNotchesVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QDial17setNotchesVisibleEb(QDial *self, bool visible) {
  self->setNotchesVisible(visible);
}

//  void QDial::setWrapping(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QDial11setWrappingEb(QDial *self, bool on) {
  self->setWrapping(on);
}
