//  Written by hand on 2026-11-25 from
//  QtMultimedia/6.12.0/QtMultimedia/private/qautoresetevent_win32_p.h, Qt
//  6.12.0, as the Qt of Windows installs it. Kept as it is when the
//  generator runs again.
//  It is final, so no Cute class is built on it. Not written: the templates
//  'callOnActivated' and the signal 'activated'.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qautoresetevent_win32_p.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qobject.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QtPrivate::QAutoResetEventWin32::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QtPrivate20QAutoResetEventWin3210metaObjectEv(
    const QtPrivate::QAutoResetEventWin32 *self) {
  return self->metaObject();
}

//  QString QtPrivate::QAutoResetEventWin32::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QtPrivate20QAutoResetEventWin322trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtPrivate::QAutoResetEventWin32::tr(s, c, n));
}

//  QtPrivate::QAutoResetEventWin32::QAutoResetEventWin32(QObject *parent)
extern "C" Q_DECL_EXPORT
QtPrivate::QAutoResetEventWin32 *ritual_ZN9QtPrivate20QAutoResetEventWin32C1EP7QObject(
    QObject *parent) {
  return new QtPrivate::QAutoResetEventWin32(parent);
}

//  QtPrivate::QAutoResetEventWin32::~QAutoResetEventWin32()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate20QAutoResetEventWin32D1Ev(
    QtPrivate::QAutoResetEventWin32 *self) {
  delete self;
}

//  bool QtPrivate::QAutoResetEventWin32::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate20QAutoResetEventWin327isValidEv(
    const QtPrivate::QAutoResetEventWin32 *self) {
  return self->isValid();
}

//  void QtPrivate::QAutoResetEventWin32::set()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate20QAutoResetEventWin323setEv(
    QtPrivate::QAutoResetEventWin32 *self) {
  self->set();
}

#endif  // defined(Q_OS_WIN)
