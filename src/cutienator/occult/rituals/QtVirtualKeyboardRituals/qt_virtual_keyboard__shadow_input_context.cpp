//  Written by dev_tooling.RitualGenerator from the records of QtVirtualKeybo
//  ard/6.12.0/QtVirtualKeyboard/private/shadowinputcontext_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/qvirtualkeyboard_global_p.h>
#include <QtVirtualKeyboard/QtVirtualKeyboard>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/shadowinputcontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QtVirtualKeyboard::ShadowInputContext::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QtVirtualKeyboard18ShadowInputContext10metaObjectEv(
    const QtVirtualKeyboard::ShadowInputContext *self) {
  return self->metaObject();
}

//  QString QtVirtualKeyboard::ShadowInputContext::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QtVirtualKeyboard18ShadowInputContext2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtVirtualKeyboard::ShadowInputContext::tr(s, c, n));
}

//  void QtVirtualKeyboard::ShadowInputContext::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard18ShadowInputContext24qt_qmlMarker_uncreatableEv(
    QtVirtualKeyboard::ShadowInputContext *self) {
  self->qt_qmlMarker_uncreatable();
}
