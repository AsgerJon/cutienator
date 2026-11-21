//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qregularexpression.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qregularexpression.h>

//  QRegularExpressionMatchIterator::QRegularExpressionMatchIterator()
extern "C" Q_DECL_EXPORT
QRegularExpressionMatchIterator *ritual_ZN31QRegularExpressionMatchIteratorC1Ev() {
  return new QRegularExpressionMatchIterator();
}

//  QRegularExpressionMatchIterator::~QRegularExpressionMatchIterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QRegularExpressionMatchIteratorD1Ev(
    QRegularExpressionMatchIterator *self) {
  delete self;
}

//  QRegularExpressionMatchIterator::QRegularExpressionMatchIterator(const
//      QRegularExpressionMatchIterator &iterator)
extern "C" Q_DECL_EXPORT
QRegularExpressionMatchIterator *ritual_ZN31QRegularExpressionMatchIteratorC1ERKS_(
    const QRegularExpressionMatchIterator *iterator) {
  return new QRegularExpressionMatchIterator(*iterator);
}

//  bool QRegularExpressionMatchIterator::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QRegularExpressionMatchIterator7isValidEv(
    const QRegularExpressionMatchIterator *self) {
  return self->isValid();
}

//  bool QRegularExpressionMatchIterator::hasNext() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QRegularExpressionMatchIterator7hasNextEv(
    const QRegularExpressionMatchIterator *self) {
  return self->hasNext();
}

//  QRegularExpressionMatch QRegularExpressionMatchIterator::next()
extern "C" Q_DECL_EXPORT
QRegularExpressionMatch *ritual_ZN31QRegularExpressionMatchIterator4nextEv(
    QRegularExpressionMatchIterator *self) {
  return new QRegularExpressionMatch(self->next());
}

//  QRegularExpressionMatch QRegularExpressionMatchIterator::peekNext() const
extern "C" Q_DECL_EXPORT
QRegularExpressionMatch *ritual_ZNK31QRegularExpressionMatchIterator8peekNextEv(
    const QRegularExpressionMatchIterator *self) {
  return new QRegularExpressionMatch(self->peekNext());
}

//  QRegularExpression QRegularExpressionMatchIterator::regularExpression()
//      const
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZNK31QRegularExpressionMatchIterator17regularExpressionEv(
    const QRegularExpressionMatchIterator *self) {
  return new QRegularExpression(self->regularExpression());
}

//  QRegularExpression::MatchType
//      QRegularExpressionMatchIterator::matchType() const
extern "C" Q_DECL_EXPORT
QRegularExpression::MatchType ritual_ZNK31QRegularExpressionMatchIterator9matchTypeEv(
    const QRegularExpressionMatchIterator *self) {
  return self->matchType();
}

//  QRegularExpression::MatchOptions
//      QRegularExpressionMatchIterator::matchOptions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK31QRegularExpressionMatchIterator12matchOptionsEv(
    const QRegularExpressionMatchIterator *self) {
  return static_cast<int>(self->matchOptions().toInt());
}
