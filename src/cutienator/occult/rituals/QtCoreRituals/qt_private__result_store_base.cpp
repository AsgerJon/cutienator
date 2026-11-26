//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qresultstore.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by
//  hand, instances of templates of the class: 20. Kept as it is when the
//  generator runs again.
#include <QtCore/qglobal.h>
#if QT_CONFIG(future)
#if QT_CONFIG(future)
#include <QtCore/qresultstore.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <utility>

//  QtPrivate::ResultStoreBase::ResultStoreBase()
extern "C" Q_DECL_EXPORT
QtPrivate::ResultStoreBase *ritual_ZN9QtPrivate15ResultStoreBaseC1Ev() {
  return new QtPrivate::ResultStoreBase();
}

//  void QtPrivate::ResultStoreBase::setFilterMode(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate15ResultStoreBase13setFilterModeEb(
    QtPrivate::ResultStoreBase *self,
    bool enable) {
  self->setFilterMode(enable);
}

//  bool QtPrivate::ResultStoreBase::filterMode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate15ResultStoreBase10filterModeEv(
    const QtPrivate::ResultStoreBase *self) {
  return self->filterMode();
}

//  int QtPrivate::ResultStoreBase::addResult(int index, const void *result)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtPrivate15ResultStoreBase9addResultEiPKv(
    QtPrivate::ResultStoreBase *self,
    int index,
    const void *result) {
  return self->addResult(index, result);
}

//  int QtPrivate::ResultStoreBase::addResults(int index, const void
//      *results, int vectorSize, int logicalCount)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtPrivate15ResultStoreBase10addResultsEiPKvii(
    QtPrivate::ResultStoreBase *self,
    int index,
    const void *results,
    int vectorSize,
    int logicalCount) {
  return self->addResults(index, results, vectorSize, logicalCount);
}

//  ResultIteratorBase QtPrivate::ResultStoreBase::begin() const
extern "C" Q_DECL_EXPORT
QtPrivate::ResultIteratorBase *ritual_ZNK9QtPrivate15ResultStoreBase5beginEv(
    const QtPrivate::ResultStoreBase *self) {
  return new QtPrivate::ResultIteratorBase(self->begin());
}

//  ResultIteratorBase QtPrivate::ResultStoreBase::end() const
extern "C" Q_DECL_EXPORT
QtPrivate::ResultIteratorBase *ritual_ZNK9QtPrivate15ResultStoreBase3endEv(
    const QtPrivate::ResultStoreBase *self) {
  return new QtPrivate::ResultIteratorBase(self->end());
}

//  bool QtPrivate::ResultStoreBase::hasNextResult() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate15ResultStoreBase13hasNextResultEv(
    const QtPrivate::ResultStoreBase *self) {
  return self->hasNextResult();
}

//  ResultIteratorBase QtPrivate::ResultStoreBase::resultAt(int index) const
extern "C" Q_DECL_EXPORT
QtPrivate::ResultIteratorBase *ritual_ZNK9QtPrivate15ResultStoreBase8resultAtEi(
    const QtPrivate::ResultStoreBase *self,
    int index) {
  return new QtPrivate::ResultIteratorBase(self->resultAt(index));
}

//  bool QtPrivate::ResultStoreBase::contains(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate15ResultStoreBase8containsEi(
    const QtPrivate::ResultStoreBase *self,
    int index) {
  return self->contains(index);
}

//  int QtPrivate::ResultStoreBase::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QtPrivate15ResultStoreBase5countEv(
    const QtPrivate::ResultStoreBase *self) {
  return self->count();
}

//  QtPrivate::ResultStoreBase::~ResultStoreBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate15ResultStoreBaseD1Ev(
    QtPrivate::ResultStoreBase *self) {
  delete self;
}

