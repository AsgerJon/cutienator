//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qvalue3daxis_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if !(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qvalue3daxis.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qvalue3daxis_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdebug.h>
#include <QtGraphs/private/qabstract3daxis_p.h>
#include <QtGraphs/private/qgraphs3dlogging_p.h>
#include <QtGraphs/private/qvalue3daxis_p.h>
#include <QtGraphs/private/qgraphs3dlogging_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from ../qtgraphs/src/graphs3d/axis/qvalue3daxis.cpp, line 358, as _ZN19QValue3DAxisPrivate8setRangeEffb
inline void QValue3DAxisPrivate::setRange(float min, float max, bool suppressWarnings)
{
    bool dirty = (min != m_min || max != m_max);

    QAbstract3DAxisPrivate::setRange(min, max, suppressWarnings);

    if (dirty)
        emitLabelsChanged();
}

//  from ../qtgraphs/src/graphs3d/axis/qvalue3daxis.cpp, line 368, as _ZN19QValue3DAxisPrivate6setMinEf
inline void QValue3DAxisPrivate::setMin(float min)
{
    bool dirty = (min != m_min);

    QAbstract3DAxisPrivate::setMin(min);

    if (dirty)
        emitLabelsChanged();
}

//  from ../qtgraphs/src/graphs3d/axis/qvalue3daxis.cpp, line 378, as _ZN19QValue3DAxisPrivate6setMaxEf
inline void QValue3DAxisPrivate::setMax(float max)
{
    bool dirty = (max != m_max);

    QAbstract3DAxisPrivate::setMax(max);

    if (dirty)
        emitLabelsChanged();
}

//  from ../qtgraphs/src/graphs3d/axis/qvalue3daxis.cpp, line 388, as _ZN19QValue3DAxisPrivate17emitLabelsChangedEv
inline void QValue3DAxisPrivate::emitLabelsChanged()
{
    Q_Q(QValue3DAxis);
    m_labelsDirty = true;
    emit q->labelsChanged();
}

//  from ../qtgraphs/src/graphs3d/axis/qvalue3daxis.cpp, line 395, as _ZN19QValue3DAxisPrivate18emitFormatterDirtyEv
inline void QValue3DAxisPrivate::emitFormatterDirty()
{
    Q_Q(QValue3DAxis);
    m_labelsDirty = true;
    emit q->formatterDirty();
}

//  from ../qtgraphs/src/graphs3d/axis/qvalue3daxis.cpp, line 414, as _ZN19QValue3DAxisPrivate9allowZeroEv
inline bool QValue3DAxisPrivate::allowZero()
{
    return m_formatter->allowZero();
}

//  from ../qtgraphs/src/graphs3d/axis/qvalue3daxis.cpp, line 419, as _ZN19QValue3DAxisPrivate14allowNegativesEv
inline bool QValue3DAxisPrivate::allowNegatives()
{
    return m_formatter->allowNegatives();
}

//  from ../qtgraphs/src/graphs3d/axis/qvalue3daxis.cpp, line 424, as _ZN19QValue3DAxisPrivate15allowMinMaxSameEv
inline bool QValue3DAxisPrivate::allowMinMaxSame()
{
    return false;
}
//  -----------------------------------------------------------------------

//  Only a class built on QValue3DAxisPrivate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQValue3DAxisPrivate : QValue3DAxisPrivate {
  using QValue3DAxisPrivate::allowZero;
  using QValue3DAxisPrivate::allowNegatives;
  using QValue3DAxisPrivate::allowMinMaxSame;
};

//  A QValue3DAxisPrivate that Python can take functions over in. Every QValue3DAxisPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQValue3DAxisPrivateCall0)(const void *, float, float, bool, int *);
typedef void (*CuteQValue3DAxisPrivateCall1)(const void *, float, int *);
typedef void (*CuteQValue3DAxisPrivateCall2)(const void *, float, int *);
typedef void (*CuteQValue3DAxisPrivateCall3)(const void *, int *);
typedef bool (*CuteQValue3DAxisPrivateCall4)(const void *, int *);
typedef bool (*CuteQValue3DAxisPrivateCall5)(const void *, int *);
typedef bool (*CuteQValue3DAxisPrivateCall6)(const void *, int *);
class CuteQValue3DAxisPrivate : public QValue3DAxisPrivate {
public:
  using QValue3DAxisPrivate::QValue3DAxisPrivate;
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

  //  void QValue3DAxisPrivate::setRange(float min, float max, bool
  //      suppressWarnings)
  void setRange(float min, float max, bool suppressWarnings) override {
    if (taken[0]) {
      int handled = 0;
      CuteQValue3DAxisPrivateCall0 call = reinterpret_cast<CuteQValue3DAxisPrivateCall0>(taken[0]);
      call(this, min, max, suppressWarnings, &handled);
      if (handled) return;
    }
    QValue3DAxisPrivate::setRange(min, max, suppressWarnings);
  }

  //  void QValue3DAxisPrivate::setMin(float min)
  void setMin(float min) override {
    if (taken[1]) {
      int handled = 0;
      CuteQValue3DAxisPrivateCall1 call = reinterpret_cast<CuteQValue3DAxisPrivateCall1>(taken[1]);
      call(this, min, &handled);
      if (handled) return;
    }
    QValue3DAxisPrivate::setMin(min);
  }

