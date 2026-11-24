//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qlocale_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qlocale_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>

//  void QLocaleData::NumericData::setZero(QStringView zero)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLocaleData11NumericData7setZeroE11QStringView(
    QLocaleData::NumericData *self,
    const QString *zero) {
  self->setZero(QStringView(*zero));
}

//  qsizetype QLocaleData::NumericData::zeroWidth() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QLocaleData11NumericData9zeroWidthEv(
    const QLocaleData::NumericData *self) {
  return self->zeroWidth();
}

//  const GroupSizes &QLocaleData::NumericData::groupSizes() const
extern "C" Q_DECL_EXPORT
QLocaleData::GroupSizes *ritual_ZNK11QLocaleData11NumericData10groupSizesEv(
    const QLocaleData::NumericData *self) {
  return new QLocaleData::GroupSizes(self->groupSizes());
}

//  bool QLocaleData::NumericData::isValid(NumberMode mode) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QLocaleData11NumericData7isValidENS_10NumberModeE(
    const QLocaleData::NumericData *self,
    QLocaleData::NumberMode mode) {
  return self->isValid(mode);
}

//  bool QLocaleData::NumericData::fractionalIsGroup() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QLocaleData11NumericData17fractionalIsGroupEv(
    const QLocaleData::NumericData *self) {
  return self->fractionalIsGroup();
}

//  QLocaleData::NumericData::~NumericData()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLocaleData11NumericDataD1Ev(
    QLocaleData::NumericData *self) {
  delete self;
}
