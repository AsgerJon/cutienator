//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickitemanimation_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemanimation_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickitemanimation_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickanimation_p.h>
#include <QtQuick/private/qquickanimation_p_p.h>
#include <QtQuick/private/qquickanimatorjob_p.h>
#include <QtQuick/private/qquickstatechangescript_p.h>
#include <QtQml/private/qqmlcontext_p.h>
#include <QtQml/qqmlpropertyvaluesource.h>
#include <QtQml/qqml.h>
#include <QtQml/qqmlinfo.h>
#include <QtQml/qqmlexpression.h>
#include <QtQml/private/qqmlstringconverters_p.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQml/private/qqmlmetatype_p.h>
#include <QtQml/private/qqmlvaluetype_p.h>
#include <QtQml/private/qqmlproperty_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtCore/qvariant.h>
#include <QtGui/qcolor.h>
#include <QtCore/qfile.h>
#include <QtQml/private/qparallelanimationgroupjob_p.h>
#include <QtQml/private/qsequentialanimationgroupjob_p.h>
#include <QtCore/qset.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qmath.h>
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

//  from ../qtdeclarative/src/quick/util/qquickanimation.cpp, line 1784, as _ZN27QQuickAnimationGroupPrivate27animationCurrentLoopChangedEP21QAbstractAnimationJob
inline void QQuickAnimationGroupPrivate::animationCurrentLoopChanged(QAbstractAnimationJob *)
{
    if (!animationDirty)
        return;
    restartFromCurrentLoop();
}

//  from ../qtdeclarative/src/quick/items/qquickitemanimation.cpp, line 141, as _ZNK28QQuickParentAnimationPrivate22computeTransformOriginEN10QQuickItem15TransformOriginEdd
inline QPointF QQuickParentAnimationPrivate::computeTransformOrigin(QQuickItem::TransformOrigin origin, qreal width, qreal height) const
{
    switch (origin) {
    default:
    case QQuickItem::TopLeft:
        return QPointF(0, 0);
    case QQuickItem::Top:
        return QPointF(width / 2., 0);
    case QQuickItem::TopRight:
        return QPointF(width, 0);
    case QQuickItem::Left:
        return QPointF(0, height / 2.);
    case QQuickItem::Center:
        return QPointF(width / 2., height / 2.);
    case QQuickItem::Right:
        return QPointF(width, height / 2.);
    case QQuickItem::BottomLeft:
        return QPointF(0, height);
    case QQuickItem::Bottom:
        return QPointF(width / 2., height);
    case QQuickItem::BottomRight:
        return QPointF(width, height);
    }
}
//  -----------------------------------------------------------------------

//  A QQuickParentAnimationPrivate that Python can take functions over in. Every QQuickParentAnimationPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickParentAnimationPrivateCall0)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickParentAnimationPrivateCall1)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickParentAnimationPrivateCall2)(const void *, QAbstractAnimationJob *, int, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickParentAnimationPrivateCall3)(const void *, QAbstractAnimationJob *, int, int *);
#endif  // QT_CONFIG(qml_animation)
class CuteQQuickParentAnimationPrivate : public QQuickParentAnimationPrivate {
public:
  using QQuickParentAnimationPrivate::QQuickParentAnimationPrivate;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN27QAnimationJobChangeListener27animationCurrentLoopChangedEP21QAbstractAnimationJob")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN27QAnimationJobChangeListener17animationFinishedEP21QAbstractAnimationJob")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN27QAnimationJobChangeListener21animationStateChangedEP21QAbstractAnimationJobNS0_5StateES2_")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN27QAnimationJobChangeListener27animationCurrentTimeChangedEP21QAbstractAnimationJobi")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
    return false;
  }

#if QT_CONFIG(qml_animation)
  //  void QQuickAnimationGroupPrivate::animationCurrentLoopChanged(QAbstra
  //      ctAnimationJob *job)
  void animationCurrentLoopChanged(QAbstractAnimationJob *job) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickParentAnimationPrivateCall0 call = reinterpret_cast<CuteQQuickParentAnimationPrivateCall0>(taken[0]);
      call(this, job, &handled);
      if (handled) return;
    }
    QQuickAnimationGroupPrivate::animationCurrentLoopChanged(job);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QQuickAbstractAnimationPrivate::animationFinished(QAbstractAnima
  //      tionJob *a0)
  void animationFinished(QAbstractAnimationJob *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickParentAnimationPrivateCall1 call = reinterpret_cast<CuteQQuickParentAnimationPrivateCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimationPrivate::animationFinished(a0);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAnimationJobChangeListener::animationStateChanged(QAbstractAnim
  //      ationJob *a0, QAbstractAnimationJob::State a1,
  //      QAbstractAnimationJob::State a2)
  void animationStateChanged(
      QAbstractAnimationJob *a0,
      QAbstractAnimationJob::State a1,
      QAbstractAnimationJob::State a2) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickParentAnimationPrivateCall2 call = reinterpret_cast<CuteQQuickParentAnimationPrivateCall2>(taken[2]);
      call(this, a0, static_cast<int>(a1), static_cast<int>(a2), &handled);
      if (handled) return;
    }
    QAnimationJobChangeListener::animationStateChanged(a0, a1, a2);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAnimationJobChangeListener::animationCurrentTimeChanged(QAbstra
  //      ctAnimationJob *a0, int a1)
  void animationCurrentTimeChanged(
      QAbstractAnimationJob *a0,
      int a1) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickParentAnimationPrivateCall3 call = reinterpret_cast<CuteQQuickParentAnimationPrivateCall3>(taken[3]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QAnimationJobChangeListener::animationCurrentTimeChanged(a0, a1);
  }
#endif  // QT_CONFIG(qml_animation)
};

//  QQuickParentAnimation *QQuickParentAnimationPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickParentAnimation *ritual_ZN28QQuickParentAnimationPrivate6q_funcEv(
    QQuickParentAnimationPrivate *self) {
  return self->q_func();
}

//  const QQuickParentAnimation *QQuickParentAnimationPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickParentAnimation *ritual_ZNK28QQuickParentAnimationPrivate6q_funcEv(
    const QQuickParentAnimationPrivate *self) {
  return self->q_func();
}

//  QPointF QQuickParentAnimationPrivate::computeTransformOrigin(QQuickItem::
//      TransformOrigin origin, qreal width, qreal height) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK28QQuickParentAnimationPrivate22computeTransformOriginEN10QQuickItem15TransformOriginEdd(
    const QQuickParentAnimationPrivate *self,
    QQuickItem::TransformOrigin origin,
    qreal width,
    qreal height) {
  return new QPointF(self->computeTransformOrigin(origin, width, height));
}

//  a Python function taken by a CuteQQuickParentAnimationPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickParentAnimationPrivate(
    QQuickParentAnimationPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickParentAnimationPrivate *>(self)->take(key, call);
}
