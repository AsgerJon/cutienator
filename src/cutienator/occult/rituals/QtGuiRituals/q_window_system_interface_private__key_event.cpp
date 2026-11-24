//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QWindowSystemInterfacePrivate::KeyEvent::KeyEvent(QWindow *w, ulong time,
//      QEvent::Type t, int k, Qt::KeyboardModifiers mods, const QString
//      &text, bool autorep, ushort count, const QInputDevice *device)
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::KeyEvent *ritual_ZN29QWindowSystemInterfacePrivate8KeyEventC1EP7QWindowmN6QEvent4TypeEi6QFlagsIN2Qt16KeyboardModifierEERK7QStringbtPK12QInputDevice(
    QWindow *w,
    ulong time,
    QEvent::Type t,
    int k,
    int mods,
    const QString *text,
    bool autorep,
    ushort count,
    const QInputDevice *device) {
  return new QWindowSystemInterfacePrivate::KeyEvent(
      w,
      time,
      t,
      k,
      QFlags<Qt::KeyboardModifier>::fromInt(mods),
      *text,
      autorep,
      count,
      device);
}

//  QWindowSystemInterfacePrivate::KeyEvent::KeyEvent(QWindow *w, ulong time,
//      QEvent::Type t, int k, Qt::KeyboardModifiers mods, quint32 nativeSC,
//      quint32 nativeVK, quint32 nativeMods, const QString &text, bool
//      autorep, ushort count, const QInputDevice *device)
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::KeyEvent *ritual_ZN29QWindowSystemInterfacePrivate8KeyEventC1EP7QWindowmN6QEvent4TypeEi6QFlagsIN2Qt16KeyboardModifierEEjjjRK7QStringbtPK12QInputDevice(
    QWindow *w,
    ulong time,
    QEvent::Type t,
    int k,
    int mods,
    quint32 nativeSC,
    quint32 nativeVK,
    quint32 nativeMods,
    const QString *text,
    bool autorep,
    ushort count,
    const QInputDevice *device) {
  return new QWindowSystemInterfacePrivate::KeyEvent(
      w,
      time,
      t,
      k,
      QFlags<Qt::KeyboardModifier>::fromInt(mods),
      nativeSC,
      nativeVK,
      nativeMods,
      *text,
      autorep,
      count,
      device);
}

//  QWindowSystemInterfacePrivate::KeyEvent::~KeyEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate8KeyEventD1Ev(
    QWindowSystemInterfacePrivate::KeyEvent *self) {
  delete self;
}
