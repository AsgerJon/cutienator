//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qrangemodel_impl.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qrangemodel.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  QHash<int, QByteArray> QRangeModelImplBase::roleNames() const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK19QRangeModelImplBase9roleNamesEv(
    const QRangeModelImplBase *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

//  QRangeModelImplBase *QRangeModelImplBase::getImplementation(QRangeModel
//      *model)
extern "C" Q_DECL_EXPORT
QRangeModelImplBase *ritual_ZN19QRangeModelImplBase17getImplementationEP11QRangeModel(
    QRangeModel *model) {
  return QRangeModelImplBase::getImplementation(model);
}

//  const QRangeModelImplBase *QRangeModelImplBase::getImplementation(const
//      QRangeModel *model)
extern "C" Q_DECL_EXPORT
const QRangeModelImplBase *ritual_ZN19QRangeModelImplBase17getImplementationEPK11QRangeModel(
    const QRangeModel *model) {
  return QRangeModelImplBase::getImplementation(model);
}

//  QHash<int, QByteArray> QRangeModelImplBase::roleNamesForSimpleType()
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZN19QRangeModelImplBase22roleNamesForSimpleTypeEv() {
  return new QHash<int, QByteArray>(
      QRangeModelImplBase::roleNamesForSimpleType());
}
