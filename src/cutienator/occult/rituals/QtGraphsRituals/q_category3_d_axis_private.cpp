//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qcategory3daxis_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d)))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qcategory3daxis.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qcategory3daxis_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdebug.h>
#include <QtGraphs/private/qabstract3daxis_p.h>
#include <QtGraphs/private/qgraphs3dlogging_p.h>
#include <QtGraphs/private/qcategory3daxis_p.h>
#include <QtGraphs/private/qquickgraphsitem_p.h>
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

//  from ../qtgraphs/src/graphs3d/axis/qabstract3daxis.cpp, line 657, as _ZN22QAbstract3DAxisPrivateC2EN15QAbstract3DAxis8AxisTypeE
inline QAbstract3DAxisPrivate::QAbstract3DAxisPrivate(QAbstract3DAxis::AxisType type)
    : m_orientation(QAbstract3DAxis::AxisOrientation::None)
    , m_type(type)
    , m_isDefaultAxis(false)
    , m_min(0.0f)
    , m_max(10.0f)
    , m_autoAdjust(true)
    , m_scaleLabelsByCount(false)
    , m_labelSize(1.0)
    , m_labelAutoAngle(0.0f)
    , m_titleOffset(0.0f)
    , m_titleVisible(false)
    , m_labelsVisible(true)
    , m_titleFixed(true)

{}

//  from ../qtgraphs/src/graphs3d/axis/qcategory3daxis.cpp, line 149, as _ZN22QCategory3DAxisPrivate14allowNegativesEv
inline bool QCategory3DAxisPrivate::allowNegatives()
{
    return false;
}

//  from ../qtgraphs/src/graphs3d/axis/qcategory3daxis.cpp, line 154, as _ZN22QCategory3DAxisPrivate15allowMinMaxSameEv
inline bool QCategory3DAxisPrivate::allowMinMaxSame()
{
    return true;
}

//  from ../qtgraphs/src/graphs3d/axis/qcategory3daxis.cpp, line 144, as _ZN22QCategory3DAxisPrivate9allowZeroEv
inline bool QCategory3DAxisPrivate::allowZero()
{
    return true;
}

//  from ../qtgraphs/src/graphs3d/axis/qcategory3daxis.cpp, line 122, as _ZN22QCategory3DAxisPrivateD2Ev
inline QCategory3DAxisPrivate::~QCategory3DAxisPrivate() {}

//  from ../qtgraphs/src/graphs3d/utils/qgraphs3dlogging.cpp, line 18, as _Z15lcAProperties3Dv
inline const QLoggingCategory &lcAProperties3D()
{
    static const QLoggingCategory category("qt.graphs3d.axis.properties");
    return category;
}

//  from ../qtgraphs/src/graphs3d/axis/qabstract3daxis.cpp, line 674, as _ZN22QAbstract3DAxisPrivateD2Ev
inline QAbstract3DAxisPrivate::~QAbstract3DAxisPrivate() {}

//  from ../qtgraphs/src/graphs3d/axis/qcategory3daxis.cpp, line 117, as _ZN22QCategory3DAxisPrivateC1Ev
inline QCategory3DAxisPrivate::QCategory3DAxisPrivate()
    : QAbstract3DAxisPrivate(QAbstract3DAxis::AxisType::Category)
    , m_labelsExplicitlySet(false)
{}

//  from ../qtgraphs/src/graphs3d/axis/qcategory3daxis.cpp, line 131, as _ZN22QCategory3DAxisPrivate13setDataLabelsERK5QListI7QStringE
inline void QCategory3DAxisPrivate::setDataLabels(const QStringList &labels)
{
    Q_Q(QCategory3DAxis);
    if (m_labelsExplicitlySet || m_labels == labels) {
        qCDebug(lcAProperties3D) << __FUNCTION__
            << "value is already set to:" << labels;
        return;
    }

    m_labels = labels;
    emit q->QAbstract3DAxis::labelsChanged();
}
//  -----------------------------------------------------------------------

//  Only a class built on QCategory3DAxisPrivate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQCategory3DAxisPrivate : QCategory3DAxisPrivate {
  using QCategory3DAxisPrivate::allowZero;
  using QCategory3DAxisPrivate::allowNegatives;
  using QCategory3DAxisPrivate::allowMinMaxSame;
};

