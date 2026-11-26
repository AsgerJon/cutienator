//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qbytearraymatcher.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qbytearraymatcher.h>
#include <QtCore/QStaticByteArrayMatcherBase>

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

//  Skiptable QStaticByteArrayMatcherBase::generate(const char *pattern,
//      size_t n)
extern "C" Q_DECL_EXPORT
QStaticByteArrayMatcherBase::Skiptable *ritual_ZN27QStaticByteArrayMatcherBase8generateEPKcm(
    const char *pattern,
    size_t n) {
  return new QStaticByteArrayMatcherBase::Skiptable(
      QStaticByteArrayMatcherBase::generate(
          pattern,
          n));
}

//  a QStaticByteArrayMatcherBase::Skiptable a ritual of
//      QStaticByteArrayMatcherBase gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QStaticByteArrayMatcherBase__QStaticByteArrayMatcherBase_Skiptable(
    QStaticByteArrayMatcherBase::Skiptable *self) {
  delete self;
}
