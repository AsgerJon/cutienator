//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qrangemodel_impl.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(rangemodel)
#if !defined(Q_QDOC)
#include <QtCore/qrangemodel.h>

//  QRangeModelDetails::ConnectionStorage::~ConnectionStorage()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRangeModelDetails17ConnectionStorageD1Ev(
    QRangeModelDetails::ConnectionStorage *self) {
  delete self;
}

#endif  // !defined(Q_QDOC)
#endif  // QT_CONFIG(rangemodel)
