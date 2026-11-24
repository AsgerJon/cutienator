//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qaccessibilityhints_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/qaccessibilityhints.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qaccessibilityhints_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qaccessibilityhints.h"
#include "qaccessibilityhints_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/kernel/qaccessibilityhints.cpp, line 10, as _ZN26QAccessibilityHintsPrivate24updateContrastPreferenceEN2Qt18ContrastPreferenceE
inline void QAccessibilityHintsPrivate::updateContrastPreference(Qt::ContrastPreference contrastPreference)
{
    if (m_contrastPreference == contrastPreference)
        return;
    m_contrastPreference = contrastPreference;

    Q_Q(QAccessibilityHints);
    emit q->contrastPreferenceChanged(contrastPreference);
}

//  from src/gui/kernel/qaccessibilityhints.cpp, line 20, as _ZN26QAccessibilityHintsPrivate22updateMotionPreferenceEN2Qt16MotionPreferenceE
inline void QAccessibilityHintsPrivate::updateMotionPreference(Qt::MotionPreference motionPreference)
{
    if (m_motionPreference == motionPreference)
        return;
    m_motionPreference = motionPreference;

    Q_Q(QAccessibilityHints);
    emit q->motionPreferenceChanged(motionPreference);
}

//  from src/gui/kernel/qaccessibilityhints.cpp, line 30, as _ZN26QAccessibilityHintsPrivate3getEP19QAccessibilityHints
inline QAccessibilityHintsPrivate *QAccessibilityHintsPrivate::get(QAccessibilityHints *q)
{
    Q_ASSERT(q);
    return q->d_func();
}
//  -----------------------------------------------------------------------

//  QAccessibilityHints *QAccessibilityHintsPrivate::q_func()
extern "C" Q_DECL_EXPORT
QAccessibilityHints *ritual_ZN26QAccessibilityHintsPrivate6q_funcEv(
    QAccessibilityHintsPrivate *self) {
  return self->q_func();
}

//  const QAccessibilityHints *QAccessibilityHintsPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAccessibilityHints *ritual_ZNK26QAccessibilityHintsPrivate6q_funcEv(
    const QAccessibilityHintsPrivate *self) {
  return self->q_func();
}

//  void QAccessibilityHintsPrivate::updateContrastPreference(Qt::ContrastPre
//      ference contrastPreference)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAccessibilityHintsPrivate24updateContrastPreferenceEN2Qt18ContrastPreferenceE(
    QAccessibilityHintsPrivate *self,
    Qt::ContrastPreference contrastPreference) {
  self->updateContrastPreference(contrastPreference);
}

//  void
//      QAccessibilityHintsPrivate::updateMotionPreference(Qt::MotionPreferen
//      ce motionPreference)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAccessibilityHintsPrivate22updateMotionPreferenceEN2Qt16MotionPreferenceE(
    QAccessibilityHintsPrivate *self,
    Qt::MotionPreference motionPreference) {
  self->updateMotionPreference(motionPreference);
}

//  QAccessibilityHintsPrivate
//      *QAccessibilityHintsPrivate::get(QAccessibilityHints *q)
extern "C" Q_DECL_EXPORT
QAccessibilityHintsPrivate *ritual_ZN26QAccessibilityHintsPrivate3getEP19QAccessibilityHints(
    QAccessibilityHints *q) {
  return QAccessibilityHintsPrivate::get(q);
}
