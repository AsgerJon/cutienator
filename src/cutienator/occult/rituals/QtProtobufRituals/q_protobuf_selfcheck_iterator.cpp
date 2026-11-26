//  Written by dev_tooling.RitualGenerator from the records of
//  QtProtobuf/6.12.0/QtProtobuf/private/qprotobufselfcheckiterator_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtProtobuf/QtProtobuf>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtProtobuf/6.12.0/QtProtobuf/private/qprotobufselfcheckiterator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearrayview.h>

//  QProtobufSelfcheckIterator::QProtobufSelfcheckIterator()
extern "C" Q_DECL_EXPORT
QProtobufSelfcheckIterator *ritual_ZN26QProtobufSelfcheckIteratorC1Ev() {
  return new QProtobufSelfcheckIterator();
}

//  QProtobufSelfcheckIterator
//      QProtobufSelfcheckIterator::fromView(QByteArrayView container)
extern "C" Q_DECL_EXPORT
QProtobufSelfcheckIterator *ritual_ZN26QProtobufSelfcheckIterator8fromViewE14QByteArrayView(
    const QByteArrayView *container) {
  return new QProtobufSelfcheckIterator(
      QProtobufSelfcheckIterator::fromView(
          *container));
}

//  QProtobufSelfcheckIterator::QProtobufSelfcheckIterator(const
//      QProtobufSelfcheckIterator &other)
extern "C" Q_DECL_EXPORT
QProtobufSelfcheckIterator *ritual_ZN26QProtobufSelfcheckIteratorC1ERKS_(
    const QProtobufSelfcheckIterator *other) {
  return new QProtobufSelfcheckIterator(*other);
}

//  QProtobufSelfcheckIterator &QProtobufSelfcheckIterator::operator=(const
//      QProtobufSelfcheckIterator &other)
extern "C" Q_DECL_EXPORT
QProtobufSelfcheckIterator *ritual_ZN26QProtobufSelfcheckIteratoraSERKS_(
    QProtobufSelfcheckIterator *self,
    const QProtobufSelfcheckIterator *other) {
  return &(self->operator=(*other));
}

//  QByteArray::const_iterator &QProtobufSelfcheckIterator::operator const
//      char *&()
extern "C" Q_DECL_EXPORT
QByteArray::const_iterator *ritual_ZN26QProtobufSelfcheckIteratorcvRPKcEv(
    QProtobufSelfcheckIterator *self) {
  return &(self->operator QByteArray::const_iterator &());
}

//  QByteArray::const_iterator QProtobufSelfcheckIterator::operator const
//      char *() const
extern "C" Q_DECL_EXPORT
QByteArray::const_iterator ritual_ZNK26QProtobufSelfcheckIteratorcvPKcEv(
    const QProtobufSelfcheckIterator *self) {
  return self->operator QByteArray::const_iterator();
}

//  char QProtobufSelfcheckIterator::operator*()
extern "C" Q_DECL_EXPORT
char ritual_ZN26QProtobufSelfcheckIteratordeEv(
    QProtobufSelfcheckIterator *self) {
  return self->operator*();
}

//  bool QProtobufSelfcheckIterator::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QProtobufSelfcheckIterator7isValidEv(
    const QProtobufSelfcheckIterator *self) {
  return self->isValid();
}

//  QProtobufSelfcheckIterator &QProtobufSelfcheckIterator::operator++()
extern "C" Q_DECL_EXPORT
QProtobufSelfcheckIterator *ritual_ZN26QProtobufSelfcheckIteratorppEv(
    QProtobufSelfcheckIterator *self) {
  return &(self->operator++());
}

//  QProtobufSelfcheckIterator QProtobufSelfcheckIterator::operator++(int a0)
extern "C" Q_DECL_EXPORT
QProtobufSelfcheckIterator *ritual_ZN26QProtobufSelfcheckIteratorppEi(
    QProtobufSelfcheckIterator *self,
    int a0) {
  return new QProtobufSelfcheckIterator(self->operator++(a0));
}

