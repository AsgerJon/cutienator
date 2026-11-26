//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickitemanimation_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_path)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemanimation_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdebug.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickitemanimation_p.h>
#include <QtQuick/private/qquickitemanimation_p_p.h>
#include <QtQuick/private/qquickstateoperations_p.h>
#include <QtQml/private/qqmlproperty_p.h>
#if QT_CONFIG(quick_path)
#include <QtQuick/private/qquickpath_p.h>
#endif
#include <QtQml/private/qparallelanimationgroupjob_p.h>
#include <QtQml/private/qsequentialanimationgroupjob_p.h>
#include <QtCore/qmath.h>
#include <QtGui/qtransform.h>
#include <QtQml/qqmlinfo.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquickitemanimation.cpp, line 886, as _ZN26QQuickPathAnimationUpdater8setValueEd
#if QT_CONFIG(quick_path)
inline void QQuickPathAnimationUpdater::setValue(qreal v)
{
    v = qMin(qMax(v, (qreal)0.0), (qreal)1.0);;

    if (interruptStart.isValid()) {
        if (reverse)
            v = 1 - v;
        qreal end = reverse ? 0.0 : 1.0;
        v = interruptStart + v * (end-interruptStart);
    }
    currentV = v;
    bool atStart = ((reverse && v == 1.0) || (!reverse && v == 0.0));
    if (!fromIsSourced && (!fromIsDefined || !toIsDefined)) {
        qreal startX = reverse ? toX + anchorPoint.x() : target->x() + anchorPoint.x();
        qreal startY = reverse ? toY + anchorPoint.y() : target->y() + anchorPoint.y();
        qreal endX = reverse ? target->x() + anchorPoint.x() : toX + anchorPoint.x();
        qreal endY = reverse ? target->y() + anchorPoint.y() : toY + anchorPoint.y();

        prevBez.isValid = false;
        painterPath = path->createPath(QPointF(startX, startY), QPointF(endX, endY), QStringList(), pathLength, attributePoints);
        fromIsSourced = true;
    }

    qreal angle;
    bool fixed = orientation == QQuickPathAnimation::Fixed;
    QPointF currentPos = !painterPath.isEmpty() ? path->sequentialPointAt(painterPath, pathLength, attributePoints, prevBez, v, fixed ? nullptr : &angle) : path->sequentialPointAt(v, fixed ? nullptr : &angle);

    //adjust position according to anchor point
    if (!anchorPoint.isNull()) {
        currentPos -= anchorPoint;
        if (atStart) {
            if (!anchorPoint.isNull() && !fixed)
                target->setTransformOriginPoint(anchorPoint);
        }
    }

    target->setPosition(currentPos);

    //adjust angle according to orientation
    if (!fixed) {
        switch (orientation) {
            case QQuickPathAnimation::RightFirst:
                angle = -angle;
                break;
            case QQuickPathAnimation::TopFirst:
                angle = -angle + 90;
                break;
            case QQuickPathAnimation::LeftFirst:
                angle = -angle + 180;
                break;
            case QQuickPathAnimation::BottomFirst:
                angle = -angle + 270;
                break;
            default:
                angle = 0;
                break;
        }

        if (atStart && !reverse) {
            startRotation = target->rotation();

            //shortest distance to correct orientation
            qreal diff = angle - startRotation;
            while (diff > 180.0) {
                startRotation = startRotation.value() + 360.0;
                diff -= 360.0;
            }
            while (diff < -180.0) {
                startRotation = startRotation.value() - 360.0;
                diff += 360.0;
            }
        }

        //smoothly transition to the desired orientation
        //TODO: shortest distance calculations
        if (startRotation.isValid()) {
            if (reverse && v == 0.0)
                angle = startRotation;
            else if (v < entryInterval)
                angle = angle * v / entryInterval + startRotation * (entryInterval - v) / entryInterval;
        }
        if (endRotation.isValid()) {
            qreal exitStart = 1 - entryInterval;
            if (!reverse && v == 1.0)
                angle = endRotation;
            else if (v > exitStart)
                angle = endRotation * (v - exitStart) / exitInterval + angle * (exitInterval - (v - exitStart)) / exitInterval;
        }
        target->setRotation(angle);
    }

    /*
        NOTE: we don't always reset the transform origin, as it can cause a
        visual jump if ending on an angle. This means that in some cases
        (anchor point and orientation both specified, and ending at an angle)
        the transform origin will always be set after running the path animation.
     */
    if ((reverse && v == 0.0) || (!reverse && v == 1.0)) {
        if (!anchorPoint.isNull() && !fixed && qFuzzyIsNull(angle))
            target->setTransformOriginPoint(QPointF());
    }
}
#endif  // QT_CONFIG(quick_path)
//  -----------------------------------------------------------------------

