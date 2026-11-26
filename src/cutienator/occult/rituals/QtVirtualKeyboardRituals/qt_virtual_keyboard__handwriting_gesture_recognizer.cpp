//  Written by dev_tooling.RitualGenerator from the records of QtVirtualKeybo
//  ard/6.12.0/QtVirtualKeyboard/private/handwritinggesturerecognizer_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/qvirtualkeyboard_global_p.h>
#include <QtVirtualKeyboard/QtVirtualKeyboard>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/handwritinggesturerecognizer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtVirtualKeyboard/qvirtualkeyboardtrace.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  const QMetaObject
//      *QtVirtualKeyboard::HandwritingGestureRecognizer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QtVirtualKeyboard28HandwritingGestureRecognizer10metaObjectEv(
    const QtVirtualKeyboard::HandwritingGestureRecognizer *self) {
  return self->metaObject();
}

//  void *QtVirtualKeyboard::HandwritingGestureRecognizer::qt_metacast(const
//      char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QtVirtualKeyboard28HandwritingGestureRecognizer11qt_metacastEPKc(
    QtVirtualKeyboard::HandwritingGestureRecognizer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtVirtualKeyboard::HandwritingGestureRecognizer::qt_metacall(QMetaObj
//      ect::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QtVirtualKeyboard28HandwritingGestureRecognizer11qt_metacallEN11QMetaObject4CallEiPPv(
    QtVirtualKeyboard::HandwritingGestureRecognizer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QtVirtualKeyboard::HandwritingGestureRecognizer::tr(const char
//      *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QtVirtualKeyboard28HandwritingGestureRecognizer2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      QtVirtualKeyboard::HandwritingGestureRecognizer::tr(
          s,
          c,
          n));
}

//  QtVirtualKeyboard::HandwritingGestureRecognizer::HandwritingGestureRecogn
//      izer(QObject *parent)
extern "C" Q_DECL_EXPORT
QtVirtualKeyboard::HandwritingGestureRecognizer *ritual_ZN17QtVirtualKeyboard28HandwritingGestureRecognizerC1EP7QObject(
    QObject *parent) {
  return new QtVirtualKeyboard::HandwritingGestureRecognizer(parent);
}

//  void QtVirtualKeyboard::HandwritingGestureRecognizer::setDpi(int dpi)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard28HandwritingGestureRecognizer6setDpiEi(
    QtVirtualKeyboard::HandwritingGestureRecognizer *self,
    int dpi) {
  self->setDpi(dpi);
}

//  int QtVirtualKeyboard::HandwritingGestureRecognizer::dpi() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QtVirtualKeyboard28HandwritingGestureRecognizer3dpiEv(
    const QtVirtualKeyboard::HandwritingGestureRecognizer *self) {
  return self->dpi();
}

//  QVariantMap
//      QtVirtualKeyboard::HandwritingGestureRecognizer::recognize(const
//      QList<QVirtualKeyboardTrace *> traceList)
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZN17QtVirtualKeyboard28HandwritingGestureRecognizer9recognizeE5QListIP21QVirtualKeyboardTraceE(
    QtVirtualKeyboard::HandwritingGestureRecognizer *self,
    const QList<QVirtualKeyboardTrace *> *traceList) {
  return new QMap<QString, QVariant>(self->recognize(*traceList));
}
