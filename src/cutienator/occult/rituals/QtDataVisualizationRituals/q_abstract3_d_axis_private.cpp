//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/qabstract3daxis_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/qabstract3daxis_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/qabstract3daxis_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/axis/qabstract3daxis.cpp, line 408, as _ZN22QAbstract3DAxisPrivate8setRangeEffb
inline void QAbstract3DAxisPrivate::setRange(float min, float max, bool suppressWarnings)
{
    bool adjusted = false;
    if (!allowNegatives()) {
        if (allowZero()) {
            if (min < 0.0f) {
                min = 0.0f;
                adjusted = true;
            }
            if (max < 0.0f) {
                max = 0.0f;
                adjusted = true;
            }
        } else {
            if (min <= 0.0f) {
                min = 1.0f;
                adjusted = true;
            }
            if (max <= 0.0f) {
                max = 1.0f;
                adjusted = true;
            }
        }
    }
    // If min >= max, we adjust ranges so that
    // m_max becomes (min + 1.0f)
    // as axes need some kind of valid range.
    bool minDirty = false;
    bool maxDirty = false;
    if (m_min != min) {
        m_min = min;
        minDirty = true;
    }
    if (m_max != max || min > max || (!allowMinMaxSame() && min == max)) {
        if (min > max || (!allowMinMaxSame() && min == max)) {
            m_max = min + 1.0f;
            adjusted = true;
        } else {
            m_max = max;
        }
        maxDirty = true;
    }

    if (minDirty || maxDirty) {
        if (adjusted && !suppressWarnings) {
            qWarning() << "Warning: Tried to set invalid range for axis."
                          " Range automatically adjusted to a valid one:"
                       << min << "-" << max << "-->" << m_min << "-" << m_max;
        }
        emit q_ptr->rangeChanged(m_min, m_max);
    }

    if (minDirty)
        emit q_ptr->minChanged(m_min);
    if (maxDirty)
        emit q_ptr->maxChanged(m_max);
}

//  from ../qtdatavis3d/src/datavisualization/axis/qabstract3daxis.cpp, line 466, as _ZN22QAbstract3DAxisPrivate6setMinEf
inline void QAbstract3DAxisPrivate::setMin(float min)
{
    if (!allowNegatives()) {
        if (allowZero()) {
            if (min < 0.0f) {
                min = 0.0f;
                qWarning() << "Warning: Tried to set negative minimum for an axis that only"
                              "supports positive values and zero:" << min;
            }
        } else {
            if (min <= 0.0f) {
                min = 1.0f;
                qWarning() << "Warning: Tried to set negative or zero minimum for an axis that only"
                              "supports positive values:" << min;
            }
        }
    }

    if (m_min != min) {
        bool maxChanged = false;
        if (min > m_max || (!allowMinMaxSame() && min == m_max)) {
            float oldMax = m_max;
            m_max = min + 1.0f;
            qWarning() << "Warning: Tried to set minimum to equal or larger than maximum for"
                          " value axis. Maximum automatically adjusted to a valid one:"
                       << oldMax <<  "-->" << m_max;
            maxChanged = true;
        }
        m_min = min;

        emit q_ptr->rangeChanged(m_min, m_max);
        emit q_ptr->minChanged(m_min);
        if (maxChanged)
            emit q_ptr->maxChanged(m_max);
    }
}

//  from ../qtdatavis3d/src/datavisualization/axis/qabstract3daxis.cpp, line 503, as _ZN22QAbstract3DAxisPrivate6setMaxEf
inline void QAbstract3DAxisPrivate::setMax(float max)
{
    if (!allowNegatives()) {
        if (allowZero()) {
            if (max < 0.0f) {
                max = 0.0f;
                qWarning() << "Warning: Tried to set negative maximum for an axis that only"
                              "supports positive values and zero:" << max;
            }
        } else {
            if (max <= 0.0f) {
                max = 1.0f;
                qWarning() << "Warning: Tried to set negative or zero maximum for an axis that only"
                              "supports positive values:" << max;
            }
        }
    }

    if (m_max != max) {
        bool minChanged = false;
        if (m_min > max || (!allowMinMaxSame() && m_min == max)) {
            float oldMin = m_min;
            m_min = max - 1.0f;
            if (!allowNegatives() && m_min < 0.0f) {
                if (allowZero())
                    m_min = 0.0f;
                else
                    m_min = max / 2.0f; // Need some positive value smaller than max

                if (!allowMinMaxSame() && max == 0.0f) {
                    m_min = oldMin;
                    qWarning() << "Unable to set maximum value to zero.";
                    return;
                }
            }
            qWarning() << "Warning: Tried to set maximum to equal or smaller than minimum for"
                          " value axis. Minimum automatically adjusted to a valid one:"
                       << oldMin <<  "-->" << m_min;
            minChanged = true;
        }
        m_max = max;
        emit q_ptr->rangeChanged(m_min, m_max);
        emit q_ptr->maxChanged(m_max);
        if (minChanged)
            emit q_ptr->minChanged(m_min);
    }
}

