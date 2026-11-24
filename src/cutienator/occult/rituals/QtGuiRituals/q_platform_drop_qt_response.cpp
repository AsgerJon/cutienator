//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformdrag.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformdrag.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QPlatformDropQtResponse::QPlatformDropQtResponse(bool accepted,
//      Qt::DropAction acceptedAction)
extern "C" Q_DECL_EXPORT
QPlatformDropQtResponse *ritual_ZN23QPlatformDropQtResponseC1EbN2Qt10DropActionE(
    bool accepted,
    Qt::DropAction acceptedAction) {
  return new QPlatformDropQtResponse(accepted, acceptedAction);
}

//  bool QPlatformDropQtResponse::isAccepted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QPlatformDropQtResponse10isAcceptedEv(
    const QPlatformDropQtResponse *self) {
  return self->isAccepted();
}

//  Qt::DropAction QPlatformDropQtResponse::acceptedAction() const
extern "C" Q_DECL_EXPORT
Qt::DropAction ritual_ZNK23QPlatformDropQtResponse14acceptedActionEv(
    const QPlatformDropQtResponse *self) {
  return self->acceptedAction();
}

//  QPlatformDropQtResponse::~QPlatformDropQtResponse()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformDropQtResponseD1Ev(QPlatformDropQtResponse *self) {
  delete self;
}

#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(draganddrop)
