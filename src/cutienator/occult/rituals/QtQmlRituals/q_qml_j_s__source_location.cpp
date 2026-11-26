//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmljssourcelocation_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljssourcelocation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>
#include <utility>
#include <QtCore/QStringView>

//  bool QQmlJS::SourceLocation::qSizeTypeCanHoldQuint32()
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS14SourceLocation23qSizeTypeCanHoldQuint32Ev() {
  return QQmlJS::SourceLocation::qSizeTypeCanHoldQuint32();
}

//  QQmlJS::SourceLocation::SourceLocation(quint32 offset, quint32 length,
//      quint32 line, quint32 column)
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZN6QQmlJS14SourceLocationC1Ejjjj(
    quint32 offset,
    quint32 length,
    quint32 line,
    quint32 column) {
  return new QQmlJS::SourceLocation(offset, length, line, column);
}

//  SourceLocation QQmlJS::SourceLocation::fromQSizeType(qsizetype offset,
//      qsizetype length, qsizetype line, qsizetype column)
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZN6QQmlJS14SourceLocation13fromQSizeTypeExxxx(
    qsizetype offset,
    qsizetype length,
    qsizetype line,
    qsizetype column) {
  return new QQmlJS::SourceLocation(
      QQmlJS::SourceLocation::fromQSizeType(
          offset,
          length,
          line,
          column));
}

//  quint32 QQmlJS::SourceLocation::offsetFrom(QStringView text, quint32
//      line, quint32 column, const SourceLocation &startHint)
extern "C" Q_DECL_EXPORT
quint32 ritual_ZN6QQmlJS14SourceLocation10offsetFromE11QStringViewjjRKS0_(
    const QString *text,
    quint32 line,
    quint32 column,
    const QQmlJS::SourceLocation *startHint) {
  return QQmlJS::SourceLocation::offsetFrom(
      QStringView(*text),
      line,
      column,
      *startHint);
}

//  std::pair<quint32, quint32>
//      QQmlJS::SourceLocation::rowAndColumnFrom(QStringView text, quint32
//      offset, const SourceLocation &startHint)
extern "C" Q_DECL_EXPORT
std::pair<quint32, quint32> *ritual_ZN6QQmlJS14SourceLocation16rowAndColumnFromE11QStringViewjRKS0_(
    const QString *text,
    quint32 offset,
    const QQmlJS::SourceLocation *startHint) {
  return new std::pair<quint32, quint32>(
      QQmlJS::SourceLocation::rowAndColumnFrom(
          QStringView(*text),
          offset,
          *startHint));
}

//  bool QQmlJS::SourceLocation::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS14SourceLocation7isValidEv(
    const QQmlJS::SourceLocation *self) {
  return self->isValid();
}

//  qsizetype QQmlJS::SourceLocation::begin() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK6QQmlJS14SourceLocation5beginEv(
    const QQmlJS::SourceLocation *self) {
  return self->begin();
}

//  qsizetype QQmlJS::SourceLocation::end() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK6QQmlJS14SourceLocation3endEv(
    const QQmlJS::SourceLocation *self) {
  return self->end();
}

//  SourceLocation QQmlJS::SourceLocation::startZeroLengthLocation() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK6QQmlJS14SourceLocation23startZeroLengthLocationEv(
    const QQmlJS::SourceLocation *self) {
  return new QQmlJS::SourceLocation(self->startZeroLengthLocation());
}

//  SourceLocation QQmlJS::SourceLocation::endZeroLengthLocation(QStringView
//      text) const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK6QQmlJS14SourceLocation21endZeroLengthLocationE11QStringView(
    const QQmlJS::SourceLocation *self,
    const QString *text) {
  return new QQmlJS::SourceLocation(
      self->endZeroLengthLocation(
          QStringView(*text)));
}

//  bool operator==(const SourceLocation &a, const SourceLocation &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJSeqERKNS_14SourceLocationES2_(
    const QQmlJS::SourceLocation *a,
    const QQmlJS::SourceLocation *b) {
  return operator==(*a, *b);
}

//  bool operator!=(const SourceLocation &a, const SourceLocation &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJSneERKNS_14SourceLocationES2_(
    const QQmlJS::SourceLocation *a,
    const QQmlJS::SourceLocation *b) {
  return operator!=(*a, *b);
}

//  QQmlJS::SourceLocation::~SourceLocation()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS14SourceLocationD1Ev(QQmlJS::SourceLocation *self) {
  delete self;
}

//  a std::pair<quint32, quint32> a ritual of QQmlJS::SourceLocation gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlJS_SourceLocation__std_pair_quint32_quint32(
    std::pair<quint32, quint32> *self) {
  delete self;
}
