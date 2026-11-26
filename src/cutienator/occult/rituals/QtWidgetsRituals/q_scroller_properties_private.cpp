//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qscrollerproperties_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(scroller)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qscrollerproperties_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QPointer>
#include <QtCore/QObject>
#include <QtCore/qmath.h>
#include <QtWidgets/qscrollerproperties.h>
#include <QtWidgets/private/qscrollerproperties_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/util/qscrollerproperties.cpp, line 118, as _ZNK26QScrollerPropertiesPrivateeqERKS_
inline bool QScrollerPropertiesPrivate::operator==(const QScrollerPropertiesPrivate &p) const
{
    bool same = true;
    same &= (mousePressEventDelay == p.mousePressEventDelay);
    same &= (dragStartDistance == p.dragStartDistance);
    same &= (dragVelocitySmoothingFactor == p.dragVelocitySmoothingFactor);
    same &= (axisLockThreshold == p.axisLockThreshold);
    same &= (scrollingCurve == p.scrollingCurve);
    same &= (decelerationFactor == p.decelerationFactor);
    same &= (minimumVelocity == p.minimumVelocity);
    same &= (maximumVelocity == p.maximumVelocity);
    same &= (maximumClickThroughVelocity == p.maximumClickThroughVelocity);
    same &= (acceleratingFlickMaximumTime == p.acceleratingFlickMaximumTime);
    same &= (acceleratingFlickSpeedupFactor == p.acceleratingFlickSpeedupFactor);
    same &= (snapPositionRatio == p.snapPositionRatio);
    same &= (snapTime == p.snapTime);
    same &= (overshootDragResistanceFactor == p.overshootDragResistanceFactor);
    same &= (overshootDragDistanceFactor == p.overshootDragDistanceFactor);
    same &= (overshootScrollDistanceFactor == p.overshootScrollDistanceFactor);
    same &= (overshootScrollTime == p.overshootScrollTime);
    same &= (hOvershootPolicy == p.hOvershootPolicy);
    same &= (vOvershootPolicy == p.vOvershootPolicy);
    same &= (frameRate == p.frameRate);
    return same;
}
//  -----------------------------------------------------------------------

//  bool QScrollerPropertiesPrivate::operator==(const
//      QScrollerPropertiesPrivate &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QScrollerPropertiesPrivateeqERKS_(
    const QScrollerPropertiesPrivate *self,
    const QScrollerPropertiesPrivate *a0) {
  return self->operator==(*a0);
}

//  QScrollerPropertiesPrivate::~QScrollerPropertiesPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QScrollerPropertiesPrivateD1Ev(
    QScrollerPropertiesPrivate *self) {
  delete self;
}

#endif  // QT_CONFIG(scroller)
