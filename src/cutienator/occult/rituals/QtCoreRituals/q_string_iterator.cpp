//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qstringiterator_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qstringiterator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>

//  bool QStringIterator::less(const QChar *lhs, const QChar *rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QStringIterator4lessEPK5QCharS2_(
    const QChar *lhs,
    const QChar *rhs) {
  return QStringIterator::less(lhs, rhs);
}

//  QStringIterator::QStringIterator(QStringView string, qsizetype idx)
extern "C" Q_DECL_EXPORT
QStringIterator *ritual_ZN15QStringIteratorC1E11QStringViewx(
    const QString *string,
    qsizetype idx) {
  return new QStringIterator(QStringView(*string), idx);
}

//  QStringIterator::QStringIterator(const QChar *begin, const QChar *end)
extern "C" Q_DECL_EXPORT
QStringIterator *ritual_ZN15QStringIteratorC1EPK5QCharS2_(
    const QChar *begin,
    const QChar *end) {
  return new QStringIterator(begin, end);
}

//  QStringIterator::QStringIterator(const QChar *begin, qsizetype idx, const
//      QChar *end)
extern "C" Q_DECL_EXPORT
QStringIterator *ritual_ZN15QStringIteratorC1EPK5QCharxS2_(
    const QChar *begin,
    qsizetype idx,
    const QChar *end) {
  return new QStringIterator(begin, idx, end);
}

//  QString::const_iterator QStringIterator::position() const
extern "C" Q_DECL_EXPORT
QString::const_iterator ritual_ZNK15QStringIterator8positionEv(
    const QStringIterator *self) {
  return self->position();
}

//  qsizetype QStringIterator::index() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK15QStringIterator5indexEv(const QStringIterator *self) {
  return self->index();
}

//  void QStringIterator::setPosition(QString::const_iterator position)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QStringIterator11setPositionEPK5QChar(
    QStringIterator *self,
    QString::const_iterator position) {
  self->setPosition(position);
}

//  bool QStringIterator::hasNext() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QStringIterator7hasNextEv(const QStringIterator *self) {
  return self->hasNext();
}

//  void QStringIterator::advance()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QStringIterator7advanceEv(QStringIterator *self) {
  self->advance();
}

//  void QStringIterator::advanceUnchecked()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QStringIterator16advanceUncheckedEv(QStringIterator *self) {
  self->advanceUnchecked();
}

//  bool QStringIterator::hasPrevious() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QStringIterator11hasPreviousEv(
    const QStringIterator *self) {
  return self->hasPrevious();
}

//  void QStringIterator::recede()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QStringIterator6recedeEv(QStringIterator *self) {
  self->recede();
}

//  void QStringIterator::recedeUnchecked()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QStringIterator15recedeUncheckedEv(QStringIterator *self) {
  self->recedeUnchecked();
}

//  QStringIterator::~QStringIterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QStringIteratorD1Ev(QStringIterator *self) {
  delete self;
}
