//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickwindowsfocusframe_p.h,
//  Qt 6.12.0. Edited by hand on 2026-11-25:
//  the includes stand under the '#if' now, as Qt's Linux kit lacks
//  the export header, the header is included by its own path with no
//  module header of QtQuickNativeStyle before it, and 'qt_metacast'
//  is gone. Qt builds the class for Windows only.
//  Kept as it is when the generator runs again.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtQuickNativeStyle/qtquicknativestyleexports.h>
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickwindowsfocusframe_p.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickWindowsFocusFrame::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuickWindowsFocusFrame10metaObjectEv(
    const QQuickWindowsFocusFrame *self) {
  return self->metaObject();
}

//  QString QQuickWindowsFocusFrame::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQuickWindowsFocusFrame2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickWindowsFocusFrame::tr(s, c, n));
}

//  QQuickWindowsFocusFrame::QQuickWindowsFocusFrame()
extern "C" Q_DECL_EXPORT
QQuickWindowsFocusFrame *ritual_ZN23QQuickWindowsFocusFrameC1Ev() {
  return new QQuickWindowsFocusFrame();
}

//  QQuickItem *QQuickWindowsFocusFrame::createFocusFrame(QQmlContext
//      *context)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN23QQuickWindowsFocusFrame16createFocusFrameEP11QQmlContext(
    QQuickWindowsFocusFrame *self,
    QQmlContext *context) {
  return self->createFocusFrame(context);
}

//  QQuickItem *QQuickWindowsFocusFrame::createFocusFrame(QQmlContext
//      *context)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_own_ZN23QQuickWindowsFocusFrame16createFocusFrameEP11QQmlContext(
    QQuickWindowsFocusFrame *self,
    QQmlContext *context) {
  return self->QQuickWindowsFocusFrame::createFocusFrame(context);
}

#endif  // defined(Q_OS_WIN)
