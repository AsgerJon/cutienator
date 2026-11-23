//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qbytearraymatcher.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qbytearraymatcher.h>

//  QStaticByteArrayMatcherBase::QStaticByteArrayMatcherBase(const char
//      *pattern, size_t n)
extern "C" Q_DECL_EXPORT
QStaticByteArrayMatcherBase *ritual_ZN27QStaticByteArrayMatcherBaseC1EPKcm(
    const char *pattern,
    size_t n) {
  return new QStaticByteArrayMatcherBase(pattern, n);
}

//  QStaticByteArrayMatcherBase::~QStaticByteArrayMatcherBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QStaticByteArrayMatcherBaseD1Ev(
    QStaticByteArrayMatcherBase *self) {
  delete self;
}

//  qsizetype QStaticByteArrayMatcherBase::indexOfIn(const char *needle,
//      size_t nlen, const char *haystack, qsizetype hlen, qsizetype from)
//      const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK27QStaticByteArrayMatcherBase9indexOfInEPKcmS1_xx(
    const QStaticByteArrayMatcherBase *self,
    const char *needle,
    size_t nlen,
    const char *haystack,
    qsizetype hlen,
    qsizetype from) {
  return self->indexOfIn(needle, nlen, haystack, hlen, from);
}