  //  void QValue3DAxisPrivate::setMax(float max)
  void setMax(float max) override {
    if (taken[2]) {
      int handled = 0;
      CuteQValue3DAxisPrivateCall2 call = reinterpret_cast<CuteQValue3DAxisPrivateCall2>(taken[2]);
      call(this, max, &handled);
      if (handled) return;
    }
    QValue3DAxisPrivate::setMax(max);
  }

  //  void QValue3DAxisPrivate::updateLabels()
  void updateLabels() override {
    if (taken[3]) {
      int handled = 0;
      CuteQValue3DAxisPrivateCall3 call = reinterpret_cast<CuteQValue3DAxisPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QValue3DAxisPrivate::updateLabels();
  }

  //  bool QValue3DAxisPrivate::allowZero()
  bool allowZero() override {
    if (taken[4]) {
      int handled = 0;
      CuteQValue3DAxisPrivateCall4 call = reinterpret_cast<CuteQValue3DAxisPrivateCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QValue3DAxisPrivate::allowZero();
  }

  //  bool QValue3DAxisPrivate::allowNegatives()
  bool allowNegatives() override {
    if (taken[5]) {
      int handled = 0;
      CuteQValue3DAxisPrivateCall5 call = reinterpret_cast<CuteQValue3DAxisPrivateCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QValue3DAxisPrivate::allowNegatives();
  }

  //  bool QValue3DAxisPrivate::allowMinMaxSame()
  bool allowMinMaxSame() override {
    if (taken[6]) {
      int handled = 0;
      CuteQValue3DAxisPrivateCall6 call = reinterpret_cast<CuteQValue3DAxisPrivateCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QValue3DAxisPrivate::allowMinMaxSame();
  }
};

//  QValue3DAxis *QValue3DAxisPrivate::q_func()
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZN19QValue3DAxisPrivate6q_funcEv(
    QValue3DAxisPrivate *self) {
  return self->q_func();
}

//  const QValue3DAxis *QValue3DAxisPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QValue3DAxis *ritual_ZNK19QValue3DAxisPrivate6q_funcEv(
    const QValue3DAxisPrivate *self) {
  return self->q_func();
}

//  void QValue3DAxisPrivate::setRange(float min, float max, bool
//      suppressWarnings)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QValue3DAxisPrivate8setRangeEffb(
    QValue3DAxisPrivate *self,
    float min,
    float max,
    bool suppressWarnings) {
  self->setRange(min, max, suppressWarnings);
}

//  void QValue3DAxisPrivate::setMin(float min)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QValue3DAxisPrivate6setMinEf(
    QValue3DAxisPrivate *self,
    float min) {
  self->setMin(min);
}

//  void QValue3DAxisPrivate::setMax(float max)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QValue3DAxisPrivate6setMaxEf(
    QValue3DAxisPrivate *self,
    float max) {
  self->setMax(max);
}

//  void QValue3DAxisPrivate::emitLabelsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QValue3DAxisPrivate17emitLabelsChangedEv(
    QValue3DAxisPrivate *self) {
  self->emitLabelsChanged();
}

//  void QValue3DAxisPrivate::emitFormatterDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QValue3DAxisPrivate18emitFormatterDirtyEv(
    QValue3DAxisPrivate *self) {
  self->emitFormatterDirty();
}

//  bool QValue3DAxisPrivate::allowZero()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QValue3DAxisPrivate9allowZeroEv(QValue3DAxisPrivate *self) {
  return self->allowZero();
}

//  bool QValue3DAxisPrivate::allowNegatives()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QValue3DAxisPrivate14allowNegativesEv(
    QValue3DAxisPrivate *self) {
  return self->allowNegatives();
}

//  bool QValue3DAxisPrivate::allowMinMaxSame()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QValue3DAxisPrivate15allowMinMaxSameEv(
    QValue3DAxisPrivate *self) {
  return self->allowMinMaxSame();
}

//  a Python function taken by a CuteQValue3DAxisPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QValue3DAxisPrivate(
    QValue3DAxisPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQValue3DAxisPrivate *>(self)->take(key, call);
}

//  bool QValue3DAxisPrivate::allowZero()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QValue3DAxisPrivate9allowZeroEv(
    QValue3DAxisPrivate *self) {
  return static_cast<OwnQValue3DAxisPrivate *>(self)->OwnQValue3DAxisPrivate::allowZero();
}

//  bool QValue3DAxisPrivate::allowNegatives()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QValue3DAxisPrivate14allowNegativesEv(
    QValue3DAxisPrivate *self) {
  return static_cast<OwnQValue3DAxisPrivate *>(self)->OwnQValue3DAxisPrivate::allowNegatives();
}

//  bool QValue3DAxisPrivate::allowMinMaxSame()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QValue3DAxisPrivate15allowMinMaxSameEv(
    QValue3DAxisPrivate *self) {
  return static_cast<OwnQValue3DAxisPrivate *>(self)->OwnQValue3DAxisPrivate::allowMinMaxSame();
}

#endif  // !(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))
