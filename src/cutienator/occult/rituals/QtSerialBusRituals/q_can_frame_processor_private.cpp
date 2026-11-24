//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/6.12.0/QtSerialBus/private/qcanframeprocessor_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSerialBus/QtSerialBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/6.12.0/QtSerialBus/private/qcanframeprocessor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qcanbusframe.h"
#include "qcanframeprocessor.h"
#include "qcanframeprocessor_p.h"
#include "qcanmessagedescription.h"
#include "qcanmessagedescription_p.h"
#include "qcansignaldescription.h"
#include "qcansignaldescription_p.h"
#include <QtCore/QHash>
#include <QtCore/QMap>
#include <QtCore/QVariant>
#include <QtCore/QtEndian>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtserialbus/src/serialbus/qcanframeprocessor.cpp, line 540, as _ZN25QCanFrameProcessorPrivate11resetErrorsEv
inline void QCanFrameProcessorPrivate::resetErrors()
{
    error = QCanFrameProcessor::Error::None;
    errorString.clear();
    warnings.clear();
}

//  from ../qtserialbus/src/serialbus/qcanframeprocessor.cpp, line 547, as _ZN25QCanFrameProcessorPrivate8setErrorEN18QCanFrameProcessor5ErrorERK7QString
inline void QCanFrameProcessorPrivate::setError(QCanFrameProcessor::Error err, const QString &desc)
{
    error = err;
    errorString = desc;
}

//  from ../qtserialbus/src/serialbus/qcanframeprocessor.cpp, line 553, as _ZN25QCanFrameProcessorPrivate10addWarningERK7QString
inline void QCanFrameProcessorPrivate::addWarning(const QString &warning)
{
    warnings.push_back(warning);
}
//  -----------------------------------------------------------------------

//  void QCanFrameProcessorPrivate::resetErrors()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QCanFrameProcessorPrivate11resetErrorsEv(
    QCanFrameProcessorPrivate *self) {
  self->resetErrors();
}

//  void QCanFrameProcessorPrivate::setError(QCanFrameProcessor::Error err,
//      const QString &desc)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QCanFrameProcessorPrivate8setErrorEN18QCanFrameProcessor5ErrorERK7QString(
    QCanFrameProcessorPrivate *self,
    QCanFrameProcessor::Error err,
    const QString *desc) {
  self->setError(err, *desc);
}

//  void QCanFrameProcessorPrivate::addWarning(const QString &warning)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QCanFrameProcessorPrivate10addWarningERK7QString(
    QCanFrameProcessorPrivate *self,
    const QString *warning) {
  self->addWarning(*warning);
}

//  QCanFrameProcessorPrivate::~QCanFrameProcessorPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QCanFrameProcessorPrivateD1Ev(
    QCanFrameProcessorPrivate *self) {
  delete self;
}
