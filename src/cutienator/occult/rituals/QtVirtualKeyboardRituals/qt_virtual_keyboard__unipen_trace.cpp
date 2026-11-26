//  Written by dev_tooling.RitualGenerator from the records of
//  QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/unipentrace_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtVirtualKeyboard/qvirtualkeyboard_global.h>
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/qvirtualkeyboard_global_p.h>
#if QT_CONFIG(vkb_record_trace_input)
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/qvirtualkeyboard_global_p.h>
#include <QtVirtualKeyboard/QtVirtualKeyboard>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/unipentrace_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtVirtualKeyboard/qvirtualkeyboardtrace.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  const QMetaObject *QtVirtualKeyboard::UnipenTrace::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QtVirtualKeyboard11UnipenTrace10metaObjectEv(
    const QtVirtualKeyboard::UnipenTrace *self) {
  return self->metaObject();
}

//  void *QtVirtualKeyboard::UnipenTrace::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QtVirtualKeyboard11UnipenTrace11qt_metacastEPKc(
    QtVirtualKeyboard::UnipenTrace *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtVirtualKeyboard::UnipenTrace::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QtVirtualKeyboard11UnipenTrace11qt_metacallEN11QMetaObject4CallEiPPv(
    QtVirtualKeyboard::UnipenTrace *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QtVirtualKeyboard::UnipenTrace::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QtVirtualKeyboard11UnipenTrace2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtVirtualKeyboard::UnipenTrace::tr(s, c, n));
}

//  QtVirtualKeyboard::UnipenTrace::UnipenTrace(const QVariantMap
//      &traceCaptureDeviceInfo, const QVariantMap &traceScreenInfo, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QtVirtualKeyboard::UnipenTrace *ritual_ZN17QtVirtualKeyboard11UnipenTraceC1ERK4QMapI7QString8QVariantES6_P7QObject(
    const QMap<QString, QVariant> *traceCaptureDeviceInfo,
    const QMap<QString, QVariant> *traceScreenInfo,
    QObject *parent) {
  return new QtVirtualKeyboard::UnipenTrace(
      *traceCaptureDeviceInfo,
      *traceScreenInfo,
      parent);
}

//  void QtVirtualKeyboard::UnipenTrace::record(const
//      QList<QVirtualKeyboardTrace *> &traceList)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard11UnipenTrace6recordERK5QListIP21QVirtualKeyboardTraceE(
    QtVirtualKeyboard::UnipenTrace *self,
    const QList<QVirtualKeyboardTrace *> *traceList) {
  self->record(*traceList);
}

//  void QtVirtualKeyboard::UnipenTrace::save(uint unicode, uint confidence)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard11UnipenTrace4saveEjj(
    QtVirtualKeyboard::UnipenTrace *self,
    uint unicode,
    uint confidence) {
  self->save(unicode, confidence);
}

//  QString QtVirtualKeyboard::UnipenTrace::directory() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QtVirtualKeyboard11UnipenTrace9directoryEv(
    const QtVirtualKeyboard::UnipenTrace *self) {
  return new QString(self->directory());
}

//  void QtVirtualKeyboard::UnipenTrace::setDirectory(const QString
//      &directory)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard11UnipenTrace12setDirectoryERK7QString(
    QtVirtualKeyboard::UnipenTrace *self,
    const QString *directory) {
  self->setDirectory(*directory);
}

#endif  // QT_CONFIG(vkb_record_trace_input)
