//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpageranges.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpageranges.h>
#include <QtCore/qstring.h>

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
