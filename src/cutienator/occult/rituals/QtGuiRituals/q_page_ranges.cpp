//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpageranges.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpageranges.h>
#include <QtCore/qstring.h>
#include <QtCore/QList>
#include <QtGui/QPageRanges>

//  QPageRanges::QPageRanges()
extern "C" Q_DECL_EXPORT
QPageRanges *ritual_ZN11QPageRangesC1Ev() {
  return new QPageRanges();
}

//  QPageRanges::~QPageRanges()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPageRangesD1Ev(QPageRanges *self) {
  delete self;
}

//  QPageRanges::QPageRanges(const QPageRanges &other)
extern "C" Q_DECL_EXPORT
QPageRanges *ritual_ZN11QPageRangesC1ERKS_(const QPageRanges *other) {
  return new QPageRanges(*other);
}

//  QPageRanges &QPageRanges::operator=(const QPageRanges &other)
extern "C" Q_DECL_EXPORT
QPageRanges *ritual_ZN11QPageRangesaSERKS_(
    QPageRanges *self,
    const QPageRanges *other) {
  return &(self->operator=(*other));
}

//  QPageRanges::QPageRanges(QPageRanges &&other)
extern "C" Q_DECL_EXPORT
QPageRanges *ritual_ZN11QPageRangesC1EOS_(QPageRanges *other) {
  return new QPageRanges(std::move(*other));
}

//  QPageRanges &QPageRanges::operator=(QPageRanges &&other)
extern "C" Q_DECL_EXPORT
QPageRanges *ritual_ZN11QPageRangesaSEOS_(
    QPageRanges *self,
    QPageRanges *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QPageRanges::swap(QPageRanges &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPageRanges4swapERS_(QPageRanges *self, QPageRanges *other) {
  self->swap(*other);
}

//  bool operator==(const QPageRanges &lhs, const QPageRanges &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK11QPageRangesS1_(
    const QPageRanges *lhs,
    const QPageRanges *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QPageRanges &lhs, const QPageRanges &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK11QPageRangesS1_(
    const QPageRanges *lhs,
    const QPageRanges *rhs) {
  return operator!=(*lhs, *rhs);
}

//  void QPageRanges::addPage(int pageNumber)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPageRanges7addPageEi(QPageRanges *self, int pageNumber) {
  self->addPage(pageNumber);
}

//  void QPageRanges::addRange(int from, int to)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPageRanges8addRangeEii(
    QPageRanges *self,
    int from,
    int to) {
  self->addRange(from, to);
}

//  QList<Range> QPageRanges::toRangeList() const
extern "C" Q_DECL_EXPORT
QList<QPageRanges::Range> *ritual_ZNK11QPageRanges11toRangeListEv(
    const QPageRanges *self) {
  return new QList<QPageRanges::Range>(self->toRangeList());
}

//  void QPageRanges::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPageRanges5clearEv(QPageRanges *self) {
  self->clear();
}

//  QString QPageRanges::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QPageRanges8toStringEv(const QPageRanges *self) {
  return new QString(self->toString());
}

//  QPageRanges QPageRanges::fromString(const QString &ranges)
extern "C" Q_DECL_EXPORT
QPageRanges *ritual_ZN11QPageRanges10fromStringERK7QString(
    const QString *ranges) {
  return new QPageRanges(QPageRanges::fromString(*ranges));
}

//  bool QPageRanges::contains(int pageNumber) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QPageRanges8containsEi(
    const QPageRanges *self,
    int pageNumber) {
  return self->contains(pageNumber);
}

//  bool QPageRanges::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QPageRanges7isEmptyEv(const QPageRanges *self) {
  return self->isEmpty();
}

//  int QPageRanges::firstPage() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QPageRanges9firstPageEv(const QPageRanges *self) {
  return self->firstPage();
}

//  int QPageRanges::lastPage() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QPageRanges8lastPageEv(const QPageRanges *self) {
  return self->lastPage();
}

//  void QPageRanges::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPageRanges6detachEv(QPageRanges *self) {
  self->detach();
}

//  bool QPageRanges::isEqual(const QPageRanges &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QPageRanges7isEqualERKS_(
    const QPageRanges *self,
    const QPageRanges *other) {
  return self->isEqual(*other);
}

//  a QList<QPageRanges::Range> a ritual of QPageRanges gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QPageRanges__QList_QPageRanges_Range(
    QList<QPageRanges::Range> *self) {
  delete self;
}
