//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qinputmethod_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/qinputmethod.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qinputmethod_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qinputmethod.h>
#include <QtGui/private/qinputmethod_p.h>
#include <QtGui/qguiapplication.h>
#include <QtGui/qpa/qplatforminputcontext_p.h>
#include <QtCore/QDebug>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/kernel/qinputmethod.cpp, line 357, as local:qinputmethod.cpp:platformSupportsHiddenText
static inline bool platformSupportsHiddenText()
{
    const QPlatformInputContext *inputContext = QGuiApplicationPrivate::platformIntegration()->inputContext();
    return inputContext && inputContext->hasCapability(QPlatformInputContext::HiddenTextCapability);
}

//  from src/gui/kernel/qinputmethod.cpp, line 363, as _ZN19QInputMethodPrivate24objectAcceptsInputMethodEP7QObject
inline bool QInputMethodPrivate::objectAcceptsInputMethod(QObject *object)
{
    bool enabled = false;
    if (object) {
        // If the platform does not support hidden text, query the hints
        // in addition and disable in case of ImhHiddenText.
        static const bool supportsHiddenText = platformSupportsHiddenText();
        QInputMethodQueryEvent query(supportsHiddenText
                                     ? Qt::InputMethodQueries(Qt::ImEnabled)
                                     : Qt::InputMethodQueries(Qt::ImEnabled | Qt::ImHints));
        QGuiApplication::sendEvent(object, &query);
        enabled = query.value(Qt::ImEnabled).toBool();
        if (enabled && !supportsHiddenText
            && Qt::InputMethodHints(query.value(Qt::ImHints).toInt()).testFlag(Qt::ImhHiddenText)) {
            enabled = false;
        }
    }
    return enabled;
}
//  -----------------------------------------------------------------------

//  QInputMethod *QInputMethodPrivate::q_func()
extern "C" Q_DECL_EXPORT
QInputMethod *ritual_ZN19QInputMethodPrivate6q_funcEv(
    QInputMethodPrivate *self) {
  return self->q_func();
}

//  const QInputMethod *QInputMethodPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QInputMethod *ritual_ZNK19QInputMethodPrivate6q_funcEv(
    const QInputMethodPrivate *self) {
  return self->q_func();
}

//  QInputMethodPrivate::QInputMethodPrivate()
extern "C" Q_DECL_EXPORT
QInputMethodPrivate *ritual_ZN19QInputMethodPrivateC1Ev() {
  return new QInputMethodPrivate();
}

//  QPlatformInputContext *QInputMethodPrivate::platformInputContext() const
extern "C" Q_DECL_EXPORT
QPlatformInputContext *ritual_ZNK19QInputMethodPrivate20platformInputContextEv(
    const QInputMethodPrivate *self) {
  return self->platformInputContext();
}

//  QInputMethodPrivate *QInputMethodPrivate::get(QInputMethod *inputMethod)
extern "C" Q_DECL_EXPORT
QInputMethodPrivate *ritual_ZN19QInputMethodPrivate3getEP12QInputMethod(
    QInputMethod *inputMethod) {
  return QInputMethodPrivate::get(inputMethod);
}

//  bool QInputMethodPrivate::objectAcceptsInputMethod(QObject *object)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QInputMethodPrivate24objectAcceptsInputMethodEP7QObject(
    QObject *object) {
  return QInputMethodPrivate::objectAcceptsInputMethod(object);
}
