//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpageranges.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpageranges.h>

//  bool QPageRanges::Range::contains(int pageNumber) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QPageRanges5Range8containsEi(
    const QPageRanges::Range *self,
    int pageNumber) {
  return self->contains(pageNumber);
}

//  bool operator==(Range lhs, Range rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqN11QPageRanges5RangeES0_(
    const QPageRanges::Range *lhs,
    const QPageRanges::Range *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(Range lhs, Range rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneN11QPageRanges5RangeES0_(
    const QPageRanges::Range *lhs,
    const QPageRanges::Range *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(Range lhs, Range rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltN11QPageRanges5RangeES0_(
    const QPageRanges::Range *lhs,
    const QPageRanges::Range *rhs) {
  return operator<(*lhs, *rhs);
}

//  QPageRanges::Range::~Range()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPageRanges5RangeD1Ev(QPageRanges::Range *self) {
  delete self;
}