//  int QtPrivate::ResultStoreBase::insertResultItem(int index, ResultItem
//      &resultItem)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtPrivate15ResultStoreBase16insertResultItemEiRNS_10ResultItemE(
    QtPrivate::ResultStoreBase *self,
    int index,
    QtPrivate::ResultItem *resultItem) {
  return self->insertResultItem(index, *resultItem);
}

//  void QtPrivate::ResultStoreBase::insertResultItemIfValid(int index,
//      ResultItem &resultItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate15ResultStoreBase23insertResultItemIfValidEiRNS_10ResultItemE(
    QtPrivate::ResultStoreBase *self,
    int index,
    QtPrivate::ResultItem *resultItem) {
  self->insertResultItemIfValid(index, *resultItem);
}

//  bool QtPrivate::ResultStoreBase::containsValidResultItem(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate15ResultStoreBase23containsValidResultItemEi(
    const QtPrivate::ResultStoreBase *self,
    int index) {
  return self->containsValidResultItem(index);
}

//  void QtPrivate::ResultStoreBase::syncPendingResults()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate15ResultStoreBase18syncPendingResultsEv(
    QtPrivate::ResultStoreBase *self) {
  self->syncPendingResults();
}

//  void QtPrivate::ResultStoreBase::syncResultCount()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate15ResultStoreBase15syncResultCountEv(
    QtPrivate::ResultStoreBase *self) {
  self->syncResultCount();
}

//  int QtPrivate::ResultStoreBase::updateInsertIndex(int index, int _count)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtPrivate15ResultStoreBase17updateInsertIndexEii(
    QtPrivate::ResultStoreBase *self,
    int index,
    int _count) {
  return self->updateInsertIndex(index, _count);
}

//  int QtPrivate::ResultStoreBase::addCanceledResult(int index)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtPrivate15ResultStoreBase17addCanceledResultEi(
    QtPrivate::ResultStoreBase *self,
    int index) {
  return self->addCanceledResult(index);
}

//  int QtPrivate::ResultStoreBase::addCanceledResults<int>(int index, int
//      _count)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtPrivate15ResultStoreBase18addCanceledResultsIiEEiii(
    QtPrivate::ResultStoreBase *self,
    int index,
    int _count) {
  return self->addCanceledResults<int>(index, _count);
}

//  int QtPrivate::ResultStoreBase::addResult<int>(int index, const int
//      *result)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtPrivate15ResultStoreBase9addResultIiEEiiPKT_(
    QtPrivate::ResultStoreBase *self,
    int index,
    const int *result) {
  return self->addResult<int>(index, result);
}

//  int QtPrivate::ResultStoreBase::moveResult<int>(int index, int &&result)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtPrivate15ResultStoreBase10moveResultIiEEiiOT_(
    QtPrivate::ResultStoreBase *self,
    int index,
    int *result) {
  return self->moveResult<int>(index, std::move(*result));
}

//  void QtPrivate::ResultStoreBase::clear<int>()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate15ResultStoreBase5clearIiEEvv(
    QtPrivate::ResultStoreBase *self) {
  self->clear<int>();
}

//  int QtPrivate::ResultStoreBase::addCanceledResults<double>(int index, int
//      _count)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtPrivate15ResultStoreBase18addCanceledResultsIdEEiii(
    QtPrivate::ResultStoreBase *self,
    int index,
    int _count) {
  return self->addCanceledResults<double>(index, _count);
}

//  int QtPrivate::ResultStoreBase::addResult<double>(int index, const double
//      *result)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtPrivate15ResultStoreBase9addResultIdEEiiPKT_(
    QtPrivate::ResultStoreBase *self,
    int index,
    const double *result) {
  return self->addResult<double>(index, result);
}

//  int QtPrivate::ResultStoreBase::moveResult<double>(int index, double
//      &&result)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtPrivate15ResultStoreBase10moveResultIdEEiiOT_(
    QtPrivate::ResultStoreBase *self,
    int index,
    double *result) {
  return self->moveResult<double>(index, std::move(*result));
}

