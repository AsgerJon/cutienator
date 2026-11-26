//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickflickable_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickflickable_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquicktimeline_p_p.h>
#include <QtCore/QDebug>
#include <QtCore/QMutex>
#include <QtCore/QThread>
#include <QtCore/QWaitCondition>
#include <QtCore/QEvent>
#include <QtCore/QCoreApplication>
#include <QtCore/QEasingCurve>
#include <QtCore/QTime>
#include <QtCore/private/qnumeric_p.h>
#include <QtCore/QHash>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/util/qquicktimeline.cpp, line 889, as _ZN20QQuickTimeLineObjectC2Ev
inline QQuickTimeLineObject::QQuickTimeLineObject()
: _t(nullptr)
{
}

//  from ../qtdeclarative/src/quick/util/qquicktimeline.cpp, line 894, as _ZN20QQuickTimeLineObjectD2Ev
inline QQuickTimeLineObject::~QQuickTimeLineObject()
{
    if (_t) {
        _t->remove(this);
        _t = nullptr;
    }
}
//  -----------------------------------------------------------------------

//  A QQuickFlickablePrivate::Velocity that Python can take functions over in. Every QQuickFlickablePrivate::Velocity
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickFlickablePrivate_VelocityCall0)(const void *, qreal, int *);
typedef qreal (*CuteQQuickFlickablePrivate_VelocityCall1)(const void *, int *);
class CuteQQuickFlickablePrivate_Velocity : public QQuickFlickablePrivate::Velocity {
public:
  using QQuickFlickablePrivate::Velocity::Velocity;
  CuteQQuickFlickablePrivate_Velocity(const QQuickFlickablePrivate::Velocity & other) : QQuickFlickablePrivate::Velocity(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QQuickTimeLineValue8setValueEd")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QQuickTimeLineValue5valueEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void QQuickFlickablePrivate::Velocity::setValue(qreal v)
  void setValue(qreal v) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickFlickablePrivate_VelocityCall0 call = reinterpret_cast<CuteQQuickFlickablePrivate_VelocityCall0>(taken[0]);
      call(this, v, &handled);
      if (handled) return;
    }
    QQuickFlickablePrivate::Velocity::setValue(v);
  }

  //  qreal QQuickTimeLineValue::value() const
  qreal value() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickFlickablePrivate_VelocityCall1 call = reinterpret_cast<CuteQQuickFlickablePrivate_VelocityCall1>(taken[1]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickTimeLineValue::value();
  }
};

//  QQuickFlickablePrivate::Velocity::Velocity(QQuickFlickablePrivate *p)
extern "C" Q_DECL_EXPORT
QQuickFlickablePrivate::Velocity *ritual_ZN22QQuickFlickablePrivate8VelocityC1EPS_(
    QQuickFlickablePrivate *p) {
  return new CuteQQuickFlickablePrivate_Velocity(p);
}

//  void QQuickFlickablePrivate::Velocity::setValue(qreal v)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate8Velocity8setValueEd(
    QQuickFlickablePrivate::Velocity *self,
    qreal v) {
  self->setValue(v);
}

//  QQuickFlickablePrivate::Velocity::~Velocity()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate8VelocityD1Ev(
    QQuickFlickablePrivate::Velocity *self) {
  delete self;
}

//  a Python function taken by a CuteQQuickFlickablePrivate_Velocity, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickFlickablePrivate_Velocity(
    QQuickFlickablePrivate::Velocity *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickFlickablePrivate_Velocity *>(self)->take(key, call);
}

//  void QQuickFlickablePrivate::Velocity::setValue(qreal v)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickFlickablePrivate8Velocity8setValueEd(
    QQuickFlickablePrivate::Velocity *self,
    qreal v) {
  self->QQuickFlickablePrivate::Velocity::setValue(v);
}
