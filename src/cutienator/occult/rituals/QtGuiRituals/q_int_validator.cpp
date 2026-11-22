//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qvalidator.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qvalidator.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QIntValidator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QIntValidator10metaObjectEv(
    const QIntValidator *self) {
  return self->metaObject();
}

//  QString QIntValidator::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QIntValidator2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QIntValidator::tr(s, c, n));
}

//  QIntValidator::QIntValidator(QObject *parent)
extern "C" Q_DECL_EXPORT
QIntValidator *ritual_ZN13QIntValidatorC1EP7QObject(QObject *parent) {
  return new QIntValidator(parent);
}

//  QIntValidator::QIntValidator(int bottom, int top, QObject *parent)
extern "C" Q_DECL_EXPORT
QIntValidator *ritual_ZN13QIntValidatorC1EiiP7QObject(
    int bottom,
    int top,
    QObject *parent) {
  return new QIntValidator(bottom, top, parent);
}

//  QIntValidator::~QIntValidator()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QIntValidatorD1Ev(QIntValidator *self) {
  delete self;
}

//  void QIntValidator::setBottom(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QIntValidator9setBottomEi(QIntValidator *self, int a0) {
  self->setBottom(a0);
}

//  void QIntValidator::setTop(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QIntValidator6setTopEi(QIntValidator *self, int a0) {
  self->setTop(a0);
}

//  void QIntValidator::setRange(int bottom, int top)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QIntValidator8setRangeEii(
    QIntValidator *self,
    int bottom,
    int top) {
  self->setRange(bottom, top);
}

//  int QIntValidator::bottom() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QIntValidator6bottomEv(const QIntValidator *self) {
  return self->bottom();
}

//  int QIntValidator::top() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QIntValidator3topEv(const QIntValidator *self) {
  return self->top();
}
