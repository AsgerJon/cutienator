//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qautoresetevent_linux_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if defined(Q_OS_LINUX) || defined(Q_OS_ANDROID) || defined(Q_OS_HARMONY)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qautoresetevent_linux_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QtPrivate::QAutoResetEventEventFD::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QtPrivate22QAutoResetEventEventFD10metaObjectEv(
    const QtPrivate::QAutoResetEventEventFD *self) {
  return self->metaObject();
}

//  void *QtPrivate::QAutoResetEventEventFD::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9QtPrivate22QAutoResetEventEventFD11qt_metacastEPKc(
    QtPrivate::QAutoResetEventEventFD *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtPrivate::QAutoResetEventEventFD::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtPrivate22QAutoResetEventEventFD11qt_metacallEN11QMetaObject4CallEiPPv(
    QtPrivate::QAutoResetEventEventFD *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QtPrivate::QAutoResetEventEventFD::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QtPrivate22QAutoResetEventEventFD2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtPrivate::QAutoResetEventEventFD::tr(s, c, n));
}

//  QtPrivate::QAutoResetEventEventFD::QAutoResetEventEventFD(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QtPrivate::QAutoResetEventEventFD *ritual_ZN9QtPrivate22QAutoResetEventEventFDC1EP7QObject(
    QObject *parent) {
  return new QtPrivate::QAutoResetEventEventFD(parent);
}

//  QtPrivate::QAutoResetEventEventFD::~QAutoResetEventEventFD()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate22QAutoResetEventEventFDD1Ev(
    QtPrivate::QAutoResetEventEventFD *self) {
  delete self;
}

//  bool QtPrivate::QAutoResetEventEventFD::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate22QAutoResetEventEventFD7isValidEv(
    const QtPrivate::QAutoResetEventEventFD *self) {
  return self->isValid();
}

//  void QtPrivate::QAutoResetEventEventFD::set()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate22QAutoResetEventEventFD3setEv(
    QtPrivate::QAutoResetEventEventFD *self) {
  self->set();
}

//  void QtPrivate::QAutoResetEventEventFD::activated()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate22QAutoResetEventEventFD9activatedEv(
    QtPrivate::QAutoResetEventEventFD *self) {
  self->activated();
}

#endif  // defined(Q_OS_LINUX) || defined(Q_OS_ANDROID) || defined(Q_OS_HARMONY)
