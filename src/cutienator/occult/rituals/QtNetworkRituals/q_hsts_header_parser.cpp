//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhsts_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhsts_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdatetime.h>

//  QDateTime QHstsHeaderParser::expirationDate() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK17QHstsHeaderParser14expirationDateEv(
    const QHstsHeaderParser *self) {
  return new QDateTime(self->expirationDate());
}

//  bool QHstsHeaderParser::includeSubDomains() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QHstsHeaderParser17includeSubDomainsEv(
    const QHstsHeaderParser *self) {
  return self->includeSubDomains();
}

//  QHstsHeaderParser::~QHstsHeaderParser()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHstsHeaderParserD1Ev(QHstsHeaderParser *self) {
  delete self;
}
