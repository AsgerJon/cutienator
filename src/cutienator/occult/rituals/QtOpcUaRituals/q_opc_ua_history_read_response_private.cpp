//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/6.12.0/QtOpcUa/private/qopcuahistoryreadresponse_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpcUa/qopcuahistoryreadresponse.h>
#include <QtOpcUa/QtOpcUa>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpcUa/6.12.0/QtOpcUa/private/qopcuahistoryreadresponse_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QOpcUaHistoryReadResponse *QOpcUaHistoryReadResponsePrivate::q_func()
extern "C" Q_DECL_EXPORT
QOpcUaHistoryReadResponse *ritual_ZN32QOpcUaHistoryReadResponsePrivate6q_funcEv(
    QOpcUaHistoryReadResponsePrivate *self) {
  return self->q_func();
}

//  const QOpcUaHistoryReadResponse
//      *QOpcUaHistoryReadResponsePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QOpcUaHistoryReadResponse *ritual_ZNK32QOpcUaHistoryReadResponsePrivate6q_funcEv(
    const QOpcUaHistoryReadResponsePrivate *self) {
  return self->q_func();
}

//  QOpcUaHistoryReadResponsePrivate::QOpcUaHistoryReadResponsePrivate(QOpcUa
//      HistoryReadResponseImpl *impl)
extern "C" Q_DECL_EXPORT
QOpcUaHistoryReadResponsePrivate *ritual_ZN32QOpcUaHistoryReadResponsePrivateC1EP29QOpcUaHistoryReadResponseImpl(
    QOpcUaHistoryReadResponseImpl *impl) {
  return new QOpcUaHistoryReadResponsePrivate(impl);
}

//  QOpcUaHistoryReadResponsePrivate::~QOpcUaHistoryReadResponsePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QOpcUaHistoryReadResponsePrivateD1Ev(
    QOpcUaHistoryReadResponsePrivate *self) {
  delete self;
}