//  void QtPrivate::ResultStoreBase::clear<double>()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate15ResultStoreBase5clearIdEEvv(
    QtPrivate::ResultStoreBase *self) {
  self->clear<double>();
}

//  int QtPrivate::ResultStoreBase::addCanceledResults<bool>(int index, int
//      _count)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtPrivate15ResultStoreBase18addCanceledResultsIbEEiii(
    QtPrivate::ResultStoreBase *self,
    int index,
    int _count) {
  return self->addCanceledResults<bool>(index, _count);
}

//  int QtPrivate::ResultStoreBase::addResult<bool>(int index, const bool
//      *result)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtPrivate15ResultStoreBase9addResultIbEEiiPKT_(
    QtPrivate::ResultStoreBase *self,
    int index,
    const bool *result) {
  return self->addResult<bool>(index, result);
}

//  int QtPrivate::ResultStoreBase::moveResult<bool>(int index, bool
//      &&result)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtPrivate15ResultStoreBase10moveResultIbEEiiOT_(
    QtPrivate::ResultStoreBase *self,
    int index,
    bool *result) {
  return self->moveResult<bool>(index, std::move(*result));
}

//  void QtPrivate::ResultStoreBase::clear<bool>()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate15ResultStoreBase5clearIbEEvv(
    QtPrivate::ResultStoreBase *self) {
  self->clear<bool>();
}

//  int QtPrivate::ResultStoreBase::addCanceledResults<QString>(int index,
//      int _count)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtPrivate15ResultStoreBase18addCanceledResultsI7QStringEEiii(
    QtPrivate::ResultStoreBase *self,
    int index,
    int _count) {
  return self->addCanceledResults<QString>(index, _count);
}

//  int QtPrivate::ResultStoreBase::addResult<QString>(int index, const
//      QString *result)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtPrivate15ResultStoreBase9addResultI7QStringEEiiPKT_(
    QtPrivate::ResultStoreBase *self,
    int index,
    const QString *result) {
  return self->addResult<QString>(index, result);
}

//  int QtPrivate::ResultStoreBase::moveResult<QString>(int index, QString
//      &&result)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtPrivate15ResultStoreBase10moveResultI7QStringEEiiOT_(
    QtPrivate::ResultStoreBase *self,
    int index,
    QString *result) {
  return self->moveResult<QString>(index, std::move(*result));
}

//  void QtPrivate::ResultStoreBase::clear<QString>()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate15ResultStoreBase5clearI7QStringEEvv(
    QtPrivate::ResultStoreBase *self) {
  self->clear<QString>();
}

//  int QtPrivate::ResultStoreBase::addCanceledResults<QVariant>(int index,
//      int _count)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtPrivate15ResultStoreBase18addCanceledResultsI8QVariantEEiii(
    QtPrivate::ResultStoreBase *self,
    int index,
    int _count) {
  return self->addCanceledResults<QVariant>(index, _count);
}

//  int QtPrivate::ResultStoreBase::addResult<QVariant>(int index, const
//      QVariant *result)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtPrivate15ResultStoreBase9addResultI8QVariantEEiiPKT_(
    QtPrivate::ResultStoreBase *self,
    int index,
    const QVariant *result) {
  return self->addResult<QVariant>(index, result);
}

//  int QtPrivate::ResultStoreBase::moveResult<QVariant>(int index, QVariant
//      &&result)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtPrivate15ResultStoreBase10moveResultI8QVariantEEiiOT_(
    QtPrivate::ResultStoreBase *self,
    int index,
    QVariant *result) {
  return self->moveResult<QVariant>(index, std::move(*result));
}

//  void QtPrivate::ResultStoreBase::clear<QVariant>()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate15ResultStoreBase5clearI8QVariantEEvv(
    QtPrivate::ResultStoreBase *self) {
  self->clear<QVariant>();
}

#endif  // QT_CONFIG(future)
#endif  // QT_CONFIG(future)
