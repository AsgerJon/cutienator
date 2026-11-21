//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qvalidator.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qvalidator.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QDoubleValidator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QDoubleValidator10metaObjectEv(
    const QDoubleValidator *self) {
  return self->metaObject();
}

//  QString QDoubleValidator::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QDoubleValidator2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDoubleValidator::tr(s, c, n));
}

//  QDoubleValidator::QDoubleValidator(QObject *parent)
extern "C" Q_DECL_EXPORT
QDoubleValidator *ritual_ZN16QDoubleValidatorC1EP7QObject(QObject *parent) {
  return new QDoubleValidator(parent);
}

//  QDoubleValidator::QDoubleValidator(double bottom, double top, int
//      decimals, QObject *parent)
extern "C" Q_DECL_EXPORT
QDoubleValidator *ritual_ZN16QDoubleValidatorC1EddiP7QObject(
    double bottom,
    double top,
    int decimals,
    QObject *parent) {
  return new QDoubleValidator(bottom, top, decimals, parent);
}

//  QDoubleValidator::~QDoubleValidator()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleValidatorD1Ev(QDoubleValidator *self) {
  delete self;
}

//  void QDoubleValidator::setRange(double bottom, double top, int decimals)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleValidator8setRangeEddi(
    QDoubleValidator *self,
    double bottom,
    double top,
    int decimals) {
  self->setRange(bottom, top, decimals);
}

//  void QDoubleValidator::setRange(double bottom, double top)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleValidator8setRangeEdd(
    QDoubleValidator *self,
    double bottom,
    double top) {
  self->setRange(bottom, top);
}

//  void QDoubleValidator::setBottom(double a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleValidator9setBottomEd(
    QDoubleValidator *self,
    double a0) {
  self->setBottom(a0);
}

//  void QDoubleValidator::setTop(double a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleValidator6setTopEd(
    QDoubleValidator *self,
    double a0) {
  self->setTop(a0);
}

//  void QDoubleValidator::setDecimals(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleValidator11setDecimalsEi(
    QDoubleValidator *self,
    int a0) {
  self->setDecimals(a0);
}

//  void QDoubleValidator::setNotation(Notation a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleValidator11setNotationENS_8NotationE(
    QDoubleValidator *self,
    QDoubleValidator::Notation a0) {
  self->setNotation(a0);
}

//  double QDoubleValidator::bottom() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK16QDoubleValidator6bottomEv(const QDoubleValidator *self) {
  return self->bottom();
}

//  double QDoubleValidator::top() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK16QDoubleValidator3topEv(const QDoubleValidator *self) {
  return self->top();
}

//  int QDoubleValidator::decimals() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QDoubleValidator8decimalsEv(const QDoubleValidator *self) {
  return self->decimals();
}

//  Notation QDoubleValidator::notation() const
extern "C" Q_DECL_EXPORT
QDoubleValidator::Notation ritual_ZNK16QDoubleValidator8notationEv(
    const QDoubleValidator *self) {
  return self->notation();
}
