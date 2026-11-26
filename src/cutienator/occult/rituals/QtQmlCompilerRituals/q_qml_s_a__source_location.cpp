//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/qqmlsasourcelocation.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtQmlCompiler/qqmlsasourcelocation.h>
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>

//  QQmlSA::SourceLocation::SourceLocation(quint32 offset, quint32 length,
//      quint32 line, quint32 column)
extern "C" Q_DECL_EXPORT
QQmlSA::SourceLocation *ritual_ZN6QQmlSA14SourceLocationC1Ejjjj(
    quint32 offset,
    quint32 length,
    quint32 line,
    quint32 column) {
  return new QQmlSA::SourceLocation(offset, length, line, column);
}

//  QQmlSA::SourceLocation::SourceLocation(const SourceLocation &a0)
extern "C" Q_DECL_EXPORT
QQmlSA::SourceLocation *ritual_ZN6QQmlSA14SourceLocationC1ERKS0_(
    const QQmlSA::SourceLocation *a0) {
  return new QQmlSA::SourceLocation(*a0);
}

//  QQmlSA::SourceLocation::SourceLocation(SourceLocation &&other)
extern "C" Q_DECL_EXPORT
QQmlSA::SourceLocation *ritual_ZN6QQmlSA14SourceLocationC1EOS0_(
    QQmlSA::SourceLocation *other) {
  return new QQmlSA::SourceLocation(std::move(*other));
}

//  SourceLocation &QQmlSA::SourceLocation::operator=(const SourceLocation
//      &a0)
extern "C" Q_DECL_EXPORT
QQmlSA::SourceLocation *ritual_ZN6QQmlSA14SourceLocationaSERKS0_(
    QQmlSA::SourceLocation *self,
    const QQmlSA::SourceLocation *a0) {
  return &(self->operator=(*a0));
}

//  SourceLocation &QQmlSA::SourceLocation::operator=(SourceLocation &&other)
extern "C" Q_DECL_EXPORT
QQmlSA::SourceLocation *ritual_ZN6QQmlSA14SourceLocationaSEOS0_(
    QQmlSA::SourceLocation *self,
    QQmlSA::SourceLocation *other) {
  return &(self->operator=(std::move(*other)));
}

//  QQmlSA::SourceLocation::~SourceLocation()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA14SourceLocationD1Ev(QQmlSA::SourceLocation *self) {
  delete self;
}

//  bool QQmlSA::SourceLocation::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlSA14SourceLocation7isValidEv(
    const QQmlSA::SourceLocation *self) {
  return self->isValid();
}

//  quint32 QQmlSA::SourceLocation::begin() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK6QQmlSA14SourceLocation5beginEv(
    const QQmlSA::SourceLocation *self) {
  return self->begin();
}

//  quint32 QQmlSA::SourceLocation::end() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK6QQmlSA14SourceLocation3endEv(
    const QQmlSA::SourceLocation *self) {
  return self->end();
}

//  quint32 QQmlSA::SourceLocation::offset() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK6QQmlSA14SourceLocation6offsetEv(
    const QQmlSA::SourceLocation *self) {
  return self->offset();
}

//  quint32 QQmlSA::SourceLocation::length() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK6QQmlSA14SourceLocation6lengthEv(
    const QQmlSA::SourceLocation *self) {
  return self->length();
}

//  quint32 QQmlSA::SourceLocation::startLine() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK6QQmlSA14SourceLocation9startLineEv(
    const QQmlSA::SourceLocation *self) {
  return self->startLine();
}

//  quint32 QQmlSA::SourceLocation::startColumn() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK6QQmlSA14SourceLocation11startColumnEv(
    const QQmlSA::SourceLocation *self) {
  return self->startColumn();
}

//  SourceLocation QQmlSA::SourceLocation::startZeroLengthLocation() const
extern "C" Q_DECL_EXPORT
QQmlSA::SourceLocation *ritual_ZNK6QQmlSA14SourceLocation23startZeroLengthLocationEv(
    const QQmlSA::SourceLocation *self) {
  return new QQmlSA::SourceLocation(self->startZeroLengthLocation());
}

//  SourceLocation QQmlSA::SourceLocation::endZeroLengthLocation(QStringView
//      text) const
extern "C" Q_DECL_EXPORT
QQmlSA::SourceLocation *ritual_ZNK6QQmlSA14SourceLocation21endZeroLengthLocationE11QStringView(
    const QQmlSA::SourceLocation *self,
    const QString *text) {
  return new QQmlSA::SourceLocation(
      self->endZeroLengthLocation(
          QStringView(*text)));
}

//  bool operator==(const SourceLocation &lhs, const SourceLocation &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSAeqERKNS_14SourceLocationES2_(
    const QQmlSA::SourceLocation *lhs,
    const QQmlSA::SourceLocation *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const SourceLocation &lhs, const SourceLocation &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSAneERKNS_14SourceLocationES2_(
    const QQmlSA::SourceLocation *lhs,
    const QQmlSA::SourceLocation *rhs) {
  return operator!=(*lhs, *rhs);
}

//  SourceLocation QQmlSA::SourceLocation::documentOrigin()
extern "C" Q_DECL_EXPORT
QQmlSA::SourceLocation *ritual_ZN6QQmlSA14SourceLocation14documentOriginEv() {
  return new QQmlSA::SourceLocation(
      QQmlSA::SourceLocation::documentOrigin());
}

//  qsizetype QQmlSA::SourceLocation::qHashImpl(const SourceLocation
//      &location, qsizetype seed)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN6QQmlSA14SourceLocation9qHashImplERKS0_x(
    const QQmlSA::SourceLocation *location,
    qsizetype seed) {
  return QQmlSA::SourceLocation::qHashImpl(*location, seed);
}

//  bool QQmlSA::SourceLocation::operatorEqualsImpl(const SourceLocation &a0,
//      const SourceLocation &a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSA14SourceLocation18operatorEqualsImplERKS0_S2_(
    const QQmlSA::SourceLocation *a0,
    const QQmlSA::SourceLocation *a1) {
  return QQmlSA::SourceLocation::operatorEqualsImpl(*a0, *a1);
}
