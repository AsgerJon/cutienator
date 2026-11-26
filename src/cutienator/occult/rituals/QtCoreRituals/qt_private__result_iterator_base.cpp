//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qresultstore.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by
//  hand, instances of templates of the class: 20. Kept as it is when the
//  generator runs again.
#include <QtCore/qglobal.h>
#if QT_CONFIG(future)
#if QT_CONFIG(future)
#include <QtCore/qresultstore.h>
#include <QtCore/QMap>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>

//  QtPrivate::ResultIteratorBase::ResultIteratorBase()
extern "C" Q_DECL_EXPORT
QtPrivate::ResultIteratorBase *ritual_ZN9QtPrivate18ResultIteratorBaseC1Ev() {
  return new QtPrivate::ResultIteratorBase();
}

//  QtPrivate::ResultIteratorBase::ResultIteratorBase(QMap<int,
//      ResultItem>::const_iterator _mapIterator, int _vectorIndex)
extern "C" Q_DECL_EXPORT
QtPrivate::ResultIteratorBase *ritual_ZN9QtPrivate18ResultIteratorBaseC1EN4QMapIiNS_10ResultItemEE14const_iteratorEi(
    const QMap<int, QtPrivate::ResultItem>::const_iterator *_mapIterator,
    int _vectorIndex) {
  return new QtPrivate::ResultIteratorBase(*_mapIterator, _vectorIndex);
}

//  int QtPrivate::ResultIteratorBase::vectorIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QtPrivate18ResultIteratorBase11vectorIndexEv(
    const QtPrivate::ResultIteratorBase *self) {
  return self->vectorIndex();
}

//  int QtPrivate::ResultIteratorBase::resultIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QtPrivate18ResultIteratorBase11resultIndexEv(
    const QtPrivate::ResultIteratorBase *self) {
  return self->resultIndex();
}

//  ResultIteratorBase QtPrivate::ResultIteratorBase::operator++()
extern "C" Q_DECL_EXPORT
QtPrivate::ResultIteratorBase *ritual_ZN9QtPrivate18ResultIteratorBaseppEv(
    QtPrivate::ResultIteratorBase *self) {
  return new QtPrivate::ResultIteratorBase(self->operator++());
}

//  int QtPrivate::ResultIteratorBase::batchSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QtPrivate18ResultIteratorBase9batchSizeEv(
    const QtPrivate::ResultIteratorBase *self) {
  return self->batchSize();
}

//  void QtPrivate::ResultIteratorBase::batchedAdvance()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate18ResultIteratorBase14batchedAdvanceEv(
    QtPrivate::ResultIteratorBase *self) {
  self->batchedAdvance();
}

//  bool QtPrivate::ResultIteratorBase::isVector() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate18ResultIteratorBase8isVectorEv(
    const QtPrivate::ResultIteratorBase *self) {
  return self->isVector();
}

//  bool QtPrivate::ResultIteratorBase::canIncrementVectorIndex() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate18ResultIteratorBase23canIncrementVectorIndexEv(
    const QtPrivate::ResultIteratorBase *self) {
  return self->canIncrementVectorIndex();
}

//  bool QtPrivate::ResultIteratorBase::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate18ResultIteratorBase7isValidEv(
    const QtPrivate::ResultIteratorBase *self) {
  return self->isValid();
}

