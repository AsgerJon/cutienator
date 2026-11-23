//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qbytearraymatcher.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qbytearraymatcher.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qbytearrayview.h>

//  QByteArrayMatcher::QByteArrayMatcher()
extern "C" Q_DECL_EXPORT
QByteArrayMatcher *ritual_ZN17QByteArrayMatcherC1Ev() {
  return new QByteArrayMatcher();
}

//  QByteArrayMatcher::QByteArrayMatcher(const QByteArray &pattern)
extern "C" Q_DECL_EXPORT
QByteArrayMatcher *ritual_ZN17QByteArrayMatcherC1ERK10QByteArray(
    const QByteArray *pattern) {
  return new QByteArrayMatcher(*pattern);
}

//  QByteArrayMatcher::QByteArrayMatcher(QByteArrayView pattern)
extern "C" Q_DECL_EXPORT
QByteArrayMatcher *ritual_ZN17QByteArrayMatcherC1E14QByteArrayView(
    const QByteArrayView *pattern) {
  return new QByteArrayMatcher(*pattern);
}

//  QByteArrayMatcher::QByteArrayMatcher(const char *pattern, qsizetype
//      length)
extern "C" Q_DECL_EXPORT
QByteArrayMatcher *ritual_ZN17QByteArrayMatcherC1EPKcx(
    const char *pattern,
    qsizetype length) {
  return new QByteArrayMatcher(pattern, length);
}

//  QByteArrayMatcher::QByteArrayMatcher(const QByteArrayMatcher &other)
extern "C" Q_DECL_EXPORT
QByteArrayMatcher *ritual_ZN17QByteArrayMatcherC1ERKS_(
    const QByteArrayMatcher *other) {
  return new QByteArrayMatcher(*other);
}

//  QByteArrayMatcher::~QByteArrayMatcher()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QByteArrayMatcherD1Ev(QByteArrayMatcher *self) {
  delete self;
}

//  void QByteArrayMatcher::setPattern(const QByteArray &pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QByteArrayMatcher10setPatternERK10QByteArray(
    QByteArrayMatcher *self,
    const QByteArray *pattern) {
  self->setPattern(*pattern);
}

//  qsizetype QByteArrayMatcher::indexIn(const char *str, qsizetype len,
//      qsizetype from) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK17QByteArrayMatcher7indexInEPKcxx(
    const QByteArrayMatcher *self,
    const char *str,
    qsizetype len,
    qsizetype from) {
  return self->indexIn(str, len, from);
}

//  qsizetype QByteArrayMatcher::indexIn(QByteArrayView data, qsizetype from)
//      const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK17QByteArrayMatcher7indexInE14QByteArrayViewx(
    const QByteArrayMatcher *self,
    const QByteArrayView *data,
    qsizetype from) {
  return self->indexIn(*data, from);
}

//  QByteArray QByteArrayMatcher::pattern() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK17QByteArrayMatcher7patternEv(
    const QByteArrayMatcher *self) {
  return new QByteArray(self->pattern());
}
