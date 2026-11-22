//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtextlayout.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtextlayout.h>

//  bool operator==(const FormatRange &lhs, const FormatRange &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN11QTextLayout11FormatRangeES2_(
    const QTextLayout::FormatRange *lhs,
    const QTextLayout::FormatRange *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const FormatRange &lhs, const FormatRange &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKN11QTextLayout11FormatRangeES2_(
    const QTextLayout::FormatRange *lhs,
    const QTextLayout::FormatRange *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QTextLayout::FormatRange::~FormatRange()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextLayout11FormatRangeD1Ev(
    QTextLayout::FormatRange *self) {
  delete self;
}