//  A QQuickPathAnimationUpdater that Python can take functions over in. Every QQuickPathAnimationUpdater
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_path)
typedef void (*CuteQQuickPathAnimationUpdaterCall0)(const void *, qreal, int *);
#endif  // QT_CONFIG(quick_path)
typedef void (*CuteQQuickPathAnimationUpdaterCall1)(const void *, const QDebug *, int, int *);
class CuteQQuickPathAnimationUpdater : public QQuickPathAnimationUpdater {
public:
  using QQuickPathAnimationUpdater::QQuickPathAnimationUpdater;
  CuteQQuickPathAnimationUpdater(const QQuickPathAnimationUpdater & other) : QQuickPathAnimationUpdater(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_path)
    if (!std::strcmp(key, "_ZN22QQuickBulkValueUpdater8setValueEd")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_path)
    if (!std::strcmp(key, "_ZNK22QQuickBulkValueUpdater12debugUpdaterE6QDebugi")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(quick_path)
  //  void QQuickPathAnimationUpdater::setValue(qreal v)
  void setValue(qreal v) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickPathAnimationUpdaterCall0 call = reinterpret_cast<CuteQQuickPathAnimationUpdaterCall0>(taken[0]);
      call(this, v, &handled);
      if (handled) return;
    }
    QQuickPathAnimationUpdater::setValue(v);
  }
#endif  // QT_CONFIG(quick_path)

  //  void QQuickBulkValueUpdater::debugUpdater(QDebug a0, int a1) const
  void debugUpdater(QDebug a0, int a1) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickPathAnimationUpdaterCall1 call = reinterpret_cast<CuteQQuickPathAnimationUpdaterCall1>(taken[1]);
      call(this, &a0, a1, &handled);
      if (handled) return;
    }
    QQuickBulkValueUpdater::debugUpdater(a0, a1);
  }
};

#if QT_CONFIG(quick_path)
//  QQuickPathAnimationUpdater::QQuickPathAnimationUpdater()
extern "C" Q_DECL_EXPORT
QQuickPathAnimationUpdater *ritual_ZN26QQuickPathAnimationUpdaterC1Ev() {
  return new CuteQQuickPathAnimationUpdater();
}
#endif  // QT_CONFIG(quick_path)

//  void QQuickPathAnimationUpdater::setValue(qreal v)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickPathAnimationUpdater8setValueEd(
    QQuickPathAnimationUpdater *self,
    qreal v) {
  self->setValue(v);
}

//  QQuickPathAnimationUpdater::~QQuickPathAnimationUpdater()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickPathAnimationUpdaterD1Ev(
    QQuickPathAnimationUpdater *self) {
  delete self;
}

//  a Python function taken by a CuteQQuickPathAnimationUpdater, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPathAnimationUpdater(
    QQuickPathAnimationUpdater *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPathAnimationUpdater *>(self)->take(key, call);
}

#if QT_CONFIG(quick_path)
//  void QQuickPathAnimationUpdater::setValue(qreal v)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QQuickPathAnimationUpdater8setValueEd(
    QQuickPathAnimationUpdater *self,
    qreal v) {
  self->QQuickPathAnimationUpdater::setValue(v);
}
#endif  // QT_CONFIG(quick_path)

#endif  // QT_CONFIG(quick_path)
