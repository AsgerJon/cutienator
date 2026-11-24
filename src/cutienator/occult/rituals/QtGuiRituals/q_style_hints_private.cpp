//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qstylehints_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/qstylehints.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qstylehints_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qaccessibilityhints.h>
#include <QtGui/private/qaccessibilityhints_p.h>
#include <QtGui/private/qaccessibilityhints_p.h>
#include <QtGui/qstylehints.h>
#include <QtGui/private/qstylehints_p.h>
#include <QtGui/qpa/qplatformintegration.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/kernel/qaccessibilityhints.cpp, line 20, as _ZN26QAccessibilityHintsPrivate22updateMotionPreferenceEN2Qt16MotionPreferenceE
inline void QAccessibilityHintsPrivate::updateMotionPreference(Qt::MotionPreference motionPreference)
{
    if (m_motionPreference == motionPreference)
        return;
    m_motionPreference = motionPreference;

    Q_Q(QAccessibilityHints);
    emit q->motionPreferenceChanged(motionPreference);
}

//  from src/gui/kernel/qaccessibilityhints.cpp, line 10, as _ZN26QAccessibilityHintsPrivate24updateContrastPreferenceEN2Qt18ContrastPreferenceE
inline void QAccessibilityHintsPrivate::updateContrastPreference(Qt::ContrastPreference contrastPreference)
{
    if (m_contrastPreference == contrastPreference)
        return;
    m_contrastPreference = contrastPreference;

    Q_Q(QAccessibilityHints);
    emit q->contrastPreferenceChanged(contrastPreference);
}

//  from src/gui/kernel/qaccessibilityhints.cpp, line 30, as _ZN26QAccessibilityHintsPrivate3getEP19QAccessibilityHints
inline QAccessibilityHintsPrivate *QAccessibilityHintsPrivate::get(QAccessibilityHints *q)
{
    Q_ASSERT(q);
    return q->d_func();
}

//  from src/gui/kernel/qstylehints.cpp, line 757, as _ZN18QStyleHintsPrivate17updateColorSchemeEN2Qt11ColorSchemeE
inline void QStyleHintsPrivate::updateColorScheme(Qt::ColorScheme colorScheme)
{
    if (m_colorScheme == colorScheme)
        return;
    m_colorScheme = colorScheme;
    Q_Q(QStyleHints);
    emit q->colorSchemeChanged(colorScheme);
}

//  from src/gui/kernel/qstylehints.cpp, line 771, as _ZN18QStyleHintsPrivate6updateEPK14QPlatformTheme
inline void QStyleHintsPrivate::update(const QPlatformTheme *theme)
{
    Q_ASSERT(theme);
    updateColorScheme(theme->colorScheme());
    auto *accessibilityHintsPrivate = QAccessibilityHintsPrivate::get(accessibilityHints());
    accessibilityHintsPrivate->updateContrastPreference(theme->contrastPreference());
    accessibilityHintsPrivate->updateMotionPreference(theme->motionPreference());
}

//  from src/gui/kernel/qstylehints.cpp, line 780, as _ZNK18QStyleHintsPrivate18accessibilityHintsEv
inline QAccessibilityHints *QStyleHintsPrivate::accessibilityHints() const
{
    Q_Q(const QStyleHints);
    if (!m_accessibilityHints)
        const_cast<QStyleHintsPrivate *>(this)->m_accessibilityHints = new QAccessibilityHints(const_cast<QStyleHints*>(q));
    return m_accessibilityHints;
}

//  from src/gui/kernel/qstylehints.cpp, line 788, as _ZN18QStyleHintsPrivate3getEP11QStyleHints
inline QStyleHintsPrivate *QStyleHintsPrivate::get(QStyleHints *q)
{
    Q_ASSERT(q);
    return q->d_func();
}
//  -----------------------------------------------------------------------

//  QStyleHints *QStyleHintsPrivate::q_func()
extern "C" Q_DECL_EXPORT
QStyleHints *ritual_ZN18QStyleHintsPrivate6q_funcEv(
    QStyleHintsPrivate *self) {
  return self->q_func();
}

//  const QStyleHints *QStyleHintsPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QStyleHints *ritual_ZNK18QStyleHintsPrivate6q_funcEv(
    const QStyleHintsPrivate *self) {
  return self->q_func();
}

//  Qt::ColorScheme QStyleHintsPrivate::colorScheme() const
extern "C" Q_DECL_EXPORT
Qt::ColorScheme ritual_ZNK18QStyleHintsPrivate11colorSchemeEv(
    const QStyleHintsPrivate *self) {
  return self->colorScheme();
}

//  void QStyleHintsPrivate::updateColorScheme(Qt::ColorScheme colorScheme)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStyleHintsPrivate17updateColorSchemeEN2Qt11ColorSchemeE(
    QStyleHintsPrivate *self,
    Qt::ColorScheme colorScheme) {
  self->updateColorScheme(colorScheme);
}

//  void QStyleHintsPrivate::update(const QPlatformTheme *theme)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStyleHintsPrivate6updateEPK14QPlatformTheme(
    QStyleHintsPrivate *self,
    const QPlatformTheme *theme) {
  self->update(theme);
}

//  QAccessibilityHints *QStyleHintsPrivate::accessibilityHints() const
extern "C" Q_DECL_EXPORT
QAccessibilityHints *ritual_ZNK18QStyleHintsPrivate18accessibilityHintsEv(
    const QStyleHintsPrivate *self) {
  return self->accessibilityHints();
}

//  QStyleHintsPrivate *QStyleHintsPrivate::get(QStyleHints *q)
extern "C" Q_DECL_EXPORT
QStyleHintsPrivate *ritual_ZN18QStyleHintsPrivate3getEP11QStyleHints(
    QStyleHints *q) {
  return QStyleHintsPrivate::get(q);
}
