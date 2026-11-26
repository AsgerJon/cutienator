//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qheightmapsurfacedataproxy_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_surface3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qheightmapsurfacedataproxy.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qheightmapsurfacedataproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qloggingcategory.h>
#include <QtCore/qdebug.h>
#include <QtCore/qfileinfo.h>
#include <QtGraphs/private/qheightmapsurfacedataproxy_p.h>
#include <QtGraphs/private/qsurface3dseries_p.h>
#include <QtGraphs/private/qgraphs3dlogging_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgraphs/src/graphs3d/data/qheightmapsurfacedataproxy.cpp, line 26, as local:qheightmapsurfacedataproxy.cpp:defaultMinValue
const float defaultMinValue = 0.0f;

//  from ../qtgraphs/src/graphs3d/data/qheightmapsurfacedataproxy.cpp, line 27, as local:qheightmapsurfacedataproxy.cpp:defaultMaxValue
const float defaultMaxValue = 10.0f;

//  from ../qtgraphs/src/graphs3d/utils/qgraphs3dlogging.cpp, line 13, as _Z14lcProperties3Dv
inline const QLoggingCategory &lcProperties3D()
{
    static const QLoggingCategory category("qt.graphs3d.properties");
    return category;
}

//  from ../qtgraphs/src/graphs3d/data/qheightmapsurfacedataproxy.cpp, line 537, as _ZN33QHeightMapSurfaceDataProxyPrivate14setValueRangesEffff
inline void QHeightMapSurfaceDataProxyPrivate::setValueRanges(float minX,
                                                       float maxX,
                                                       float minZ,
                                                       float maxZ)
{
    Q_Q(QHeightMapSurfaceDataProxy);
    bool minXChanged = false;
    bool maxXChanged = false;
    bool minZChanged = false;
    bool maxZChanged = false;
    if (m_minXValue != minX) {
        m_minXValue = minX;
        minXChanged = true;
    }
    if (m_minZValue != minZ) {
        m_minZValue = minZ;
        minZChanged = true;
    }
    if (m_maxXValue != maxX || minX >= maxX) {
        if (minX >= maxX) {
            m_maxXValue = minX + 1.0f;
            qCWarning(lcProperties3D, "%s tried to set invalid range for X value range."
                     " Range automatically adjusted to a valid one: %f - %f --> %f - %f",
                     qUtf8Printable(QLatin1String(__FUNCTION__)),
                     minX,
                     maxX,
                     m_minXValue,
                     m_maxXValue);
        } else {
            m_maxXValue = maxX;
        }
        maxXChanged = true;
    }
    if (m_maxZValue != maxZ || minZ >= maxZ) {
        if (minZ >= maxZ) {
            m_maxZValue = minZ + 1.0f;
            qCWarning(lcProperties3D, "%s tried to set invalid range for Z value range."
                     " Range automatically adjusted to a valid one: %f - %f --> %f - %f",
                     qUtf8Printable(QLatin1String(__FUNCTION__)),
                     minZ,
                     maxZ,
                     m_minZValue,
                     m_maxZValue);
        } else {
            m_maxZValue = maxZ;
        }
        maxZChanged = true;
    }

    if (minXChanged)
        emit q->minXValueChanged(m_minXValue);
    if (minZChanged)
        emit q->minZValueChanged(m_minZValue);
    if (maxXChanged)
        emit q->maxXValueChanged(m_maxXValue);
    if (maxZChanged)
        emit q->maxZValueChanged(m_maxZValue);

    if ((minXChanged || minZChanged || maxXChanged || maxZChanged) && !m_resolveTimer.isActive())
        m_resolveTimer.start(0);
}