//  QProtobufSelfcheckIterator &QProtobufSelfcheckIterator::operator--()
extern "C" Q_DECL_EXPORT
QProtobufSelfcheckIterator *ritual_ZN26QProtobufSelfcheckIteratormmEv(
    QProtobufSelfcheckIterator *self) {
  return &(self->operator--());
}

//  QProtobufSelfcheckIterator QProtobufSelfcheckIterator::operator--(int a0)
extern "C" Q_DECL_EXPORT
QProtobufSelfcheckIterator *ritual_ZN26QProtobufSelfcheckIteratormmEi(
    QProtobufSelfcheckIterator *self,
    int a0) {
  return new QProtobufSelfcheckIterator(self->operator--(a0));
}

//  QProtobufSelfcheckIterator
//      &QProtobufSelfcheckIterator::operator+=(qsizetype count)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QProtobufSelfcheckIteratorpLEx(
    QProtobufSelfcheckIterator *self,
    qsizetype count) {
  self->operator+=(count);
}

//  QProtobufSelfcheckIterator
//      &QProtobufSelfcheckIterator::operator-=(qsizetype count)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QProtobufSelfcheckIteratormIEx(
    QProtobufSelfcheckIterator *self,
    qsizetype count) {
  self->operator-=(count);
}

//  const char *QProtobufSelfcheckIterator::data() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK26QProtobufSelfcheckIterator4dataEv(
    const QProtobufSelfcheckIterator *self) {
  return self->data();
}

//  qsizetype QProtobufSelfcheckIterator::bytesLeft() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK26QProtobufSelfcheckIterator9bytesLeftEv(
    const QProtobufSelfcheckIterator *self) {
  return self->bytesLeft();
}

//  QProtobufSelfcheckIterator::QProtobufSelfcheckIterator(QByteArrayView
//      container)
extern "C" Q_DECL_EXPORT
QProtobufSelfcheckIterator *ritual_ZN26QProtobufSelfcheckIteratorC1E14QByteArrayView(
    const QByteArrayView *container) {
  return new QProtobufSelfcheckIterator(*container);
}

//  bool operator==(const QProtobufSelfcheckIterator &lhs, const
//      QProtobufSelfcheckIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK26QProtobufSelfcheckIteratorS1_(
    const QProtobufSelfcheckIterator *lhs,
    const QProtobufSelfcheckIterator *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QProtobufSelfcheckIterator &lhs, const
//      QProtobufSelfcheckIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK26QProtobufSelfcheckIteratorS1_(
    const QProtobufSelfcheckIterator *lhs,
    const QProtobufSelfcheckIterator *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(const QProtobufSelfcheckIterator &lhs, const
//      QByteArray::const_iterator &other)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK26QProtobufSelfcheckIteratorRKPKc(
    const QProtobufSelfcheckIterator *lhs,
    const QByteArray::const_iterator *other) {
  return operator==(*lhs, *other);
}

//  bool operator!=(const QProtobufSelfcheckIterator &lhs, const
//      QByteArray::const_iterator &other)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK26QProtobufSelfcheckIteratorRKPKc(
    const QProtobufSelfcheckIterator *lhs,
    const QByteArray::const_iterator *other) {
  return operator!=(*lhs, *other);
}

//  qint64 operator-(const QProtobufSelfcheckIterator &lhs, const
//      QProtobufSelfcheckIterator &rhs)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZmiRK26QProtobufSelfcheckIteratorS1_(
    const QProtobufSelfcheckIterator *lhs,
    const QProtobufSelfcheckIterator *rhs) {
  return operator-(*lhs, *rhs);
}

//  QProtobufSelfcheckIterator::~QProtobufSelfcheckIterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QProtobufSelfcheckIteratorD1Ev(
    QProtobufSelfcheckIterator *self) {
  delete self;
}
