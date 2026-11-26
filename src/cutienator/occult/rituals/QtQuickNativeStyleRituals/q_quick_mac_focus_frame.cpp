//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickmacfocusframe_p.h,
//  Qt 6.12.0. Edited by hand on 2026-11-25:
//  the includes stand under the '#if' now, as Qt's Linux kit lacks
//  the export header, the header is included by its own path with no
//  module header of QtQuickNativeStyle before it, and 'qt_metacast'
//  is gone. Qt builds the class for macOS only.
//  Kept as it is when the generator runs again.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_MACOS)
#include <QtQuickNativeStyle/qtquicknativestyleexports.h>
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickmacfocusframe_p.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickMacFocusFrame::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickMacFocusFrame10metaObjectEv(
    const QQuickMacFocusFrame *self) {
  return self->metaObject();
}

//  QString QQuickMacFocusFrame::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickMacFocusFrame2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickMacFocusFrame::tr(s, c, n));
}

//  QQuickMacFocusFrame::QQuickMacFocusFrame()
extern "C" Q_DECL_EXPORT
QQuickMacFocusFrame *ritual_ZN19QQuickMacFocusFrameC1Ev() {
  return new QQuickMacFocusFrame();
}

//  QQuickItem *QQuickMacFocusFrame::createFocusFrame(QQmlContext *context)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN19QQuickMacFocusFrame16createFocusFrameEP11QQmlContext(
    QQuickMacFocusFrame *self,
    QQmlContext *context) {
  return self->createFocusFrame(context);
}

//  QQuickItem *QQuickMacFocusFrame::createFocusFrame(QQmlContext *context)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_own_ZN19QQuickMacFocusFrame16createFocusFrameEP11QQmlContext(
    QQuickMacFocusFrame *self,
    QQmlContext *context) {
  return self->QQuickMacFocusFrame::createFocusFrame(context);
}

#endif  // defined(Q_OS_MACOS)
