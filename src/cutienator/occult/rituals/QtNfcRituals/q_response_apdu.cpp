//  Written by dev_tooling.RitualGenerator from the records of
//  QtNfc/6.12.0/QtNfc/private/qapduutils_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtNfc/6.12.0/QtNfc/private/qtnfcglobal_p.h>
#include <QtNfc/QtNfc>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNfc/6.12.0/QtNfc/private/qapduutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qapduutils_p.h"
#include <QtCore/QtEndian>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtconnectivity/src/nfc/qapduutils.cpp, line 25, as _ZN13QResponseApduC1ERK10QByteArray
inline QResponseApdu::QResponseApdu(const QByteArray &response)
{
    const auto view = qToByteArrayViewIgnoringNull(response);
    if (view.size() < 2) {
        m_status = Empty;
        m_data = response;
    } else {
        const auto dataSize = view.size() - 2;
        m_status = qFromBigEndian(qFromUnaligned<uint16_t>(view.data() + dataSize));
        m_data = response.left(dataSize);
    }
}
//  -----------------------------------------------------------------------

//  QResponseApdu::QResponseApdu(const QByteArray &response)
extern "C" Q_DECL_EXPORT
QResponseApdu *ritual_ZN13QResponseApduC1ERK10QByteArray(
    const QByteArray *response) {
  return new QResponseApdu(*response);
}

//  const QByteArray &QResponseApdu::data() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK13QResponseApdu4dataEv(const QResponseApdu *self) {
  return new QByteArray(self->data());
}

//  bool QResponseApdu::isOk() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QResponseApdu4isOkEv(const QResponseApdu *self) {
  return self->isOk();
}

//  QResponseApdu::~QResponseApdu()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QResponseApduD1Ev(QResponseApdu *self) {
  delete self;
}
