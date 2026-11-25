//  Written by hand on 2026-11-25 from
//  QtRemoteObjectsQml/6.12.0/QtRemoteObjectsQml/private/
//  qremoteobjectsqml_p.h, Qt 6.12.0, from Qt's source. Kept as it is
//  when the generator runs again.
//  Qt builds the part only where QtNetwork has 'localserver' (and
//  QtQuick is there), so the file stands under QT_CONFIG(localserver).
//  The class line has no export macro (the part is made with
//  NO_GENERATE_CPP_EXPORTS), so Qt's library offers nothing of this
//  class by name: only its inline functions are written, the
//  destructor and watch, and metaObject(), called through the object.
//  Not written: the implicit constructor and 'tr'.
#include <QtRemoteObjects/qtremoteobjectglobal.h>
#include <QtNetwork/qtnetworkglobal.h>
#if QT_CONFIG(localserver)
#include <QtRemoteObjectsQml/6.12.0/QtRemoteObjectsQml/private/qremoteobjectsqml_p.h>
#include <QtQml/qjsvalue.h>
#include <QtRemoteObjects/qremoteobjectpendingcall.h>

//  const QMetaObject *QtQmlRemoteObjects::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QtQmlRemoteObjects10metaObjectEv(
    const QtQmlRemoteObjects *self) {
  return self->metaObject();
}

//  QtQmlRemoteObjects::~QtQmlRemoteObjects()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtQmlRemoteObjectsD1Ev(QtQmlRemoteObjects *self) {
  delete self;
}

//  QJSValue QtQmlRemoteObjects::watch(const QRemoteObjectPendingCall &reply,
//      int timeout)
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZN18QtQmlRemoteObjects5watchERK24QRemoteObjectPendingCalli(
    QtQmlRemoteObjects *self,
    const QRemoteObjectPendingCall *reply,
    int timeout) {
  return new QJSValue(self->watch(*reply, timeout));
}

#endif  // QT_CONFIG(localserver)