//  from ../qtdatavis3d/src/datavisualization/axis/qabstract3daxis.cpp, line 403, as _ZN22QAbstract3DAxisPrivate12updateLabelsEv
inline void QAbstract3DAxisPrivate::updateLabels()
{
    // Default implementation does nothing
}

//  from ../qtdatavis3d/src/datavisualization/axis/qabstract3daxis.cpp, line 393, as _ZN22QAbstract3DAxisPrivate14setOrientationEN15QAbstract3DAxis15AxisOrientationE
inline void QAbstract3DAxisPrivate::setOrientation(QAbstract3DAxis::AxisOrientation orientation)
{
    if (m_orientation == QAbstract3DAxis::AxisOrientationNone) {
        m_orientation = orientation;
        emit q_ptr->orientationChanged(orientation);
    } else {
        Q_ASSERT("Attempted to reset axis orientation.");
    }
}
//  -----------------------------------------------------------------------

//  Only a class built on QAbstract3DAxisPrivate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQAbstract3DAxisPrivate : QAbstract3DAxisPrivate {
  using QAbstract3DAxisPrivate::updateLabels;
};

//  A QAbstract3DAxisPrivate that Python can take functions over in. Every QAbstract3DAxisPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAbstract3DAxisPrivateCall0)(const void *, float, float, bool, int *);
typedef void (*CuteQAbstract3DAxisPrivateCall1)(const void *, float, int *);
typedef void (*CuteQAbstract3DAxisPrivateCall2)(const void *, float, int *);
typedef void (*CuteQAbstract3DAxisPrivateCall3)(const void *, int *);
typedef bool (*CuteQAbstract3DAxisPrivateCall4)(const void *, int *);
typedef bool (*CuteQAbstract3DAxisPrivateCall5)(const void *, int *);
typedef bool (*CuteQAbstract3DAxisPrivateCall6)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstract3DAxisPrivateCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstract3DAxisPrivateCall8)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DAxisPrivateCall9)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DAxisPrivateCall10)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DAxisPrivateCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DAxisPrivateCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DAxisPrivateCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstract3DAxisPrivate : public QAbstract3DAxisPrivate {
public:
  using QAbstract3DAxisPrivate::QAbstract3DAxisPrivate;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN22QAbstract3DAxisPrivate8setRangeEffb")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstract3DAxisPrivate6setMinEf")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstract3DAxisPrivate6setMaxEf")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstract3DAxisPrivate12updateLabelsEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstract3DAxisPrivate9allowZeroEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstract3DAxisPrivate14allowNegativesEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstract3DAxisPrivate15allowMinMaxSameEv")) {
      taken[6] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QAbstract3DAxisPrivate::setRange(float min, float max, bool
  //      suppressWarnings)
  void setRange(float min, float max, bool suppressWarnings) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstract3DAxisPrivateCall0 call = reinterpret_cast<CuteQAbstract3DAxisPrivateCall0>(taken[0]);
      call(this, min, max, suppressWarnings, &handled);
      if (handled) return;
    }
    QAbstract3DAxisPrivate::setRange(min, max, suppressWarnings);
  }

  //  void QAbstract3DAxisPrivate::setMin(float min)
  void setMin(float min) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstract3DAxisPrivateCall1 call = reinterpret_cast<CuteQAbstract3DAxisPrivateCall1>(taken[1]);
      call(this, min, &handled);
      if (handled) return;
    }
    QAbstract3DAxisPrivate::setMin(min);
  }

  //  void QAbstract3DAxisPrivate::setMax(float max)
  void setMax(float max) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstract3DAxisPrivateCall2 call = reinterpret_cast<CuteQAbstract3DAxisPrivateCall2>(taken[2]);
      call(this, max, &handled);
      if (handled) return;
    }
    QAbstract3DAxisPrivate::setMax(max);
  }

  //  void QAbstract3DAxisPrivate::updateLabels()
  void updateLabels() override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstract3DAxisPrivateCall3 call = reinterpret_cast<CuteQAbstract3DAxisPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstract3DAxisPrivate::updateLabels();
  }

  //  bool QAbstract3DAxisPrivate::allowZero()
  bool allowZero() override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstract3DAxisPrivateCall4 call = reinterpret_cast<CuteQAbstract3DAxisPrivateCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QAbstract3DAxisPrivate::allowNegatives()
  bool allowNegatives() override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstract3DAxisPrivateCall5 call = reinterpret_cast<CuteQAbstract3DAxisPrivateCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QAbstract3DAxisPrivate::allowMinMaxSame()
  bool allowMinMaxSame() override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstract3DAxisPrivateCall6 call = reinterpret_cast<CuteQAbstract3DAxisPrivateCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstract3DAxisPrivateCall7 call = reinterpret_cast<CuteQAbstract3DAxisPrivateCall7>(taken[7]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQAbstract3DAxisPrivateCall8 call = reinterpret_cast<CuteQAbstract3DAxisPrivateCall8>(taken[8]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAbstract3DAxisPrivateCall9 call = reinterpret_cast<CuteQAbstract3DAxisPrivateCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQAbstract3DAxisPrivateCall10 call = reinterpret_cast<CuteQAbstract3DAxisPrivateCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQAbstract3DAxisPrivateCall11 call = reinterpret_cast<CuteQAbstract3DAxisPrivateCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQAbstract3DAxisPrivateCall12 call = reinterpret_cast<CuteQAbstract3DAxisPrivateCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[13]) {
      int handled = 0;
      CuteQAbstract3DAxisPrivateCall13 call = reinterpret_cast<CuteQAbstract3DAxisPrivateCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstract3DAxisPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QAbstract3DAxisPrivate10metaObjectEv(
    const QAbstract3DAxisPrivate *self) {
  return self->metaObject();
}

//  void *QAbstract3DAxisPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QAbstract3DAxisPrivate11qt_metacastEPKc(
    QAbstract3DAxisPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAbstract3DAxisPrivate::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QAbstract3DAxisPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QAbstract3DAxisPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QAbstract3DAxisPrivate::~QAbstract3DAxisPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstract3DAxisPrivateD1Ev(QAbstract3DAxisPrivate *self) {
  delete self;
}

//  void
//      QAbstract3DAxisPrivate::setOrientation(QAbstract3DAxis::AxisOrientati
//      on orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstract3DAxisPrivate14setOrientationEN15QAbstract3DAxis15AxisOrientationE(
    QAbstract3DAxisPrivate *self,
    QAbstract3DAxis::AxisOrientation orientation) {
  self->setOrientation(orientation);
}

//  bool QAbstract3DAxisPrivate::isDefaultAxis()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QAbstract3DAxisPrivate13isDefaultAxisEv(
    QAbstract3DAxisPrivate *self) {
  return self->isDefaultAxis();
}

