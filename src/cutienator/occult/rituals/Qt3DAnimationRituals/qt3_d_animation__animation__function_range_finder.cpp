//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/functionrangefinder_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/functionrangefinder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/private/functionrangefinder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/animation/backend/functionrangefinder.cpp, line 39, as _ZN13Qt3DAnimation9Animation19FunctionRangeFinderC1EP5QListIfE
namespace Qt3DAnimation::Animation {
inline FunctionRangeFinder::FunctionRangeFinder(QList<float> *x)
    : m_x(x)
    , m_previousLowerBound(0)
    , m_correlated(0)
    , m_rangeSize(2)
    , m_correlationThreshold(1)
    , m_ascending(true)
{
    updateAutomaticCorrelationThreshold();
    if (!m_x->isEmpty())
        m_ascending = (m_x->last() >= m_x->first());
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/functionrangefinder.cpp, line 56, as _ZNK13Qt3DAnimation9Animation19FunctionRangeFinder6locateEf
namespace Qt3DAnimation::Animation {
inline int FunctionRangeFinder::locate(float x) const
{
    if (m_x->size() < 2 || m_rangeSize < 2 || m_rangeSize > m_x->size())
        return -1;

    qsizetype jLower = 0;
    qsizetype jUpper = m_x->size() - 1;
    while (jUpper - jLower > 1) {
        qsizetype jMid = (jUpper + jLower) >> 1;
        if ((x >= m_x->at(jMid)) == m_ascending)
            jLower = jMid;
        else
            jUpper = jMid;
    }

    m_correlated = std::abs(jLower - m_previousLowerBound) <= m_correlationThreshold;
    m_previousLowerBound = jLower;

    return qMax(0, qMin(m_x->size() - m_rangeSize, jLower - ((m_rangeSize - 2) >> 1)));
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/functionrangefinder.cpp, line 81, as _ZNK13Qt3DAnimation9Animation19FunctionRangeFinder4huntEf
namespace Qt3DAnimation::Animation {
inline int FunctionRangeFinder::hunt(float x) const
{
    if (m_x->size() < 2 || m_rangeSize < 2 || m_rangeSize > m_x->size())
        return -1;

    qsizetype jLower = m_previousLowerBound;
    qsizetype jMid;
    qsizetype jUpper;
    if (jLower < 0 || jLower > (m_x->size() - 1)) {
        jLower = 0;
        jUpper = m_x->size() - 1;
    } else {
        qsizetype increment = 1;
        if ((x >= m_x->at(jLower)) == m_ascending) {
            for (;;) {
                jUpper = jLower + increment;
                if (jUpper >= m_x->size() - 1) {
                    jUpper = m_x->size() - 1;
                    break;
                } else if ((x < m_x->at(jUpper)) == m_ascending) {
                    break;
                } else {
                    jLower = jUpper;
                    increment += increment;
                }
            }
        } else {
            jUpper = jLower;
            for (;;) {
                jLower = jLower - increment;
                if (jLower <= 0) {
                    jLower = 0;
                    break;
                } else if ((x >= m_x->at(jLower)) == m_ascending) {
                    break;
                } else {
                    jUpper = jLower;
                    increment += increment;
                }
            }
        }
    }

    while (jUpper - jLower > 1) {
        jMid = (jUpper + jLower) >> 1;
        if ((x >= m_x->at(jMid)) == m_ascending)
            jLower = jMid;
        else
            jUpper = jMid;
    }

    m_correlated = std::abs(jLower - m_previousLowerBound) <= m_correlationThreshold;
    m_previousLowerBound = jLower;

    return qMax(0, qMin(m_x->size() - m_rangeSize, jLower - ((m_rangeSize - 2) >> 1)));
}
}  // namespace Qt3DAnimation::Animation
//  -----------------------------------------------------------------------

//  Qt3DAnimation::Animation::FunctionRangeFinder::FunctionRangeFinder(QList<
//      float> *x)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::FunctionRangeFinder *ritual_ZN13Qt3DAnimation9Animation19FunctionRangeFinderC1EP5QListIfE(
    QList<float> *x) {
  return new Qt3DAnimation::Animation::FunctionRangeFinder(x);
}

//  int Qt3DAnimation::Animation::FunctionRangeFinder::findLowerBound(float
//      x) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13Qt3DAnimation9Animation19FunctionRangeFinder14findLowerBoundEf(
    const Qt3DAnimation::Animation::FunctionRangeFinder *self,
    float x) {
  return self->findLowerBound(x);
}

//  int Qt3DAnimation::Animation::FunctionRangeFinder::rangeSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13Qt3DAnimation9Animation19FunctionRangeFinder9rangeSizeEv(
    const Qt3DAnimation::Animation::FunctionRangeFinder *self) {
  return self->rangeSize();
}

//  void Qt3DAnimation::Animation::FunctionRangeFinder::setRangeSize(int
//      rangeSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation19FunctionRangeFinder12setRangeSizeEi(
    Qt3DAnimation::Animation::FunctionRangeFinder *self,
    int rangeSize) {
  self->setRangeSize(rangeSize);
}

//  bool Qt3DAnimation::Animation::FunctionRangeFinder::isAscending() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13Qt3DAnimation9Animation19FunctionRangeFinder11isAscendingEv(
    const Qt3DAnimation::Animation::FunctionRangeFinder *self) {
  return self->isAscending();
}

//  void Qt3DAnimation::Animation::FunctionRangeFinder::setAscending(bool
//      ascending)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation19FunctionRangeFinder12setAscendingEb(
    Qt3DAnimation::Animation::FunctionRangeFinder *self,
    bool ascending) {
  self->setAscending(ascending);
}

//  int Qt3DAnimation::Animation::FunctionRangeFinder::correlationThreshold()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13Qt3DAnimation9Animation19FunctionRangeFinder20correlationThresholdEv(
    const Qt3DAnimation::Animation::FunctionRangeFinder *self) {
  return self->correlationThreshold();
}

//  void Qt3DAnimation::Animation::FunctionRangeFinder::updateAutomaticCorrel
//      ationThreshold()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation19FunctionRangeFinder35updateAutomaticCorrelationThresholdEv(
    Qt3DAnimation::Animation::FunctionRangeFinder *self) {
  self->updateAutomaticCorrelationThreshold();
}

//  int Qt3DAnimation::Animation::FunctionRangeFinder::locate(float x) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13Qt3DAnimation9Animation19FunctionRangeFinder6locateEf(
    const Qt3DAnimation::Animation::FunctionRangeFinder *self,
    float x) {
  return self->locate(x);
}

//  int Qt3DAnimation::Animation::FunctionRangeFinder::hunt(float x) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13Qt3DAnimation9Animation19FunctionRangeFinder4huntEf(
    const Qt3DAnimation::Animation::FunctionRangeFinder *self,
    float x) {
  return self->hunt(x);
}

//  Qt3DAnimation::Animation::FunctionRangeFinder::~FunctionRangeFinder()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation19FunctionRangeFinderD1Ev(
    Qt3DAnimation::Animation::FunctionRangeFinder *self) {
  delete self;
}
