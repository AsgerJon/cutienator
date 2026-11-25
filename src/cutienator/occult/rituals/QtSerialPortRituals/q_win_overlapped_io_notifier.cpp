//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialPort/6.12.0/QtSerialPort/private/qwinoverlappedionotifier_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-25: Qt does not export the class, and the
//  code taken from Qt's source for its constructor, destructor and
//  'setEnabled' needs 'QWinOverlappedIoNotifierPrivate', which only Qt's
//  'qwinoverlappedionotifier.cpp' defines. So, as for every class Qt does
//  not export, only what goes through the object is written: 'metaObject'
//  and the destructor. Left out: the constructor, 'tr', 'setEnabled' and
//  the Cute class. Kept as it is when the generator runs again.
#include <QtSerialPort/qserialportglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtSerialPort/QtSerialPort>
#include <QtSerialPort/6.12.0/QtSerialPort/private/qwinoverlappedionotifier_p.h>
#include <QtCore/qmetaobject.h>

//  const QMetaObject *QWinOverlappedIoNotifier::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QWinOverlappedIoNotifier10metaObjectEv(
    const QWinOverlappedIoNotifier *self) {
  return self->metaObject();
}

//  QWinOverlappedIoNotifier::~QWinOverlappedIoNotifier()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QWinOverlappedIoNotifierD1Ev(
    QWinOverlappedIoNotifier *self) {
  delete self;
}

#endif  // defined(Q_OS_WIN)