//  void QAbstract3DAxisPrivate::setDefaultAxis(bool isDefault)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstract3DAxisPrivate14setDefaultAxisEb(
    QAbstract3DAxisPrivate *self,
    bool isDefault) {
  self->setDefaultAxis(isDefault);
}

//  void QAbstract3DAxisPrivate::setRange(float min, float max, bool
//      suppressWarnings)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstract3DAxisPrivate8setRangeEffb(
    QAbstract3DAxisPrivate *self,
    float min,
    float max,
    bool suppressWarnings) {
  self->setRange(min, max, suppressWarnings);
}

//  void QAbstract3DAxisPrivate::setMin(float min)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstract3DAxisPrivate6setMinEf(
    QAbstract3DAxisPrivate *self,
    float min) {
  self->setMin(min);
}

//  void QAbstract3DAxisPrivate::setMax(float max)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstract3DAxisPrivate6setMaxEf(
    QAbstract3DAxisPrivate *self,
    float max) {
  self->setMax(max);
}

//  void QAbstract3DAxisPrivate::updateLabels()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstract3DAxisPrivate12updateLabelsEv(
    QAbstract3DAxisPrivate *self) {
  self->updateLabels();
}

//  bool QAbstract3DAxisPrivate::allowZero()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QAbstract3DAxisPrivate9allowZeroEv(
    QAbstract3DAxisPrivate *self) {
  return self->allowZero();
}

//  bool QAbstract3DAxisPrivate::allowNegatives()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QAbstract3DAxisPrivate14allowNegativesEv(
    QAbstract3DAxisPrivate *self) {
  return self->allowNegatives();
}

//  bool QAbstract3DAxisPrivate::allowMinMaxSame()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QAbstract3DAxisPrivate15allowMinMaxSameEv(
    QAbstract3DAxisPrivate *self) {
  return self->allowMinMaxSame();
}

//  a Python function taken by a CuteQAbstract3DAxisPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstract3DAxisPrivate(
    QAbstract3DAxisPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstract3DAxisPrivate *>(self)->take(key, call);
}

//  void QAbstract3DAxisPrivate::setRange(float min, float max, bool
//      suppressWarnings)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QAbstract3DAxisPrivate8setRangeEffb(
    QAbstract3DAxisPrivate *self,
    float min,
    float max,
    bool suppressWarnings) {
  self->QAbstract3DAxisPrivate::setRange(min, max, suppressWarnings);
}

//  void QAbstract3DAxisPrivate::setMin(float min)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QAbstract3DAxisPrivate6setMinEf(
    QAbstract3DAxisPrivate *self,
    float min) {
  self->QAbstract3DAxisPrivate::setMin(min);
}

//  void QAbstract3DAxisPrivate::setMax(float max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QAbstract3DAxisPrivate6setMaxEf(
    QAbstract3DAxisPrivate *self,
    float max) {
  self->QAbstract3DAxisPrivate::setMax(max);
}

//  void QAbstract3DAxisPrivate::updateLabels()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QAbstract3DAxisPrivate12updateLabelsEv(
    QAbstract3DAxisPrivate *self) {
  static_cast<OwnQAbstract3DAxisPrivate *>(self)->OwnQAbstract3DAxisPrivate::updateLabels();
}
