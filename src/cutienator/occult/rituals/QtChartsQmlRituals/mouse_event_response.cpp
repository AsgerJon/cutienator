//  Written by dev_tooling.RitualGenerator from the records of
//  QtChartsQml/6.12.0/QtChartsQml/private/declarativeabstractrendernode_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#include <QtChartsQml/QtChartsQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativeabstractrendernode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>

//  MouseEventResponse::MouseEventResponse()
extern "C" Q_DECL_EXPORT
MouseEventResponse *ritual_ZN18MouseEventResponseC1Ev() {
  return new MouseEventResponse();
}

//  MouseEventResponse::MouseEventResponse(MouseEventType t, const QPoint &p,
//      const QXYSeries *s)
extern "C" Q_DECL_EXPORT
MouseEventResponse *ritual_ZN18MouseEventResponseC1ENS_14MouseEventTypeERK6QPointPK9QXYSeries(
    MouseEventResponse::MouseEventType t,
    const QPoint *p,
    const QXYSeries *s) {
  return new MouseEventResponse(t, *p, s);
}

//  MouseEventResponse::~MouseEventResponse()
extern "C" Q_DECL_EXPORT
void ritual_ZN18MouseEventResponseD1Ev(MouseEventResponse *self) {
  delete self;
}