//  from ../qtgraphs/src/graphs3d/data/qheightmapsurfacedataproxy.cpp, line 599, as _ZN33QHeightMapSurfaceDataProxyPrivate12setMinXValueEf
inline void QHeightMapSurfaceDataProxyPrivate::setMinXValue(float min)
{
    Q_Q(QHeightMapSurfaceDataProxy);
    if (min != m_minXValue) {
        bool maxChanged = false;
        if (min >= m_maxXValue) {
            float oldMax = m_maxXValue;
            m_maxXValue = min + 1.0f;
            qCWarning(lcProperties3D, "%s tried to set minimum X to equal or larger"
                     " than maximum X for value "
                     "range. Maximum automatically adjusted to a valid one: %f --> %f",
                     qUtf8Printable(QLatin1String(__func__)),
                     oldMax,
                     m_maxXValue);
            maxChanged = true;
        }
        m_minXValue = min;
        emit q->minXValueChanged(m_minXValue);
        if (maxChanged)
            emit q->maxXValueChanged(m_maxXValue);

        if (!m_resolveTimer.isActive())
            m_resolveTimer.start(0);
    }
}

//  from ../qtgraphs/src/graphs3d/data/qheightmapsurfacedataproxy.cpp, line 625, as _ZN33QHeightMapSurfaceDataProxyPrivate12setMaxXValueEf
inline void QHeightMapSurfaceDataProxyPrivate::setMaxXValue(float max)
{
    Q_Q(QHeightMapSurfaceDataProxy);
    if (m_maxXValue != max) {
        bool minChanged = false;
        if (max <= m_minXValue) {
            float oldMin = m_minXValue;
            m_minXValue = max - 1.0f;
            qCWarning(lcProperties3D, "%s tried to set maximum X to equal or smaller than minimum X"
                     " for value range. Minimum automatically adjusted to a valid one: %f --> %f",
                     qUtf8Printable(QLatin1String(__func__)),
                     oldMin,
                     m_minXValue);
            minChanged = true;
        }
        m_maxXValue = max;
        emit q->maxXValueChanged(m_maxXValue);
        if (minChanged)
            emit q->minXValueChanged(m_minXValue);

        if (!m_resolveTimer.isActive())
            m_resolveTimer.start(0);
    }
}

//  from ../qtgraphs/src/graphs3d/data/qheightmapsurfacedataproxy.cpp, line 650, as _ZN33QHeightMapSurfaceDataProxyPrivate12setMinZValueEf
inline void QHeightMapSurfaceDataProxyPrivate::setMinZValue(float min)
{
    Q_Q(QHeightMapSurfaceDataProxy);
    if (min != m_minZValue) {
        bool maxChanged = false;
        if (min >= m_maxZValue) {
            float oldMax = m_maxZValue;
            m_maxZValue = min + 1.0f;
            qCWarning(lcProperties3D, "%s tried to set minimum Z to equal or larger than maximum Z"
                     " for value range. Maximum automatically adjusted to a valid one: %f --> %f",
                     qUtf8Printable(QLatin1String(__func__)),
                     oldMax,
                     m_maxZValue);
            maxChanged = true;
        }
        m_minZValue = min;
        emit q->minZValueChanged(m_minZValue);
        if (maxChanged)
            emit q->maxZValueChanged(m_maxZValue);

        if (!m_resolveTimer.isActive())
            m_resolveTimer.start(0);
    }
}

//  from ../qtgraphs/src/graphs3d/data/qheightmapsurfacedataproxy.cpp, line 675, as _ZN33QHeightMapSurfaceDataProxyPrivate12setMaxZValueEf
inline void QHeightMapSurfaceDataProxyPrivate::setMaxZValue(float max)
{
    Q_Q(QHeightMapSurfaceDataProxy);
    if (m_maxZValue != max) {
        bool minChanged = false;
        if (max <= m_minZValue) {
            float oldMin = m_minZValue;
            m_minZValue = max - 1.0f;
            qCWarning(lcProperties3D, "%s tried to set maximum Z to equal or smaller than minimum Z"
                     " for value range. Minimum automatically adjusted to a valid one: %f --> %f",
                     qUtf8Printable(QLatin1String(__func__)),
                     oldMin,
                     m_minZValue);
            minChanged = true;
        }
        m_maxZValue = max;
        emit q->maxZValueChanged(m_maxZValue);
        if (minChanged)
            emit q->minZValueChanged(m_minZValue);

        if (!m_resolveTimer.isActive())
            m_resolveTimer.start(0);
    }
}

