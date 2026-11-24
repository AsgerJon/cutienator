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

//  QLocaleData::DigitSequence::DigitSequence(const DigitSequence &a0)
extern "C" Q_DECL_EXPORT
QLocaleData::DigitSequence *ritual_ZN11QLocaleData13DigitSequenceC1ERKS0_(
    const QLocaleData::DigitSequence *a0) {
  return new QLocaleData::DigitSequence(*a0);
}

//  QLocaleData::DigitSequence::~DigitSequence()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLocaleData13DigitSequenceD1Ev(
    QLocaleData::DigitSequence *self) {
  delete self;
}

//  qsizetype QLocaleData::DigitSequence::endIndex() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QLocaleData13DigitSequence8endIndexEv(
    const QLocaleData::DigitSequence *self) {
  return self->endIndex();
}

//  qsizetype QLocaleData::DigitSequence::size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QLocaleData13DigitSequence4sizeEv(
    const QLocaleData::DigitSequence *self) {
  return self->size();
}

//  bool QLocaleData::DigitSequence::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QLocaleData13DigitSequence7isEmptyEv(
    const QLocaleData::DigitSequence *self) {
  return self->isEmpty();
}

//  bool QLocaleData::DigitSequence::hasSign() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QLocaleData13DigitSequence7hasSignEv(
    const QLocaleData::DigitSequence *self) {
  return self->hasSign();
}

//  DigitSequence QLocaleData::DigitSequence::first(qsizetype count) const
extern "C" Q_DECL_EXPORT
QLocaleData::DigitSequence *ritual_ZNK11QLocaleData13DigitSequence5firstEx(
    const QLocaleData::DigitSequence *self,
    qsizetype count) {
  return new QLocaleData::DigitSequence(self->first(count));
}

//  DigitSequence QLocaleData::DigitSequence::last(qsizetype count) const
extern "C" Q_DECL_EXPORT
QLocaleData::DigitSequence *ritual_ZNK11QLocaleData13DigitSequence4lastEx(
    const QLocaleData::DigitSequence *self,
    qsizetype count) {
  return new QLocaleData::DigitSequence(self->last(count));
}

//  DigitSequence QLocaleData::DigitSequence::sliced(qsizetype from) const
extern "C" Q_DECL_EXPORT
QLocaleData::DigitSequence *ritual_ZNK11QLocaleData13DigitSequence6slicedEx(
    const QLocaleData::DigitSequence *self,
    qsizetype from) {
  return new QLocaleData::DigitSequence(self->sliced(from));
}

//  DigitSequence QLocaleData::DigitSequence::sliced(qsizetype from,
//      qsizetype count) const
extern "C" Q_DECL_EXPORT
QLocaleData::DigitSequence *ritual_ZNK11QLocaleData13DigitSequence6slicedExx(
    const QLocaleData::DigitSequence *self,
    qsizetype from,
    qsizetype count) {
  return new QLocaleData::DigitSequence(self->sliced(from, count));
}

//  QStringView QLocaleData::DigitSequence::used(const QStringView text,
//      qsizetype from) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QLocaleData13DigitSequence4usedE11QStringViewx(
    const QLocaleData::DigitSequence *self,
    const QString *text,
    qsizetype from) {
  return new QString(self->used(QStringView(*text), from).toString());
}

//  QStringView QLocaleData::DigitSequence::used(const QStringView text)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QLocaleData13DigitSequence4usedE11QStringView(
    const QLocaleData::DigitSequence *self,
    const QString *text) {
  return new QString(self->used(QStringView(*text)).toString());
}
