//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qioring_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if (QT_CONFIG(liburing)) || (QT_CONFIG(windows_ioring))
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qioring_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QIORingRequestOffsetFdBase::~QIORingRequestOffsetFdBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QIORingRequestOffsetFdBaseD1Ev(
    QIORingRequestOffsetFdBase *self) {
  delete self;
}

#endif  // (QT_CONFIG(liburing)) || (QT_CONFIG(windows_ioring))