//  from ../qtgraphs/src/graphs3d/data/qheightmapsurfacedataproxy.cpp, line 700, as _ZN33QHeightMapSurfaceDataProxyPrivate12setMinYValueEf
inline void QHeightMapSurfaceDataProxyPrivate::setMinYValue(float min)
{
    Q_Q(QHeightMapSurfaceDataProxy);
    if (m_minYValue != min) {
        bool maxChanged = false;
        if (min >= m_maxYValue) {
            float oldMax = m_maxYValue;
            m_maxYValue = min + 1.0f;
            qCWarning(lcProperties3D, "%s tried to set minimum Y to equal or larger than maximum Y"
                     " for value range. Maximum automatically adjusted to a valid one: %f --> %f",
                     qUtf8Printable(QLatin1String(__func__)),
                     oldMax,
                     m_maxYValue);
            maxChanged = true;
        }
        m_minYValue = min;
        emit q->minYValueChanged(m_minYValue);
        if (maxChanged)
            emit q->maxYValueChanged(m_maxYValue);

        if (!m_resolveTimer.isActive())
            m_resolveTimer.start(0);
    }
}

//  from ../qtgraphs/src/graphs3d/data/qheightmapsurfacedataproxy.cpp, line 725, as _ZN33QHeightMapSurfaceDataProxyPrivate12setMaxYValueEf
inline void QHeightMapSurfaceDataProxyPrivate::setMaxYValue(float max)
{
    Q_Q(QHeightMapSurfaceDataProxy);
    if (m_maxYValue != max) {
        bool minChanged = false;
        if (max <= m_minYValue) {
            float oldMin = m_minYValue;
            m_minYValue = max - 1.0f;
            qCWarning(lcProperties3D, "%s tried to set maximum Y to equal or smaller than minimum Y"
                     " for value range. Minimum automatically adjusted to a valid one: %f --> %f",
                     qUtf8Printable(QLatin1String(__func__)),
                     oldMin,
                     m_minYValue);
            minChanged = true;
        }
        m_maxYValue = max;
        emit q->maxYValueChanged(m_maxYValue);
        if (minChanged)
            emit q->minYValueChanged(m_minYValue);

        if (!m_resolveTimer.isActive())
            m_resolveTimer.start(0);
    }
}

//  from ../qtgraphs/src/graphs3d/data/qheightmapsurfacedataproxy.cpp, line 750, as _ZN33QHeightMapSurfaceDataProxyPrivate13setAutoScaleYEb
inline void QHeightMapSurfaceDataProxyPrivate::setAutoScaleY(bool enabled)
{
    Q_Q(QHeightMapSurfaceDataProxy);
    if (enabled == m_autoScaleY) {
        qCDebug(lcProperties3D) << __FUNCTION__
            << "value is already set to:" << enabled;
        return;
    }

    m_autoScaleY = enabled;
    emit q->autoScaleYChanged(m_autoScaleY);

    if (!m_resolveTimer.isActive())
        m_resolveTimer.start(0);
}
//  -----------------------------------------------------------------------

//  A QHeightMapSurfaceDataProxyPrivate that Python can take functions over in. Every QHeightMapSurfaceDataProxyPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQHeightMapSurfaceDataProxyPrivateCall0)(const void *, QAbstract3DSeries *, int *);
class CuteQHeightMapSurfaceDataProxyPrivate : public QHeightMapSurfaceDataProxyPrivate {
public:
  using QHeightMapSurfaceDataProxyPrivate::QHeightMapSurfaceDataProxyPrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN25QAbstractDataProxyPrivate9setSeriesEP17QAbstract3DSeries")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QSurfaceDataProxyPrivate::setSeries(QAbstract3DSeries *series)
  void setSeries(QAbstract3DSeries *series) override {
    if (taken[0]) {
      int handled = 0;
      CuteQHeightMapSurfaceDataProxyPrivateCall0 call = reinterpret_cast<CuteQHeightMapSurfaceDataProxyPrivateCall0>(taken[0]);
      call(this, series, &handled);
      if (handled) return;
    }
    QSurfaceDataProxyPrivate::setSeries(series);
  }
};

