//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/qlogvalue3daxisformatter_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/qlogvalue3daxisformatter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/qvalue3daxisformatter_p.h>
#include <QtDataVisualization/private/qvalue3daxis_p.h>
#include <QtDataVisualization/private/qlogvalue3daxisformatter_p.h>
#include <QtDataVisualization/private/qvalue3daxis_p.h>
#include <QtCore/qmath.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/axis/qvalue3daxisformatter.cpp, line 290, as _ZN28QValue3DAxisFormatterPrivateC2EP21QValue3DAxisFormatter
inline QValue3DAxisFormatterPrivate::QValue3DAxisFormatterPrivate(QValue3DAxisFormatter *q)
    : QObject(0),
      q_ptr(q),
      m_needsRecalculate(true),
      m_min(0.0f),
      m_max(0.0f),
      m_rangeNormalizer(0.0f),
      m_axis(0),
      m_preparsedParamType(Utils::ParamTypeUnknown),
      m_allowNegatives(true),
      m_allowZero(true),
      m_formatPrecision(6), // 6 and 'g' are defaults in Qt API for format precision and spec
      m_formatSpec('g'),
      m_cLocaleInUse(true)
{
}

//  from ../qtdatavis3d/src/datavisualization/axis/qvalue3daxisformatter.cpp, line 325, as _ZN28QValue3DAxisFormatterPrivate13doRecalculateEv
inline void QValue3DAxisFormatterPrivate::doRecalculate()
{
    int segmentCount = m_axis->segmentCount();
    int subGridCount = m_axis->subSegmentCount() - 1;
    QString labelFormat =  m_axis->labelFormat();

    m_gridPositions.resize(segmentCount + 1);
    m_subGridPositions.resize(segmentCount * subGridCount);

    m_labelPositions.resize(segmentCount + 1);
    m_labelStrings.clear();
    m_labelStrings.reserve(segmentCount + 1);

    // Use qreals for intermediate calculations for better accuracy on label values
    qreal segmentStep = 1.0 / qreal(segmentCount);
    qreal subSegmentStep = 0;
    if (subGridCount > 0)
        subSegmentStep = segmentStep / qreal(subGridCount + 1);

    // Calculate positions
    qreal rangeNormalizer = qreal(m_max - m_min);
    for (int i = 0; i < segmentCount; i++) {
        qreal gridValue = segmentStep * qreal(i);
        m_gridPositions[i] = float(gridValue);
        m_labelPositions[i] = float(gridValue);
        m_labelStrings << q_ptr->stringForValue(gridValue * rangeNormalizer + qreal(m_min),
                                                labelFormat);
        if (m_subGridPositions.size()) {
            for (int j = 0; j < subGridCount; j++)
                m_subGridPositions[i * subGridCount + j] = gridValue + subSegmentStep * (j + 1);
        }
    }

    // Ensure max value doesn't suffer from any rounding errors
    m_gridPositions[segmentCount] = 1.0f;
    m_labelPositions[segmentCount] = 1.0f;
    m_labelStrings << q_ptr->stringForValue(qreal(m_max), labelFormat);
}

