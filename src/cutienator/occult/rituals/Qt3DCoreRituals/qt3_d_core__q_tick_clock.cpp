//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qtickclock_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qtickclock_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/private/qtickclock_p.h>
#include <QtCore/QThread>
#include <Qt3DCore/private/corelogging_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/core/qtickclock.cpp, line 14, as _ZN8Qt3DCore10QTickClockC1Ev
namespace Qt3DCore {
inline QTickClock::QTickClock()
    : m_tickInterval(1000000000 / 60) // Nanoseconds
    , m_time(0)
{
}
}  // namespace Qt3DCore

//  from ../qt3d/src/core/qtickclock.cpp, line 20, as _ZN8Qt3DCore10QTickClock16setTickFrequencyEf
namespace Qt3DCore {
inline void QTickClock::setTickFrequency(float frequency)
{
    Q_ASSERT(frequency > 0.0f);
    m_tickInterval = static_cast<qint64>(1000000000 / frequency);
}
}  // namespace Qt3DCore

//  from ../qt3d/src/core/qtickclock.cpp, line 33, as _ZN8Qt3DCore10QTickClock5resetEv
namespace Qt3DCore {
inline void QTickClock::reset()
{
    m_time = 0;
}
}  // namespace Qt3DCore
//  -----------------------------------------------------------------------

//  Qt3DCore::QTickClock::QTickClock()
extern "C" Q_DECL_EXPORT
Qt3DCore::QTickClock *ritual_ZN8Qt3DCore10QTickClockC1Ev() {
  return new Qt3DCore::QTickClock();
}

//  void Qt3DCore::QTickClock::setTickFrequency(float frequency)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QTickClock16setTickFrequencyEf(
    Qt3DCore::QTickClock *self,
    float frequency) {
  self->setTickFrequency(frequency);
}

//  void Qt3DCore::QTickClock::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QTickClock5resetEv(Qt3DCore::QTickClock *self) {
  self->reset();
}

//  Qt3DCore::QTickClock::~QTickClock()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QTickClockD1Ev(Qt3DCore::QTickClock *self) {
  delete self;
}
