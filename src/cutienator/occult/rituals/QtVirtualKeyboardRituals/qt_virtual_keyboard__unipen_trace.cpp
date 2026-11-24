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

//  const QMetaObject *QtVirtualKeyboard::UnipenTrace::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QtVirtualKeyboard11UnipenTrace10metaObjectEv(
    const QtVirtualKeyboard::UnipenTrace *self) {
  return self->metaObject();
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

#endif  // QT_CONFIG(vkb_record_trace_input)
