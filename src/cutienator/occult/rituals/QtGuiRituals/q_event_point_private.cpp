//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qeventpoint_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qeventpoint_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>

//  QEventPointPrivate::QEventPointPrivate(int id, const QPointingDevice
//      *device)
extern "C" Q_DECL_EXPORT
QEventPointPrivate *ritual_ZN18QEventPointPrivateC1EiPK15QPointingDevice(
    int id,
    const QPointingDevice *device) {
  return new QEventPointPrivate(id, device);
}

//  QEventPointPrivate::QEventPointPrivate(int pointId, QEventPoint::State
//      state, const QPointF &scenePosition, const QPointF &globalPosition)
extern "C" Q_DECL_EXPORT
QEventPointPrivate *ritual_ZN18QEventPointPrivateC1EiN11QEventPoint5StateERK7QPointFS4_(
    int pointId,
    QEventPoint::State state,
    const QPointF *scenePosition,
    const QPointF *globalPosition) {
  return new QEventPointPrivate(
      pointId,
      state,
      *scenePosition,
      *globalPosition);
}

//  bool QEventPointPrivate::operator==(const QEventPointPrivate &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QEventPointPrivateeqERKS_(
    const QEventPointPrivate *self,
    const QEventPointPrivate *other) {
  return self->operator==(*other);
}

//  QEventPointPrivate::~QEventPointPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QEventPointPrivateD1Ev(QEventPointPrivate *self) {
  delete self;
}
