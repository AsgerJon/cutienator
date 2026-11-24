//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformdrag.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(draganddrop)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformdrag.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>

//  QPlatformDragQtResponse::QPlatformDragQtResponse(bool accepted,
//      Qt::DropAction acceptedAction, QRect answerRect)
extern "C" Q_DECL_EXPORT
QPlatformDragQtResponse *ritual_ZN23QPlatformDragQtResponseC1EbN2Qt10DropActionE5QRect(
    bool accepted,
    Qt::DropAction acceptedAction,
    const QRect *answerRect) {
  return new QPlatformDragQtResponse(accepted, acceptedAction, *answerRect);
}

//  QRect QPlatformDragQtResponse::answerRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK23QPlatformDragQtResponse10answerRectEv(
    const QPlatformDragQtResponse *self) {
  return new QRect(self->answerRect());
}

//  QPlatformDragQtResponse::~QPlatformDragQtResponse()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformDragQtResponseD1Ev(QPlatformDragQtResponse *self) {
  delete self;
}

#endif  // QT_CONFIG(draganddrop)
