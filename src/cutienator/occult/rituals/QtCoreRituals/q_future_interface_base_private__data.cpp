//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qfutureinterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(future)
#if QT_CONFIG(future)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qfutureinterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

#if !defined(QT_NO_EXCEPTIONS)
//  void QFutureInterfaceBasePrivate::Data::setException(const
//      std::exception_ptr &e)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QFutureInterfaceBasePrivate4Data12setExceptionERKNSt15__exception_ptr13exception_ptrE(
    QFutureInterfaceBasePrivate::Data *self,
    const std::exception_ptr *e) {
  self->setException(*e);
}
#endif  // !defined(QT_NO_EXCEPTIONS)

//  QFutureInterfaceBasePrivate::Data::~Data()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QFutureInterfaceBasePrivate4DataD1Ev(
    QFutureInterfaceBasePrivate::Data *self) {
  delete self;
}

#endif  // QT_CONFIG(future)
#endif  // QT_CONFIG(future)
