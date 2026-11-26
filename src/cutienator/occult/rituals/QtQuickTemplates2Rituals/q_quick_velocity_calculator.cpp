//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickvelocitycalculator_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickvelocitycalculator_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/private/qquickvelocitycalculator_p_p.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquickvelocitycalculator.cpp, line 29, as _ZN24QQuickVelocityCalculator14startMeasuringERK7QPointFx
inline void QQuickVelocityCalculator::startMeasuring(const QPointF &point1, qint64 timestamp)
{
    m_point1 = point1;
    m_point1Timestamp = timestamp;
}

//  from ../qtdeclarative/src/quicktemplates/qquickvelocitycalculator.cpp, line 35, as _ZN24QQuickVelocityCalculator13stopMeasuringERK7QPointFx
inline void QQuickVelocityCalculator::stopMeasuring(const QPointF &point2, qint64 timestamp)
{
    if (timestamp == 0) {
        qWarning() << "QQuickVelocityCalculator: a call to stopMeasuring() must be preceded by a call to startMeasuring()";
        return;
    }

    m_point2 = point2;
    m_point2Timestamp = timestamp;
}

//  from ../qtdeclarative/src/quicktemplates/qquickvelocitycalculator.cpp, line 46, as _ZNK24QQuickVelocityCalculator8velocityEv
inline QPointF QQuickVelocityCalculator::velocity() const
{
    if (m_point2Timestamp == 0 || m_point1Timestamp == m_point2Timestamp)
        return QPointF();

    const qreal secondsElapsed = (m_point2Timestamp - m_point1Timestamp) / 1000.0;
    const QPointF distance = m_point2 - m_point1;
    return distance / secondsElapsed;
}
//  -----------------------------------------------------------------------

//  void QQuickVelocityCalculator::startMeasuring(const QPointF &point1,
//      qint64 timestamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickVelocityCalculator14startMeasuringERK7QPointFx(
    QQuickVelocityCalculator *self,
    const QPointF *point1,
    qint64 timestamp) {
  self->startMeasuring(*point1, timestamp);
}

//  void QQuickVelocityCalculator::stopMeasuring(const QPointF &m_point2,
//      qint64 timestamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickVelocityCalculator13stopMeasuringERK7QPointFx(
    QQuickVelocityCalculator *self,
    const QPointF *m_point2,
    qint64 timestamp) {
  self->stopMeasuring(*m_point2, timestamp);
}

//  void QQuickVelocityCalculator::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickVelocityCalculator5resetEv(
    QQuickVelocityCalculator *self) {
  self->reset();
}

//  QPointF QQuickVelocityCalculator::velocity() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK24QQuickVelocityCalculator8velocityEv(
    const QQuickVelocityCalculator *self) {
  return new QPointF(self->velocity());
}

//  QQuickVelocityCalculator::~QQuickVelocityCalculator()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickVelocityCalculatorD1Ev(
    QQuickVelocityCalculator *self) {
  delete self;
}