//  from ../qtdatavis3d/src/datavisualization/axis/qlogvalue3daxisformatter.cpp, line 276, as _ZN31QLogValue3DAxisFormatterPrivate11recalculateEv
inline void QLogValue3DAxisFormatterPrivate::recalculate()
{
    // When doing position/value mappings, base doesn't matter, so just use natural logarithm
    m_logMin = qLn(qreal(m_min));
    m_logMax = qLn(qreal(m_max));
    m_logRangeNormalizer = m_logMax - m_logMin;

    int subGridCount = m_axis->subSegmentCount() - 1;
    int segmentCount = m_axis->segmentCount();
    QString labelFormat =  m_axis->labelFormat();
    qreal segmentStep;
    if (m_base > 0.0) {
        // Update parent axis segment counts
        qreal logMin = qLn(qreal(m_min)) / qLn(m_base);
        qreal logMax = qLn(qreal(m_max)) / qLn(m_base);
        qreal logRangeNormalizer = logMax - logMin;

        qreal minDiff = qCeil(logMin) - logMin;
        qreal maxDiff = logMax - qFloor(logMax);

        m_evenMinSegment = qFuzzyIsNull(minDiff);
        m_evenMaxSegment = qFuzzyIsNull(maxDiff);

        segmentCount = qRound(logRangeNormalizer - minDiff - maxDiff);

        if (!m_evenMinSegment)
            segmentCount++;
        if (!m_evenMaxSegment)
            segmentCount++;

        segmentStep = 1.0 / logRangeNormalizer;

        if (m_autoSubGrid) {
            subGridCount = qCeil(m_base) - 2; // -2 for subgrid because subsegment count is base - 1
            if (subGridCount < 0)
                subGridCount = 0;
        }

        m_gridPositions.resize(segmentCount + 1);
        m_subGridPositions.resize(segmentCount * subGridCount);
        m_labelPositions.resize(segmentCount + 1);
        m_labelStrings.clear();
        m_labelStrings.reserve(segmentCount + 1);

        // Calculate segment positions
        int index = 0;
        if (!m_evenMinSegment) {
            m_gridPositions[0] = 0.0f;
            m_labelPositions[0] = 0.0f;
            if (m_showEdgeLabels)
                m_labelStrings << qptr()->stringForValue(qreal(m_min), labelFormat);
            else
                m_labelStrings << QString();
            index++;
        }
        for (int i = 0; i < segmentCount; i++) {
            float gridValue = float((minDiff + qreal(i)) / qreal(logRangeNormalizer));
            m_gridPositions[index] = gridValue;
            m_labelPositions[index] = gridValue;
            m_labelStrings << qptr()->stringForValue(qPow(m_base, minDiff + qreal(i) + logMin),
                                                    labelFormat);
            index++;
        }
        // Ensure max value doesn't suffer from any rounding errors
        m_gridPositions[segmentCount] = 1.0f;
        m_labelPositions[segmentCount] = 1.0f;
        QString finalLabel;
        if (m_showEdgeLabels || m_evenMaxSegment)
            finalLabel = qptr()->stringForValue(qreal(m_max), labelFormat);

        if (m_labelStrings.size() > segmentCount)
            m_labelStrings.replace(segmentCount, finalLabel);
        else
            m_labelStrings << finalLabel;
    } else {
        // Grid lines and label positions are the same as the parent class, so call parent impl
        // first to populate those
        QValue3DAxisFormatterPrivate::doRecalculate();

        // Label string list needs to be repopulated
        segmentStep = 1.0 / qreal(segmentCount);

        m_labelStrings << qptr()->stringForValue(qreal(m_min), labelFormat);
        for (int i = 1; i < m_labelPositions.size() - 1; i++)
            m_labelStrings[i] = qptr()->stringForValue(qExp(segmentStep * qreal(i)
                                                           * m_logRangeNormalizer + m_logMin),
                                                      labelFormat);
        m_labelStrings << qptr()->stringForValue(qreal(m_max), labelFormat);

        m_evenMaxSegment = true;
        m_evenMinSegment = true;
    }

    // Subgrid line positions are logarithmically spaced
    if (subGridCount > 0) {
        float oneSegmentRange = valueAt(float(segmentStep)) - m_min;
        float subSegmentStep = oneSegmentRange / float(subGridCount + 1);

        // Since the logarithm has the same curvature across whole axis range, we can just calculate
        // subgrid positions for the first segment and replicate them to other segments.
        QList<float> actualSubSegmentSteps(subGridCount);

        for (int i = 0; i < subGridCount; i++) {
            float currentSubPosition = positionAt(m_min + ((i + 1) * subSegmentStep));
            actualSubSegmentSteps[i] = currentSubPosition;
        }

        float firstPartialSegmentAdjustment = float(segmentStep) - m_gridPositions.at(1);
        for (int i = 0; i < segmentCount; i++) {
            for (int j = 0; j < subGridCount; j++) {
                float position = m_gridPositions.at(i) + actualSubSegmentSteps.at(j);
                if (!m_evenMinSegment && i == 0)
                    position -= firstPartialSegmentAdjustment;
                if (position > 1.0f)
                    position = 1.0f;
                if (position < 0.0f)
                    position = 0.0f;
                m_subGridPositions[i * subGridCount + j] = position;
            }
        }
    }
}

//  from ../qtdatavis3d/src/datavisualization/axis/qlogvalue3daxisformatter.cpp, line 410, as _ZNK31QLogValue3DAxisFormatterPrivate10positionAtEf
inline float QLogValue3DAxisFormatterPrivate::positionAt(float value) const
{
    qreal logValue = qLn(qreal(value));
    float retval = float((logValue - m_logMin) / m_logRangeNormalizer);

    return retval;
}

