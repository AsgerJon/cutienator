//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickpresshandler_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpresshandler_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquickpresshandler_p_p.h"
#include <QtCore/private/qobject_p.h>
#include <QtGui/qguiapplication.h>
#include <QtGui/qstylehints.h>
#include <QtQuick/qquickitem.h>
#include <QtQuick/private/qquickevents_p_p.h>
#include <QtQuickTemplates2/private/qquicktextarea_p.h>
#include <QtQuickTemplates2/private/qquicktextfield_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquickpresshandler.cpp, line 17, as _ZN18QQuickPressHandler15mousePressEventEP11QMouseEvent
inline void QQuickPressHandler::mousePressEvent(QMouseEvent *event)
{
    longPress = false;
    pressPos = event->position();
    if (Qt::LeftButton == (event->buttons() & Qt::LeftButton)) {
        timer.start(QGuiApplication::styleHints()->mousePressAndHoldInterval(), control);
        delayedMousePressEvent = std::make_unique<QMouseEvent>(event->type(), event->position().toPoint(), event->globalPosition().toPoint(),
                                                 event->button(), event->buttons(), event->modifiers(), event->pointingDevice());
    } else {
        timer.stop();
    }

    if (isSignalConnected(control, "pressed(QQuickMouseEvent*)", pressedSignalIndex)) {
        QQuickMouseEvent mev;
        mev.reset(pressPos.x(), pressPos.y(), event->button(), event->buttons(),
                  event->modifiers(), false/*isClick*/, false/*wasHeld*/);
        mev.setAccepted(true);
        QQuickMouseEvent *mevPtr = &mev;
        void *args[] = { nullptr, &mevPtr };
        QMetaObject::metacall(control, QMetaObject::InvokeMetaMethod, pressedSignalIndex, args);
        event->setAccepted(mev.isAccepted());
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquickpresshandler.cpp, line 41, as _ZN18QQuickPressHandler14mouseMoveEventEP11QMouseEvent
inline void QQuickPressHandler::mouseMoveEvent(QMouseEvent *event)
{
    if (qAbs(event->position().x() - pressPos.x()) > QGuiApplication::styleHints()->startDragDistance())
        timer.stop();
}

//  from ../qtdeclarative/src/quicktemplates/qquickpresshandler.cpp, line 47, as _ZN18QQuickPressHandler17mouseReleaseEventEP11QMouseEvent
inline void QQuickPressHandler::mouseReleaseEvent(QMouseEvent *event)
{
    if (!longPress)
        timer.stop();

    if (isSignalConnected(control, "released(QQuickMouseEvent*)", releasedSignalIndex)) {
        QQuickMouseEvent mev;
        mev.reset(pressPos.x(), pressPos.y(), event->button(), event->buttons(),
                  event->modifiers(), false/*isClick*/, false/*wasHeld*/);
        mev.setAccepted(true);
        QQuickMouseEvent *mevPtr = &mev;
        void *args[] = { nullptr, &mevPtr };
        QMetaObject::metacall(control, QMetaObject::InvokeMetaMethod, releasedSignalIndex, args);
        event->setAccepted(mev.isAccepted());
    }

}

//  from ../qtdeclarative/src/quicktemplates/qquickpresshandler.cpp, line 65, as _ZN18QQuickPressHandler10timerEventEP11QTimerEvent
inline void QQuickPressHandler::timerEvent(QTimerEvent *)
{
    timer.stop();
    clearDelayedMouseEvent();

    longPress = isSignalConnected(control, "pressAndHold(QQuickMouseEvent*)", pressAndHoldSignalIndex);
    if (longPress) {
        QQuickMouseEvent mev;
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
        mev.reset(pressPos.x(), pressPos.y(), Qt::LeftButton, Qt::LeftButton,
                  QGuiApplication::keyboardModifiers(), false/*isClick*/, true/*wasHeld*/);
QT_WARNING_POP
        mev.setAccepted(true);
        // Use fast signal invocation since we already got its index
        QQuickMouseEvent *mevPtr = &mev;
        void *args[] = { nullptr, &mevPtr };
        QMetaObject::metacall(control, QMetaObject::InvokeMetaMethod, pressAndHoldSignalIndex, args);
        if (!mev.isAccepted())
            longPress = false;
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquickpresshandler.cpp, line 88, as _ZN18QQuickPressHandler22clearDelayedMouseEventEv
inline void QQuickPressHandler::clearDelayedMouseEvent()
{
    delayedMousePressEvent.reset();
}

//  from ../qtdeclarative/src/quicktemplates/qquickpresshandler.cpp, line 93, as _ZN18QQuickPressHandler8isActiveEv
inline bool QQuickPressHandler::isActive()
{
    return !(timer.isActive() || longPress);
}

//  from ../qtdeclarative/src/quicktemplates/qquickpresshandler.cpp, line 98, as _ZN18QQuickPressHandler17isSignalConnectedEP10QQuickItemPKcRi
inline bool QQuickPressHandler::isSignalConnected(QQuickItem *item, const char *signalName, int &signalIndex)
{
    if (signalIndex == -1)
        signalIndex = item->metaObject()->indexOfSignal(signalName);
    Q_ASSERT(signalIndex != -1);
    const auto signalMetaMethod = item->metaObject()->method(signalIndex);
    if (QQuickTextArea *textArea = qobject_cast<QQuickTextArea*>(item)) {
        return textArea->isSignalConnected(signalMetaMethod);
    } else if (QQuickTextField *textField = qobject_cast<QQuickTextField*>(item)) {
        return textField->isSignalConnected(signalMetaMethod);
    }
    qFatal("Unhandled control type for signal name: %s", signalName);
    return false;
}
//  -----------------------------------------------------------------------

//  void QQuickPressHandler::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPressHandler15mousePressEventEP11QMouseEvent(
    QQuickPressHandler *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void QQuickPressHandler::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPressHandler14mouseMoveEventEP11QMouseEvent(
    QQuickPressHandler *self,
    QMouseEvent *event) {
  self->mouseMoveEvent(event);
}

//  void QQuickPressHandler::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPressHandler17mouseReleaseEventEP11QMouseEvent(
    QQuickPressHandler *self,
    QMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void QQuickPressHandler::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPressHandler10timerEventEP11QTimerEvent(
    QQuickPressHandler *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  void QQuickPressHandler::clearDelayedMouseEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPressHandler22clearDelayedMouseEventEv(
    QQuickPressHandler *self) {
  self->clearDelayedMouseEvent();
}

//  bool QQuickPressHandler::isActive()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQuickPressHandler8isActiveEv(QQuickPressHandler *self) {
  return self->isActive();
}

//  bool QQuickPressHandler::isSignalConnected(QQuickItem *item, const char
//      *signalName, int &signalIndex)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQuickPressHandler17isSignalConnectedEP10QQuickItemPKcRi(
    QQuickItem *item,
    const char *signalName,
    int *signalIndex) {
  return QQuickPressHandler::isSignalConnected(
      item,
      signalName,
      *signalIndex);
}