//  bool operator==(const ResultIteratorBase &lhs, const ResultIteratorBase
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivateeqERKNS_18ResultIteratorBaseES2_(
    const QtPrivate::ResultIteratorBase *lhs,
    const QtPrivate::ResultIteratorBase *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const ResultIteratorBase &lhs, const ResultIteratorBase
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivateneERKNS_18ResultIteratorBaseES2_(
    const QtPrivate::ResultIteratorBase *lhs,
    const QtPrivate::ResultIteratorBase *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QtPrivate::ResultIteratorBase::~ResultIteratorBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate18ResultIteratorBaseD1Ev(
    QtPrivate::ResultIteratorBase *self) {
  delete self;
}

//  int *QtPrivate::ResultIteratorBase::pointer<int>()
extern "C" Q_DECL_EXPORT
int * ritual_ZN9QtPrivate18ResultIteratorBase7pointerIiEEPT_v(
    QtPrivate::ResultIteratorBase *self) {
  return self->pointer<int>();
}

//  const int *QtPrivate::ResultIteratorBase::pointer<int>() const
extern "C" Q_DECL_EXPORT
const int * ritual_ZNK9QtPrivate18ResultIteratorBase7pointerIiEEPKT_v(
    const QtPrivate::ResultIteratorBase *self) {
  return self->pointer<int>();
}

//  int &QtPrivate::ResultIteratorBase::value<int>()
extern "C" Q_DECL_EXPORT
int * ritual_ZN9QtPrivate18ResultIteratorBase5valueIiEERT_v(
    QtPrivate::ResultIteratorBase *self) {
  return &(self->value<int>());
}

//  const int &QtPrivate::ResultIteratorBase::value<int>() const
extern "C" Q_DECL_EXPORT
const int * ritual_ZNK9QtPrivate18ResultIteratorBase5valueIiEERKT_v(
    const QtPrivate::ResultIteratorBase *self) {
  return &(self->value<int>());
}

//  double *QtPrivate::ResultIteratorBase::pointer<double>()
extern "C" Q_DECL_EXPORT
double * ritual_ZN9QtPrivate18ResultIteratorBase7pointerIdEEPT_v(
    QtPrivate::ResultIteratorBase *self) {
  return self->pointer<double>();
}

//  const double *QtPrivate::ResultIteratorBase::pointer<double>() const
extern "C" Q_DECL_EXPORT
const double * ritual_ZNK9QtPrivate18ResultIteratorBase7pointerIdEEPKT_v(
    const QtPrivate::ResultIteratorBase *self) {
  return self->pointer<double>();
}

//  double &QtPrivate::ResultIteratorBase::value<double>()
extern "C" Q_DECL_EXPORT
double * ritual_ZN9QtPrivate18ResultIteratorBase5valueIdEERT_v(
    QtPrivate::ResultIteratorBase *self) {
  return &(self->value<double>());
}

//  const double &QtPrivate::ResultIteratorBase::value<double>() const
extern "C" Q_DECL_EXPORT
const double * ritual_ZNK9QtPrivate18ResultIteratorBase5valueIdEERKT_v(
    const QtPrivate::ResultIteratorBase *self) {
  return &(self->value<double>());
}

//  bool *QtPrivate::ResultIteratorBase::pointer<bool>()
extern "C" Q_DECL_EXPORT
bool * ritual_ZN9QtPrivate18ResultIteratorBase7pointerIbEEPT_v(
    QtPrivate::ResultIteratorBase *self) {
  return self->pointer<bool>();
}

//  const bool *QtPrivate::ResultIteratorBase::pointer<bool>() const
extern "C" Q_DECL_EXPORT
const bool * ritual_ZNK9QtPrivate18ResultIteratorBase7pointerIbEEPKT_v(
    const QtPrivate::ResultIteratorBase *self) {
  return self->pointer<bool>();
}

//  bool &QtPrivate::ResultIteratorBase::value<bool>()
extern "C" Q_DECL_EXPORT
bool * ritual_ZN9QtPrivate18ResultIteratorBase5valueIbEERT_v(
    QtPrivate::ResultIteratorBase *self) {
  return &(self->value<bool>());
}

//  const bool &QtPrivate::ResultIteratorBase::value<bool>() const
extern "C" Q_DECL_EXPORT
const bool * ritual_ZNK9QtPrivate18ResultIteratorBase5valueIbEERKT_v(
    const QtPrivate::ResultIteratorBase *self) {
  return &(self->value<bool>());
}

//  QString *QtPrivate::ResultIteratorBase::pointer<QString>()
extern "C" Q_DECL_EXPORT
QString * ritual_ZN9QtPrivate18ResultIteratorBase7pointerI7QStringEEPT_v(
    QtPrivate::ResultIteratorBase *self) {
  return self->pointer<QString>();
}

//  const QString *QtPrivate::ResultIteratorBase::pointer<QString>() const
extern "C" Q_DECL_EXPORT
const QString * ritual_ZNK9QtPrivate18ResultIteratorBase7pointerI7QStringEEPKT_v(
    const QtPrivate::ResultIteratorBase *self) {
  return self->pointer<QString>();
}

//  QString &QtPrivate::ResultIteratorBase::value<QString>()
extern "C" Q_DECL_EXPORT
QString * ritual_ZN9QtPrivate18ResultIteratorBase5valueI7QStringEERT_v(
    QtPrivate::ResultIteratorBase *self) {
  return &(self->value<QString>());
}

//  const QString &QtPrivate::ResultIteratorBase::value<QString>() const
extern "C" Q_DECL_EXPORT
const QString * ritual_ZNK9QtPrivate18ResultIteratorBase5valueI7QStringEERKT_v(
    const QtPrivate::ResultIteratorBase *self) {
  return &(self->value<QString>());
}

//  QVariant *QtPrivate::ResultIteratorBase::pointer<QVariant>()
extern "C" Q_DECL_EXPORT
QVariant * ritual_ZN9QtPrivate18ResultIteratorBase7pointerI8QVariantEEPT_v(
    QtPrivate::ResultIteratorBase *self) {
  return self->pointer<QVariant>();
}

//  const QVariant *QtPrivate::ResultIteratorBase::pointer<QVariant>() const
extern "C" Q_DECL_EXPORT
const QVariant * ritual_ZNK9QtPrivate18ResultIteratorBase7pointerI8QVariantEEPKT_v(
    const QtPrivate::ResultIteratorBase *self) {
  return self->pointer<QVariant>();
}

//  QVariant &QtPrivate::ResultIteratorBase::value<QVariant>()
extern "C" Q_DECL_EXPORT
QVariant * ritual_ZN9QtPrivate18ResultIteratorBase5valueI8QVariantEERT_v(
    QtPrivate::ResultIteratorBase *self) {
  return &(self->value<QVariant>());
}

//  const QVariant &QtPrivate::ResultIteratorBase::value<QVariant>() const
extern "C" Q_DECL_EXPORT
const QVariant * ritual_ZNK9QtPrivate18ResultIteratorBase5valueI8QVariantEERKT_v(
    const QtPrivate::ResultIteratorBase *self) {
  return &(self->value<QVariant>());
}

#endif  // QT_CONFIG(future)
#endif  // QT_CONFIG(future)
