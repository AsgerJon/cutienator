//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qrangemodel_impl.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if !defined(Q_QDOC)
#include <QtCore/qrangemodel.h>

//  bool operator==(const Connection &lhs, const Connection &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QRangeModelDetailseqERKNS_17ConnectionStorage10ConnectionES3_(
    const QRangeModelDetails::ConnectionStorage::Connection *lhs,
    const QRangeModelDetails::ConnectionStorage::Connection *rhs) {
  return operator==(*lhs, *rhs);
}

//  QRangeModelDetails::ConnectionStorage::Connection::~Connection()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRangeModelDetails17ConnectionStorage10ConnectionD1Ev(
    QRangeModelDetails::ConnectionStorage::Connection *self) {
  delete self;
}

#endif  // !defined(Q_QDOC)
