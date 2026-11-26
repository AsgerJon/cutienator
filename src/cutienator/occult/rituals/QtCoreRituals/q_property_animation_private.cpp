//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qpropertyanimation_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(animation)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qpropertyanimation.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qpropertyanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qvariantanimation.h"
#include "qvariantanimation_p.h"
#include <QtCore/qrect.h>
#include <QtCore/qline.h>
#include <QtCore/qmutex.h>
#include <QtCore/private/qlocking_p.h>
#include <algorithm>
#include "qpropertyanimation.h"
#include "qanimationgroup.h"
#include "qpropertyanimation_p.h"
#include <QtCore/QMutex>
#include <QtCore/QHash>
#include <QtCore/private/qlocking_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/animation/qvariantanimation.cpp, line 159, as _ZN24QVariantAnimationPrivate13convertValuesEi
inline void QVariantAnimationPrivate::convertValues(int t)
{
    auto type = QMetaType(t);
    //this ensures that all the keyValues are of type t
    for (int i = 0; i < keyValues.size(); ++i) {
        QVariantAnimation::KeyValue &pair = keyValues[i];
        pair.second.convert(type);
    }
    //we also need update to the current interval if needed
    currentInterval.start.second.convert(type);
    currentInterval.end.second.convert(type);

    //... and the interpolator
    updateInterpolator();
}

//  from src/corelib/animation/qpropertyanimation.cpp, line 100, as _ZN25QPropertyAnimationPrivate14updatePropertyERK8QVariant
inline void QPropertyAnimationPrivate::updateProperty(const QVariant &newValue)
{
    if (state == QAbstractAnimation::Stopped)
        return;

    if (!targetObject)
        return;

    if (newValue.userType() == propertyType) {
        //no conversion is needed, we directly call the QMetaObject::metacall
        //check QMetaProperty::write for an explanation of these
        int status = -1;
        int flags = 0;
        void *argv[] = { const_cast<void *>(newValue.constData()), const_cast<QVariant *>(&newValue), &status, &flags };
        QMetaObject::metacall(targetObject, QMetaObject::WriteProperty, propertyIndex, argv);
    } else {
        targetObject->setProperty(propertyName.value().constData(), newValue);
    }
}
//  -----------------------------------------------------------------------

//  QPropertyAnimation *QPropertyAnimationPrivate::q_func()
extern "C" Q_DECL_EXPORT
QPropertyAnimation *ritual_ZN25QPropertyAnimationPrivate6q_funcEv(
    QPropertyAnimationPrivate *self) {
  return self->q_func();
}

//  const QPropertyAnimation *QPropertyAnimationPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QPropertyAnimation *ritual_ZNK25QPropertyAnimationPrivate6q_funcEv(
    const QPropertyAnimationPrivate *self) {
  return self->q_func();
}

//  void QPropertyAnimationPrivate::setTargetObjectForwarder(QObject *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPropertyAnimationPrivate24setTargetObjectForwarderEP7QObject(
    QPropertyAnimationPrivate *self,
    QObject *target) {
  self->setTargetObjectForwarder(target);
}

//  void QPropertyAnimationPrivate::targetObjectDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPropertyAnimationPrivate21targetObjectDestroyedEv(
    QPropertyAnimationPrivate *self) {
  self->targetObjectDestroyed();
}

//  void QPropertyAnimationPrivate::setPropertyName(const QByteArray
//      &propertyName)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPropertyAnimationPrivate15setPropertyNameERK10QByteArray(
    QPropertyAnimationPrivate *self,
    const QByteArray *propertyName) {
  self->setPropertyName(*propertyName);
}

//  void QPropertyAnimationPrivate::updateProperty(const QVariant &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPropertyAnimationPrivate14updatePropertyERK8QVariant(
    QPropertyAnimationPrivate *self,
    const QVariant *a0) {
  self->updateProperty(*a0);
}

#endif  // QT_CONFIG(animation)
