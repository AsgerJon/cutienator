//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qabstract3daxis_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d)))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qabstract3daxis.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qabstract3daxis_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdebug.h>
#include <QtGraphs/private/qabstract3daxis_p.h>
#include <QtGraphs/private/qgraphs3dlogging_p.h>
#include <QtCore/qloggingcategory.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgraphs/src/graphs3d/axis/qabstract3daxis.cpp, line 687, as _ZN22QAbstract3DAxisPrivate12updateLabelsEv
inline void QAbstract3DAxisPrivate::updateLabels()
{
    // Default implementation does nothing
}

//  from ../qtgraphs/src/graphs3d/axis/qabstract3daxis.cpp, line 800, as _ZN22QAbstract3DAxisPrivate6setMaxEf
inline void QAbstract3DAxisPrivate::setMax(float max)
{
    Q_Q(QAbstract3DAxis);
    if (!allowNegatives()) {
        if (allowZero()) {
            if (max < 0.0f) {
                max = 0.0f;
                qCWarning(lcAProperties3D, "%s tried to set negative maximum for an axis that only"
                         " supports positive values and zero: %f",
                         qUtf8Printable(QLatin1String(__FUNCTION__)),
                         max);
            }
        } else {
            if (max <= 0.0f) {
                max = 1.0f;
                qCWarning(lcAProperties3D, "%s tried to set negative or zero maximum for an "
                         "axis that only"
                         " supports positive values: %f",
                         qUtf8Printable(QLatin1String(__FUNCTION__)),
                         max);
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
                    qCWarning(lcAProperties3D, "%s unable to set maximum value to zero.",
                              qUtf8Printable(QLatin1String(__FUNCTION__)));
                    return;
                }
            }
            qCWarning(lcAProperties3D, "%s tried to set maximum to equal or smaller than minimum "
                     "for value axis. Minimum automatically adjusted to a valid one: %f --> %f",
                     qUtf8Printable(QLatin1String(__FUNCTION__)),
                     oldMin,
                     m_min);
            minChanged = true;
        }
        m_max = max;
        emit q->rangeChanged(m_min, m_max);
        emit q->maxChanged(m_max);
        if (minChanged)
            emit q->minChanged(m_min);
    }
}

//  from ../qtgraphs/src/graphs3d/axis/qabstract3daxis.cpp, line 755, as _ZN22QAbstract3DAxisPrivate6setMinEf
inline void QAbstract3DAxisPrivate::setMin(float min)
{
    Q_Q(QAbstract3DAxis);
    if (!allowNegatives()) {
        if (allowZero()) {
            if (min < 0.0f) {
                min = 0.0f;
                qCWarning(lcAProperties3D, "%s tried to set negative minimum for an axis that only"
                         "supports positive values and zero: %f",
                         qUtf8Printable(QLatin1String(__FUNCTION__)),
                         min);
            }
        } else {
            if (min <= 0.0f) {
                min = 1.0f;
                qCWarning(lcAProperties3D, "%s tried to set negative or zero minimum for an "
                         "axis that only"
                         "supports positive values: %f",
                         qUtf8Printable(QLatin1String(__FUNCTION__)),
                         min);
            }
        }
    }

    if (m_min != min) {
        bool maxChanged = false;
        if (min > m_max || (!allowMinMaxSame() && min == m_max)) {
            float oldMax = m_max;
            m_max = min + 1.0f;
            qCWarning(lcAProperties3D, "%s tried to set minimum to equal or larger than maximum for"
                     " value axis. Maximum automatically adjusted to a valid one: %f --> %f",
                     qUtf8Printable(QLatin1String(__FUNCTION__)),
                     oldMax,
                     m_max);
            maxChanged = true;
        }
        m_min = min;

        emit q->rangeChanged(m_min, m_max);
        emit q->minChanged(m_min);
        if (maxChanged)
            emit q->maxChanged(m_max);
    }
}

//  from ../qtgraphs/src/graphs3d/axis/qabstract3daxis.cpp, line 692, as _ZN22QAbstract3DAxisPrivate8setRangeEffb
inline void QAbstract3DAxisPrivate::setRange(float min, float max, bool suppressWarnings)
{
    Q_Q(QAbstract3DAxis);
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
            qCWarning(lcAProperties3D, "%s tried to set invalid range for axis. Range automatically adjusted "
                     "to a valid one: %f - %f --> %f - %f",
                     qUtf8Printable(QLatin1String(__FUNCTION__)),
                     min,
                     max,
                     m_min,
                     m_max);
        }
        emit q->rangeChanged(m_min, m_max);
    }

    if (minDirty)
        emit q->minChanged(m_min);
    if (maxDirty)
        emit q->maxChanged(m_max);
}

//  from ../qtgraphs/src/graphs3d/axis/qabstract3daxis.cpp, line 674, as _ZN22QAbstract3DAxisPrivateD2Ev
inline QAbstract3DAxisPrivate::~QAbstract3DAxisPrivate() {}

//  from ../qtgraphs/src/graphs3d/utils/qgraphs3dlogging.cpp, line 18, as _Z15lcAProperties3Dv
inline const QLoggingCategory &lcAProperties3D()
{
    static const QLoggingCategory category("qt.graphs3d.axis.properties");
    return category;
}

//  from ../qtgraphs/src/graphs3d/axis/qabstract3daxis.cpp, line 676, as _ZN22QAbstract3DAxisPrivate14setOrientationEN15QAbstract3DAxis15AxisOrientationE
inline void QAbstract3DAxisPrivate::setOrientation(QAbstract3DAxis::AxisOrientation orientation)
{
    Q_Q(QAbstract3DAxis);
    if (m_orientation == QAbstract3DAxis::AxisOrientation::None) {
        m_orientation = orientation;
        emit q->orientationChanged(orientation);
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
class CuteQAbstract3DAxisPrivate : public QAbstract3DAxisPrivate {
public:
  using QAbstract3DAxisPrivate::QAbstract3DAxisPrivate;
  void *taken[7] = {};

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
};

//  QAbstract3DAxis *QAbstract3DAxisPrivate::q_func()
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_ZN22QAbstract3DAxisPrivate6q_funcEv(
    QAbstract3DAxisPrivate *self) {
  return self->q_func();
}

//  const QAbstract3DAxis *QAbstract3DAxisPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAbstract3DAxis *ritual_ZNK22QAbstract3DAxisPrivate6q_funcEv(
    const QAbstract3DAxisPrivate *self) {
  return self->q_func();
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

#endif  // (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d)))
