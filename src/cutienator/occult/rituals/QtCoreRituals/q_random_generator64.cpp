//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qrandom.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qrandom.h>

//  quint64 QRandomGenerator64::generate()
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN18QRandomGenerator648generateEv(QRandomGenerator64 *self) {
  return self->generate();
}

//  result_type QRandomGenerator64::operator()()
extern "C" Q_DECL_EXPORT
QRandomGenerator64::result_type ritual_ZN18QRandomGenerator64clEv(
    QRandomGenerator64 *self) {
  return self->operator()();
}

#if !defined(Q_QDOC)
//  QRandomGenerator64::QRandomGenerator64(quint32 seedValue)
extern "C" Q_DECL_EXPORT
QRandomGenerator64 *ritual_ZN18QRandomGenerator64C1Ej(quint32 seedValue) {
  return new QRandomGenerator64(seedValue);
}
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
//  QRandomGenerator64::QRandomGenerator64(const quint32 *seedBuffer,
//      qsizetype len)
extern "C" Q_DECL_EXPORT
QRandomGenerator64 *ritual_ZN18QRandomGenerator64C1EPKjx(
    const quint32 *seedBuffer,
    qsizetype len) {
  return new QRandomGenerator64(seedBuffer, len);
}
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
//  QRandomGenerator64::QRandomGenerator64(std::seed_seq &sseq)
extern "C" Q_DECL_EXPORT
QRandomGenerator64 *ritual_ZN18QRandomGenerator64C1ERSt8seed_seq(
    std::seed_seq *sseq) {
  return new QRandomGenerator64(*sseq);
}
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
//  QRandomGenerator64::QRandomGenerator64(const quint32 *begin, const
//      quint32 *end)
extern "C" Q_DECL_EXPORT
QRandomGenerator64 *ritual_ZN18QRandomGenerator64C1EPKjS1_(
    const quint32 *begin,
    const quint32 *end) {
  return new QRandomGenerator64(begin, end);
}
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
//  QRandomGenerator64::QRandomGenerator64(const QRandomGenerator &other)
extern "C" Q_DECL_EXPORT
QRandomGenerator64 *ritual_ZN18QRandomGenerator64C1ERK16QRandomGenerator(
    const QRandomGenerator *other) {
  return new QRandomGenerator64(*other);
}
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
//  void QRandomGenerator64::discard(unsigned long long z)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRandomGenerator647discardEy(
    QRandomGenerator64 *self,
    unsigned long long z) {
  self->discard(z);
}
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
//  result_type QRandomGenerator64::min()
extern "C" Q_DECL_EXPORT
QRandomGenerator64::result_type ritual_ZN18QRandomGenerator643minEv() {
  return QRandomGenerator64::min();
}
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
//  result_type QRandomGenerator64::max()
extern "C" Q_DECL_EXPORT
QRandomGenerator64::result_type ritual_ZN18QRandomGenerator643maxEv() {
  return QRandomGenerator64::max();
}
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
//  QRandomGenerator64 *QRandomGenerator64::system()
extern "C" Q_DECL_EXPORT
QRandomGenerator64 *ritual_ZN18QRandomGenerator646systemEv() {
  return QRandomGenerator64::system();
}
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
//  QRandomGenerator64 *QRandomGenerator64::global()
extern "C" Q_DECL_EXPORT
QRandomGenerator64 *ritual_ZN18QRandomGenerator646globalEv() {
  return QRandomGenerator64::global();
}
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
//  QRandomGenerator64 QRandomGenerator64::securelySeeded()
extern "C" Q_DECL_EXPORT
QRandomGenerator64 *ritual_ZN18QRandomGenerator6414securelySeededEv() {
  return new QRandomGenerator64(QRandomGenerator64::securelySeeded());
}
#endif  // !defined(Q_QDOC)

//  QRandomGenerator64::~QRandomGenerator64()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRandomGenerator64D1Ev(QRandomGenerator64 *self) {
  delete self;
}
