//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qrandom.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qrandom.h>

//  QRandomGenerator::QRandomGenerator(quint32 seedValue)
extern "C" Q_DECL_EXPORT
QRandomGenerator *ritual_ZN16QRandomGeneratorC1Ej(quint32 seedValue) {
  return new QRandomGenerator(seedValue);
}

//  QRandomGenerator::QRandomGenerator(const QRandomGenerator &other)
extern "C" Q_DECL_EXPORT
QRandomGenerator *ritual_ZN16QRandomGeneratorC1ERKS_(
    const QRandomGenerator *other) {
  return new QRandomGenerator(*other);
}

//  QRandomGenerator::~QRandomGenerator()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QRandomGeneratorD1Ev(QRandomGenerator *self) {
  delete self;
}

//  bool operator==(const QRandomGenerator &rng1, const QRandomGenerator
//      &rng2)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK16QRandomGeneratorS1_(
    const QRandomGenerator *rng1,
    const QRandomGenerator *rng2) {
  return operator==(*rng1, *rng2);
}

//  bool operator!=(const QRandomGenerator &rng1, const QRandomGenerator
//      &rng2)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK16QRandomGeneratorS1_(
    const QRandomGenerator *rng1,
    const QRandomGenerator *rng2) {
  return operator!=(*rng1, *rng2);
}

//  quint32 QRandomGenerator::generate()
extern "C" Q_DECL_EXPORT
quint32 ritual_ZN16QRandomGenerator8generateEv(QRandomGenerator *self) {
  return self->generate();
}

//  quint64 QRandomGenerator::generate64()
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN16QRandomGenerator10generate64Ev(QRandomGenerator *self) {
  return self->generate64();
}

//  double QRandomGenerator::generateDouble()
extern "C" Q_DECL_EXPORT
double ritual_ZN16QRandomGenerator14generateDoubleEv(
    QRandomGenerator *self) {
  return self->generateDouble();
}

//  double QRandomGenerator::bounded(double highest)
extern "C" Q_DECL_EXPORT
double ritual_ZN16QRandomGenerator7boundedEd(
    QRandomGenerator *self,
    double highest) {
  return self->bounded(highest);
}

//  quint32 QRandomGenerator::bounded(quint32 highest)
extern "C" Q_DECL_EXPORT
quint32 ritual_ZN16QRandomGenerator7boundedEj(
    QRandomGenerator *self,
    quint32 highest) {
  return self->bounded(highest);
}

//  quint32 QRandomGenerator::bounded(quint32 lowest, quint32 highest)
extern "C" Q_DECL_EXPORT
quint32 ritual_ZN16QRandomGenerator7boundedEjj(
    QRandomGenerator *self,
    quint32 lowest,
    quint32 highest) {
  return self->bounded(lowest, highest);
}

//  int QRandomGenerator::bounded(int highest)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QRandomGenerator7boundedEi(
    QRandomGenerator *self,
    int highest) {
  return self->bounded(highest);
}

//  int QRandomGenerator::bounded(int lowest, int highest)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QRandomGenerator7boundedEii(
    QRandomGenerator *self,
    int lowest,
    int highest) {
  return self->bounded(lowest, highest);
}

//  quint64 QRandomGenerator::bounded(quint64 highest)
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN16QRandomGenerator7boundedEy(
    QRandomGenerator *self,
    quint64 highest) {
  return self->bounded(highest);
}

//  quint64 QRandomGenerator::bounded(quint64 lowest, quint64 highest)
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN16QRandomGenerator7boundedEyy(
    QRandomGenerator *self,
    quint64 lowest,
    quint64 highest) {
  return self->bounded(lowest, highest);
}

//  qint64 QRandomGenerator::bounded(qint64 highest)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN16QRandomGenerator7boundedEx(
    QRandomGenerator *self,
    qint64 highest) {
  return self->bounded(highest);
}

//  qint64 QRandomGenerator::bounded(qint64 lowest, qint64 highest)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN16QRandomGenerator7boundedExx(
    QRandomGenerator *self,
    qint64 lowest,
    qint64 highest) {
  return self->bounded(lowest, highest);
}

//  qint64 QRandomGenerator::bounded(int lowest, qint64 highest)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN16QRandomGenerator7boundedEix(
    QRandomGenerator *self,
    int lowest,
    qint64 highest) {
  return self->bounded(lowest, highest);
}

//  qint64 QRandomGenerator::bounded(qint64 lowest, int highest)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN16QRandomGenerator7boundedExi(
    QRandomGenerator *self,
    qint64 lowest,
    int highest) {
  return self->bounded(lowest, highest);
}

//  quint64 QRandomGenerator::bounded(unsigned int lowest, quint64 highest)
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN16QRandomGenerator7boundedEjy(
    QRandomGenerator *self,
    unsigned int lowest,
    quint64 highest) {
  return self->bounded(lowest, highest);
}

//  quint64 QRandomGenerator::bounded(quint64 lowest, unsigned int highest)
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN16QRandomGenerator7boundedEyj(
    QRandomGenerator *self,
    quint64 lowest,
    unsigned int highest) {
  return self->bounded(lowest, highest);
}

//  void QRandomGenerator::generate(quint32 *begin, quint32 *end)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QRandomGenerator8generateEPjS0_(
    QRandomGenerator *self,
    quint32 *begin,
    quint32 *end) {
  self->generate(begin, end);
}

//  result_type QRandomGenerator::operator()()
extern "C" Q_DECL_EXPORT
QRandomGenerator::result_type ritual_ZN16QRandomGeneratorclEv(
    QRandomGenerator *self) {
  return self->operator()();
}

//  void QRandomGenerator::seed(quint32 s)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QRandomGenerator4seedEj(QRandomGenerator *self, quint32 s) {
  self->seed(s);
}

//  void QRandomGenerator::discard(unsigned long long z)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QRandomGenerator7discardEy(
    QRandomGenerator *self,
    unsigned long long z) {
  self->discard(z);
}

//  result_type QRandomGenerator::min()
extern "C" Q_DECL_EXPORT
QRandomGenerator::result_type ritual_ZN16QRandomGenerator3minEv() {
  return QRandomGenerator::min();
}

//  result_type QRandomGenerator::max()
extern "C" Q_DECL_EXPORT
QRandomGenerator::result_type ritual_ZN16QRandomGenerator3maxEv() {
  return QRandomGenerator::max();
}

//  QRandomGenerator *QRandomGenerator::system()
extern "C" Q_DECL_EXPORT
QRandomGenerator *ritual_ZN16QRandomGenerator6systemEv() {
  return QRandomGenerator::system();
}

//  QRandomGenerator *QRandomGenerator::global()
extern "C" Q_DECL_EXPORT
QRandomGenerator *ritual_ZN16QRandomGenerator6globalEv() {
  return QRandomGenerator::global();
}

//  QRandomGenerator QRandomGenerator::securelySeeded()
extern "C" Q_DECL_EXPORT
QRandomGenerator *ritual_ZN16QRandomGenerator14securelySeededEv() {
  return new QRandomGenerator(QRandomGenerator::securelySeeded());
}