//  A QCategory3DAxisPrivate that Python can take functions over in. Every QCategory3DAxisPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQCategory3DAxisPrivateCall0)(const void *, int *);
typedef bool (*CuteQCategory3DAxisPrivateCall1)(const void *, int *);
typedef bool (*CuteQCategory3DAxisPrivateCall2)(const void *, int *);
typedef void (*CuteQCategory3DAxisPrivateCall3)(const void *, float, float, bool, int *);
typedef void (*CuteQCategory3DAxisPrivateCall4)(const void *, float, int *);
typedef void (*CuteQCategory3DAxisPrivateCall5)(const void *, float, int *);
typedef void (*CuteQCategory3DAxisPrivateCall6)(const void *, int *);
class CuteQCategory3DAxisPrivate : public QCategory3DAxisPrivate {
public:
  using QCategory3DAxisPrivate::QCategory3DAxisPrivate;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN22QAbstract3DAxisPrivate9allowZeroEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstract3DAxisPrivate14allowNegativesEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstract3DAxisPrivate15allowMinMaxSameEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstract3DAxisPrivate8setRangeEffb")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstract3DAxisPrivate6setMinEf")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstract3DAxisPrivate6setMaxEf")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstract3DAxisPrivate12updateLabelsEv")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  bool QCategory3DAxisPrivate::allowZero()
  bool allowZero() override {
    if (taken[0]) {
      int handled = 0;
      CuteQCategory3DAxisPrivateCall0 call = reinterpret_cast<CuteQCategory3DAxisPrivateCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QCategory3DAxisPrivate::allowZero();
  }

  //  bool QCategory3DAxisPrivate::allowNegatives()
  bool allowNegatives() override {
    if (taken[1]) {
      int handled = 0;
      CuteQCategory3DAxisPrivateCall1 call = reinterpret_cast<CuteQCategory3DAxisPrivateCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QCategory3DAxisPrivate::allowNegatives();
  }

  //  bool QCategory3DAxisPrivate::allowMinMaxSame()
  bool allowMinMaxSame() override {
    if (taken[2]) {
      int handled = 0;
      CuteQCategory3DAxisPrivateCall2 call = reinterpret_cast<CuteQCategory3DAxisPrivateCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QCategory3DAxisPrivate::allowMinMaxSame();
  }

  //  void QAbstract3DAxisPrivate::setRange(float min, float max, bool
  //      suppressWarnings)
  void setRange(float min, float max, bool suppressWarnings) override {
    if (taken[3]) {
      int handled = 0;
      CuteQCategory3DAxisPrivateCall3 call = reinterpret_cast<CuteQCategory3DAxisPrivateCall3>(taken[3]);
      call(this, min, max, suppressWarnings, &handled);
      if (handled) return;
    }
    QAbstract3DAxisPrivate::setRange(min, max, suppressWarnings);
  }

  //  void QAbstract3DAxisPrivate::setMin(float min)
  void setMin(float min) override {
    if (taken[4]) {
      int handled = 0;
      CuteQCategory3DAxisPrivateCall4 call = reinterpret_cast<CuteQCategory3DAxisPrivateCall4>(taken[4]);
      call(this, min, &handled);
      if (handled) return;
    }
    QAbstract3DAxisPrivate::setMin(min);
  }

  //  void QAbstract3DAxisPrivate::setMax(float max)
  void setMax(float max) override {
    if (taken[5]) {
      int handled = 0;
      CuteQCategory3DAxisPrivateCall5 call = reinterpret_cast<CuteQCategory3DAxisPrivateCall5>(taken[5]);
      call(this, max, &handled);
      if (handled) return;
    }
    QAbstract3DAxisPrivate::setMax(max);
  }

  //  void QAbstract3DAxisPrivate::updateLabels()
  void updateLabels() override {
    if (taken[6]) {
      int handled = 0;
      CuteQCategory3DAxisPrivateCall6 call = reinterpret_cast<CuteQCategory3DAxisPrivateCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstract3DAxisPrivate::updateLabels();
  }
};

//  QCategory3DAxis *QCategory3DAxisPrivate::q_func()
extern "C" Q_DECL_EXPORT
QCategory3DAxis *ritual_ZN22QCategory3DAxisPrivate6q_funcEv(
    QCategory3DAxisPrivate *self) {
  return self->q_func();
}

//  const QCategory3DAxis *QCategory3DAxisPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QCategory3DAxis *ritual_ZNK22QCategory3DAxisPrivate6q_funcEv(
    const QCategory3DAxisPrivate *self) {
  return self->q_func();
}

//  QCategory3DAxisPrivate::QCategory3DAxisPrivate()
extern "C" Q_DECL_EXPORT
QCategory3DAxisPrivate *ritual_ZN22QCategory3DAxisPrivateC1Ev() {
  return new CuteQCategory3DAxisPrivate();
}

//  QCategory3DAxisPrivate::~QCategory3DAxisPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QCategory3DAxisPrivateD1Ev(QCategory3DAxisPrivate *self) {
  delete self;
}

//  void QCategory3DAxisPrivate::setDataLabels(const QStringList &labels)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QCategory3DAxisPrivate13setDataLabelsERK5QListI7QStringE(
    QCategory3DAxisPrivate *self,
    const QList<QString> *labels) {
  self->setDataLabels(*labels);
}

//  bool QCategory3DAxisPrivate::allowZero()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QCategory3DAxisPrivate9allowZeroEv(
    QCategory3DAxisPrivate *self) {
  return self->allowZero();
}

//  bool QCategory3DAxisPrivate::allowNegatives()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QCategory3DAxisPrivate14allowNegativesEv(
    QCategory3DAxisPrivate *self) {
  return self->allowNegatives();
}

//  bool QCategory3DAxisPrivate::allowMinMaxSame()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QCategory3DAxisPrivate15allowMinMaxSameEv(
    QCategory3DAxisPrivate *self) {
  return self->allowMinMaxSame();
}

//  a Python function taken by a CuteQCategory3DAxisPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCategory3DAxisPrivate(
    QCategory3DAxisPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCategory3DAxisPrivate *>(self)->take(key, call);
}

//  bool QCategory3DAxisPrivate::allowZero()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QCategory3DAxisPrivate9allowZeroEv(
    QCategory3DAxisPrivate *self) {
  return static_cast<OwnQCategory3DAxisPrivate *>(self)->OwnQCategory3DAxisPrivate::allowZero();
}

//  bool QCategory3DAxisPrivate::allowNegatives()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QCategory3DAxisPrivate14allowNegativesEv(
    QCategory3DAxisPrivate *self) {
  return static_cast<OwnQCategory3DAxisPrivate *>(self)->OwnQCategory3DAxisPrivate::allowNegatives();
}

//  bool QCategory3DAxisPrivate::allowMinMaxSame()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QCategory3DAxisPrivate15allowMinMaxSameEv(
    QCategory3DAxisPrivate *self) {
  return static_cast<OwnQCategory3DAxisPrivate *>(self)->OwnQCategory3DAxisPrivate::allowMinMaxSame();
}

#endif  // (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d)))
