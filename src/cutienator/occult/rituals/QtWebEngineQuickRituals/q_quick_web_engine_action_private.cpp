//  Written by dev_tooling.RitualGenerator from the records of QtWebEngineQui
//  ck/6.12.0/QtWebEngineQuick/private/qquickwebengineaction_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qtwebenginequickglobal_p.h>
#include <QtWebEngineQuick/QtWebEngineQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebengineaction_p.h>
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebengineaction_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineQuick/private/qquickwebengineaction_p.h>
#include <QtWebEngineQuick/private/qquickwebengineaction_p_p.h>
#include <QtWebEngineQuick/private/qquickwebengineview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtwebengine/src/webenginequick/api/qquickwebengineaction.cpp, line 43, as _ZN28QQuickWebEngineActionPrivateC1ERK8QVariantRK7QStringS5_b
inline QQuickWebEngineActionPrivate::QQuickWebEngineActionPrivate(const QVariant &data, const QString &text, const QString &iconName, bool enabled)
    : m_data(data)
    , m_text(text)
    , m_iconName(iconName)
    , m_enabled(enabled)
{
}

//  from ../qtwebengine/src/webenginequick/api/qquickwebengineaction.cpp, line 51, as _ZN28QQuickWebEngineActionPrivateD1Ev
inline QQuickWebEngineActionPrivate::~QQuickWebEngineActionPrivate()
{
}

//  from ../qtwebengine/src/webenginequick/api/qquickwebengineaction.cpp, line 55, as _ZN28QQuickWebEngineActionPrivate10setEnabledEb
inline void QQuickWebEngineActionPrivate::setEnabled(bool enabled)
{
    Q_Q(QQuickWebEngineAction);
    if (m_enabled == enabled)
        return;
    m_enabled = enabled;
    emit q->enabledChanged();
}

//  from ../qtwebengine/src/webenginequick/api/qquickwebengineaction.cpp, line 64, as _ZNK28QQuickWebEngineActionPrivate4dataEv
inline QVariant QQuickWebEngineActionPrivate::data() const
{
    return m_data;
}

//  from ../qtwebengine/src/webenginequick/api/qquickwebengineaction.cpp, line 69, as _ZN28QQuickWebEngineActionPrivate7triggerEv
inline void QQuickWebEngineActionPrivate::trigger()
{
    Q_Q(QQuickWebEngineAction);
    if (QQuickWebEngineView *view = static_cast<QQuickWebEngineView*>(q->parent())) {
        view->triggerWebAction(static_cast<QQuickWebEngineView::WebAction>(data().toInt()));
    }
}
//  -----------------------------------------------------------------------

//  QQuickWebEngineAction *QQuickWebEngineActionPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickWebEngineAction *ritual_ZN28QQuickWebEngineActionPrivate6q_funcEv(
    QQuickWebEngineActionPrivate *self) {
  return self->q_func();
}

//  const QQuickWebEngineAction *QQuickWebEngineActionPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickWebEngineAction *ritual_ZNK28QQuickWebEngineActionPrivate6q_funcEv(
    const QQuickWebEngineActionPrivate *self) {
  return self->q_func();
}

//  QQuickWebEngineActionPrivate::QQuickWebEngineActionPrivate(const QVariant
//      &data, const QString &text, const QString &iconName, bool enabled)
extern "C" Q_DECL_EXPORT
QQuickWebEngineActionPrivate *ritual_ZN28QQuickWebEngineActionPrivateC1ERK8QVariantRK7QStringS5_b(
    const QVariant *data,
    const QString *text,
    const QString *iconName,
    bool enabled) {
  return new QQuickWebEngineActionPrivate(*data, *text, *iconName, enabled);
}

//  QQuickWebEngineActionPrivate::~QQuickWebEngineActionPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickWebEngineActionPrivateD1Ev(
    QQuickWebEngineActionPrivate *self) {
  delete self;
}

//  void QQuickWebEngineActionPrivate::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickWebEngineActionPrivate10setEnabledEb(
    QQuickWebEngineActionPrivate *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  QVariant QQuickWebEngineActionPrivate::data() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK28QQuickWebEngineActionPrivate4dataEv(
    const QQuickWebEngineActionPrivate *self) {
  return new QVariant(self->data());
}

//  void QQuickWebEngineActionPrivate::trigger()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickWebEngineActionPrivate7triggerEv(
    QQuickWebEngineActionPrivate *self) {
  self->trigger();
}
