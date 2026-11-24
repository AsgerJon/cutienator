//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qsslellipticcurve.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qsslellipticcurve.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QSslEllipticCurve::QSslEllipticCurve()
extern "C" Q_DECL_EXPORT
QSslEllipticCurve *ritual_ZN17QSslEllipticCurveC1Ev() {
  return new QSslEllipticCurve();
}

//  QSslEllipticCurve QSslEllipticCurve::fromShortName(const QString &name)
extern "C" Q_DECL_EXPORT
QSslEllipticCurve *ritual_ZN17QSslEllipticCurve13fromShortNameERK7QString(
    const QString *name) {
  return new QSslEllipticCurve(QSslEllipticCurve::fromShortName(*name));
}

//  QSslEllipticCurve QSslEllipticCurve::fromLongName(const QString &name)
extern "C" Q_DECL_EXPORT
QSslEllipticCurve *ritual_ZN17QSslEllipticCurve12fromLongNameERK7QString(
    const QString *name) {
  return new QSslEllipticCurve(QSslEllipticCurve::fromLongName(*name));
}

//  QString QSslEllipticCurve::shortName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QSslEllipticCurve9shortNameEv(
    const QSslEllipticCurve *self) {
  return new QString(self->shortName());
}

//  QString QSslEllipticCurve::longName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QSslEllipticCurve8longNameEv(
    const QSslEllipticCurve *self) {
  return new QString(self->longName());
}

//  bool QSslEllipticCurve::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QSslEllipticCurve7isValidEv(const QSslEllipticCurve *self) {
  return self->isValid();
}

//  bool QSslEllipticCurve::isTlsNamedCurve() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QSslEllipticCurve15isTlsNamedCurveEv(
    const QSslEllipticCurve *self) {
  return self->isTlsNamedCurve();
}

//  bool operator==(QSslEllipticCurve lhs, QSslEllipticCurve rhs)
extern "C" Q_DECL_EXPORT
bool ritual_Zeq17QSslEllipticCurveS_(
    const QSslEllipticCurve *lhs,
    const QSslEllipticCurve *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(QSslEllipticCurve lhs, QSslEllipticCurve rhs)
extern "C" Q_DECL_EXPORT
bool ritual_Zne17QSslEllipticCurveS_(
    const QSslEllipticCurve *lhs,
    const QSslEllipticCurve *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QSslEllipticCurve::~QSslEllipticCurve()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslEllipticCurveD1Ev(QSslEllipticCurve *self) {
  delete self;
}

//  QList<QSslEllipticCurve>::QList()
extern "C" Q_DECL_EXPORT
QList<QSslEllipticCurve> *ritual_list_make_QSslEllipticCurve() {
  return new QList<QSslEllipticCurve>();
}

//  void QList<QSslEllipticCurve>::append(const QSslEllipticCurve &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QSslEllipticCurve(
    QList<QSslEllipticCurve> *self,
    const QSslEllipticCurve *element) {
  self->append(*element);
}

//  qsizetype QList<QSslEllipticCurve>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QSslEllipticCurve(
    const QList<QSslEllipticCurve> *self) {
  return self->size();
}

//  const QSslEllipticCurve &QList<QSslEllipticCurve>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QSslEllipticCurve *ritual_list_at_QSslEllipticCurve(
    const QList<QSslEllipticCurve> *self,
    long long index) {
  return new QSslEllipticCurve(self->at(index));
}

//  QList<QSslEllipticCurve>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QSslEllipticCurve(QList<QSslEllipticCurve> *self) {
  delete self;
}