//  from ../qtdatavis3d/src/datavisualization/axis/qlogvalue3daxisformatter.cpp, line 418, as _ZNK31QLogValue3DAxisFormatterPrivate7valueAtEf
inline float QLogValue3DAxisFormatterPrivate::valueAt(float position) const
{
    qreal logValue = (qreal(position) * m_logRangeNormalizer) + m_logMin;
    return float(qExp(logValue));
}

//  from ../qtdatavis3d/src/datavisualization/axis/qlogvalue3daxisformatter.cpp, line 424, as _ZN31QLogValue3DAxisFormatterPrivate4qptrEv
inline QLogValue3DAxisFormatter *QLogValue3DAxisFormatterPrivate::qptr()
{
    return static_cast<QLogValue3DAxisFormatter *>(q_ptr);
}
//  -----------------------------------------------------------------------

//  A QLogValue3DAxisFormatterPrivate that Python can take functions over in. Every QLogValue3DAxisFormatterPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLogValue3DAxisFormatterPrivateCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLogValue3DAxisFormatterPrivateCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLogValue3DAxisFormatterPrivateCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLogValue3DAxisFormatterPrivateCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLogValue3DAxisFormatterPrivateCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLogValue3DAxisFormatterPrivateCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLogValue3DAxisFormatterPrivateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQLogValue3DAxisFormatterPrivate : public QLogValue3DAxisFormatterPrivate {
public:
  using QLogValue3DAxisFormatterPrivate::QLogValue3DAxisFormatterPrivate;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQLogValue3DAxisFormatterPrivateCall0 call = reinterpret_cast<CuteQLogValue3DAxisFormatterPrivateCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLogValue3DAxisFormatterPrivateCall1 call = reinterpret_cast<CuteQLogValue3DAxisFormatterPrivateCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQLogValue3DAxisFormatterPrivateCall2 call = reinterpret_cast<CuteQLogValue3DAxisFormatterPrivateCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQLogValue3DAxisFormatterPrivateCall3 call = reinterpret_cast<CuteQLogValue3DAxisFormatterPrivateCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQLogValue3DAxisFormatterPrivateCall4 call = reinterpret_cast<CuteQLogValue3DAxisFormatterPrivateCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQLogValue3DAxisFormatterPrivateCall5 call = reinterpret_cast<CuteQLogValue3DAxisFormatterPrivateCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQLogValue3DAxisFormatterPrivateCall6 call = reinterpret_cast<CuteQLogValue3DAxisFormatterPrivateCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QLogValue3DAxisFormatterPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QLogValue3DAxisFormatterPrivate10metaObjectEv(
    const QLogValue3DAxisFormatterPrivate *self) {
  return self->metaObject();
}

//  QLogValue3DAxisFormatterPrivate::~QLogValue3DAxisFormatterPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QLogValue3DAxisFormatterPrivateD1Ev(
    QLogValue3DAxisFormatterPrivate *self) {
  delete self;
}

//  void QLogValue3DAxisFormatterPrivate::recalculate()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QLogValue3DAxisFormatterPrivate11recalculateEv(
    QLogValue3DAxisFormatterPrivate *self) {
  self->recalculate();
}

//  float QLogValue3DAxisFormatterPrivate::positionAt(float value) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK31QLogValue3DAxisFormatterPrivate10positionAtEf(
    const QLogValue3DAxisFormatterPrivate *self,
    float value) {
  return self->positionAt(value);
}

//  float QLogValue3DAxisFormatterPrivate::valueAt(float position) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK31QLogValue3DAxisFormatterPrivate7valueAtEf(
    const QLogValue3DAxisFormatterPrivate *self,
    float position) {
  return self->valueAt(position);
}

//  QLogValue3DAxisFormatter *QLogValue3DAxisFormatterPrivate::qptr()
extern "C" Q_DECL_EXPORT
QLogValue3DAxisFormatter *ritual_ZN31QLogValue3DAxisFormatterPrivate4qptrEv(
    QLogValue3DAxisFormatterPrivate *self) {
  return self->qptr();
}

//  a Python function taken by a CuteQLogValue3DAxisFormatterPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLogValue3DAxisFormatterPrivate(
    QLogValue3DAxisFormatterPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLogValue3DAxisFormatterPrivate *>(self)->take(key, call);
}
