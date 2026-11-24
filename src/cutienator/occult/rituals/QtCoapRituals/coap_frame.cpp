//  Written by dev_tooling.RitualGenerator from the records of
//  QtCoap/6.12.0/QtCoap/private/qcoapconnection_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCoap/QtCoap>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCoap/6.12.0/QtCoap/private/qcoapconnection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>

//  CoapFrame::CoapFrame(const QByteArray &pdu, const QString &hostName,
//      quint16 portNumber)
extern "C" Q_DECL_EXPORT
CoapFrame *ritual_ZN9CoapFrameC1ERK10QByteArrayRK7QStringt(
    const QByteArray *pdu,
    const QString *hostName,
    quint16 portNumber) {
  return new CoapFrame(*pdu, *hostName, portNumber);
}

//  CoapFrame::~CoapFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN9CoapFrameD1Ev(CoapFrame *self) {
  delete self;
}