//  QHeightMapSurfaceDataProxy *QHeightMapSurfaceDataProxyPrivate::q_func()
extern "C" Q_DECL_EXPORT
QHeightMapSurfaceDataProxy *ritual_ZN33QHeightMapSurfaceDataProxyPrivate6q_funcEv(
    QHeightMapSurfaceDataProxyPrivate *self) {
  return self->q_func();
}

//  const QHeightMapSurfaceDataProxy
//      *QHeightMapSurfaceDataProxyPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QHeightMapSurfaceDataProxy *ritual_ZNK33QHeightMapSurfaceDataProxyPrivate6q_funcEv(
    const QHeightMapSurfaceDataProxyPrivate *self) {
  return self->q_func();
}

//  QHeightMapSurfaceDataProxyPrivate::~QHeightMapSurfaceDataProxyPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QHeightMapSurfaceDataProxyPrivateD1Ev(
    QHeightMapSurfaceDataProxyPrivate *self) {
  delete self;
}

//  void QHeightMapSurfaceDataProxyPrivate::setValueRanges(float minX, float
//      maxX, float minZ, float maxZ)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QHeightMapSurfaceDataProxyPrivate14setValueRangesEffff(
    QHeightMapSurfaceDataProxyPrivate *self,
    float minX,
    float maxX,
    float minZ,
    float maxZ) {
  self->setValueRanges(minX, maxX, minZ, maxZ);
}

//  void QHeightMapSurfaceDataProxyPrivate::setMinXValue(float min)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QHeightMapSurfaceDataProxyPrivate12setMinXValueEf(
    QHeightMapSurfaceDataProxyPrivate *self,
    float min) {
  self->setMinXValue(min);
}

//  void QHeightMapSurfaceDataProxyPrivate::setMaxXValue(float max)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QHeightMapSurfaceDataProxyPrivate12setMaxXValueEf(
    QHeightMapSurfaceDataProxyPrivate *self,
    float max) {
  self->setMaxXValue(max);
}

//  void QHeightMapSurfaceDataProxyPrivate::setMinZValue(float min)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QHeightMapSurfaceDataProxyPrivate12setMinZValueEf(
    QHeightMapSurfaceDataProxyPrivate *self,
    float min) {
  self->setMinZValue(min);
}

//  void QHeightMapSurfaceDataProxyPrivate::setMaxZValue(float max)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QHeightMapSurfaceDataProxyPrivate12setMaxZValueEf(
    QHeightMapSurfaceDataProxyPrivate *self,
    float max) {
  self->setMaxZValue(max);
}

//  void QHeightMapSurfaceDataProxyPrivate::setMinYValue(float min)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QHeightMapSurfaceDataProxyPrivate12setMinYValueEf(
    QHeightMapSurfaceDataProxyPrivate *self,
    float min) {
  self->setMinYValue(min);
}

//  void QHeightMapSurfaceDataProxyPrivate::setMaxYValue(float max)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QHeightMapSurfaceDataProxyPrivate12setMaxYValueEf(
    QHeightMapSurfaceDataProxyPrivate *self,
    float max) {
  self->setMaxYValue(max);
}

//  void QHeightMapSurfaceDataProxyPrivate::setAutoScaleY(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QHeightMapSurfaceDataProxyPrivate13setAutoScaleYEb(
    QHeightMapSurfaceDataProxyPrivate *self,
    bool enabled) {
  self->setAutoScaleY(enabled);
}

//  a Python function taken by a CuteQHeightMapSurfaceDataProxyPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHeightMapSurfaceDataProxyPrivate(
    QHeightMapSurfaceDataProxyPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHeightMapSurfaceDataProxyPrivate *>(self)->take(key, call);
}

#endif  // (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_surface3d))
