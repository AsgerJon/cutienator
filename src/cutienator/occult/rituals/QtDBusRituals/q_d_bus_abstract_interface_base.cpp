//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/qdbusabstractinterface.h, Qt 6.12.0. Changes made here are lost.
#include <QtDBus/qtdbusglobal.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/qdbusabstractinterface.h>

//  int QDBusAbstractInterfaceBase::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QDBusAbstractInterfaceBase11qt_metacallEN11QMetaObject4CallEiPPv(
    QDBusAbstractInterfaceBase *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QDBusAbstractInterfaceBase::QDBusAbstractInterfaceBase(QDBusAbstractInter
//      facePrivate &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
QDBusAbstractInterfaceBase *ritual_ZN26QDBusAbstractInterfaceBaseC1ER29QDBusAbstractInterfacePrivateP7QObject(
    QDBusAbstractInterfacePrivate *dd,
    QObject *parent) {
  return new QDBusAbstractInterfaceBase(*dd, parent);
}

//  QDBusAbstractInterfacePrivate *QDBusAbstractInterfaceBase::d_func()
extern "C" Q_DECL_EXPORT
QDBusAbstractInterfacePrivate *ritual_ZN26QDBusAbstractInterfaceBase6d_funcEv(
    QDBusAbstractInterfaceBase *self) {
  return self->d_func();
}

//  const QDBusAbstractInterfacePrivate *QDBusAbstractInterfaceBase::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QDBusAbstractInterfacePrivate *ritual_ZNK26QDBusAbstractInterfaceBase6d_funcEv(
    const QDBusAbstractInterfaceBase *self) {
  return self->d_func();
}

#endif  // !defined(QT_NO_DBUS)
